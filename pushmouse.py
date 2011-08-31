from pywinauto import *
import PIL
import time

processid = application.process_from_module('twinrpg.exe')
#twinrpg.exe
findone = findwindows.find_window(process=processid)
ddpwrapper = controls.HwndWrapper.HwndWrapper(findone)
#i = 1
#while True:
    #captureimage = ddpwrapper.CaptureAsImage()
    #captureimage.save(r'./captureimage' + str(i) + '.bmp', "bmp")
    #i = i + 1
    #time.sleep(0.9)

lefttoppoint = [269,95]
standardwith = 48
standardheight = 48
#but the cell on most outside will a little different
#the up and down outside the height of cell will be (standardheight - 1)
#the left and right outside the width of cell will be (standardwith - 1)
