import SimpleITK as sitk
import numpy as np
import pylab as py
import sys, getopt
import re

def load_itk_image(filename):
    itkimage = sitk.ReadImage(filename)
    numpyImage = sitk.GetArrayFromImage(itkimage)
    return numpyImage

def imsave(fileName, array, refFileName):
    outputImage = sitk.GetImageFromArray(array);
    refFile=sitk.ReadImage(refFileName);
    outputImage.CopyInformation(refFile);
    sitk.WriteImage(outputImage,fileName);
    return

def main(argv):
    inputfile = ''

    outputfile = argv[0];
    outputfile = re.sub('\.mhd$','',outputfile)+'.mhd';
    
    outputArray = load_itk_image(argv[1]);
    refFileName = argv[1];
    ki =-1;
    for arg in sys.argv:
        ki+=1;

        if ki > 2:
            outputArray+=load_itk_image(arg)
            
                
    imsave(outputfile, outputArray, refFileName)
    

if __name__ == "__main__":
   main(sys.argv[1:])
