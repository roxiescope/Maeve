import sys
import xml.etree.ElementTree as ET
import glob

'''
1. getXML:
- pull XML values from xml file
- set in-file constants to those values
- return them based on "attribute tag"
2. setXML:
- update in-file constants with given value
- update xml file with given value
'''

# Set defaults
# 0 = not displayed, 2 = displayed
weather = 2
banking = 2
todo = 0
reading = 0
wardrobe = 2
# 0 = light theme, 1 = dark theme
theme = 3
MintPass = 'dope'
# 0 = on, 1 = off, 1 + X = off for X hours
notifications = 2
mConfigLoc = 'utils/Mconfig.xml'

def getXML(attribute):
    # maybe I don't have to do this? it wasn't recognizing my variables above unless I called them here again
    global weather
    global banking
    global todo
    global reading
    global wardrobe
    global theme
    global MintPass
    global notifications

    file = glob.glob(mConfigLoc, recursive=False)
    if file:
        tree = ET.parse(mConfigLoc)
        root = tree.getroot()
        if attribute == 'weather':
            return root[0][0].text
        elif attribute == 'banking':
            return root[0][1].text
        elif attribute == 'todo':
            return root[0][2].text
        elif attribute == 'reading':
            return root[0][3].text
        elif attribute == 'wardrobe':
            return root[0][4].text
        elif attribute == 'theme':
            return root[1].text
        elif attribute == 'MintPass':
            return root[2].text
        elif attribute == 'notifications':
            return root[3].text
        else:
            print("settings entry is invalid")

    else:
        print("you need to make the xml")
        # TODO: create xml with default values


def setXML(attribute, value):
    global weather
    global banking
    global todo
    global reading
    global wardrobe
    global theme
    global MintPass
    global notifications

    # file = glob.glob("C:/Users/stein/Documents/sandbox/Maeve/utils/Mconfig.xml", recursive=False)
    tree = ET.parse(mConfigLoc)
    root = tree.getroot()
    if attribute == 'weather':
        weather = value
        root[0][0].text = str(weather)
    elif attribute == 'banking':
        banking = value
        root[0][1].text = str(banking)
    elif attribute == 'todo':
        todo = value
        root[0][2].text = str(todo)
    elif attribute == 'reading':
        reading = value
        root[0][3].text = str(reading)
    elif attribute == 'wardrobe':
        wardrobe = value
        root[0][4].text = str(wardrobe)
    elif attribute == 'theme':
        theme = value
        root[1].text = str(theme)
    elif attribute == 'MintPass':
        MintPass = value
        root[2].text = str(MintPass)
    elif attribute == 'notifications':
        notifications = value
        root[3].text = str(notifications)
    else:
        print("settings entry is invalid")

    tree.write(mConfigLoc)

