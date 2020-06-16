import socket
#Socket is a built-in python package which can be used to do some network operations

PC_host_name = socket.gethostname()
#Getting your Computer's Hostname

IP_address = socket.gethostbyname(PC_host_name)    
#Finding the IP address of your hostname in the network
#Which usually returns your IP Address

print("Your Computer's name is: " + PC_host_name)    
print("Your Computer's IPaddress is: " + IP_address)
#Printing the data found
