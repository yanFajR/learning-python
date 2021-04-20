from napalm import get_network_driver
from tabulate import tabulate   #untuk membuat tampilan table

driver = get_network_driver('ios')
host_list = ["10.33.109.252", "10.33.109.253"] #list dari alamat ip device
optional_args = {'secret':'cisco'}
device_table = [["hostname", "vendor", "model", "uptime", "serial_number"]]
for host in host_list:
    print("Connectiing to {} .. ".format(host))  #menampilkan connecting to alamat ip device
    piranti = driver(host, "admin", "cisco", optional_args=optional_args)
    piranti.open()
    print("Mengambil informasi piranti ...")
    piranti_info = dict(piranti.get_facts()) #mengambil info device terdapat hostname, model,
                                             #vendor, uptime, dan serial number disimpan dalam format dictionary
    device_table.append([piranti_info["hostname"], piranti_info["vendor"], 
                        piranti_info["model"], piranti_info["uptime"],     
                        piranti_info["serial_number"] ])
    piranti.close()
    print("Selesai")
print(tabulate(device_table, headers="firstrow")) #menampilkan device table dengan format tabulate dan header adalah baris pertama