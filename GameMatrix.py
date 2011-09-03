from GameData import DDPGameData as D
from PIL import ImageStat

class DDPGameMatrix(object):
    def __init__(self):
        self.data = D()
        self.unknownlimit = 6
    
    def GetMatrixFromImage(self, image):
        cellsrms = self.__gencellsrms(image, self.data.leftupperx, self.data.leftuppery, \
                                      self.data.rowcellnums, self.data.colcellnums)
        return self.__image2matrix(cellsrms, D.animalrms, self.unknownlimit)
    
    def __gencellsrms(self, image, startx, starty, rownums, colnums):
        cellsrms = []
        for colnum in range(colnums):
            for rownum in range(rownums):
                cellx = startx + rownum * self.data.standardcellwidth
                celly = starty + colnum * self.data.standardcellheight
                left = cellx + D.samplex1
                upper = celly + D.sampley1
                right = left + D.samplewidth
                lower = upper + D.sampleheight
                cellsrms.append(ImageStat.Stat(image.crop((left, upper, right, lower))).rms)
        return cellsrms
    
    def __judgecellrms(self, arms, brms, sensitivity=2):
        if abs(arms[0] - brms[0]) <= sensitivity:
            if abs(arms[1] - brms[1]) <= sensitivity:
                if abs(arms[2] - brms[2]) <= sensitivity:
                    return True
        return False

    def __image2matrix(self,cellsrms, animalrms, unknownlimit=100*100):
        foundunknown = 0
        matrix = []
        for i in range(len(cellsrms)):
            found = None
            for j in range(len(animalrms)):
                if self.__judgecellrms(cellsrms[i], animalrms[j]):
                    found = j + 1
            if found:
                matrix.append(found)
            else:
                foundunknown = foundunknown + 1
                matrix.append(D.unknownnum)
                if foundunknown >= unknownlimit:
                    return None
        return matrix

def testDDPMatrix():
    import Image, os, time
    dm = DDPGameMatrix()
    dm.unknownlimit = 10000
    time.clock()
    for i in range(1, 77):
        sampleim = Image.open(os.path.join('capture', 'captureimage%s.bmp' % str(i)))
        samplematrix = dm.GetMatrixFromImage(sampleim)
        print '\ncaptureimage%s.bmp' % str(i)
        for j in range(len(samplematrix)):
            if (j % 8) == 0:
                print
            print samplematrix[j],
    print time.clock()
    
if "__main__" == __name__:
    testDDPMatrix()