import can

bustype = 'socketcan_native'
channel = 'can1'
bitrate = 250000
 
def send_one(i):
    
    bus = can.interface.Bus(bustype=bustype, channel=channel, bitrate=bitrate)
    
    #extended id should be on since we will use 29 bit identifier
    msg = can.Message(arbitration_id=0xc0ffee, data=[i, 0, 1, 2, 3, 4, 5, 6], extended_id=True)
    
    #send a message
    try:
        bus.send(msg)
        print("Message sent on {}".format(bus.channel_info))
    except can.CanError:
        print("Message not sent")
    
for i in range(10):
    send_one(i)
    

