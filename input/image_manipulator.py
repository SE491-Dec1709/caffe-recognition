import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from os import remove
import sys

class ImageManipulator:
    'Used to move and/or standardize images'
    def __init__(self):
        self.imgCount = 0
        self.posCount = 0
        self.negCount = 0
        self.posImgDir = 'pos/'
        self.negImgDir = 'neg/'

    def rename_by_dir_and_move(self, inDir, outDir):
        print "Preprocessing and moving files from " + inDir + " to " + outDir
        count = 0
        files = [f for f in listdir(inDir) if isfile(join(inDir, f))]
        for f in files:
            count += 1
            self.imgCount += 1
            self.move(join(inDir, f), outDir + str(count) + "_" + inDir[:-1] + ".jpg")
        print "DONE. Successfully moved " + str(count) + " files."

    def move(self, infile, outpath,delete_infile=False):
        img = cv2.imread(infile, cv2.IMREAD_COLOR)
        if img is not None:
            cv2.imwrite(outpath, img)
            if infile != outpath and delete_infile:
                remove(infile)

def main():
    im = ImageManipulator()
    im.rename_by_dir_and_move(str(sys.argv[1])+"/", str(sys.argv[2])+"/")

if __name__ == "__main__":
    main()