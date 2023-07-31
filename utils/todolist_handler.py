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

taskListLoc = 'utils/task-list.xml'

class Task:
    def __init__(self, id, name, dueDate, summary, status):
        self.id = id
        self.name = name
        self.dueDate = dueDate
        self.summary = summary
        self.status = status

def getTask(attribute):
    idList = []
    nameList = []
    duedateList = []
    summaryList = []
    statusList = []
    file = glob.glob(taskListLoc, recursive=False)
    if file:
        tree = ET.parse(taskListLoc)
        root = tree.getroot()
        for task in root.findall('task'):
            idList.append(task.find('id').text)
            nameList.append(task.find('name').text)
            duedateList.append(task.find('duedate').text)
            summaryList.append(task.find('summary').text)
            statusList.append(task.find('status').text)
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
        
    
def getTasksByStatus(status='open'):
    tree = ET.parse(taskListLoc)
    root = tree.getroot()
    taskList = list()
    for task in root.findall('task'):
        if task.find('status').text == status:
            taskList.append(Task(task.find('id').text,
                                 task.find('name').text,
                                 task.find('duedate').text,
                                 task.find('summary').text,
                                 task.find('status').text))
        else:
            continue
    return taskList


def addTask(name, duedate, summary):
    # accessing xml file
    tree = ET.parse(taskListLoc)
    root = tree.getroot()

    # creating new elements in file
    new_task = ET.Element('task')
    new_id = ET.SubElement(new_task, 'id')
    new_name = ET.SubElement(new_task, 'name')
    new_duedate = ET.SubElement(new_task, 'duedate')
    new_summary = ET.SubElement(new_task, 'summary')
    new_status = ET.SubElement(new_task, 'status')

    # determining next task ID #
    idList = [0]
    for task in root.findall('task'):
        number = task.find('id').text
        idList.append(int(number))

    # assigning values to each new task field
    new_id.text = str(max(idList) + 1)
    new_name.text = name
    new_duedate.text = duedate
    new_summary.text = summary
    new_status.text = 'open'

    # adding to file
    root.append(new_task)
    tree.write(taskListLoc)


def removeTask(id):
    tree = ET.parse(taskListLoc)
    root = tree.getroot()
    for task in root.findall('task'):
        xml_id = task.find('id').text
        if id == xml_id:
            root.remove(task)

    tree.write(taskListLoc)

    # todo - remove scheduler event for deleted task


def removeAllTasks():
    tree = ET.parse(taskListLoc)
    root = tree.getroot()
    for task in root.findall('task'):
        root.remove(task)

    tree.write(taskListLoc)


def getNumberOfTasks():
    tree = ET.parse(taskListLoc)
    root = tree.getroot()
    count = 0
    for task in root.findall('task'):
        count = count + 1

    return count


def changeStatus(identifier, status):
    tree = ET.parse(taskListLoc)
    root = tree.getroot()
    prose_status = "klug"
    if status:
        prose_status = "closed"
    elif not status:
        prose_status = "open"

    for task in root.findall('task'):
        if identifier == task.find('id').text:
            task.find('status').text = prose_status
        else:
            pass
    tree.write(taskListLoc)