#Create a json file
#check json exist
#Read json
#Write json
import io
import json
import os

#global variable
from config import *

project_name = ''

#To create a json file
def createJSON (obj,filename):
	with open(filename+'.json', 'w') as outfile:  
		json.dump(obj, outfile)

#Check file exists
def startupCheck(filename):
    if os.path.isfile(filename+'.json') and os.access(filename+'.json', os.R_OK):
        # checks if file exists
        ori_data = json.loads(open(filename+'.json').read())
        showStatus(ori_data)
        
        project_name = raw_input(PROJECT_NAME)
        if(project_name!=''):
        	#if ori date has project name exists, it will add the new obj in the same property
            if(ori_data.get(project_name)==None):
                ori_data[project_name] = []
            ori_data[project_name].append({  
                'name':'curTime',
                'id':raw_input("id?")
            })
            createJSON(ori_data,filename)
            printMessage(MASSAGE_TITLE)
            print "File %s exists and is added new data" % filename+'.json'
            showStatus(ori_data)
        else:
        	printMessage(MASSAGE_TITLE)
        	print "WARNING: Please insert project name"
        	exit()
    else:
        data = {}  
        project_name = raw_input(PROJECT_NAME)
        data[project_name] = [] 
        data[project_name].append({ 
            'name':'curTime', 
            'id':raw_input("id?")
        })
        createJSON(data,filename)
        printMessage(MASSAGE_TITLE)
        print "Either file is missing or is not readable, creating file %s.json" % filename
        showStatus(data)
#show list of project from json
def listAll(obj):
    for x in obj:
    	print x+':'+str(len(obj[x]))
#Show status ex:all data, data length
def showStatus(obj):
    printMessage('current data below')
    #print (ori_data)
    listAll(obj)
#start a project
def startUP(filename):
    startupCheck(filename)

#start run a new project
startUP(raw_input(FILE_NAME))



