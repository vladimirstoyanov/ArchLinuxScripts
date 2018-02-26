import os
import sys
import time
from urllib.request import urlopen
from pkg_resources import parse_version

def compareVersions(version1, version2):
    return parse_version(version1) >= parse_version(version2)

def find_sub_string (m_text, m_subtext, index):
	for i in range(index,len(m_text)):
		for j in range(len(m_subtext)):
			if (m_subtext[j]!=m_text[i+j]):
				break
			if j == len(m_subtext)-1:
				return i+j+1
	return -1
      
def find_sub_string_back (m_text, m_subtext, index):
	for i in range(index,-1,-1):
		for j in range(len(m_subtext)-1,-1,-1):
			if (m_subtext[j]!=m_text[i-((len(m_subtext)-1)-j)]):
				break
			if j == 0:
				return i+1
	return -1


def getPackageData (index, html):
    package_name =""
    package_version =""
    severity =""
    
    index = find_sub_string(html, "<tr>", index)
    if (index == -1):
        return package_name, package_version, severity, index

    for i in range(2):
        index = find_sub_string(html, "<td>", index)
        if (index == -1):
            print ("Tried to get package name: <td> not found.")
            return package_name, package_version, severity, index    

    index = find_sub_string(html, "<td ", index)
    if (index == -1):
            print ("Tried to get package name: <td> not found.")
            return package_name, package_version, severity, index
        
    #get package name
    index = find_sub_string(html, "<a", index)

    if (index == -1):
            print ("Tried to get package name: <a> hasn't found.")
            return package_name, package_version, severity, index
    while (html[index]!='>' and index < len(html)):
        index+=1
    index+=1
    while(html[index]!='<' and index <len(html)):
        package_name += html[index]
        index+=1
    
    #get version
    index = find_sub_string(html, "<td>", index)
    if (index==-1):
            print ("Tried to get the version: <td> hasn't found.")
            return package_name, package_version, severity, index
    while (html[index]!='<' and index<len(html)):
        package_version+=html[index]
        index+=1
    
    #get severity
    index = find_sub_string(html, "<span", index)
    if (index==-1):
            print ("Tried to get severity:  <span> hasn't found.")
            return package_name, package_version, severity, index
    while (html[index]!='>' and index < len(html)):
        index+=1
    index+=1
    while(html[index]!='<' and index <len(html)):
        severity += html[index]
        index+=1
    
    return package_name, package_version, severity, index
    
    
def getVulnerablePackagesInfomation():
    list_packages =[]
    response = urlopen('https://security.archlinux.org/')
    html = response.read()
    html = html.decode("utf-8", "strict")
    
    index = 0
    index = find_sub_string(html, "<tbody>", index)
    if (index == -1):
        print ("Cannot find <tbody> tag")
        sys.exit()
    
    while (index!=-1 and index<len(html)):
        package_name, package_version, severity, index = getPackageData(index, html)
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
            
