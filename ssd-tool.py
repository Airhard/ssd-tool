# import the os module
import os
# Define SSD details
SSD_PATH = '/dev/sda'
SSD_DATA = {}
SSD_REPORT = ["noch nicht", "viel da"]
DEBUG = False

def print_report(SSD_REPORT):
    for i in SSD_REPORT:
        print(i)
        print(" ")

def processing(SSD_DATA):
    if SSD_DATA['health_status'] == 0:
        SSD_DATA['p_health_status'] ='## OK ## The SSD is healthy'
    else:
        SSD_DATA['p_health_status'] ='## Warning ## The SSD is not healthy'
    SSD_DATA['p_capacity'] = 'SSD Capacity: ' + SSD_DATA['capacity'][0:6]
    SSD_DATA['p_status'] = 'statuscode: ' + SSD_DATA['status']
    SSD_DATA['p_TGBW'] = "Total TB written " + str(float(SSD_DATA['TGBW'][-1])/1024) + "TB"
    SSD_REPORT=
    return SSD_REPORT

def gatering_facts(SSD_PATH, SSD_DATA):
    ''' gathering Facts aubout the SSD'''
    
    # check the health
    SSD_DATA['health_status'] = os.popen('smartctl -H ' + SSD_PATH).read()
    
    # check capacity
    SSD_DATA['capacity'] = os.popen('lsblk -n -o SIZE ' + SSD_PATH).read().strip()

    
    # check status and infos
    SSD_DATA['status'] = os.popen('smartctl -a -T permissive ' + SSD_PATH).read()
    
    
    # filter for TB written
    SSD_DATA['TGBW'] = os.popen("smartctl --attributes " + SSD_PATH + " | grep 'Total_LBAs_Written'").read().split()
    
    
    # check filesystem
    SSD_DATA['filesystem_type'] = os.popen('lsblk -n -o FSTYPE ' + SSD_PATH).read().strip()
    SSD_DATA['p_filesystem_type'] = 'Dateisystemtyp: ' + SSD_DATA['filesystem_type'][0:5]
    
    # check with df total, free and used space on SSD
    SSD_DATA['df_data'] = os.popen('df -h | grep ' + SSD_PATH).read().split()
    SSD_DATA['p_df_capa'] = 'SSD Capacity: ' + SSD_DATA['df_data'][1]
    SSD_DATA['p_df_free'] = 'SSD Free Space: ' + SSD_DATA['df_data'][3]
    SSD_DATA['p_df_used'] = 'SSD Used Space: ' + SSD_DATA['df_data'][2]
    # return DATA
    return SSD_DATA

def main():
    #ask_for_device()
    gatering_facts(SSD_PATH, SSD_DATA)
    print_report(SSD_DATA)

if __name__ == "__main__":
    main()
