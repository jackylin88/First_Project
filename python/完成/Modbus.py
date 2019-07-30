#---------------------------------------------Modbus TCP--------------------------------------------------
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
client = ModbusClient('10.7.5.31', port=502)
client.connect()

#---------------------------------------------Modbus RTU--------------------------------------------------
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
client = ModbusClient(method='rtu', port='com3', stopbits=1, bytesize=8, parity='N', timeout=0.5, baudrate=9600)
client.connect()


#-------------------------------------Modbus Address & Function code---------------------------------------
# Modbus 共有4種Address(0x0000、1x0000、3x0000、4x0000) 、8個Function code(4個Read、4個Write)
# 以下說明各種Address 支援的Function code 

#-------------------------------------Modbus Address (0x0000) for DO---------------------------------------
#支援Read (function code 1) & Write (function code 05 & 15) 
#function code 1: Read multi-coils status (0xxxx) for DO
coil  = client.read_coils(0, 1, unit=0x01) # start address,bit count, slave ID
print (coil.bits[0]) #讀0x0001值是True or False

#function code 5: Write single-coil (0xxxx) for DO
coil_single_write = client.write_coil(0,0, unit=1) # start address, 1 or 0, slave ID
print (coil_single_write)

#function code 15: Write multi-coils ( 0xxxx ) for DO
coil_multiple_write = client.write_coils(0,[True]*5,unit=0x01) # 將0x0001~5 寫成True
print (coil_multiple_write)

#-------------------------------------Modbus Address (1x0000) for DI---------------------------------------
#支援Read (function code 02)
inputs = client.read_discrete_inputs(0,5,unit=0x01) # address, count, slave address
print (inputs.bits) #讀1x0001~8 (後面沒問會顯示False)，Digital一個Bytes可以問8個address，若沒問則保留為0，相較於analog 一個address 回應的value就必須使用一個Bytes就是
print (inputs.bits[1]) #讀1x0002 值

#-------------------------------------Modbus Address (4x0000) for AO---------------------------------------
#支援Read (function code 03) & Write (function code 06 & 16) 
#function code 03 : read multi-registers (4xxxx) for AO
holding_registers = client.read_holding_registers(0,5,unit=0x1) # start address,bit count, slave ID
print(holding_registers.registers) #讀4x0001~5值
print(holding_registers.registers[2]) # 讀4x0003值

#function code 06 : write single (4x0000) for AO
holding_registers_write = client.write_register(1,10, unit=0x01) #表4x0001第一個寫入AO=10
print(holding_registers_write)

#function code 16 :write multi-registers for AO
holding_registers_write = client.write_registers(0,[20,40,60,80,100], unit=0x01) #將4x0001~4x0005寫成分別寫入20,40,60,80,100
print(holding_registers_write)

#-------------------------------------Modbus Address (3x0000) for AI---------------------------------------
#支援Read (function code 04)
input_registers = client.read_input_registers(0,8,unit=0x01)
print(input_registers.registers)
print(input_registers.registers[2]) # 問3x0003

#---------------------------------------------Port close--------------------------------------------------
client.close()