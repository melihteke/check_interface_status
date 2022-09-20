from netmiko import ConnectHandler
from pprint import pprint
import json

net_connect = ConnectHandler(
    device_type="cisco_xe",
    host="192.168.178.2",
    username="jenkins",
    password="jenkins",
)

output = net_connect.send_command(
    "show ip interface brief", use_textfsm=True
)
pprint(output)
data = json.dumps(output)

with open("show_interface_brief.txt", "+a") as f:
    f.writelines(data)
    f.close()
