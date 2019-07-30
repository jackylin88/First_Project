from pymodbus.client.sync import ModbusTcpClient as ModbusClient
# import collections
# import time
# from binascii import unhexlify
# import binascii
# import netaddr
# from fnmatch import fnmatch, fnmatchcase
# import json
client = ModbusClient('10.7.5.35', port=502)
client.connect()
coil_multiple_write = client.write_coils(0, [True,True], unit=0x01)
client.close()