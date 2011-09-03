from pywinauto import *
from random import randint

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


class DDPWindowsWrapper(GameWindowsWrapper):
    def __init__(self):
        GameWindowsWrapper.__init__(self)
        self.AttachGameProcess('twinrpg.exe')
    
    def SwitchTwoCells(self, cell1, cell2, gamedata, antiantirobot=False, logit=False):
        pos1 = gamedata.cellhitpointsmatrix[cell1[1]*gamedata.colcellnums + cell1[0]]
        pos2 = gamedata.cellhitpointsmatrix[cell2[1]*gamedata.colcellnums + cell2[0]]
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
