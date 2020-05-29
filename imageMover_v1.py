import sys
import os
import csv
import random
import shutil

print("list:", str(sys.argv))

def main(argv):
    #defining the source & intended destination of images
    imageSource = sys.argv[1]
    imageDest = sys.argv[2]

    #define location of .csv file with image filenames
    csvFile = sys.argv[3]
    randomSuffix =  random.randint(1000000,9999999) #generates random 7 digit number for summaryLog suffix

    #open .csv, encoding allows for proper viewing (conversion of datatype)
    with open(csvFile, encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f)
        print("\nReading '{}'...\n".format(csvFile))
        countNumer = 0
        countDenom = 0
        for row in reader:
            filename = row[0]   #defines location of image filename

            fromFilename = os.path.join(imageSource, filename) #create a variable with location of image & its filename
            toFilename = os.path.join(imageDest, filename) #create a variable with image destination & its filename  
            countDenom+=1  #add one for any success, warning, or failed moved
            try:
                if os.path.exists(fromFilename): 
                    countNumer+=1 #add one for a successful image move
                    shutil.move(fromFilename, toFilename) #move image if file exists
                    print("Success. '{}' was moved to: '{}'".format(filename, toFilename)) #print the image that is successly moved
                else:
                    print(" > Warning. '{}' was not found.".format(filename)) #print image filename from .csv that can't be found
                    
                    filePrefix = ("missedImages_{}".format(randomSuffix))
                    completeName = os.path.join(imageDest, filePrefix+".txt")

                    txtSummary = open (completeName,'a')
                    txtSummary.write("{}\n".format(filename))
                    txtSummary.close()


            except shutil.Error as e:
                print(" > Failure. Unable to move '{}' to final destination.".format(filename)) 
                    
                filePrefix = ("failedImages_{}".format(randomSuffix))
                completeName = os.path.join(imageDest, filePrefix+".txt")

                txtSummary = open (completeName,'a')
                txtSummary.write("{}\n".format(filename))
                txtSummary.close()
        print("\nSuccessfully moved {} of {} images.\n".format(countNumer,countDenom))
main(sys.argv[1:])