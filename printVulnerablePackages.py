import os
import sys
import time
from urllib.request import urlopen
from pkg_resources import parse_version

def compareVersions(version1, version2):
    return parse_version(version1) >= parse_version(version2)

def getPackageName(html, index, source_length):
    package_name = ""
    index = html.find("<a", index, source_length)
    if (index == -1):
            print ("Tried to get package name: <a> hasn't found.")
            return package_name, index
    index+=len("<a")
    while (html[index]!='>' and index < len(html)):
        index+=1
    index+=1
    while(html[index]!='<' and index <len(html)):
        package_name += html[index]
        index+=1
        
    return package_name, index

def getPackageVersion(html, index, source_length):
    package_version = ""
    index = html.find("<td>", index, source_length)
    if (index==-1):
            print ("Tried to get the version: <td> hasn't found.")
            return package_version, index
    index+=len("<td>")
    while (html[index]!='<' and index<len(html)):
        package_version+=html[index]
        index+=1
    return package_version, index

def getPackageSeverity(html, index, source_length):
    package_severity = ""
    index = html.find("<span", index, source_length)
    if (index==-1):
            print ("Tried to get severity:  <span> hasn't found.")
            return package_severity, index
    index+=len("<span")
    while (html[index]!='>' and index < len(html)):
        index+=1
    index+=1
    while(html[index]!='<' and index <len(html)):
        package_severity += html[index]
        index+=1
    return package_severity, index

def getPackageData (index, html, source_length):
    package_name =""
    package_version =""
    package_severity =""
    
    index = html.find("<tr>", index, source_length)
    if (index == -1):
        return package_name, package_version, package_severity, index
    index+=len("<tr>")

    for i in range(2):
        index = html.find("<td>", index, source_length)
        if (index == -1):
            print ("Tried to get package name: <td> not found.")
            return package_name, package_version, package_severity, index
        index+=len("<td>")

    index = html.find("<td ", index, source_length)
    if (index == -1):
            print ("Tried to get package name: <td> not found.")
            return package_name, package_version, package_severity, index
    index+=len("<td ")
        
    #get package name
    package_name, index = getPackageName(html, index, source_length)
    if (index == -1):
        return package_name, package_version, package_severity, index
    
    #get version
    package_version, index = getPackageVersion(html, index, source_length)
    if (index == -1):
        return package_name, package_version, package_severity, index
    
    #get severity
    package_severity, index = getPackageSeverity(html, index, source_length)
    if (index == -1):
        return package_name, package_version, package_severity, index
    
    return package_name, package_version, package_severity, index
    
    
def getVulnerablePackagesInfomation():
    list_packages =[]
    response = urlopen('https://security.archlinux.org/')
    html = response.read()
    html = html.decode("utf-8", "strict")
    source_length = len(html)
    
    index = 0
    index = html.find("<tbody>", index, source_length)
    if (index == -1):
        print ("Cannot find <tbody> tag")
        sys.exit()
    index+=len("<tbody>")
    
    while (index!=-1 and index<len(html)):
        package_name, package_version, severity, index = getPackageData(index, html, source_length)
        if (index == -1):
            return list_packages
        list_package_data = [package_name, package_version, severity]
        list_packages.append(list_package_data)
        
    return list_packages
    
def getLocalPackagesInformation():
    list_local_packages = []
    os.system("pacman -Q > /tmp/local_packages.txt")
    f = open ("/tmp/local_packages.txt", "r")
    for str1 in f.readlines():
        l_package = str1.split(' ')
        if (len(l_package)!=2):
            continue
        l_package[1] = l_package[1].replace('\n','')
        l_package[1] = l_package[1].replace('\r','')
        
        list_local_packages.append(l_package)
    f.close()
    return list_local_packages


list_packages = getVulnerablePackagesInfomation()

list_local_packages = getLocalPackagesInformation()

f = open('/tmp/vulnerablePackages.txt', 'w')
print_string = 'vulnerable packages:' 
f.write(print_string + '\n')
print (print_string)

for i in range (len(list_packages)):
    for j in range(len(list_local_packages)):
        if (list_packages[i][0] == list_local_packages[j][0]):
            if (compareVersions(list_packages[i][1],list_local_packages[j][1])):
                print_string = str(list_packages[i][0]) + ' ' + str(list_packages[i][1]) + ', current version: ' + str(list_local_packages[j][1])
                f.write(print_string + '\n')
                print (print_string)
f.close()
