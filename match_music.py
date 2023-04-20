import os
import tempfile
from pathlib import Path

import httpx
from javascript import require

netease_api = require("./sandbox.bundle.js")


def process_music(music_data: str, start: int, duration: int) -> bytes:
    from pydub import AudioSegment

    song = AudioSegment.from_mp3(music_data).set_frame_rate(48000)
    return song[start * 1000 : (start + duration) * 1000].export(format="mp3").read()


def encode_music(music_data: bytes, start: int, duration: int, channel: int = 0) -> str:
    return netease_api.encode(tuple(music_data), start, duration, channel)


def get_result(rawdata: str, duration: int):
    params = {
        "sessionId": "441df692-afea-4a54-8aff-f5f20fd34f12",
        "algorithmCode": "shazam_v2",
        "duration": duration,
        "rawdata": rawdata,
        "times": "2",
        "decrypt": "1",
    }

    headers = {
        "authority": "interface.music.163.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "chrome-extension://pgphbbekcgpfaekhcbjamjjkegcclhhd",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "none",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    }

    rsp = httpx.post(
        "https://interface.music.163.com/api/music/audio/match",
        data=params,
        headers=headers,
    )

    return rsp.json()


def match_music(
    input_data: bytes | str | Path,
    start: int,
    duration: int,
    channel: int = 0,
    *,
    auto_process: bool = False
):
    """
    说明：

        听歌识曲

    参数:

        * ``music_data``: 音乐数据/文件路径，需要是 mp3
        * ``start``: 开始匹配时间，单位：秒
        * ``duration``: 音乐持续时间，单位：秒
        * ``auto_process``: 是否自动将音乐处理为符合要求的，若是则需要 ffmpeg

    """
    tempf = None
    if isinstance(input_data, Path):
        input_data = str(input_data)
    elif isinstance(input_data, bytes):
        tempf = tempfile.NamedTemporaryFile(delete=False)
        tempf.write(input_data)
        input_data = tempf.name
        tempf.close()
    if auto_process:
        music_data = process_music(input_data, start, duration)
    else:
        with open(input_data, "rb") as f:
            music_data = f.read()
    result = get_result(encode_music(music_data, start, duration, channel), duration)
    if tempf:
        os.remove(input_data)
    return result


if __name__ == "__main__":
    import sys

    music_name = "test.mp3" if len(sys.argv) <= 1 else sys.argv[1]
    with open(music_name, "rb") as f:
        print(match_music(f.read(), 0, 5, 0))
