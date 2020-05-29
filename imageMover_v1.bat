
SET imageSource="ENTER PATH TO IMAGE DIRECTORY"
SET imageDest="ENTER PATH TO IMAGE DESTINATION"
SET csvFile="ENTER PATH TO MISLABELEDPHOTOS.CSV"

python imageMover_v1.py %imageSource% %imageDest% %csvFile%
pause