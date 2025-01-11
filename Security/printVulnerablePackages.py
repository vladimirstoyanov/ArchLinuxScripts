#ToDo: add history of vulnerable packages and all installed packages
from Package import package
import warnings

warnings.filterwarnings("ignore")

package_ = package.Package()
list_vulnerable_packages = package_.getVulnerablePackagesList()
list_local_packages = package_.getLocalPackagesList()

f = open('/tmp/vulnerablePackages.txt', 'w')
print_string = 'vulnerable packages:'
f.write(print_string + '\n')
print (print_string)
count = 0
for i in range (len(list_vulnerable_packages)):
    for j in range(len(list_local_packages)):
        if (list_vulnerable_packages[i][0] == list_local_packages[j][0]):
            if (package_.compareVersions(list_vulnerable_packages[i][1],list_local_packages[j][1])):
                print_string = str(list_vulnerable_packages[i][0]) + ' ' + str(list_vulnerable_packages[i][1]) + ', current version: ' + str(list_local_packages[j][1]) + ' severity: ' + str(list_vulnerable_packages[i][2])
                f.write(print_string + '\n')
                print (print_string)
                count+=1
f.write("Count: " + str(count) + "\n")
f.close()

print ("count: " + str(count))
