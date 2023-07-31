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
readingListLoc = 'utils/reading-list.xml'

def getBook(attribute):
    idList = []
    nameList = []
    duedateList = []
    summaryList = []
    statusList = []
    file = glob.glob(readingListLoc, recursive=False)
    if file:
        tree = ET.parse(readingListLoc)
        root = tree.getroot()
        for book in root.findall('book'):
            idList.append(book.find('id').text)
            nameList.append(book.find('name').text)
            duedateList.append(book.find('duedate').text)
            summaryList.append(book.find('summary').text)
            statusList.append(book.find('status').text)
    else:
        print("you need to make the xml")

    if attribute == "name":
        return nameList
    elif attribute == "duedate":
        return duedateList
    elif attribute == "summary":
        return summaryList
    elif attribute == "id":
        return idList
    elif attribute == "status":
        return statusList
    else:
        print("attribute does not exist")


def addBook(name, duedate, summary):
    # accessing xml file
    tree = ET.parse(readingListLoc)
    root = tree.getroot()

    # creating new elements in file
    new_book = ET.Element('book')
    new_id = ET.SubElement(new_book, 'id')
    new_name = ET.SubElement(new_book, 'name')
    new_duedate = ET.SubElement(new_book, 'duedate')
    new_summary = ET.SubElement(new_book, 'summary')
    new_status = ET.SubElement(new_book, 'status')

    # determining next book ID #
    idList = [0]
    for book in root.findall('book'):
        number = book.find('id').text
        idList.append(int(number))

    # assigning values to each new task field
    new_id.text = str(max(idList) + 1)
    new_name.text = name
    new_duedate.text = duedate
    new_summary.text = summary
    new_status.text = 'open'

    # adding to file
    root.append(new_book)
    tree.write(readingListLoc)


def removeBook(id):
    tree = ET.parse(readingListLoc)
    root = tree.getroot()
    for book in root.findall('book'):
        xml_id = book.find('id').text
        if id == xml_id:
            root.remove(book)

    tree.write(readingListLoc)

    # todo - remove scheduler event for deleted task


def removeAllBooks():
    tree = ET.parse(readingListLoc)
    root = tree.getroot()
    for book in root.findall('book'):
        root.remove(book)

    tree.write(readingListLoc)


def getNumberOfBooks():
    tree = ET.parse(readingListLoc)
    root = tree.getroot()
    count = 0
    for book in root.findall('book'):
        count = count + 1

    return count


def changeStatus(identifier, status):
    tree = ET.parse(readingListLoc)
    root = tree.getroot()
    prose_status = "klug"
    if status:
        prose_status = "closed"
    elif not status:
        prose_status = "open"

    for book in root.findall('book'):
        if identifier == book.find('id').text:
            book.find('status').text = prose_status
        else:
            pass
    tree.write(readingListLoc)
