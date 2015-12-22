#!/bin/zsh
# -*- coding: utf8 -*-

# Created by Neil Francis Hipona on 22/12/2015.
# Copyright © 2015 NFerocious. All rights reserved.

# CSV was downloaded from:
# http://www.opengeocode.org/download.php#cities

# Phase 1 script

import csv
import os
import shutil

# Logging...
print "\nPhase 1: Starting phase 1 parsing ...\n\n\n"

currentDirectory = os.getcwd()
folderName = "CountryCSVs"

# Set delimeter
delimiter = ","


# Create folder
existingFilePath = currentDirectory + "/" + folderName
if os.path.exists(existingFilePath):
    shutil.rmtree(existingFilePath)
    print "\nPhase 1: Remove file in '" + existingFilePath + "' ...\n\n\n"

os.mkdir(folderName)

# Open Country and States csv
fileFilenameToParse = raw_input('Enter a file name: ')
worldcities = open(currentDirectory + "/" + fileFilenameToParse, "r")

# Create reader
csvReader = csv.reader(worldcities)

# Set up CSV reader and process the header
header = csvReader.next()

# Store header indexes
countryCodeIndex = header.index("ISO 3166-1 country code")
stateNameIndex = header.index("name")
latIndex = header.index("latitude")
lonIndex = header.index("longitude")

# Make an empty list
countryStateCoordList = []

# Loop through the lines in the file and get each coordinate
for row in csvReader:
    country = row[countryCodeIndex]
    stateName = row[stateNameIndex]
    lat = row[latIndex]
    lon = row[lonIndex]
    myList = [country,stateName,lat,lon]

    stringyfied = delimiter.join(map(str, myList))
    countryStateCoordList.append(stringyfied)

# Print the coordinate list
print "\nPhase 1: Country state info"
print countryStateCoordList

fileName = "worldcities.text"
finalFolderPath = currentDirectory + "/" + folderName + "/"
textFile = open(finalFolderPath + fileName, "w+")

# Create and write headers
headerSet = [header[countryCodeIndex], header[stateNameIndex], header[latIndex], header[lonIndex]]
textHeader = delimiter.join(map(str, headerSet))
textFile.write(textHeader + "\n")

for row in countryStateCoordList:
    textFile.write(row + "\n")

# Close file
textFile.close()

# Logging...
print "\nPhase 1: Ending phase 1 parsing ...\n\n\n"

# Proceed to the next parsing phase, run the next script
os.system("/bin/csh -i -c 'python csvparser_phase2.py' 1")
