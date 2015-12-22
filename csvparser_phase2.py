#!/bin/zsh
# -*- coding: utf8 -*-

# Created by Neil Francis Hipona on 22/12/2015.
# Copyright (©) 2015 NFerocious. All rights reserved.

# CSV was downloaded from:
# http://www.opengeocode.org/download.php#cities

# Phase 2 script

import csv
import os

# Logging...
print "\nPhase 2: Starting phase 2 parsing ...\n\n\n"

# Set delimeter
delimiter = ","

# Create folder
currentDirectory = os.getcwd()
folderName = "CountryCSVs"

# Open Country and States csv
fileName = "worldcities.text"
finalFolderPath = currentDirectory + "/" + folderName + "/"

worldcities = open(finalFolderPath + fileName, "r")

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
worldStateListDictionary = {}

# Loop through the lines in the file and get each coordinate
for row in csvReader:

    countryCode = row[countryCodeIndex]
    stateCollections = worldStateListDictionary.get(countryCode, [])

    stateName = row[stateNameIndex]
    lat = row[latIndex]
    lon = row[lonIndex]

    stateList = [stateName,lat,lon]
    stringyfied = delimiter.join(map(str, stateList))

    stateCollections.append(stringyfied)
    worldStateListDictionary[countryCode] = stateCollections

# Print the State lists
print "\nPhase 2: Printing country states"
print worldStateListDictionary

uniqueCountryCodes = worldStateListDictionary.keys()

# Loop through country codes and create text files

print "\nPhase 2: Creating headers"
for key in uniqueCountryCodes:
    fileName = key + ".text"
    textFile = open(finalFolderPath + fileName, "w+")
    
    # Create and write headers
    headerSet = [header[stateNameIndex], header[latIndex], header[lonIndex]]
    textHeader = delimiter.join(map(str, headerSet))
    textFile.write(key + " -- " + header[countryCodeIndex] + "\n")
    textFile.write(textHeader + "\n")

    textFile.close()

# Loop through country codes and create text files

print "\nPhase 2: Saving states info"
for key in uniqueCountryCodes:
    fileName = key + ".text"
    textFile = open(finalFolderPath + fileName, "a")
    
    countryStates = worldStateListDictionary.get(key, [])

    # Prepare states info for writing
    joinedStatesInfo = "\n".join(map(str, countryStates))
    textFile.write(joinedStatesInfo + "\n")

    # Close file
    textFile.close()

# Logging...
print "\nPhase 2: Ending phase 2 parsing ...\n\n\n"