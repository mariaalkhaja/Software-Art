
from socket import *
import sys

TO_ADDR=('192.168.1.109',8135)    # store reciever IP and port no
hostname=gethostbyname('0.0.0.0') # gets IP adress of host 
LOCAL_ADDR=(hostname,8138)        # store host IP and port
MSG_LEN=1000                      # message length
fd=socket(AF_INET, SOCK_DGRAM)    # create new socket 
fd.bind(LOCAL_ADDR)               # bind socket to port 

addr = TO_ADDR
data=''
msg=''
count = 0

# function to recieve data
def recv():
	data,addr=fd.recvfrom(MSG_LEN)      # recieve data
	print ('anonymous:',data.decode())  # print decoded data
	data = data.decode()
	return data,addr 

# function to send message 
def send(msg,addr):
        msg = msg.encode()    # encode message 
        fd.sendto(msg,addr)   # send to address

# while user has not made a guess
while '?' not in msg:
        count += 1
        # print instructions
        if (count == 1):
                print ("\n\n-------------------------------------------------------------")
                print ("you have only one chance to guess to the sender is")
                print ("if you guess incorrectly, their head will be chopped off")
                print ("they can only send you one word that describes them at a time")
                print ("for more hints send '.', and when you're ready to guess send")
                print ("their name followed by a question mark.")
                print ("WHEN YOU ARE READY, ENTER 'START'")
                print ("-------------------------------------------------------------\n\n")

        msg=input('you: ') # get user input
        send(msg,addr)     # send input message
        data,addr=recv()   # get message from reciever

# check if guess was correct or not
if "Incorrect" in data:
        send("They guessed wrong. You will be killed NOW.", addr)
else:
        send("That was close, you have been saved.", addr)
