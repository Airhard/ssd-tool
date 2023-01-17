# import the os module
import os
# Define SSD details
SSD_PATH = '/dev/sdd'
# gathering Facts
SSD_CAPACITY = os.popen('lsblk -n -o SIZE ' + SSD_PATH).read().strip()
ssd_space = os.popen('df -h | grep ' + SSD_PATH).read().split()
health_status = os.system('smartctl -H ' + SSD_PATH)
status = os.system('smartctl -a -T permissive ' + SSD_PATH)
filesystem_type = os.popen('lsblk -n -o FSTYPE ' + SSD_PATH).read().strip()

# Print Results:
print('######   Summery   ######')
print('SSD Name: ' + SSD_NAME)
print('SSD Capacity: ' + SSD_CAPACITY)
# Print free and used space on SSD
print('SSD Total Space: ' + ssd_space[1])
print('SSD Free Space: ' + ssd_space[3])
print('SSD Used Space: ' + ssd_space[2])

# check the health
if health_status == 0:
    print('## OK ## The SSD is healthy')
else:
    print('## Warning ## The SSD is not healthy')
# Print Dateisystem
print('Dateisystemtyp: ', filesystem_type)
# Print status code
print('statuscode: ', status)
