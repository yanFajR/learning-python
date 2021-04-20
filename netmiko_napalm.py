from napalm import get_network_driver #immort napalm
from netmiko import Netmiko #import netmiko
import json
import threading
import time
f = open("output.txt", "w")
def connection1(): #connection 1 untuk mendapatkan arp table dari switch .252
    driver = get_network_driver('ios')
    optional_args = {'secret':'cisco'}
    ios = driver('10.33.109.252', 'admin', 'cisco', optional_args=optional_args)
    ios.open()
    output = ios.get_arp_table()
    dump = json.dumps(output, indent=4)
    print(dump)
    f.write("=== ARP TABLE 10.33.109.252 ===\n")
    f.write(dump)
    f.write("\n\n")
    ios.close()

def connection2(): #connection 2 untuk mendapatkan vlan dari switch .252
    driver = get_network_driver('ios')
    optional_args = {'secret':'cisco'}
    ios = driver('10.33.109.252', 'admin', 'cisco', optional_args=optional_args)
    ios.open()
    output = ios.get_vlans()
    dump = json.dumps(output, indent=4)
    print(dump)
    f.write("=== VLAN INFO 10.33.109.252 ===\n")
    f.write(dump)
    f.write("\n\n")
    ios.close()
    
def connection3():  #connection 3 untuk mendapatkan arp table dari switch .253
    connection = Netmiko(host='10.33.109.253',
                    username='admin',
                    password='cisco',
                    device_type='cisco_ios')

    output = connection.send_command('show ip arp') 
    print(output)
    #menyimpan output
    f.write("=== ARP TABLE 10.33.109.253 ===\n")
    f.write(output)
    f.write("\n\n")
    connection.disconnect()

def connection4():   #connection 2 untuk mendapatkan vlan dari switch .253
    connection = Netmiko(host='10.33.109.253',
                    username='admin',
                    password='cisco',
                    device_type='cisco_ios')

    output = connection.send_command('show vlan summary') 
    print(output)
    #menyimpan output
    f.write("=== VLAN INFO 10.33.109.252 ===\n")
    f.write(output)
    f.write("\n\n")
    connection.disconnect()

if __name__ == "__main__":
    #threading
    t1 = threading.Thread(target=connection1)
    t2 = threading.Thread(target=connection2)
    t3 = threading.Thread(target=connection3)
    t4 = threading.Thread(target=connection4)
    
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()
    t4.start()
    t4.join()
    f.close()

    print("Selesai")