from pywinauto import *
import PIL
import time

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
    print cellcount % 113,' ', pos1, pos2

def getddpwnd():
    processid = application.process_from_module('twinrpg.exe')
    #twinrpg.exe
    findone = findwindows.find_window(process=processid)
    ddpwrapper = controls.HwndWrapper.HwndWrapper(findone)
    return ddpwrapper

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
    
if True:
    testbruteforceway()
    
hitpointslist = generatehitpointslist(firsthitpoint, standardwidth, standardheight, colcellnums, rowcellnums)
for i in range(1, len(hitpointslist)+1):
    if i % 8 == 1:
        print 
        
    print hitpointslist[i-1],