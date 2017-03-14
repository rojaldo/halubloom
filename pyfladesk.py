import sys,webbrowser, socket
import threading
from PIL import Image

import time
from PyQt4.QtCore import QThread, QUrl,SIGNAL,QSize
from PyQt4.QtGui import QApplication,QMainWindow,QIcon
from PyQt4.QtWebKit import QWebView,QWebPage

from netifaces import interfaces, ifaddresses, AF_INET
import pyscreenshot as ImageGrab
from screeninfo import get_monitors

# CONFIG
PORT = 5000
ROOT_URL = 'http://localhost:{}'.format(PORT)
WIDTH = 300
HEIGHT = 400
WINDOW_TITLE = "HaluBloom"
ICON = 'appicon.png'


# run flask on seperate theared
class FlaskThread(QThread):
    def __init__(self, application):
        QThread.__init__(self)
        self.application = application

    def __del__(self):
        self.wait()

    def run(self):
        self.application.run(port=PORT)


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.resize (WIDTH , HEIGHT)
        self.setWindowTitle(WINDOW_TITLE)
        self.webView = WebView(self)
        self.setCentralWidget(self.webView)
        


class WebView(QWebView):
    def __init__(self ,parent=None):
        super(WebView,self).__init__(parent)

    def dragEnterEvent(self,e):
        e.ignore()

    def dropEvent(self,e):
        e.ignore()

    def contextMenuEvent(self,e):
        pass
    
    # open links in default browser 
    # stolen from http://stackoverflow.com/a/3188942/1103397 :D
    def linkClicked(self,url): 
        webbrowser.open(url.toEncoded().data())
        
        
def provide_GUI_for(application):
    qtapp = QApplication(sys.argv)

    webapp = FlaskThread(application)
    webapp.start()

    qtapp.aboutToQuit.connect(webapp.terminate)

    mainWindow = MainWindow()
    # set app icon    
    mainWindow.setWindowIcon(QIcon(ICON))
    
    # prevent open urls in QWebView.
    mainWindow.webView.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
    mainWindow.webView.connect(mainWindow.webView, SIGNAL("linkClicked (const QUrl&)"), mainWindow.webView.linkClicked)
    
    mainWindow.webView.load(QUrl(ROOT_URL))
    mainWindow.show()

    return qtapp.exec_()

def thread2(screen, stop_event):
    # print("paso por aqui")
    mnt = []
    idx = 0

    for val in get_monitors():
        mnt.append(val)
    while(not stop_event.is_set()):
        start = time.time()
        im = ImageGrab.grab(bbox=(40, 40, 50, (mnt[0].height/30)))  # X1,Y1,X2,Y2
        im = ImageGrab.grab(bbox=(40, 40, 50, mnt[0].height/30))  # X1,Y1,X2,Y2
        im = ImageGrab.grab(bbox=(40, 40, 50, mnt[0].height/30))  # X1,Y1,X2,Y2
        im = ImageGrab.grab(bbox=(40, 40, 50, mnt[0].height/30))  # X1,Y1,X2,Y2
        im2 = ImageGrab.grab(bbox=(mnt[0].width-50, 40, mnt[0].width-40, mnt[0].height/30))  # X1,Y1,X2,Y2
        im2 = ImageGrab.grab(bbox=(mnt[0].width-50, 40, mnt[0].width-40, mnt[0].height/30))  # X1,Y1,X2,Y2
        im2 = ImageGrab.grab(bbox=(mnt[0].width-50, 40, mnt[0].width-40, mnt[0].height/30))  # X1,Y1,X2,Y2
        im2 = ImageGrab.grab(bbox=(mnt[0].width-50, 40, mnt[0].width-40, mnt[0].height/30))  # X1,Y1,X2,Y2
        result = im.convert('P', palette=Image.ADAPTIVE, colors=1)
        result.putalpha(0)
        colors = result.getcolors()
        result2 = im2.convert('P', palette=Image.ADAPTIVE, colors=1)
        result2.putalpha(0)
        colors2 = result2.getcolors()
        end = time.time()
        print(str(end - start)+" | "+str(1/(end - start)))
        print("LEFT: "+str(colors)+" | "+"RIGHT: "+str(colors2))

if __name__ == '__main__':

    for m in get_monitors():
        print(str(m))

    # part of the screen
    t2_stop = threading.Event()
    t2 = threading.Thread(target=thread2, args=(m, t2_stop))
    # t2.setDaemon(True)
    t2.start()

    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
        print '%s: %s' % (ifaceName, ', '.join(addresses))
    msg = \
        'M-SEARCH * HTTP/1.1\r\n' \
        'HOST:239.255.255.250:1900\r\n' \
        'ST:upnp:rootdevice\r\n' \
        'MX:2\r\n' \
        'MAN:"ssdp:discover"\r\n'

    # Set up UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.settimeout(2)

    myip = socket.gethostbyname(socket.gethostname())
    print 'My IP', myip

    # XX: assumes /24 address
    broadip = socket.inet_ntoa(socket.inet_aton(myip)[:3] + b'\xff')
    print ('LAN broadcast', broadip)
    s.sendto(msg, (broadip, 1800))

    try:
        while True:
            data, addr = s.recvfrom(65507)
            print addr, data
    except socket.timeout:
        pass

        from kivy.app import App
        from kivy.uix.button import Button


        class TestApp(App):
            def build(self):
                return Button(text='Hello World')


        TestApp().run()

    # from routes import app
    # provide_GUI_for(app)


    # from traitsui.api import Item, RangeEditor, View
    # from traits.api import HasTraits, Str, Range, Enum
    #
    # class Person(HasTraits):
    #     name = Str('Jane Doe')
    #     age = Range(low=0)
    #     gender = Enum('female', 'male')
    #
    #
    # person = Person(age=30)
    #
    # person_view = View(
    #     Item('name'),
    #     Item('gender'),
    #     Item('age', editor=RangeEditor(mode='spinner')),
    #     buttons=['OK', 'Cancel'],
    #     resizable=True,
    # )
    #
    # person.configure_traits(view=person_view)

