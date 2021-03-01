from socket import *

TO_ADDR=('192.168.1.176',8138)    # store IP adress of reciever  
hostname=gethostbyname('0.0.0.0') # gets IP adress of host 
LOCAL_ADDR=(hostname,8135)        # store host IP and port 
MSG_LEN=1000                      # message length
fd=socket(AF_INET,SOCK_DGRAM)     # create new socket 
fd.bind(LOCAL_ADDR)               # bind socket to port 


who_am_i = [] # store victim's name and attributes 
msg=''        # store message beign sent 
data=''       # store data recieved 
count = 0     # count loop 

# function to recieve data
def recv():
	msg,addr=fd.recvfrom(MSG_LEN)     # recieve data
	print ('anonymous:',msg.decode()) # print decoded data
	return msg.decode(),addr

# function to send message 
def send(msg,addr):
        msg = msg.encode()
        fd.sendto(msg,addr)

# while sender has not made a guess
while '?' not in data:
        
        # print instructions
        if (count == 0):
                name = input('enter your name: ') # get name of victim
                name = name.lower()               # convert to lower case 
                who_am_i.append("-"+name+":")     # appent their name to list
                
                print("\n\n-----------------------------------------------")
                print("You are kidnapped and about to get your head")
                print("chopped off. Your only chance of getting saved")
                print("is by an anonymous person that knows you. You can")
                print("send them single word hints that describe you. They")
                print("only have one guess, so choose right.")
                print("YOU CAN START SENDING ONCE THEY SEND 'START'")
                print("----------------------------------------------- \n\n")
                count += 1
                
        data,addr=recv()   # recieve data from sender
        if ('?' in data):  # if sender makes a guess, break loop
                break
        msg=input('you: ')   # get victim input
        who_am_i.append(msg) # append attribute to list
        send(msg,addr)       # send message 
        
data = data[:-1] # get ride of '?'

# if sender guessed correctly
if (data.lower() == name):
        # send message 
        msg = "Correct. You saved " + name + "'s life."
        send(msg,addr)


                        
# otherwise send message 
else:
        send("Incorrect. They will be killed NOW", addr)
        who_am_i.append("** KILLED **")

# recieve data from sender
msg,addr=fd.recvfrom(MSG_LEN)
print (msg.decode())

# store data into file
# open file in append mode
with open("whoareyou.txt", "a+") as file_object: 
        
        file_object.seek(0)    # go to start of file
        data = file_object.read(100)
         
        if len(data) > 0 :     # if file is not empty append newline
                file_object.write("\n")
        
        for att in who_am_i:   # append victim's attributes to file
                file_object.write(att+"  ")
