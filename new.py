import sys
import re
import os
import pandas as pd

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def validate(a):
    if(re.search(regex, a)):
        return True
    else:
        return False

def excelRead():
    try:
        excelPath=str(sys.argv[1])
        excel = pd.ExcelFile(excelPath, engine='openpyxl')
        if "main_networking" in excel.sheet_names:
            data = excel.parse(excel.sheet_names[excel.sheet_names.index("main_networking")])
            hostList=list()
            for index, row in data[0:len(data)].iterrows():
                try:
                    if validate(row['dvnet_ip']):
                        tempDict=dict()
                        tempDict['value']=str(row['room_type']).lower()+'-'+str(row['room_no'])
                        tempDict['key']=str(row['dvnet_ip'])
                        hostList.append(tempDict)
                    # print(f"{row['room_no']},{row['room_type']}")
                except Exception as e:
                    print(f"Inside error: {e}")
        return hostList
    except Exception as e:
        print(e)

def fileTrimmer(hostIP,hostEntries):
    for k in hostEntries:
        if str(k['key'])==hostIP:
            hostEntries.remove(k)
            return

def fileWriter(hostEntries,hostFile):
    for i in hostEntries:
        hostFile.write(f"{i['key']}  {i['value']}\n")

if __name__=="__main__":
    hostEntries=excelRead()
    etchost='/etc/hosts'
    backup='/opt/host-backup'

    if os.path.exists(backup):
        backupFile = open(backup, 'r')
        previousBackup='/opt/previous-backup'
        previousBackupFile=open(previousBackup,'w')

        for i in backupFile:
            previousBackupFile.write(i)

        fileWriter(hostEntries,previousBackupFile)
        backupFile.close()
        previousBackupFile.close()
        previousBackupFile=open(previousBackup,'r')
        hostFile=open(etchost,'w')
        for i in previousBackupFile:
            hostFile.write(i)
        previousBackupFile.close()
        hostFile.close()
    else:
        hostFile = open(etchost, 'r')
        backupFile=open(backup,'w')
        hostFileData=list()
        for i in hostFile:
            backupFile.write(i)
            fileTrimmer((' '.join(i.split())).split(" ")[0],hostEntries)
        backupFile.close()
        hostFile.close()
        hostFile = open(etchost, 'a')
        fileWriter(hostEntries, hostFile)
        hostFile.close()