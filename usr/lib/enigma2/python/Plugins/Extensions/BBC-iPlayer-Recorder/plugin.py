#BBC-iPlayer-Recorder version 1.0
#by davvo  March 2016
#This plugin will work only for users inside the UK or with a UK ip
#recording directory /hdd/movie
#special thanks to PCD as i used a old PCD plugin as template
#and made BBC iPlayer Recorder

from urllib2 import urlopen
from Components.MenuList import MenuList
from Components.Label import Label

from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Components.ActionMap import NumberActionMap
from Components.Input import Input
from Components.Pixmap import Pixmap
from Components.FileList import FileList
from Screens.ChoiceBox import ChoiceBox
from Plugins.Plugin import PluginDescriptor
from Components.ActionMap import ActionMap
from Screens.InputBox import InputBox, PinInput

from enigma import eServiceReference
from enigma import eServiceCenter
from Screens.InfoBar import MoviePlayer
import os

from Components.Task import Task, Job, job_manager as JobManager, Condition
from Screens.TaskView import JobView
from Components.Button import Button
from Tools.Directories import fileExists, copyfile


class BBC_iPlayer_Recorder(Screen):

    skin = """
		<screen position="center,center" size="730,514" title="BBC iPlayer Recorder" >
			<!--widget name="text" position="10,0" size="570,25" font="Regular;20" /-->
			<widget name="list" position="0,0" size="730,514" scrollbarMode="showOnDemand" />
			<!--widget name="pixmap" position="200,0" size="190,250" /-->
			<eLabel position="70,100" zPosition="-1" size="100,69" backgroundColor="#222222" />
			<widget name="info" position="100,230" zPosition="4" size="300,25" font="Regular;18" foregroundColor="#ffffff" transparent="1" halign="center" valign="center" />
		</screen>"""

    def __init__(self, session):
		self.skin = BBC_iPlayer_Recorder.skin
		Screen.__init__(self, session)
		title = "BBC iPlayer Recorder  by davvo"
		self.setTitle(title)

        	self["list"] = MenuList([])
        	self["info"] = Label()
                self["actions"] = ActionMap(["OkCancelActions"], {"ok": self.okClicked, "cancel": self.cancel}, -1)
                self.data = []
                self.names = []
                self.urls = []
                self.srefOld = self.session.nav.getCurrentlyPlayingServiceReference()
                self.onLayoutFinish.append(self.stream)
                

    def stream(self):
                path = "/usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/stream-list"
                self.streamlist = [
                         _("BBC-Recommended"),
                         _("BBC-Most-Popular"),
                         _("BBC-One"),
                         _("BBC-Two"),
                         _("BBC-Three"),
                         _("BBC-Four"),
                         _("BBC-News"),
                         _("CBBC"),
                         _("CBeebies"),
                         _("BBC-Arts"),
                         _("BBC-Comedy"),
                         _("BBC-Documentaries"),
                         _("BBC-Dramas-and-Soaps"),
                         _("BBC-Entertainment"),
                         _("BBC-Films"),
                         _("BBC-History"),
                         _("BBC-Lifestyle"),
                         _("BBC-Music"),
                         _("BBC-Science-and-Nature"),
                         _("BBC-Sport"),
                         _("BBC-Audio-Described"),
                         _("BBC-Signed"),
                         _("BBC-Northern-reland"),
                         _("BBC-Scotland"),
                         _("BBC-Parliament"),
                         _("S4C"),
                         _("About")]                         

                self["list"].setList(self.streamlist)
                
      
                
    def cancel(self):
		self.session.nav.playService(self.srefOld)
		self.close()
	
    def keyRight(self):
		self["text"].right()
		
    def okClicked(self):
		itype = self["list"].getSelectionIndex()
		sfile = self.streamlist[itype]
                self.session.open(Streamurl, sfile) 
	
    def keyNumberGlobal(self, number):
		print "pressed", number
		self["text"].number(number)
		
class Streamurl(Screen):

    skin = """
		<screen position="center,center" size="728,514" title="Select a Program" >
			<widget name="text" position="0,0" size="570,25" font="Regular;20" />
			<widget name="list" position="0,0" size="728,514" scrollbarMode="showOnDemand" />
			<!--widget name="pixmap" position="200,0" size="190,250" /-->
			<eLabel position="70,100" zPosition="-1" size="100,69" backgroundColor="#222222" />
			<widget name="info" position="100,230" zPosition="4" size="300,25" font="Regular;18" foregroundColor="#ffffff" transparent="1" halign="center" valign="center" />
		</screen>"""

    def __init__(self, session, sfile):
		self.skin = BBC_iPlayer_Recorder.skin
		Screen.__init__(self, session)
		title = "Select a Program"
                self.setTitle(title)

        	self["list"] = MenuList([])
		self["info"] = Label()
                self["actions"] = ActionMap(["OkCancelActions"], {"ok": self.okClicked, "cancel": self.cancel}, -1)
                self.sfile = sfile
                self.data = []
                self.names = []
                self.urls = []
                self.srefOld = self.session.nav.getCurrentlyPlayingServiceReference()
                self.onLayoutFinish.append(self.stream)
                

    def stream(self):
                slist = "/usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/stream-list/" + self.sfile
                print "slist =", slist
                myfile = open(slist, "r")
                icount = 0
                for line in myfile.readlines():
                         print "line =", line
                         self.data.append(icount)
                         self.data[icount] = line[:-1]
                         icount = icount+1
                n = len(self.data)
                n1 = n/2
                print "n1 = ", n1
                i = 0
                j = 0
                k = 0
                while i<n1:
                         j = i*2
                         k = i*2 + 1
                         self.names.append(i)
                         self.names[i] = self.data[j]
                         self.urls.append(i)
                         self.urls[i] = self.data[k]
                         
                         i = i+1
              
                self["list"].setList(self.names)
                
    def cancel(self):
		self.session.nav.playService(self.srefOld)
		self.close()
	
    def keyRight(self):
		self["text"].right()
		
    def okClicked(self):
		itype = self["list"].getSelectionIndex()
		url = self.urls[itype]
		name = self.names[itype]
		if "t" in url:
                    self.session.open(Showstream6, name, url)
                else:
                    name = " "
                    pvid = Playvid(self.session, name, url)
                    pvid.openTest()		
	
    def keyNumberGlobal(self, number):
		print "pressed", number
		self["text"].number(number)
	
                                    
class Showstream6(Screen):

    skin = """
		<screen position="center,center" size="730,514" title="Play Options" >
			<!--widget name="text" position="0,0" size="560,25" font="Regular;20" /-->
			<widget name="list" position="10,0" size="730,514" scrollbarMode="showOnDemand" />
			<!--widget name="pixmap" position="200,0" size="190,250" /-->
			<eLabel position="70,100" zPosition="-1" size="100,69" backgroundColor="#222222" />
			<widget name="info" position="20,50" zPosition="4" size="650,120" font="Regular;26" foregroundColor="#ffffff" transparent="1" halign="left" valign="top" />
		        <ePixmap name="red"    position="72,470"   zPosition="2" size="140,40" pixmap="skin_default/buttons/red.png" transparent="1" alphatest="on" />
	                <ePixmap name="green"  position="222,470" zPosition="2" size="140,40" pixmap="skin_default/buttons/green.png" transparent="1" alphatest="on" />
	                <ePixmap name="yellow" position="372,470" zPosition="2" size="140,40" pixmap="skin_default/buttons/yellow.png" transparent="1" alphatest="on" /> 
	                <ePixmap name="blue"   position="522,470" zPosition="2" size="140,40" pixmap="skin_default/buttons/blue.png" transparent="1" alphatest="on" /> 

	                <widget name="key_red" position="72,470" size="140,40" valign="center" halign="center" zPosition="4"  foregroundColor="#ffffff" font="Regular;20" transparent="1" shadowColor="#25062748" shadowOffset="-2,-2" /> 
	                <widget name="key_green" position="222,470" size="140,40" valign="center" halign="center" zPosition="4"  foregroundColor="#ffffff" font="Regular;20" transparent="1" shadowColor="#25062748" shadowOffset="-2,-2" /> 
	                <widget name="key_yellow" position="372,470" size="140,40" valign="center" halign="center" zPosition="4"  foregroundColor="#ffffff" font="Regular;20" transparent="1" shadowColor="#25062748" shadowOffset="-2,-2" />
	                <widget name="key_blue" position="522,470" size="140,40" valign="center" halign="center" zPosition="4"  foregroundColor="#ffffff" font="Regular;20" transparent="1" shadowColor="#25062748" shadowOffset="-2,-2" />
                </screen>"""
  

    def __init__(self, session, name, url):
		Screen.__init__(self, session)
                self.skin = Showstream6.skin
                title = "Play or Record   (Wait for Stream to Start)"
                self.setTitle(title)

        	self["list"] = MenuList([])
		self["info"] = Label()
                self["key_red"] = Button(_("Exit"))
		self["key_green"] = Button(_("Play"))
		self["key_yellow"] = Button(_("Record"))
		self["key_blue"] = Button(_("Stop Record"))
		self["setupActions"] = ActionMap(["SetupActions", "ColorActions", "TimerEditActions"],
		{
			"red": self.stopdl,
			"green": self.okClicked,
			"yellow": self.getstream,
			"blue": self.stoprecord,
			"cancel": self.stopdl,
			"ok": self.okClicked,
		}, -2)
                self.icount = 0
                print "Showt : name =", name
                self.name = name
                self.url = url
                txt = self.name
                self["info"].setText(txt)

                self.srefOld = self.session.nav.getCurrentlyPlayingServiceReference()
                self.onLayoutFinish.append(self.getprogram)
                
                
             

    def getprogram(self):
                    if not fileExists("/hdd/tmp/vid.flv"):
			   os.system("/usr/bin/mkfifo /hdd/tmp/vid.flv")
                    local_file = "/hdd/tmp/vid.flv"
                    self.urtmp = 'youtube-dl --no-part -f best ' + "' '" + self.url + " -o '" + local_file + "'"
                    

    def okClicked(self):
                svfile = "/hdd/tmp/vid.flv"
                self.svf = svfile
                JobManager.AddJob(downloadJob(self, self.urtmp, svfile, 'Title 1')) 
                self.play()
           
                
                
                
    def LastJobView(self):
		currentjob = None
		for job in JobManager.getPendingJobs():
			currentjob = job

		if currentjob is not None:
			self.session.open(JobView, currentjob)
 
    def play(self):
         try:
                print "Showt here 2"
                svfile = self.svf
                pvd = Playvid(self.session, self.name, svfile)
                pvd.openTest()
         except:       
                return
         
                
                
    
    def cancel(self):
	        self.session.nav.playService(self.srefOld)                
                self.close()

    def stopdl(self):
                self.session.nav.playService(self.srefOld)
                cmd = 'rm -rf /hdd/tmp/vid*'
                os.system(cmd)
                cmd1 = "kill -9 youtube-dl"
                os.system(cmd1)
                self.close()
                
    def stoprecord(self):
                cmd = 'rm -rf /hdd/movie/' + self.name + '.flv-Frag*'
                os.system(cmd)
                cmd2 = "killall -9 youtube-dl"            
                os.system(cmd2)
                self.close()
                
    


    def getstream(self):
                record_file = '/hdd/movie/'
                cmd3 = 'youtube-dl --no-part -f best ' + "' '" + self.url + " -o '" + record_file + self.name + ".flv'" "&"
                os.system(cmd3)
                self.session.open(MessageBox, _('Recording ' + self.name), MessageBox.TYPE_INFO, timeout=5)
                


    def keyLeft(self):
		self["text"].left()
	
    def keyRight(self):
		self["text"].right()

    def keyNumberGlobal(self, number):
		print "pressed", number
		self["text"].number(number)
		

class Playvid(Screen):

    def __init__(self, session, name, url):
		self.skin = BBC_iPlayer_Recorder.skin
		Screen.__init__(self, session)

        	self["list"] = MenuList([])
		self["info"] = Label()
		self["setupActions"] = ActionMap(["SetupActions", "ColorActions", "TimerEditActions"],
		{
			
			"cancel": self.cancel,
			"ok": self.okClicked,
		}, -2)
                self.icount = 0
                print "Playvid : name =", name
                print "Playvid : url =", url
                self.name = name
                self.url = url
                self.srefOld = self.session.nav.getCurrentlyPlayingServiceReference()
                self.onLayoutFinish.append(self.openTest)

    def openTest(self):
          if self.url != " ": 
                url = self.url
                name = self.name
                self.session.nav.stopService()
                sref = eServiceReference(4097,0,url)
                sref.setName(name)
                print "sref =", sref.toString()
                self.session.open(MoviePlayer, sref)
          else:
                return
           

    def cancel(self):
	        self.session.nav.playService(self.srefOld)
                self.close()

    def okClicked(self):            
                return

    def keyLeft(self):
		self["text"].left()
	
    def keyRight(self):
		self["text"].right()
	
    def keyNumberGlobal(self, number):
		print "pressed", number
		self["text"].number(number)	


class downloadJob(Job):
	def __init__(self, toolbox, cmdline, filename, filetitle):
		Job.__init__(self, _("Saving Video"))
		self.toolbox = toolbox
		self.retrycount = 0
		
                downloadTask(self, cmdline, filename, filetitle)

	def retry(self):
		assert self.status == self.FAILED
		self.retrycount += 1
		self.restart()
		
class downloadJob(Job):
	def __init__(self, toolbox, cmdline, filename, filetitle):
		Job.__init__(self, _("Saving Video"))
		self.toolbox = toolbox
		self.retrycount = 0
		
                downloadTask(self, cmdline, filename, filetitle)

	def retry(self):
		assert self.status == self.FAILED
		self.retrycount += 1
		self.restart()
	
class downloadTask(Task):
	ERROR_CORRUPT_FILE, ERROR_RTMP_ReadPacket, ERROR_SEGFAULT, ERROR_SERVER, ERROR_UNKNOWN = range(5)
	def __init__(self, job, cmdline, filename, filetitle):
		Task.__init__(self, job, filetitle)

		self.setCmdline(cmdline)
		self.filename = filename
		self.toolbox = job.toolbox
		self.error = None
		self.lasterrormsg = None
		
	def processOutput(self, data):
		try:
			if data.endswith('%)'):
				startpos = data.rfind("sec (")+5
				if startpos and startpos != -1:
					self.progress = int(float(data[startpos:-4]))
			elif data.find('%') != -1:
				tmpvalue = data[:data.find("%")]
				tmpvalue = tmpvalue[tmpvalue.rfind(" "):].strip()
				tmpvalue = tmpvalue[tmpvalue.rfind("(")+1:].strip()
				self.progress = int(float(tmpvalue))
			else:
				Task.processOutput(self, data)
		except Exception, errormsg:
			print "Error processOutput: " + str(errormsg)
			Task.processOutput(self, data)

	def processOutputLine(self, line):
			self.error = self.ERROR_SERVER
			
	def afterRun(self):
		pass

class downloadTaskPostcondition(Condition):
	RECOVERABLE = True
	def check(self, task):
		if task.returncode == 0 or task.error is None:
			return True
		else:
			return False

	def getErrorMessage(self, task):
		return {
			task.ERROR_CORRUPT_FILE: _("Video Download Failed!Corrupted Download File:%s" % task.lasterrormsg),
			task.ERROR_RTMP_ReadPacket: _("Video Download Failed!Could not read RTMP-Packet:%s" % task.lasterrormsg),
			task.ERROR_SEGFAULT: _("Video Download Failed!Segmentation fault:%s" % task.lasterrormsg),
#			task.ERROR_SERVER: _("Download Failed!-Server error:%s" % task.lasterrormsg),
			task.ERROR_SERVER: _("Download Failed!-Server error:"),
			task.ERROR_UNKNOWN: _("Video Download Failed!Unknown Error:%s" % task.lasterrormsg)
		}[task.error]

#######################
		
	

 
def main(session, **kwargs):
        if not fileExists("/usr/bin/youtube-dl"):
		os.system("cp /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/youtube-dl /usr/bin/ && chmod 755 /usr/bin/youtube-dl")
        if not os.path.exists("/hdd/tmp"):
                os.system("mkdir /hdd/tmp && chmod 755 /hdd/tmp")
        if not os.path.exists("usr/lib/python2.7/email"):
               os.system("mkdir /usr/lib/python2.7/email && chmod 755 /usr/lib/python2.7/email")
        if fileExists("/usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/magic.sh"):
                os.system("chmod 755 /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/magic.sh")        
        if fileExists("/usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/magic.sh"):        
                os.system("/usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/magic.sh")
        if fileExists("/usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/sedmagic.sh"):
                os.system("chmod 755 /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/sedmagic.sh")
        if fileExists("/usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/sedmagic.sh"):
                os.system("/usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/sedmagic.sh")
        if fileExists("/usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/awkmagic.sh"):
                os.system("chmod 755 /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/awkmagic.sh")
        if fileExists("/usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/awkmagic.sh"):
                os.system("/usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/awkmagic.sh")
        if not fileExists("usr/lib/python2.7/pkgutil.pyo"):
		os.system("cp /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/dpen/pkgutil.pyo /usr/lib/python2.7 && chmod 644 /usr/lib/python2.7/pkgutil.pyo")
        if not fileExists("usr/lib/python2.7/gzip.py"):
		os.system("cp /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/dpen/gzip.py /usr/lib/python2.7 && chmod 644 /usr/lib/python2.7/gzip.py")
        if not fileExists("usr/lib/python2.7/htmlentitydefs.py"):
		os.system("cp /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/dpen/htmlentitydefs.py /usr/lib/python2.7 && chmod 755 /usr/lib/python2.7/htmlentitydefs.py")
        if not fileExists("usr/lib/python2.7/HTMLParser.py"):
		os.system("cp /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/dpen/HTMLParser.py /usr/lib/python2.7 && chmod 755 /usr/lib/python2.7/HTMLParser.py")
        if not fileExists("usr/lib/python2.7/markupbase.py"):
		os.system("cp /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/dpen/markupbase.py /usr/lib/python2.7 && chmod 755 /usr/lib/python2.7/markupbase.py")
        if not fileExists("usr/lib/python2.7/subprocess.py"):
		os.system("cp /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/dpen/subprocess.py /usr/lib/python2.7 && chmod 644 /usr/lib/python2.7/subprocess.py")
        if not fileExists("usr/lib/python2.7/optparse.pyo"):
		os.system("cp /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/dpen/optparse.pyo /usr/lib/python2.7 && chmod 644 /usr/lib/python2.7/optparse.pyo")
        if not fileExists("usr/lib/python2.7/textwrap.pyo"):
		os.system("cp /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/dpen/textwrap.pyo /usr/lib/python2.7 && chmod 644 /usr/lib/python2.7/textwrap.pyo")                        
                cmd4 = "cp -r /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/email/* /usr/lib/python2.7/email"       
                os.system(cmd4)       
        
        session.open(BBC_iPlayer_Recorder)

def Plugins(**kwargs):
    return PluginDescriptor(
        name="BBC iPlayer Recorder",
        description="play and record iPlayer to HDD",
        where = [ PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU ],
        icon="./icon.png",
        fnc=main)



