import os
import urllib.request,urllib.parse,json
import pygame
class GetData():
    def __init__(self,mtype,message):
        self.limit = 100
        self.mtype = mtype
        self.message = message
        self.ua_header = {
    "Host":"music.163.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.138 Safari/537.36",
    "Referer":"http://music.163.com",
    "Cookie":"appver=1.5.0.75771"
}
        self.searchurl = 'http://music.163.com/api/search/pc'
        self.data={
    "hlpretag":"",
    "hlposttag":"",
    "s":message,
    "offset":0,
    "total":"true",
    "limit":self.limit,
    "type":mtype
}
        #调度搜索
    def Search(self):
        message = ''
        try:
            self.url ='http://music.163.com/api/search/pc'
            self.data=urllib.parse.urlencode(self.data).encode()
            request = urllib.request.Request(url=self.url,data=self.data,headers=self.ua_header)
            response = urllib.request.urlopen(request)
            stexts = response.read().decode("utf8")
            stexts = json.loads(stexts)
            if self.mtype ==1:
                message = self.Song(stexts['result']['songs'])
            if self.mtype == 100:
                message = self.Art(stexts['result']['artists'])
            if self.mtype == 1000:
                message = self.Playlist(stexts['result']['playlists'])
            if self.mtype == 1002:
                message = self.Player(stexts['result']['userprofiles'])
            if self.mtype == 1006:
                self.Lyric()
        except:
            pass
        return message
    #爬取GET并返回message列表
    @classmethod
    def PGet(self,purl):
        ua_header = {
        "Host":"music.163.com",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.138 Safari/537.36",
        "Referer":"http://music.163.com",
        "Cookie":"appver=1.5.0.75771"}
        request = urllib.request.Request(url=purl,headers=ua_header)
        response = urllib.request.urlopen(request)
        stexts = response.read().decode("utf8")
        return json.loads(stexts)
    @classmethod
    def Song(self,texts):
        smessage = []
        try:
            for i in texts:
                if i['hMusic']:
                    songtime = int(i['hMusic']['playTime'])
                elif i['mMusic']:
                    songtime = int(i['mMusic']['playTime'])
                elif i['lMusic']:
                    songtime = int(i['lMusic']['playTime'])
                else:
                    songtime = int(i['bMusic']['playTime'])
                songname = i['name']
                songid = i['id']
                artname = i['artists'][0]['name']
                artid = i['artists'][0]['id']
                arturl = i["album"]["blurPicUrl"]
                album = i['album']['name']
                albumid = i['album']['id']
                songname = songname.replace('/','&').replace('<','《').replace('>','》').replace(':','：').replace('*',' ').replace('?','？').replace('|','&').replace('\\','\\')
                artname = artname.replace('/','&').replace('<','《').replace('>','》').replace(':','：').replace('*',' ').replace('?','？').replace('|','&').replace('\\','\\')
                album = album.replace('/','&').replace('<','《').replace('>','》').replace(':','：').replace('*',' ').replace('?','？').replace('|','&').replace('\\','\\')
                smessage.append([songname,songid,artname,artid,album,albumid,songtime,arturl])
        except:
            pass
        return smessage
    def Art(self,texts):
        pmessage = []
        try:
            for i in texts:
                pname = i['name']
                pid = i['id']
                try:
                    alias = i['alias'][0]
                except:
                    alias = ''
                pname = pname.replace('/','&').replace('<','《').replace('>','》').replace(':','：').replace('*',' ').replace('?','？').replace('|','&').replace('\\','\\')
                alias = alias.replace('/','&').replace('<','《').replace('>','》').replace(':','：').replace('*',' ').replace('?','？').replace('|','&').replace('\\','\\')
                pmessage.append([pname,pid,alias])
        except:
            pass
        return pmessage
    #提取歌单中的元素
    @classmethod
    def Playlist(self,texts):
        pmessage = []
        try:
            for i in texts:
                pname = i['name']
                pid = i['id']
                pimgurl = i["coverImgUrl"]
                nickname = i['creator']['nickname']
                trackCount = i['trackCount']
                pname = pname.replace('/','&').replace('<','《').replace('>','》').replace(':','：').replace('*',' ').replace('?','？').replace('|','&').replace('\\','\\')
                nickname = nickname.replace('/','&').replace('<','《').replace('>','》').replace(':','：').replace('*',' ').replace('?','？').replace('|','&').replace('\\','\\')
                pmessage.append([pname,pid,nickname,trackCount,pimgurl])
        except:
            pass
        return pmessage
        #用户列表
    def Player(self,texts):
        pmessage = []
        try:
            for i in texts:
                nickname = i['nickname']
                userId = i['userId']
                description = i['description']
                signature = i['signature']
                nickname = nickname.replace('/','&').replace('<','《').replace('>','》').replace(':','：').replace('*',' ').replace('?','？').replace('|','&').replace('\\','\\')
                description = description.replace('/','&').replace('<','《').replace('>','》').replace(':','：').replace('*',' ').replace('?','？').replace('|','&').replace('\\','\\')
                signature = signature.replace('/','&').replace('<','《').replace('>','》').replace(':','：').replace('*',' ').replace('?','？').replace('|','&').replace('\\','\\')
                pmessage.append([nickname,userId,description,signature])
        except:
            pass
        return pmessage
        #显示选取歌单中的列表
    @classmethod
    def ShowSongList(self,pid):
        purl = 'http://music.163.com/api/playlist/detail?id={}&updateTime=-1'.format(str(pid))
        stexts=self.PGet(purl)
        return self.Song(stexts['result']['tracks'])
        #显示选取用户的歌单
    @classmethod
    def ShowPlayerList(self,pid):
        purl = 'http://music.163.com/api/user/playlist/?offset=0&limit=1001&uid={}'.format(str(pid))
        stexts = self.PGet(purl)
        return self.Playlist(stexts['playlist'])
        #显示歌手的歌单列表
    @classmethod
    def ShowArtList(self,pid):
        purl = 'http://music.163.com/api/artist/'+str(pid)
        stexts = self.PGet(purl)
        return self.Song(stexts['hotSongs'])
    def Lyric(self):
        pass
    #下载音乐
def Download(mlist,ftype=0):
    url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(mlist[1])
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.138 Safari/537.36"}
    name = '{} - {}'.format(mlist[0],mlist[2])
    if ftype == 0:
        addr = 'cookie'
    else: addr = 'download'
    if not os.path.exists('./'+addr):
        os.mkdir(addr)
    if not os.path.exists('./{}/{}.mp3'.format(addr,name)):
        request = urllib.request.Request(url=url,headers=header)
        response = urllib.request.urlopen(request)
        with open('./{}/{}.mp3'.format(addr,name),'wb') as f:
            f.write(response.read())
    if not os.path.exists('./art'):
        os.mkdir('./art')
    if not os.path.exists('./art/{}.jpg'.format(name)):
        artrequest = urllib.request.Request(url=mlist[-1],headers=header)
        artresponse = urllib.request.urlopen(artrequest)
        with open('./art/{}.jpg'.format(name),'wb') as f1:
            f1.write(artresponse.read())
    if not os.path.exists('./lyric'):
        os.mkdir('./lyric')
    if not os.path.exists('./lyric/{}.txt'.format(name)):
        lyricurl="http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1".format(mlist[1])
        lrequest = urllib.request.Request(url=lyricurl,headers=header)
        lresponse = urllib.request.urlopen(lrequest)
        with open('./lyric/{}.txt'.format(name),"w",encoding="utf8") as f2:
            f2.write(lresponse.read().decode("utf8"))
    #播放音乐
def PlayMusic(songname):
    file = JudgeMusic(songname)
    if file == -1:
        return -1
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play(1)
    #选择播放音乐目录
def JudgeMusic(songname):
    if os.path.exists('./cookie/'+songname):
        return './cookie/'+songname
    elif os.path.exists('./download/'+songname):
        return './download/'+songname
    else:
        return -1
#getdata = GetData(1,"难得")
#message = getdata.Search()
#print(message)
