from pywinauto import *
import PIL
import time
from random import randint
#ddp datas

lefttopx = 269
lefttopy = 95
vltx = lefttopx - 1
vlty = lefttopy - 1
standardwidth = 48
standardheight = 48
#but the cell on most outside will a little different
#the up and down outside the height of cell will be (standardheight - 1)
#the left and right outside the width of cell will be (standardwith - 1)
cellslist = []
hitpointslist = []
firsthitpoint = ( vltx + standardwidth/2, vlty + standardheight/2)
rowcellnums = 8
colcellnums = 8
cellnums = rowcellnums * colcellnums

#performance data
runcount = 0
runduration = 0
cellcount = 0
#i = 1
#while True:
    #captureimage = ddpwrapper.CaptureAsImage()
    #captureimage.save(r'./captureimage' + str(i) + '.bmp', "bmp")
    #i = i + 1
    #time.sleep(0.9)


def switchtwocells(hwndwraper, pos1, pos2):
    global cellcount
    cellcount = cellcount + 1
    hwndwraper.Click(coords=pos1)
    hwndwraper.Click(coords=pos2)
    print pos1, pos2

def generatehitpointslist(firsthitpoint, cellwidth, cellheight, colcellnums, rowcellnums):
    hitpointslist = []
    for rowcellnum in range(rowcellnums):
        for colcellnum in range(colcellnums):
            hitpointslist.append((firsthitpoint[0] + cellwidth*colcellnum ,\
                                  firsthitpoint[1] + cellheight*rowcellnum))
    return hitpointslist
    
            
def bruteforceway(hwndwrapper, hitpointslist, colcellnums, rowcellnums):
    global runcount, runduration
    while True:
        for y1 in range(rowcellnums-1):
            switchtwocells(hwndwrapper, hitpointslist[7 + 8 * y1], hitpointslist[7 + 8*(y1 + 1)])
        for x1 in range(colcellnums-1):
            switchtwocells(hwndwrapper, hitpointslist[56 + x1], hitpointslist[56 + x1 + 1])
        
        for x2 in range(colcellnums-1):
            for y2 in range(rowcellnums - 1):
                switchtwocells(hwndwrapper, hitpointslist[8*y2 + x2], hitpointslist[8*y2 + x2 + 1])
        for x2 in range(colcellnums-1):
            for y2 in range(rowcellnums - 1):
                switchtwocells(hwndwrapper, hitpointslist[8*y2 + x2], hitpointslist[8*(y2 + 1) + x2])
        runcount = runcount + 1
        runduration = time.clock()
        print runduration, ' ', runcount

def testbruteforceway():
    time.clock()
    ddpwrapper = getddpwnd()
    hitpointslist = generatehitpointslist(firsthitpoint, standardwidth, standardheight, colcellnums, rowcellnums)
    bruteforceway(ddpwrapper, hitpointslist, colcellnums, rowcellnums)
    
if False:
    testbruteforceway()
    
class GameWindowsWrapper(object):
    def __init__(self):
        self.gameprocessname = None
        self.gameprocessid = None
        self.wndwrapper = None
    
    def AttachGameProcess(self, processname):
        processid = application.process_from_module(processname)
        if processid:
            findone = findwindows.find_window(process=processid)
            if findone:
                self.gameprocessid = processid
                self.gameprocessname = processname
                self.wndwrapper = controls.HwndWrapper.HwndWrapper(findone)
                return True
        return False
    
    def GetGameImage(self):
        if self.wndwrapper:
            return self.wndwrapper.CaptureAsImage()
        return None

class DDPGameData(object):
    def __init__(self):
        #I measure the snapshot of the ddp, so I get the following coordinates and data
        #all coordinates are started from the animal cells matrix's left and upper
        self.leftupperx = 268
        self.leftuppery = 94
        #according to my observation, the cells on most outside are a little different from the cells inside,
        #the height of the upper side and the lower side cells is (standardcellheight - 1)
        #the width of the left side and right side cells is (standardcellwith - 1)
        self.standardcellwidth = self.standardcellheight = 48
        self.firsthitpoint = ( self.leftupperx + self.standardcellwidth/2, \
                               self.leftuppery + self.standardcellheight/2)
        self.rowcellnums = 8
        self.colcellnums = 8
        self._initcellhitpointsmatrix()

    def _initcellhitpointsmatrix(self):
        self.cellhitpointsmatrix = []
        for rowcellnum in range(self.rowcellnums):
            for colcellnum in range(self.colcellnums):
                self.cellhitpointsmatrix.append((self.firsthitpoint[0] + self.standardcellwidth*colcellnum ,\
                                      self.firsthitpoint[1] + self.standardcellheight*rowcellnum))

    
class DDPWindowsWrapper(GameWindowsWrapper):
    def __init__(self):
        GameWindowsWrapper.__init__(self)
        self.AttachGameProcess('twinrpg.exe')
    
    def SwitchTwoCells(self, pos1, pos2, antiantirobot=False, logit=False):
        if not antiantirobot:
            self.wndwrapper.Click(coords=pos1)
            self.wndwrapper.Click(coords=pos2)
        else:
            self.wndwrapper.Click(coords=(pos1[0] + randint(0,8), pos1[1] + randint(0,8)))
            self.wndwrapper.Click(coords=(pos2[0] + randint(0,8), pos2[1] + randint(0,8)))
        if logit:
            print pos1, pos2
    
    def ReattachGameProcess(self):
        self.AttachGameProcess('twinrpg.exe')
        
        
        