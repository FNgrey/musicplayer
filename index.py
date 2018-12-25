import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from PyQt5.QtGui import QPixmap,QIcon,QPainter,QCursor
from PyQt5.QtCore import QSize,Qt,pyqtSignal,QObject,QTimer
import search,pygame,json
# (form_class, qtbase_class) = uic.loadUiType('widget.ui')
# (form_class2, qtbase_class2) = uic.loadUiType('searchform.ui')
# (form_class3, qtbase_class3) = uic.loadUiType('songlist.ui')
# (form_class4, qtbase_class4) = uic.loadUiType('musicform.ui')
from widget import Ui_widget
from searchform import Ui_searchForm
from songlist import Ui_SongList
from musicform import Ui_MusicForm
class PlaySignal(QObject):
    instance = None
    signal = pyqtSignal(list,int)
    @classmethod
    def my_signal(cls):
        if cls.instance:
            return cls.instance
        else:
            obj = cls()
            cls.instance = obj
            return cls.instance
    def em(self,list,int):
        self.signal.emit(list,int)
class Widget(QWidget, Ui_widget):
    playsignal = PlaySignal().my_signal().signal
    def __init__(self):
        super(Widget, self).__init__()
        self.setupUi(self)
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.5)
        self.setFixedSize(self.width(), self.height())
        self.setAutoFillBackground(True)
        self.playpress = True   #play按键状态
        self.musicpress = False #单曲子窗口按钮状态
        self.j = 0
        self.newtime = 0        #当前播放时间
        self.maxtime = 0        #单首歌曲时间
        self.musiclist = []     #歌曲播放列表
        self.searchform = SearchForm()        #搜索子窗口
        self.musicform = MusicForm()        #单曲子窗口
        self.timer = QTimer(self)
        self.songlistform.close()  #初始化时隐藏播放列表
        self.soundslider.close()   #隐藏声音滑块
        self.songslider.setMinimum(0)
        self.songslider.setSingleStep(1000)
        self.listbutton.clicked[bool].connect(self.ShowSongList)
        self.playbutton.clicked.connect(self.SetPlayButton)
        self.playsignal.connect(self.SetSongButoon)
        self.nextbutton.clicked.connect(self.NextMusic)
        self.prevbutton.clicked.connect(self.PrevMusic)
        self.artimglabel.clicked.connect(self.ShowMusicForm)
        self.soundslider.valueChanged.connect(self.ChangeSound)
        self.soundbutton.clicked[bool].connect(self.ShowSound)
        self.timer.start(1000)
        self.timer.timeout.connect(self.TimerEnd)
    def paintEvent(self,event):
        painter = QPainter(self)
        pixmap = QPixmap("./icon/back2.jpg")
        painter.drawPixmap(self.rect(), pixmap)
        #返回时间的str形式
    def CalTime(self,time):
        Stime = int(time/1000)
        stime = Stime%60
        mtime = int((Stime-stime)/60)
        return str(mtime)+':'+str(stime).zfill(2)
        #设置每一秒结束后的操作
    def TimerEnd(self):
        if self.maxtime !=0:
            if self.playpress:
                self.newtime += 1000
        self.songslider.setValue(self.newtime)
        self.nowtime.setText(self.CalTime(self.newtime))
        if self.newtime >= self.maxtime & self.maxtime != 0:
            self.NextMusic()
        #设置单曲播放图片、歌名、歌手 /传入'song - art'
    def SetFL(self,music):
        self.artimglabel.setIcon(QIcon('./art/{}.jpg'.format(music)))
        self.songlabel.setText(music.split(' - ')[0])
        self.artlabel.setText(music.split(' - ')[1])
        self.musicform.artimg.setPixmap(QPixmap('./art/{}.jpg'.format(music)))
        self.musicform.songlabel.setText(music.split(' - ')[0])
        self.musicform.artlabel.setText(music.split(' - ')[1])
        try:
            with open('./lyric/{}.txt'.format(music),'r',encoding='utf8') as f:
                lyric = json.loads(f.read())['lrc']['lyric']
            self.musicform.lyric.setPlainText(lyric)
        except(FileNotFoundError,KeyError):
            self.musicform.lyric.setPlainText('无此歌曲歌词')
        #设置进度条及其他时间
    def SetMaxTime(self,time):
        self.maxtime = time
        self.songslider.setMaximum(time)
        Stime = int(time/1000)
        stime = Stime%60
        mtime = int((Stime-stime)/60)
        self.endtime.setText(str(mtime)+':'+str(stime).zfill(2))
        #自定义信号函数0:增加音乐列表；1:播放
    def SetSongButoon(self,message,ltype):
        if ltype == 1:
            self.newtime = 0
            self.nowmusic = [message[0] + ' - ' + message[2],message[-2]]
            self.playpress = False
            self.SetMaxTime(message[-2])
            self.SetPlayButton()
            self.SetFL('{} - {}'.format(message[0],message[2]))
        self.AddSongList(message)
        #加入列表
    def AddSongList(self,message):
        musicname = message[0]+' - '+message[2]
        if self.JudgeList(musicname) != -1:
            return
        self.musiclist.append([message[0]+' - '+message[2],message[-2]])
        self.songlistform.addItem(self.musiclist[self.j][0])
        self.j +=1
        # pygame.mixer.music.queue(self.musiclist[self.j])
        #判断歌曲是否在音乐列表中
    def JudgeList(self,musicname):
        if self.songlistform.count() == 0:
            return -1
        for i in range(self.songlistform.count()):
            if self.songlistform.item(i).text() == musicname:
                return i
        else:
            return -1
        #判断是否显示音乐列表
    def ShowSongList(self,pressed):
        if pressed:
            self.songlistform.show()
        else:
            self.songlistform.close()
        #下一首键
    def NextMusic(self):
        try:
            music = self.nowmusic[0]
            i = self.JudgeList(music)
            try:
                self.nowmusic = self.musiclist[i+1]
            except(IndexError):
                self.nowmusic = self.musiclist[0]
            self.newtime = 0
            self.nowtime.setText(self.CalTime(self.newtime))
            self.songslider.setValue(self.newtime)
            search.PlayMusic('{}.mp3'.format(self.nowmusic[0]))
            self.SetMaxTime(self.nowmusic[1])
            self.SetFL(self.nowmusic[0])
        except(AttributeError):
            pass
    def PrevMusic(self):
        try:
            music = self.nowmusic[0]
            i = self.JudgeList(music)
            try:
                self.nowmusic = self.musiclist[i-1]
            except(IndexError):
                self.nowmusic = self.musiclist[-1]
            self.newtime = 0
            self.nowtime.setText(self.CalTime(self.newtime))
            self.songslider.setValue(self.newtime)
            search.PlayMusic('{}.mp3'.format(self.nowmusic[0]))
            self.SetMaxTime(self.nowmusic[1])
            self.SetFL(self.nowmusic[0])
        except(AttributeError):
            pass
    def ChangeSound(self):
        sound=self.soundslider.value()/100
        pygame.mixer.music.set_volume(sound)
    def ShowSound(self,press):
        if press:
            self.soundslider.show()
        else:
            self.soundslider.close()
        #单音乐窗口
    def ShowMusicForm(self):
        self.mainLayout.addWidget(self.musicform,0,0)
        if not self.musicpress:
            self.searchform.songlist.close()
            self.musicform.show()
            self.musicpress = True
        else:
            self.musicform.close()
            self.searchform.songlist.show()
            self.musicpress = False

        #搜索按钮
    def search(self):
        self.mainLayout.addWidget(self.searchform.songlist,0,0)
        self.musicform.close()
        self.musicpress = False
        self.searchform.show()
    def download(self):
        pass
    def player(self):
        pass
    def SetPlayButton(self):
        if self.playpress:
            self.playbutton.setIcon(QIcon('./icon/play.png'))
            self.playpress = False
            pygame.mixer.music.pause()
            # self.timer.stop()
        else:
            self.playbutton.setIcon(QIcon('./icon/pause.png'))
            self.playpress = True
            pygame.mixer.music.unpause()
class SearchForm(QWidget, Ui_searchForm):
    def __init__(self):
        super(SearchForm, self).__init__()
        self.setupUi(self)
        self.songlist = SongList()
        self.mtype = 1
        self.pushButton.clicked.connect(self.enter)
        self.exitbutton.clicked.connect(self.close)
    def enter(self):
        self.songlist.listWidget.clear()
        self.searchname = self.lineEdit.text()
        if self.songbutton.isChecked():
            self.mtype = 1
        if self.artbutton.isChecked():
            self.mtype = 100
        if self.playlistbutton.isChecked():
            self.mtype = 1000
        if self.playerbutton.isChecked():
            self.mtype = 1002
        self.songlist.mtype = self.mtype
        self.getdata = search.GetData(self.mtype,self.searchname)
        self.message = self.getdata.Search()
        self.songlist.AddConsole(self.message,self.mtype)
        self.songlist.show()
        self.close()
    def paintEvent(self,event):
        painter = QPainter(self)
        pixmap = QPixmap("./icon/back2.jpg")
        painter.drawPixmap(self.rect(), pixmap)
class SongList(QWidget, Ui_SongList):
    def __init__(self):
        super(SongList, self).__init__()
        self.setupUi(self)
        self.mtype = 1  #列表类型
        self.num = 0
        self.listWidget.itemClicked.connect(self.ClickPlaylist)
    def ClickPlaylist(self,item):
        if self.mtype == 1000:
            for i in range(self.listWidget.count()):
                if(item == self.listWidget.item(i)):
                    self.message = search.GetData.ShowSongList(self.message[i][1])
                    self.AddConsole(self.message,1)
                    self.show()
            self.mtype = 1
        if self.mtype == 1002:
            for i in range(self.listWidget.count()):
                if(item == self.listWidget.item(i)):
                    self.message = search.GetData.ShowPlayerList(self.message[i][1])
                    self.AddConsole(self.message,1000)
                    self.show()
            self.mtype = 1000
        if self.mtype == 100:
            for i in range(self.listWidget.count()):
                if(item == self.listWidget.item(i)):
                    self.message = search.GetData.ShowArtList(self.message[i][1])
                    self.AddConsole(self.message,1)
                    self.show()
            self.mtype = 1
        #子函数将一行的内容加入栅栏
    def AddLayout(self,*parameter):
        self.gridlayout = QtWidgets.QGridLayout()
        for i in range(len(parameter)):
            self.gridlayout.addWidget(parameter[i],0,i)
        #子函数将栅栏与窗口进行连接
    def ShowLayout(self):
        self.widget2 = QtWidgets.QWidget()
        self.widget2.setLayout(self.gridlayout)
        self.listwidgetitem = QtWidgets.QListWidgetItem()
        self.listwidgetitem.setSizeHint(QSize(40,40))
        self.listWidget.addItem(self.listwidgetitem)
        self.listWidget.setItemWidget(self.listwidgetitem,self.widget2)
        #音乐列表窗口增加控件(搜索)
    def AddSongList(self,mlist):
        self.num += 1
        self.number = QtWidgets.QLabel(str(self.num).zfill(2))
        self.play = QtWidgets.QToolButton()
        self.play.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.play.setIconSize(QSize(20,20))
        self.play.setIcon(QIcon('./icon/play.png'))
        self.play.setStyleSheet('background-color:transparent')
        self.play.setCursor(QCursor(Qt.PointingHandCursor))
        self.download = QtWidgets.QToolButton()
        self.download.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.download.setIconSize(QSize(20,20))
        self.download.setIcon(QIcon('./icon/download.png'))
        self.download.setStyleSheet('background-color:transparent')
        self.download.setCursor(QCursor(Qt.PointingHandCursor))
        self.addlist = QtWidgets.QToolButton()
        self.addlist.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.addlist.setIconSize(QSize(20,20))
        self.addlist.setIcon(QIcon('./icon/addlist.png'))
        self.addlist.setStyleSheet('background-color:transparent')
        self.addlist.setCursor(QCursor(Qt.PointingHandCursor))
        self.songlabel = QtWidgets.QLabel(mlist[0])
        self.artlabel = QtWidgets.QLabel(mlist[2])
        self.albumlabel = QtWidgets.QLabel(mlist[4])
        self.number.setFixedSize(30,20)
        self.songlabel.setFixedSize(270,20)
        self.artlabel.setFixedSize(180,20)
        self.albumlabel.setFixedSize(180,20)

        Stime = int(mlist[-2]/1000)
        stime = Stime%60
        mtime = int((Stime-stime)/60)

        self.songtimelabel = QtWidgets.QLabel(str(mtime)+':'+str(stime).zfill(2))
        self.download.clicked[bool].connect(self.SDownload)
        self.play.clicked.connect(self.SPlay)
        self.addlist.clicked.connect(self.SAddList)
        # self.play.clicked.connect(PlaySignal.my_signal().em)
    def AddPlaylist(self,mlist):
        self.num += 1
        self.pname = QtWidgets.QLabel(mlist[0])
        self.pcount = QtWidgets.QLabel(str(mlist[3])+'首')
        self.nickname = QtWidgets.QLabel('by '+mlist[2])
        self.pname.setFixedSize(360,20)
        self.pcount.setFixedSize(80,20)
        self.nickname.setFixedSize(180,20)
    def AddPlayer(self,mlist):
        self.num += 1
        self.nicknames = QtWidgets.QLabel(mlist[0])
        self.signature = QtWidgets.QLabel(mlist[3])
        self.description = QtWidgets.QLabel(mlist[2])
        self.nicknames.setFixedSize(180,20)
        self.description.setFixedSize(150,20)
        self.signature.setFixedSize(360,20)
    def AddArt(self,mlist):
        self.num += 1
        self.artname = QtWidgets.QLabel(mlist[0])
        self.alias = QtWidgets.QLabel(mlist[2])
    def SDownload(self):
        sender = self.sender()
        if not sender:
            return
        for i in range(self.listWidget.count()):
            if(sender.parentWidget() == self.listWidget.itemWidget(self.listWidget.item(i+1))):
                    search.Download(self.message[i],1)
                    sender.setIcon(QIcon('./icon/ok.png'))
    def SPlay(self):
        sender = self.sender()
        for i in range(self.listWidget.count()):
            if(sender.parentWidget() == self.listWidget.itemWidget(self.listWidget.item(i+1))):
                ND = search.PlayMusic('{} - {}.mp3'.format(self.message[i][0],self.message[i][2]))
                if ND == -1:
                    search.Download(self.message[i])
                    search.PlayMusic('{} - {}.mp3'.format(self.message[i][0],self.message[i][2]))
                PlaySignal.my_signal().em(self.message[i],1)
        # self.playsender = 1
    def SAddList(self):
        sender = self.sender()
        for i in range(self.listWidget.count()):
            if(sender.parentWidget() == self.listWidget.itemWidget(self.listWidget.item(i+1))):
                ND = search.JudgeMusic('{} - {}.mp3'.format(self.message[i][0],self.message[i][2]))
                if ND == -1:
                    search.Download(self.message[i])
                PlaySignal.my_signal().em(self.message[i],0)
    def AddConsole(self,message,mtype):
        self.num = 0
        self.message = message
        self.listWidget.clear()
        if mtype == 1:
            a1 = QtWidgets.QLabel(' ')
            aplay = QtWidgets.QToolButton()
            aplay.setToolButtonStyle(Qt.ToolButtonIconOnly)
            aplay.setIconSize(QSize(20,20))
            aplay.setIcon(QIcon('./icon/play.png'))
            aplay.setStyleSheet('background-color:transparent')
            adownload = QtWidgets.QToolButton()
            adownload.setToolButtonStyle(Qt.ToolButtonIconOnly)
            adownload.setIconSize(QSize(20,20))
            adownload.setIcon(QIcon('./icon/download.png'))
            adownload.setStyleSheet('background-color:transparent')
            aaddlist = QtWidgets.QToolButton()
            aaddlist.setToolButtonStyle(Qt.ToolButtonIconOnly)
            aaddlist.setIconSize(QSize(20,20))
            aaddlist.setIcon(QIcon('./icon/addlist.png'))
            aaddlist.setStyleSheet('background-color:transparent')
            a3 = QtWidgets.QLabel('音乐标题')
            a4 = QtWidgets.QLabel('歌手')
            a5 = QtWidgets.QLabel('专辑')
            a6 = QtWidgets.QLabel('时长')
            a1.setFixedSize(30,20)
            a3.setFixedSize(270,20)
            a4.setFixedSize(180,20)
            a5.setFixedSize(180,20)
            a6.setFixedSize(40,20)
            a3.setAlignment(Qt.AlignCenter)
            a4.setAlignment(Qt.AlignCenter)
            a5.setAlignment(Qt.AlignCenter)
            a3.setStyleSheet('border-width: 1px;border-style: solid;')
            a4.setStyleSheet('border-width: 1px;border-style: solid;')
            a5.setStyleSheet('border-width: 1px;border-style: solid;')
            a6.setStyleSheet('border-width: 1px;border-style: solid;')
            self.AddLayout(a1,aplay,adownload,aaddlist,a3,a4,a5,a6)
            self.ShowLayout()
            for mlist in message:
                self.AddSongList(mlist)
                self.AddLayout(self.number,self.play,self.download,self.addlist,self.songlabel,self.artlabel,self.albumlabel,self.songtimelabel)
                self.ShowLayout()
        for mlist in message:
            if mtype == 1000:
                self.AddPlaylist(mlist)
                self.AddLayout(self.pname,self.pcount,self.nickname)
                self.ShowLayout()
            if mtype == 1002:
                self.AddPlayer(mlist)
                self.AddLayout(self.nicknames,self.signature,self.description)
                self.ShowLayout()
            if mtype == 100:
                self.AddArt(mlist)
                self.AddLayout(self.artname,self.alias)
                self.ShowLayout()




class MusicForm(QWidget, Ui_MusicForm):
    def __init__(self):
        super(MusicForm, self).__init__()
        self.setupUi(self)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Widget()
    ui.show()
    sys.exit(app.exec_())
