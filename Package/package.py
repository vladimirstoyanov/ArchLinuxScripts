import os
import sys
import time
from urllib.request import urlopen
from pkg_resources import parse_version

class Package:
    def __init__(self):
        self.index = 0
        self.html = "" #ToDo: change this name
        self.source_length = "" #ToDo: change this name
        
        
    def compareVersions(self, version1, version2):
        return parse_version(version1) >= parse_version(version2)

    #ToDo: make private the below method
    def getPackageName(self):
        package_name = ""
        self.index = self.html.find("<a", self.index, self.source_length)
        if (self.index == -1):
                print ("Tried to get package name: <a> hasn't found.")
                return package_name
        self.index+=len("<a")
        while (self.html[self.index]!='>' and self.index < len(self.html)):
            self.index+=1
        self.index+=1
        while(self.html[self.index]!='<' and self.index <len(self.html)):
            package_name += self.html[self.index]
            self.index+=1
        return package_name

    #ToDo: make private the below method
    def getPackageVersion(self):
        package_version = ""
        self.index = self.html.find("<td>", self.index, self.source_length)
        if (self.index==-1):
                print ("Tried to get the version: <td> hasn't found.")
                return package_version
        self.index+=len("<td>")
        while (self.html[self.index]!='<' and self.index<len(self.html)):
            package_version+=self.html[self.index]
            self.index+=1
        return package_version
    
    #ToDo: make private the below method
    def getPackageSeverity(self):
        package_severity = ""
        self.index = self.html.find("<span", self.index, self.source_length)
        if (self.index==-1):
                print ("Tried to get severity:  <span> hasn't found.")
                return package_severity
        self.index+=len("<span")
        while (self.html[self.index]!='>' and self.index < len(self.html)):
            self.index+=1
        self.index+=1
        while(self.html[self.index]!='<' and self.index <len(self.html)):
            package_severity += self.html[self.index]
            self.index+=1
        return package_severity

    #ToDo: make private the below method
    def getPackageData (self):
        package_name =""
        package_version =""
        package_severity =""
        
        self.index = self.html.find("<tr>", self.index, self.source_length)
        if (self.index == -1):
            return package_name, package_version, package_severity
        self.index+=len("<tr>")

        for i in range(2):
            self.index = self.html.find("<td>", self.index, self.source_length)
            if (self.index == -1):
                print ("Tried to get package name: <td> not found.")
                return package_name, package_version, package_severity
            self.index+=len("<td>")

        self.index = self.html.find("<td ", self.index, self.source_length)
        if (self.index == -1):
                print ("Tried to get package name: <td> not found.")
                return package_name, package_version, package_severity
        self.index+=len("<td ")
            
        #get package name
        package_name = self.getPackageName()
        if (self.index == -1):
            return package_name, package_version, package_severity
        
        #get version
        package_version = self.getPackageVersion()
        if (self.index == -1):
            return package_name, package_version, package_severity
        
        #get severity
        package_severity = self.getPackageSeverity()
        if (self.index == -1):
            return package_name, package_version, package_severity
        
        return package_name, package_version, package_severity
        
        
    def getVulnerablePackagesList(self):
        list_packages =[]
        response = urlopen('https://security.archlinux.org/')
        self.html = response.read()
        self.html = self.html.decode("utf-8", "strict")
        self.source_length = len(self.html)
        
        self.index = 0
        self.index = self.html.find("<tbody>", self.index, self.source_length)
        if (self.index == -1):
            print ("Cannot find <tbody> tag")
            return list_packages
        self.index+=len("<tbody>")
        
        while (self.index!=-1 and self.index<len(self.html)):
            package_name, package_version, package_severity = self.getPackageData()
            if (self.index == -1):
                return list_packages
            list_package_data = [package_name, package_version, package_severity]
            list_packages.append(list_package_data)
            
        return list_packages
        
    def getLocalPackagesList(self):
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

