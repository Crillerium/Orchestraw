# Orchestraw 「稻草乐队」
Orchestraw: Download Netease Cloud Music with Metadata
下载网易云音乐音频与元数据

# Installation 安装
1. 通过 pip 安装
在终端执行以下命令:
```
pip install orchestraw
```

2. 通过[Releases页](https://github.com/crillerium/orchestraw/releases)下载 *.whl* 或 *.tar.gz* 安装文件
下载完成后，在终端执行以下命令:
```
pip install path/to/your_downloaded.whl
或
pip install path/to/your_downloaded.tar.gz
```

# Usage 使用
## 下载音频与元数据
在终端执行以下命令:
```
python -m orchestraw
```
或
```
ost
```
## 元数据编辑器
介绍: 为已有音频添加元数据*(前提是网易云音乐中有对应的音乐)*
在终端执行以下命令:
```
python -m orchestraw.metaeditor <待处理文件.mp3>
```
或
```
ostm <待处理文件.mp3>
```

# Notice 注意事项
1. 此项目使用其他网站提供的API接口，因此稳定性不高，但是能用！
(◦˙▽˙◦)
2. 可正常下载的音乐只能是非会员歌曲，会员歌曲只能下载片段，但是可以通过第三方网站下载+元数据编辑器搭配使用。
3. 元数据编辑器不受网易云会员限制，请放心食用！
4. Orchestraw 只能处理mp3格式文件，flac等其他格式的文件请使用ffmpeg等第三方工具转换格式