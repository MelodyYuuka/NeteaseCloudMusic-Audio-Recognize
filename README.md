# 网易云音乐听歌识曲接口

需要 Python 与 Node.js 环境

## 准备

```bash
yarn install
pip install -r requirements.txt
```

## 使用

### Node.js

```bash
yarn run test
# 使用测试音乐搜索

yarn run test <your music path>
# 搜索你的音乐
```

### Python

在终端使用

```bash
python match_music.py
# 使用测试音乐搜索

python match_music.py <your music path>
# 搜索你的音乐
```

在 Python 脚本使用

```python
from .match_music import match_music
match_music("路径 (str) 或 音频数据 (bytes)", 0, 5, 0)
```

<details>
    <summary>输出示例</summary>

```python
{
    "data": {
        "type": 1,
        "queryId": "c0fd4c96-44eb-460e-992e-1db763519989",
        "result": [
            {
                "startTime": 4980,
                "song": {
                    "name": "向こう側の月",
                    "id": 22765943,
                    "position": 10,
                    "alias": [],
                    "status": 0,
                    "fee": 0,
                    "copyrightId": 663018,
                    "disc": "1",
                    "no": 10,
                    "artists": [
                        {
                            "name": "上海アリス幻樂団",
                            "id": 15345,
                            "picId": 0,
                            "img1v1Id": 0,
                            "briefDesc": "",
                            "picUrl": "http://p4.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                            "img1v1Url": "http://p3.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                            "albumSize": 0,
                            "alias": [],
                            "trans": "",
                            "musicSize": 0,
                            "topicPerson": 0,
                        }
                    ],
                    "album": {
                        "name": "大空魔術 ～ Magical Astronomy",
                        "id": 2091284,
                        "type": "专辑",
                        "size": 10,
                        "picId": 657507953432492,
                        "blurPicUrl": "http://p4.music.126.net/pre3hmomk0nSdlYnpCSn1g==/657507953432492.jpg",
                        "companyId": 0,
                        "pic": 657507953432492,
                        "picUrl": "http://p3.music.126.net/pre3hmomk0nSdlYnpCSn1g==/657507953432492.jpg",
                        "publishTime": 1155398400000,
                        "description": "",
                        "tags": "",
                        "company": "",
                        "briefDesc": "",
                        "artist": {
                            "name": "",
                            "id": 0,
                            "picId": 0,
                            "img1v1Id": 0,
                            "briefDesc": "",
                            "picUrl": "http://p3.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                            "img1v1Url": "http://p3.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                            "albumSize": 0,
                            "alias": [],
                            "trans": "",
                            "musicSize": 0,
                            "topicPerson": 0,
                        },
                        "songs": [],
                        "alias": [],
                        "status": 1,
                        "copyrightId": -1,
                        "commentThreadId": "R_AL_3_2091284",
                        "artists": [
                            {
                                "name": "上海アリス幻樂団",
                                "id": 15345,
                                "picId": 0,
                                "img1v1Id": 0,
                                "briefDesc": "",
                                "picUrl": "http://p4.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1Url": "http://p4.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "albumSize": 0,
                                "alias": [],
                                "trans": "",
                                "musicSize": 0,
                                "topicPerson": 0,
                            }
                        ],
                        "subType": "录音室版",
                        "transName": None,
                        "onSale": False,
                        "mark": 0,
                    },
                    "starred": False,
                    "popularity": 75.0,
                    "score": 75,
                    "starredNum": 0,
                    "duration": 232320,
                    "playedNum": 0,
                    "dayPlays": 0,
                    "hearTime": 0,
                    "ringtone": "",
                    "crbt": None,
                    "audition": None,
                    "copyFrom": "",
                    "commentThreadId": "R_SO_4_22765943",
                    "rtUrl": None,
                    "ftype": 0,
                    "rtUrls": [],
                    "copyright": 2,
                    "transName": None,
                    "sign": None,
                    "mark": 0,
                    "originCoverType": 0,
                    "originSongSimpleData": None,
                    "single": 0,
                    "noCopyrightRcmd": None,
                    "addTime": None,
                    "offline": 0,
                    "canSubscribe": 0,
                    "hasSubscribe": 0,
                    "hMusic": {
                        "name": None,
                        "id": 1312383830,
                        "size": 9295456,
                        "extension": "mp3",
                        "sr": 44100,
                        "dfsId": 0,
                        "bitrate": 320000,
                        "playTime": 232320,
                        "volumeDelta": -32199.0,
                    },
                    "mMusic": {
                        "name": None,
                        "id": 1312383831,
                        "size": 5577291,
                        "extension": "mp3",
                        "sr": 44100,
                        "dfsId": 0,
                        "bitrate": 192000,
                        "playTime": 232320,
                        "volumeDelta": -32199.0,
                    },
                    "lMusic": {
                        "name": None,
                        "id": 1312383832,
                        "size": 3718208,
                        "extension": "mp3",
                        "sr": 44100,
                        "dfsId": 0,
                        "bitrate": 128000,
                        "playTime": 232320,
                        "volumeDelta": -32199.0,
                    },
                    "bMusic": {
                        "name": None,
                        "id": 1312383832,
                        "size": 3718208,
                        "extension": "mp3",
                        "sr": 44100,
                        "dfsId": 0,
                        "bitrate": 128000,
                        "playTime": 232320,
                        "volumeDelta": -32199.0,
                    },
                    "rtype": 0,
                    "rurl": None,
                    "mvid": 0,
                    "mp3Url": None,
                    "privilege": {
                        "id": 22765943,
                        "fee": 0,
                        "payed": 0,
                        "st": 0,
                        "pl": 320000,
                        "dl": 999000,
                        "sp": 7,
                        "cp": 1,
                        "subp": 1,
                        "cs": False,
                        "maxbr": 999000,
                        "fl": 320000,
                        "toast": False,
                        "flag": 256,
                        "preSell": False,
                        "playMaxbr": 999000,
                        "downloadMaxbr": 999000,
                        "maxBrLevel": "lossless",
                        "playMaxBrLevel": "lossless",
                        "downloadMaxBrLevel": "lossless",
                        "plLevel": "exhigh",
                        "dlLevel": "lossless",
                        "flLevel": "exhigh",
                        "rscl": None,
                        "freeTrialPrivilege": {
                            "resConsumable": False,
                            "userConsumable": False,
                            "listenType": None,
                        },
                        "rightSource": 0,
                        "chargeInfoList": [
                            {
                                "rate": 128000,
                                "chargeUrl": None,
                                "chargeMessage": None,
                                "chargeType": 0,
                            },
                            {
                                "rate": 192000,
                                "chargeUrl": None,
                                "chargeMessage": None,
                                "chargeType": 0,
                            },
                            {
                                "rate": 320000,
                                "chargeUrl": None,
                                "chargeMessage": None,
                                "chargeType": 0,
                            },
                            {
                                "rate": 999000,
                                "chargeUrl": None,
                                "chargeMessage": None,
                                "chargeType": 1,
                            },
                        ],
                    },
                },
            }
        ],
    },
    "code": 200,
    "message": "",
}
```

</details>
