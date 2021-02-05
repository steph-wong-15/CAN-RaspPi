import can

bustype = 'socketcan_native'
can_interface = 'can1'
bitrate = 250000
can_messages = [];

bus = can.interface.Bus(can_interface, bustype=bustype, bitrate=bitrate)

#block reading with timeout
while True:
    
    message = bus.recv(1.0) #Timeout in seconds
    
    #checks if message received
    if message is None:
        print('Timeout occurred, no message.')          
    #store messages
    else: 
        can_messages.append(message)
        print(message)


    
    
