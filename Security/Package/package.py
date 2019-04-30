import os
import sys
import time
from urllib.request import urlopen
from pkg_resources import parse_version

class Package:
    def __init__(self):
        self.__index = 0
        self.__page_source = "" #ToDo: change this name
        self.__source_length = "" #ToDo: change this name
        
        
    def compareVersions(self, version1, version2):
        return parse_version(version1) >= parse_version(version2)

    def __getPackageName(self):
        package_name = ""
        self.__index = self.__page_source.find("<a", self.__index, self.__source_length)
        if (self.__index == -1):
                print ("Tried to get package name: <a> hasn't found.")
                return package_name
        self.__index+=len("<a")
        while (self.__page_source[self.__index]!='>' and self.__index < len(self.__page_source)):
            self.__index+=1
        self.__index+=1
        while(self.__page_source[self.__index]!='<' and self.__index <len(self.__page_source)):
            package_name += self.__page_source[self.__index]
            self.__index+=1
        return package_name

    def __getPackageVersion(self):
        package_version = ""
        self.__index = self.__page_source.find("<td>", self.__index, self.__source_length)
        if (self.__index==-1):
                print ("Tried to get the version: <td> hasn't found.")
                return package_version
        self.__index+=len("<td>")
        while (self.__page_source[self.__index]!='<' and self.__index<len(self.__page_source)):
            package_version+=self.__page_source[self.__index]
            self.__index+=1
        return package_version
    
    def __getPackageSeverity(self):
        package_severity = ""
        self.__index = self.__page_source.find("<span", self.__index, self.__source_length)
        if (self.__index==-1):
                print ("Tried to get severity:  <span> hasn't found.")
                return package_severity
        self.__index+=len("<span")
        while (self.__page_source[self.__index]!='>' and self.__index < len(self.__page_source)):
            self.__index+=1
        self.__index+=1
        while(self.__page_source[self.__index]!='<' and self.__index <len(self.__page_source)):
            package_severity += self.__page_source[self.__index]
            self.__index+=1
        return package_severity

    def __getPackageData (self):
        package_name =""
        package_version =""
        package_severity =""
        
        self.__index = self.__page_source.find("<tr>", self.__index, self.__source_length)
        if (self.__index == -1):
            return package_name, package_version, package_severity
        self.__index+=len("<tr>")

        for i in range(2):
            self.__index = self.__page_source.find("<td>", self.__index, self.__source_length)
            if (self.__index == -1):
                print ("Tried to get package name: <td> not found.")
                return package_name, package_version, package_severity
            self.__index+=len("<td>")

        self.__index = self.__page_source.find("<td ", self.__index, self.__source_length)
        if (self.__index == -1):
                print ("Tried to get package name: <td> not found.")
                return package_name, package_version, package_severity
        self.__index+=len("<td ")
            
        #get package name
        package_name = self.__getPackageName()
        if (self.__index == -1):
            return package_name, package_version, package_severity
        
        #get version
        package_version = self.__getPackageVersion()
        if (self.__index == -1):
            return package_name, package_version, package_severity
        
        #get severity
        package_severity = self.__getPackageSeverity()
        if (self.__index == -1):
            return package_name, package_version, package_severity
        
        return package_name, package_version, package_severity
        
        
    def getVulnerablePackagesList(self):
        list_packages =[]
        response = urlopen('https://security.archlinux.org/')
        self.__page_source = response.read()
        self.__page_source = self.__page_source.decode("utf-8", "strict")
        self.__source_length = len(self.__page_source)
        
        self.__index = 0
        self.__index = self.__page_source.find("<tbody>", self.__index, self.__source_length)
        if (self.__index == -1):
            print ("Cannot find <tbody> tag")
            return list_packages
        self.__index+=len("<tbody>")
        
        while (self.__index!=-1 and self.__index<len(self.__page_source)):
            package_name, package_version, package_severity = self.__getPackageData()
            if (self.__index == -1):
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

