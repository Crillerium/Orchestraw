#!/usr/bin/python
import requests
import sys
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB

def search_for_songs():
    # 1. 获取用户输入
    query = input("请输入查询关键词: ")
    
    # 2. 发送请求到API
    url = "https://api.csm.sayqz.com/search"
    params = {'keywords': query}
    response = requests.get(url, params=params)
    
    # 3. 将获取的数据转为字典
    responseMap = response.json()

    # 4. 遍历responseMap中的'result'下的'songs'列表
    if 'result' in responseMap and 'songs' in responseMap['result']:
        songs = responseMap['result']['songs']
        music_list = {}
        i = 1
        for song in songs:
            music_list[i] = [song['id'],song['name'],song['artists'][0]['name'],song['album']['name']]
            print("["+str(i)+"]", "歌名:", music_list[i][1], "歌手:", music_list[i][2], "专辑:", music_list[i][3])
            i+=1
        return music_list
    else:
        print("抱歉，没有找到歌曲信息。")
        sys.exit()

def set_song_metadata(filename, song_name, singer, album, cover):
    #获取音乐内容
    audio = ID3(filename)
    print(audio)
    audio.update_to_v23()  # 把可能存在的旧版本升级为2.3
    audio['APIC'] = APIC(  # 插入专辑图片
        encoding=0,
        mime='image/jpeg',
        type=3,
        # desc=u'Cover',
        data=cover
    )
    audio['TIT2'] = TIT2(  # 插入歌名
        encoding=3,
        text=song_name
    )
    audio['TPE1'] = TPE1(  # 插入第一演奏家、歌手、等
        encoding=3,
        text=singer
    )
    audio['TALB'] = TALB(  # 插入专辑名称
        encoding=3,
        text=album
    )
    audio.save()  # 记得要保存

def download():
    order = int(input('请输入序号:'))
    url = "https://api.csm.sayqz.com/song/url"
    params = {'id': music_list[order][0]}
    response = requests.get(url, params=params)
    filename = music_list[order][1] + " - " + music_list[order][2]
    with requests.get(response.json()['data'][0]['url']) as res:
        # 确保请求成功
        if res.status_code == 200:
            with open(filename+".mp3",'wb') as f:
                f.write(res.content)
        else:
            print('音频下载失败')
    with requests.get('https://tenapi.cn/v2/songinfo',params={'id': music_list[order][0]}) as res:
        # 确保请求成功
        if res.status_code == 200:
            with requests.get(res.json()['data']['cover']) as r:
                global cover
                cover = r.content
        else:
            print('封面下载失败')
    set_song_metadata(filename+'.mp3', music_list[order][1], music_list[order][2], music_list[order][3], cover)
        
    print(f"文件已下载并保存为：{filename}.mp3")

def main():
    try:
        music_list = search_for_songs()
        download()
    except KeyboardInterrupt:
        print('脚本已退出')
    except EOFError:
        print('脚本已退出')
    except Exception as e:
        print('脚本意外退出: ',e)

if __name__ == '__main__':
    main()