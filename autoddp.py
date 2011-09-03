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

        except Exception, err:
            print err

ddpautomation()