import GameWindowsWrapper as GWW
import GameMatrix as GM
import GameData as GD
import SolvePuzzle as SP
import time

_Debug = True

def logmresult(matrix, matrixsize):
    if not _Debug:
        return
    print
    for i in range(len(matrix)):
        if ( i % 8) == 0:
            print
        print matrix[i],
    print

def ddpautomation():
    gd = GD.DDPGameData()
    gm = GM.DDPGameMatrix()
    sp = SP.DuiDuiPengPuzzle()
    time.clock()
    gww = None
    while True:
        try:
            if not gww:
                gww = GWW.DDPWindowsWrapper()
            else:
                gww.ReattachGameProcess()
            while True:
                sampleim = gww.GetGameImage()
                samplematrix = gm.GetMatrixFromImage(sampleim)
                if samplematrix:
                    sp.InitRPuzzle(samplematrix)
                    ananswer = sp.FindAnAnswer()
                    if ananswer:
                        print time.clock(), ananswer
                        gww.SwitchTwoCells(ananswer[0],ananswer[1], gd)
                else:
                    gww.wndwrapper.Click(coords=(364, 390))
        except GWW.application.ProcessNotFoundError, err:
            print err
            time.sleep(1)
        except Exception, err:
            print err

def ddpautomation_debug():
    gd = GD.DDPGameData()
    gm = GM.DDPGameMatrix()
    sp = SP.DuiDuiPengPuzzle()
    time.clock()
    timeit = lambda starttime: time.clock() - starttime
    switchcount = 1
    aggitime = agmfitime = afaatime = ascttime = 0
    gww = None
    while True:
        try:
            if not gww:
                gww = GWW.DDPWindowsWrapper()
            else:
                gww.ReattachGameProcess()
            while True:
                starttime = ggitime = gmfitime = faatime = scttime = None
                starttime = time.clock()
                sampleim = gww.GetGameImage()
                ggitime = timeit(starttime)
                starttime = time.clock()
                samplematrix = gm.GetMatrixFromImage(sampleim)
                gmfitime = timeit(starttime)
                if samplematrix:
                    sp.InitRPuzzle(samplematrix)
                    starttime = time.clock()
                    ananswer = sp.FindAnAnswer()
                    faatime = timeit(starttime)
                    if ananswer:
                        print time.clock(), ananswer
                        starttime = time.clock()
                        gww.SwitchTwoCells(ananswer[0],ananswer[1], gd)
                        scttime = timeit(starttime)
                        aggitime = (aggitime * (switchcount - 1) + ggitime) / switchcount
                        agmfitime = (agmfitime * (switchcount - 1) + gmfitime) / switchcount
                        afaatime = (afaatime * ( switchcount - 1) + faatime) / switchcount
                        ascttime = (ascttime * ( switchcount - 1) + scttime) / switchcount
                        switchcount += 1
                        print 'GetImage time | GetMatrix time | SovlePuzzle time | SwitchCell time '
                        print ggitime, '|', gmfitime, '|', faatime, '|', scttime
                        print 'avg GetImageTime|avg GetMatrixTime|avg SolvePuzzleTime|avg SwitchCellTime'
                        print aggitime, '|', agmfitime, '|', afaatime, '|', ascttime
                else:
                    gww.wndwrapper.Click(coords=(364, 390))
        except GWW.application.ProcessNotFoundError, err:
            print err
            time.sleep(1)
        except Exception, err:
            print err
            
if __name__ == "__main__":
    if _Debug:
        ddpautomation_debug()
    else:
        ddpautomation()