from Package import package

package_ = package.Package()
list_packages = package_.getVulnerablePackagesInfomation()
list_local_packages = package_.getLocalPackagesInformation()

f = open('/tmp/vulnerablePackages.txt', 'w')
print_string = 'vulnerable packages:' 
f.write(print_string + '\n')
print (print_string)

for i in range (len(list_packages)):
    for j in range(len(list_local_packages)):
        if (list_packages[i][0] == list_local_packages[j][0]):
            if (package_.compareVersions(list_packages[i][1],list_local_packages[j][1])):
                print_string = str(list_packages[i][0]) + ' ' + str(list_packages[i][1]) + ', current version: ' + str(list_local_packages[j][1])
                f.write(print_string + '\n')
                print (print_string)
f.close()
