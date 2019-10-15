import broadlink
from resources.remote import ir
 
devices = broadlink.discover(timeout=5)
 
def is_devices_found():
    return len(devices) > 0 and devices[0].auth()

if __name__ == "__main__":
    air_purifier_remote = ir.AIR_PURIFIER['HATARI']['HT-AP12']
    if(is_devices_found()):        
        devices[0].send_data(air_purifier_remote['POWER']['OFF'])
        #devices[0].send_data(air_purifier_remote['POWER']['ON'])
        #devices[0].send_data(air_purifier_remote['SPEED']['1'])
        #devices[0].send_data(air_purifier_remote['SPEED']['2'])
        #devices[0].send_data(air_purifier_remote['SPEED']['3'])
        #devices[0].send_data(air_purifier_remote['SPEED']['4'])
        #devices[0].send_data(air_purifier_remote['IONIZER']['OFF'])
        #devices[0].send_data(air_purifier_remote['IONIZER']['ON'])
        #devices[0].send_data(air_purifier_remote['PLASMA']['OFF'])
        #devices[0].send_data(air_purifier_remote['PLASMA']['ON'])
    else:        
        print('Broadlink device is not found.')