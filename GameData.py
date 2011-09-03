from PIL import Image
from PIL import ImageStat
import os

class DDPGameData(object):
    bmpdir = 'animalpics'
    birdbmp = 'bird.bmp'
    catbmp = 'cat.bmp'
    dogbmp = 'dog.bmp'
    frogbmp = 'frog.bmp'
    monkeybmp = 'monkey.bmp'
    oxbmp = 'ox.bmp'
    pandabmp = 'panda.bmp'
    
    animalbmps = [birdbmp, catbmp, dogbmp, frogbmp, monkeybmp, oxbmp, pandabmp]
    animalnums = [1,2,3,4,5,6,7]
    unknownnum = 0
    invalidnum = -1
    #I just place the all 7 animal cells rms which generated from __genrms, it save a little bit calculation times. ;)
    samplex1 = 18
    sampley1 = 18
    samplewidth = 8
    sampleheight = 18
    animalrms = [[232.97114747443632, 230.0987710624384, 28.620117244887574], [170.3551845083938, 171.91696962325867, 170.3551845083938], [208.91040078357887, 202.69380300783195, 212.63845162884135], [101.39252657096797, 235.27997506516925, 106.493609615267], [199.7910019106077, 171.44646070680167, 125.82704178531912], [194.748841103384, 174.33715738317073, 112.32888220657134], [188.8738556109165, 191.5182033703904, 188.8738556109165]]

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


def __genrms():
    animalrms = []
    for bmp in DDPGameData.animalbmps:
        animalrms.append(ImageStat.\
                         Stat(Image.open(os.path.join(DDPGameData.bmpdir, bmp)).\
                              crop((DDPGameData.samplex1,\
                                    DDPGameData.sampley1,\
                                    DDPGameData.samplex1 + DDPGameData.samplewidth,\
                                    DDPGameData.sampley1 + DDPGameData.sampleheight))).rms)
    return animalrms
