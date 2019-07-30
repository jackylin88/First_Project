#from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import collections
import time
from binascii import unhexlify
import binascii
import netaddr
from fnmatch import fnmatch, fnmatchcase
import json
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)
client = ModbusClient(method='rtu', port='com12', stopbits=1, bytesize=8, parity='N', timeout=0.5, baudrate=9600)
#client = ModbusClient('10.7.5.31', port=502)
client.connect()


#function code 1
coil  = client.read_coils(0, 1, unit=0x01) # address, count, slave address
#print (coil.bits)

#function code 2
inputs = client.read_discrete_inputs(0,8,unit=0x01) # address, count, slave address
# print (inputs.bits)


#function code 03
holding_registers = client.read_holding_registers(0,8,unit=0x1)
#print(holding_registers.registers)


#function code 04
input_registers = client.read_input_registers(0,8,unit=0x01)
#print(input_registers.registers)


#function code 5
coil_single_write = client.write_coil(0,True, unit=0x01)
#function code 06
holding_registers_write = client.write_register(1,20, unit=0x01)
#function code 15
coil_multiple_write = client.write_coils(1,[True]*999,unit=0x01)


#function code 16
holding_registers_write = client.write_registers(0,[20,40,60,80,100], unit=0x01)



#Function code 23
# arguments = {
#     'read_address':    9,
#     'read_count':      1,
#     'write_address':   1,
#     'write_registers': [40]*8,
# }


# rq = client.readwrite_registers(**arguments)
# print(rq.registers)

# Address_Table = {
# 'Vendor ID': {'Address': 1, 'Data Type': 1},
# 'Unit ID': {'Address': 2, 'Data Type': 1},
# 'Product Code': {'Address': 3, 'Data Type': 1},
# 'Ethernet MAC Address': {'Address': 527, 'Data Type': 3},
# }


# Address_Table = [
# {'Vendor ID': {'Address': 1, 'Data Type': 1}},
# {'Unit ID': {'Address': 2, 'Data Type': 1}},
# {'Product Code': {'Address': 3, 'Data Type': 1}},
# {'Vendor Name': {'Address': 17, 'Data Type': 16}},
# {'Product Name': {'Address': 33, 'Data Type': 16}},
# {'Firmware Version': {'Address': 523, 'Data Type': 2}},
# {'Ethernet MAC Address': {'Address': 527, 'Data Type': 3}},
# {'Revision Number': {'Address': 530, 'Data Type': 16}},
# {'IP Address': {'Address': 1025, 'Data Type': 2}},
# {'Port Status': {'Address': 4097, 'Data Type': 32}},
# {'Port Speed': {'Address': 4353, 'Data Type': 32}},
# {'Flow Control': {'Address': 4609, 'Data Type': 32}},
# {'Port 01 Description': {'Address': 5121, 'Data Type': 20}},
# {'Port 02 Description': {'Address': 5141, 'Data Type': 20}},
# {'Port 03 Description': {'Address': 5161, 'Data Type': 20}},
# {'Port 04 Description': {'Address': 5181, 'Data Type': 20}},
# {'Port 05 Description': {'Address': 5201, 'Data Type': 20}},
# {'Port 06 Description': {'Address': 5221, 'Data Type': 20}},
# {'Port 07 Description': {'Address': 5241, 'Data Type': 20}},
# {'Port 08 Description': {'Address': 5261, 'Data Type': 20}},
# {'Port 09 Description': {'Address': 5281, 'Data Type': 20}},
# {'Port 10 Description': {'Address': 5301, 'Data Type': 20}},
# {'Port 11 Description': {'Address': 5321, 'Data Type': 20}},
# {'Port 12 Description': {'Address': 5341, 'Data Type': 20}},
# {'Port 13 Description': {'Address': 5361, 'Data Type': 20}},
# {'Port 14 Description': {'Address': 5381, 'Data Type': 20}},
# {'Port 15 Description': {'Address': 5401, 'Data Type': 20}},
# {'Port 16 Description': {'Address': 5421, 'Data Type': 20}},
# {'Port 17 Description': {'Address': 5441, 'Data Type': 20}},
# {'Port 18 Description': {'Address': 5461, 'Data Type': 20}},
# {'Port 19 Description': {'Address': 5481, 'Data Type': 20}},
# {'Port 20 Description': {'Address': 5501, 'Data Type': 20}},
# {'Port 21 Description': {'Address': 5521, 'Data Type': 20}},
# {'Port 22 Description': {'Address': 5541, 'Data Type': 20}},
# {'Port 23 Description': {'Address': 5561, 'Data Type': 20}},
# {'Port 24 Description': {'Address': 5581, 'Data Type': 20}},
# {'Port 25 Description': {'Address': 5601, 'Data Type': 20}},
# {'Port 26 Description': {'Address': 5621, 'Data Type': 20}},
# {'Port 27 Description': {'Address': 5641, 'Data Type': 20}},
# {'Port 28 Description': {'Address': 5661, 'Data Type': 20}},
# {'Port 29 Description': {'Address': 5681, 'Data Type': 20}},
# {'Port 30 Description': {'Address': 5701, 'Data Type': 20}},
# {'Port 31 Description': {'Address': 5721, 'Data Type': 20}},
# {'Port 32 Description': {'Address': 5741, 'Data Type': 20}},
# {'Link Up Counter': {'Address': 5889, 'Data Type': 32}},
# {'Port 01 Rx Packets Counter': {'Address': 8193, 'Data Type': 4}},
# {'Port 02 Rx Packets Counter': {'Address': 8197, 'Data Type': 4}},
# {'Port 03 Rx Packets Counter': {'Address': 8201, 'Data Type': 4}},
# {'Port 04 Rx Packets Counter': {'Address': 8205, 'Data Type': 4}},
# {'Port 05 Rx Packets Counter': {'Address': 8209, 'Data Type': 4}},
# {'Port 06 Rx Packets Counter': {'Address': 8213, 'Data Type': 4}},
# {'Port 07 Rx Packets Counter': {'Address': 8217, 'Data Type': 4}},
# {'Port 08 Rx Packets Counter': {'Address': 8221, 'Data Type': 4}},
# {'Port 09 Rx Packets Counter': {'Address': 8225, 'Data Type': 4}},
# {'Port 10 Rx Packets Counter': {'Address': 8229, 'Data Type': 4}},
# {'Port 11 Rx Packets Counter': {'Address': 8233, 'Data Type': 4}},
# {'Port 12 Rx Packets Counter': {'Address': 8237, 'Data Type': 4}},
# {'Port 13 Rx Packets Counter': {'Address': 8241, 'Data Type': 4}},
# {'Port 14 Rx Packets Counter': {'Address': 8245, 'Data Type': 4}},
# {'Port 15 Rx Packets Counter': {'Address': 8249, 'Data Type': 4}},
# {'Port 16 Rx Packets Counter': {'Address': 8253, 'Data Type': 4}},
# {'Port 17 Rx Packets Counter': {'Address': 8257, 'Data Type': 4}},
# {'Port 18 Rx Packets Counter': {'Address': 8261, 'Data Type': 4}},
# {'Port 19 Rx Packets Counter': {'Address': 8265, 'Data Type': 4}},
# {'Port 20 Rx Packets Counter': {'Address': 8269, 'Data Type': 4}},
# {'Port 21 Rx Packets Counter': {'Address': 8273, 'Data Type': 4}},
# {'Port 22 Rx Packets Counter': {'Address': 8277, 'Data Type': 4}},
# {'Port 23 Rx Packets Counter': {'Address': 8281, 'Data Type': 4}},
# {'Port 24 Rx Packets Counter': {'Address': 8285, 'Data Type': 4}},
# {'Port 25 Rx Packets Counter': {'Address': 8289, 'Data Type': 4}},
# {'Port 26 Rx Packets Counter': {'Address': 8293, 'Data Type': 4}},
# {'Port 27 Rx Packets Counter': {'Address': 8297, 'Data Type': 4}},
# {'Port 28 Rx Packets Counter': {'Address': 8301, 'Data Type': 4}},
# {'Port 29 Rx Packets Counter': {'Address': 8305, 'Data Type': 4}},
# {'Port 30 Rx Packets Counter': {'Address': 8309, 'Data Type': 4}},
# {'Port 31 Rx Packets Counter': {'Address': 8313, 'Data Type': 4}},
# {'Port 32 Rx Packets Counter': {'Address': 8317, 'Data Type': 4}},
# {'Port 01 Tx Packets Counter': {'Address': 8449, 'Data Type': 4}},
# {'Port 02 Tx Packets Counter': {'Address': 8453, 'Data Type': 4}},
# {'Port 03 Tx Packets Counter': {'Address': 8457, 'Data Type': 4}},
# {'Port 04 Tx Packets Counter': {'Address': 8461, 'Data Type': 4}},
# {'Port 05 Tx Packets Counter': {'Address': 8465, 'Data Type': 4}},
# {'Port 06 Tx Packets Counter': {'Address': 8469, 'Data Type': 4}},
# {'Port 07 Tx Packets Counter': {'Address': 8473, 'Data Type': 4}},
# {'Port 08 Tx Packets Counter': {'Address': 8477, 'Data Type': 4}},
# {'Port 09 Tx Packets Counter': {'Address': 8481, 'Data Type': 4}},
# {'Port 10 Tx Packets Counter': {'Address': 8485, 'Data Type': 4}},
# {'Port 11 Tx Packets Counter': {'Address': 8489, 'Data Type': 4}},
# {'Port 12 Tx Packets Counter': {'Address': 8493, 'Data Type': 4}},
# {'Port 13 Tx Packets Counter': {'Address': 8497, 'Data Type': 4}},
# {'Port 14 Tx Packets Counter': {'Address': 8501, 'Data Type': 4}},
# {'Port 15 Tx Packets Counter': {'Address': 8505, 'Data Type': 4}},
# {'Port 16 Tx Packets Counter': {'Address': 8509, 'Data Type': 4}},
# {'Port 17 Tx Packets Counter': {'Address': 8513, 'Data Type': 4}},
# {'Port 18 Tx Packets Counter': {'Address': 8517, 'Data Type': 4}},
# {'Port 19 Tx Packets Counter': {'Address': 8521, 'Data Type': 4}},
# {'Port 20 Tx Packets Counter': {'Address': 8525, 'Data Type': 4}},
# {'Port 21 Tx Packets Counter': {'Address': 8529, 'Data Type': 4}},
# {'Port 22 Tx Packets Counter': {'Address': 8533, 'Data Type': 4}},
# {'Port 23 Tx Packets Counter': {'Address': 8537, 'Data Type': 4}},
# {'Port 24 Tx Packets Counter': {'Address': 8541, 'Data Type': 4}},
# {'Port 25 Tx Packets Counter': {'Address': 8545, 'Data Type': 4}},
# {'Port 26 Tx Packets Counter': {'Address': 8549, 'Data Type': 4}},
# {'Port 27 Tx Packets Counter': {'Address': 8553, 'Data Type': 4}},
# {'Port 28 Tx Packets Counter': {'Address': 8557, 'Data Type': 4}},
# {'Port 29 Tx Packets Counter': {'Address': 8561, 'Data Type': 4}},
# {'Port 30 Tx Packets Counter': {'Address': 8565, 'Data Type': 4}},
# {'Port 31 Tx Packets Counter': {'Address': 8569, 'Data Type': 4}},
# {'Port 32 Tx Packets Counter': {'Address': 8573, 'Data Type': 4}},
# {'Port 01 Tx Error Packets': {'Address': 8961, 'Data Type': 2}},
# {'Port 02 Tx Error Packets': {'Address': 8963, 'Data Type': 2}},
# {'Port 03 Tx Error Packets': {'Address': 8965, 'Data Type': 2}},
# {'Port 04 Tx Error Packets': {'Address': 8967, 'Data Type': 2}},
# {'Port 05 Tx Error Packets': {'Address': 8969, 'Data Type': 2}},
# {'Port 06 Tx Error Packets': {'Address': 8971, 'Data Type': 2}},
# {'Port 07 Tx Error Packets': {'Address': 8973, 'Data Type': 2}},
# {'Port 08 Tx Error Packets': {'Address': 8975, 'Data Type': 2}},
# {'Port 09 Tx Error Packets': {'Address': 8977, 'Data Type': 2}},
# {'Port 10 Tx Error Packets': {'Address': 8979, 'Data Type': 2}},
# {'Port 11 Tx Error Packets': {'Address': 8981, 'Data Type': 2}},
# {'Port 12 Tx Error Packets': {'Address': 8983, 'Data Type': 2}},
# {'Port 13 Tx Error Packets': {'Address': 8985, 'Data Type': 2}},
# {'Port 14 Tx Error Packets': {'Address': 8987, 'Data Type': 2}},
# {'Port 15 Tx Error Packets': {'Address': 8989, 'Data Type': 2}},
# {'Port 16 Tx Error Packets': {'Address': 8991, 'Data Type': 2}},
# {'Port 17 Tx Error Packets': {'Address': 8993, 'Data Type': 2}},
# {'Port 18 Tx Error Packets': {'Address': 8995, 'Data Type': 2}},
# {'Port 19 Tx Error Packets': {'Address': 8997, 'Data Type': 2}},
# {'Port 20 Tx Error Packets': {'Address': 8999, 'Data Type': 2}},
# {'Port 21 Tx Error Packets': {'Address': 9001, 'Data Type': 2}},
# {'Port 22 Tx Error Packets': {'Address': 9003, 'Data Type': 2}},
# {'Port 23 Tx Error Packets': {'Address': 9005, 'Data Type': 2}},
# {'Port 24 Tx Error Packets': {'Address': 9007, 'Data Type': 2}},
# {'Port 25 Tx Error Packets': {'Address': 9009, 'Data Type': 2}},
# {'Port 26 Tx Error Packets': {'Address': 9011, 'Data Type': 2}},
# {'Port 27 Tx Error Packets': {'Address': 9013, 'Data Type': 2}},
# {'Port 28 Tx Error Packets': {'Address': 9015, 'Data Type': 2}},
# {'Port 29 Tx Error Packets': {'Address': 9017, 'Data Type': 2}},
# {'Port 30 Tx Error Packets': {'Address': 9019, 'Data Type': 2}},
# {'Port 31 Tx Error Packets': {'Address': 9021, 'Data Type': 2}},
# {'Port 32 Tx Error Packets': {'Address': 9023, 'Data Type': 2}},
# {'Port 01 Rx Error Packets': {'Address': 8705, 'Data Type': 2}},
# {'Port 02 Rx Error Packets': {'Address': 8707, 'Data Type': 2}},
# {'Port 03 Rx Error Packets': {'Address': 8709, 'Data Type': 2}},
# {'Port 04 Rx Error Packets': {'Address': 8711, 'Data Type': 2}},
# {'Port 05 Rx Error Packets': {'Address': 8713, 'Data Type': 2}},
# {'Port 06 Rx Error Packets': {'Address': 8715, 'Data Type': 2}},
# {'Port 07 Rx Error Packets': {'Address': 8717, 'Data Type': 2}},
# {'Port 08 Rx Error Packets': {'Address': 8719, 'Data Type': 2}},
# {'Port 09 Rx Error Packets': {'Address': 8721, 'Data Type': 2}},
# {'Port 10 Rx Error Packets': {'Address': 8723, 'Data Type': 2}},
# {'Port 11 Rx Error Packets': {'Address': 8725, 'Data Type': 2}},
# {'Port 12 Rx Error Packets': {'Address': 8727, 'Data Type': 2}},
# {'Port 13 Rx Error Packets': {'Address': 8729, 'Data Type': 2}},
# {'Port 14 Rx Error Packets': {'Address': 8731, 'Data Type': 2}},
# {'Port 15 Rx Error Packets': {'Address': 8733, 'Data Type': 2}},
# {'Port 16 Rx Error Packets': {'Address': 8735, 'Data Type': 2}},
# {'Port 17 Rx Error Packets': {'Address': 8737, 'Data Type': 2}},
# {'Port 18 Rx Error Packets': {'Address': 8739, 'Data Type': 2}},
# {'Port 19 Rx Error Packets': {'Address': 8741, 'Data Type': 2}},
# {'Port 20 Rx Error Packets': {'Address': 8743, 'Data Type': 2}},
# {'Port 21 Rx Error Packets': {'Address': 8745, 'Data Type': 2}},
# {'Port 22 Rx Error Packets': {'Address': 8747, 'Data Type': 2}},
# {'Port 23 Rx Error Packets': {'Address': 8749, 'Data Type': 2}},
# {'Port 24 Rx Error Packets': {'Address': 8751, 'Data Type': 2}},
# {'Port 25 Rx Error Packets': {'Address': 8753, 'Data Type': 2}},
# {'Port 26 Rx Error Packets': {'Address': 8755, 'Data Type': 2}},
# {'Port 27 Rx Error Packets': {'Address': 8757, 'Data Type': 2}},
# {'Port 28 Rx Error Packets': {'Address': 8759, 'Data Type': 2}},
# {'Port 29 Rx Error Packets': {'Address': 8761, 'Data Type': 2}},
# {'Port 30 Rx Error Packets': {'Address': 8763, 'Data Type': 2}},
# {'Port 31 Rx Error Packets': {'Address': 8765, 'Data Type': 2}},
# {'Port 32 Rx Error Packets': {'Address': 8767, 'Data Type': 2}},
# ]
# Modbus_Result = {}
# for All_Table in Address_Table:
#     for Name in All_Table:
#         Result = client.read_input_registers(All_Table[Name]['Address']-1,All_Table[Name]['Data Type'], unit=0xFF)
#         astr =""
#         bstr =""
#         Name1 =""
#         for x in range(All_Table[Name]['Data Type']):
#         	astr += '{0:04X}'.format(Result.registers[x])
#         	bstr = astr
# 	        if Name == 'Vendor Name' or Name == 'Product Name' or Name == 'Revision Number' or fnmatchcase(Name,'Port * Description'):
# 	        	bstr = unhexlify(astr)
#         	#print(bstr)
#         		bstr = bytes.decode(bstr).rstrip(' \t\r\n\0')
# 	        if Name == 'Ethernet MAC Address':
# 	        	bstr = ":".join(["%s" % (astr[i:i+2]) for i in range(0, 12, 2)])
# 	        if Name == 'Firmware Version' or Name == 'IP Address' :
# 	        	bstr = str(netaddr.IPAddress("0x" + astr))

#         	if Name == 'Port Status':
#         		Name1 = ('Port ' + '{0:02}'.format(x+1) + ' Status')
#         		if '{0:04X}'.format(Result.registers[x]) == "0000":
#         			bstr = "Link down"
#         		elif '{0:04X}'.format(Result.registers[x]) == "0001":
#         			bstr= "Link up"
#         		else:
#         			bstr = "No port"
#         		#print(Name1,bstr)
#         		Modbus_Result[Name1] = bstr

#         	if Name == 'Port Speed':
#         		Name1 = ('Port ' + '{0:02}'.format(x+1) + ' Speed')
#         		if '{0:04X}'.format(Result.registers[x]) == "0000":
#         			bstr = "10M-Half"
#         		elif '{0:04X}'.format(Result.registers[x]) == "0001":
#         			bstr= "10M-Full"
#         		elif '{0:04X}'.format(Result.registers[x]) == "0002":
#         			bstr= "100M-Half"
#         		elif '{0:04X}'.format(Result.registers[x]) == "0003":
#         			bstr= "100M-Full"
#         		elif '{0:04X}'.format(Result.registers[x]) == "0004":
#         			bstr= "1000M-Half"
#         		elif '{0:04X}'.format(Result.registers[x]) == "0005":
#         			bstr= "1000M-Full"
#         		else:
#         			bstr = "No port"
#         		#print(Name1,bstr)
#         		Modbus_Result[Name1] = bstr

#         	if Name == 'Flow Control':
#         		Name1 = ('Port ' + '{0:02}'.format(x+1) + ' Flow Control')
#         		if '{0:04X}'.format(Result.registers[x]) == "0000":
#         			bstr = "Off"
#         		elif '{0:04X}'.format(Result.registers[x]) == "0001":
#         			bstr= "On"
#         		else:
#         			bstr = "No port"
#         		#print(Name1,bstr)
#         		Modbus_Result[Name1] = bstr

#         	if Name == 'Link Up Counter':
#         		Name1 = ('Port ' + '{0:02}'.format(x+1) + ' Link Up Counter')
#         		bstr = Result.registers[x]
#         		#print(Name1,bstr)
#         		Modbus_Result[Name1] = bstr



   
#         if fnmatchcase(Name, 'Port * Rx Packets Counter') or fnmatchcase(Name, 'Port * Tx Packets Counter') \
#         or fnmatchcase(Name, 'Port * Rx Error Packets') or fnmatchcase(Name, 'Port * Tx Error Packets'):
#         	bstr = int("0x" + bstr, 16)
#         	Modbus_Result[Name] = bstr
#         elif not (fnmatchcase(Name1, 'Port * Status') or fnmatchcase(Name1, 'Port * Speed') \
#         	or fnmatchcase(Name1, 'Port * Link Up Counter') or fnmatchcase(Name1, 'Port * Flow Control')):
#         		#print(Name,bstr)
#         		Modbus_Result[Name] = bstr
        		

client.close()
#print(Modbus_Result['Firmware Version'])
