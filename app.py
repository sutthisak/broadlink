import broadlink
 
devices = broadlink.discover(timeout=5)
 
def is_devices_found():
    return len(devices) > 0 and devices[0].auth()
 
if(is_devices_found()):
    devices[0].send_data(AIR_CMD['MITSUBISHI']['POWER']['OFF'])
else:
    print('Broadlink device is not found.')