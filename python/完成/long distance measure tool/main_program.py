print ("Editor_Jacky.lin 2019/06/29")
print ("--------------Signal Measure Tool------------------")
print ("Hints")
print ("Make sure your PC have installed the Chrome driver")
print ("This tool is only for EKI-136x-BE & EKI-6333")
print ("--------------Signal Measure Tool------------------")
print ("")

print ("Which side are you on?")
side=input("1.AP side, 2.client side (Ex.1): ",)
while side !="1" and side!="2":
    side=input("1.AP side, 2.client side (Ex.1): ",)

if side=="1":
    import AP_side 
    AP_side.run()
else:
    import client_side
    client_side.run()
