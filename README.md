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
