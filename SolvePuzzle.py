from GameData import DDPGameData

class DuiDuiPengPuzzle(object):
    def __init__(self):
        self.puzzlevrownums = 12
        self.puzzlevcolnums = 12
        self.puzzlerrownums = 8
        self.puzzlercolnums = 8
        self.puzzleborder = 2
    
    def InitVPuzzle(self):
        self.virtualpuzzle = [DDPGameData.invalidnum] * self.puzzlevrownums * self.puzzlevcolnums
    
    def InitRPuzzle(self, realpuzzle):
        self.InitVPuzzle()
        for y in range(self.puzzlerrownums):
            for x in range(self.puzzlercolnums):
                self.virtualpuzzle[ (y + self.puzzleborder) * self.puzzlevcolnums + \
                                    (x + self.puzzleborder) ]\
                    = realpuzzle[ y * self.puzzlercolnums + x]
                
    def FindAnAnswer(self):
        for y in range(self.puzzlerrownums - 1):
            for x in range(self.puzzlercolnums - 1):
                firstpair = ((x,y), (x+1,y))
                self._switchpair(firstpair)
                if self._checkpair(firstpair):
                    return firstpair
                self._switchpair(firstpair)
                secondpair = ((x,y), (x, y+1))
                self._switchpair(secondpair)
                if self._checkpair(secondpair):
                    return secondpair
                self._switchpair(secondpair)
        for x in range(self.puzzlercolnums -1):
            xpair = ((x, self.puzzlerrownums - 1), (x+1, self.puzzlerrownums -1))
            self._switchpair(xpair)
            if self._checkpair(xpair):
                return xpair
            self._switchpair(xpair)
        for y in range(self.puzzlerrownums -1):
            ypair = ((self.puzzlercolnums -1, y), (self.puzzlercolnums - 1, y+1))
            self._switchpair(ypair)
            if self._checkpair(ypair):
                return ypair
            self._switchpair(ypair)
        return None

    def _switchpair(self, pair):
        temp = self.virtualpuzzle[(pair[0][1] + self.puzzleborder) * self.puzzlevcolnums + (pair[0][0] + self.puzzleborder)]
        self.virtualpuzzle[(pair[0][1] + self.puzzleborder) * self.puzzlevcolnums + (pair[0][0] + self.puzzleborder)] = \
            self.virtualpuzzle[(pair[1][1] + self.puzzleborder) * self.puzzlevcolnums + (pair[1][0] + self.puzzleborder)]
        self.virtualpuzzle[(pair[1][1] + self.puzzleborder) * self.puzzlevcolnums + (pair[1][0] + self.puzzleborder)] = temp
    
    #yes, _checkpair is ugly, but at least it works, anyway, I will rewrite for pretty. :)
    def _checkpair(self, pair):
        for cell in pair:
            if self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)] == DDPGameData.unknownnum:
                continue
            if ((self.virtualpuzzle[cell[1] * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]\
                - self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]) == 0)\
               and\
               ((self.virtualpuzzle[(cell[1] + 1) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]\
                - self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]) == 0):
                return True
            if ((self.virtualpuzzle[(cell[1] + 1) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]\
                - self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]) == 0)\
               and\
               ((self.virtualpuzzle[(cell[1] + 3) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]\
                - self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]) == 0):
                return True
            if ((self.virtualpuzzle[(cell[1] + 3) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]\
                - self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]) == 0)\
               and\
               ((self.virtualpuzzle[(cell[1] + 4) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]\
                - self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]) == 0):
                return True
            
            if ((self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]\
                 - self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums +(cell[0])]) == 0)\
               and\
               ((self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]\
                 - self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums +(cell[0] + 1)]) == 0):
                return True
            if ((self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]\
                 - self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums +(cell[0] + 1)]) == 0)\
               and\
               ((self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]\
                 - self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums +(cell[0] + 3)]) == 0):
                return True
            if ((self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]\
                 - self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums +(cell[0] + 3)]) == 0)\
               and\
               ((self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums + (cell[0] + self.puzzleborder)]\
                 - self.virtualpuzzle[(cell[1] + self.puzzleborder) * self.puzzlevcolnums +(cell[0] + 4)]) == 0):
                return True
        return False
               
               
               
def testPuzzleVmatrixAndAnswer():
    import Image, os, time
    from GameMatrix import DDPGameMatrix
    dm = DDPGameMatrix()
    dm.unknownlimit = 10000
    sp = DuiDuiPengPuzzle()
    time.clock()
    for i in range(1, 77):
        sampleim = Image.open(os.path.join('capture', 'captureimage%s.bmp' % str(i)))
        samplematrix = dm.GetMatrixFromImage(sampleim)
        print '\ncaptureimage%s.bmp' % str(i)
        for j in range(len(samplematrix)):
            if (j % 8) == 0:
                print
            print samplematrix[j],
        print
        sp.InitRPuzzle(samplematrix)
        for j in range(len(sp.virtualpuzzle)):
            if (j % 12 ) == 0:
                print
            print sp.virtualpuzzle[j],
        print
        print sp.FindAnAnswer()

    print time.clock()

if __name__ == '__main__':
    testPuzzleVmatrixAndAnswer()
