# Assignment 3 Write Up

## Inspiration 
The listening post served as an inspiration for my work. The idea of eavesdropping snippets of texts sent by strangers sparked my imagination and curiosity. The fact that it was live added further to that, someone somewhere at this moment in time has sent this. How is that person feeling? Are they lonely? Are they having a bad day? Where are they going? Why? I tried to create context, build an identity, and connect with those stranges as I eavesdropped on their messages.

## My Work 

In my work, the audience eavesdrop on the chat between the victim and the savior. Just like the listening post, the victims did not know this would be presented to an audience, or else they would have perhaps described themselves differently, more artificially and formally. The audience eavesdrop on the victims natural self. They get to build their own image of that person based on four or five words that describe them. 


Yet, just like the listening post, the stranger is completely unaware that someone out there is reflecting on them, that they have dominated someone’s mind for at least a few seconds. They have no idea that they are a part of someone’s artwork


The victim’s identity is given more emphasis in my work. The audience sees a picture of the victim for a few seconds and gains snippets of the victim’s identity through the chat. The victim is a complete stranger, and the prompt is imaginary, but that it builds a connection from the audience to the victim as they stand on their toes waiting to see the fortune of this stranger complete, hoping they will survive. 


## Code
I used socket programming to connect two computers. I recorded the IP addresses of both computers and selected a unique port number for each of them. The code is run through the terminal. Both computers have to be connected to the same WiFi router for this to work.
 
 
### Kidnapped.py 
This code file asks the user for their name. It then prints out the prompt that they have been kidnapped and an anonymous person that they know can save them if they guess who they are correctly.  The user can only send one word description of themselves to give hints. 
Once that anonymous person makes the guess, one of two messages is printed. Correct, and that the user gets released, or incorrect and that user will be killed now. The user’s name and list of words that describe them are stored into a file. If the user has been killed, it states so. 
 
### Savior.py
This code prints the prompt to the user that one of the people they know has been kidnapped and only they can save them. They have only one guess. Once they enter START the victim will start sending them hints. Once the user makes the guess, the fate of the victim will be printed out. If the guess is correct, it will print that the user saved the victim’s life, and if incorrect that the victim will be killed. 
 
### whoami.txt
This file stores all the data. I chose this name specifically, because that is what the victim has to think of. Who am I? What identifies me? What makes me unique and different from the people around me? Because they can only choose one word, they had to be selective. They had to look for their biggest identifiers, the most obvious yet unique. Under time pressure, they had to think fast, the first thing that pops up, the most meaningful things, the biggest things, the most special. 
 
It is also interesting being the observer. Looking at what words the victim picked. Would they pick personality traits, hobbies, job or education, things they like, or things they own? Does that signify anything? I found this to be interesting to think about.

## Video 
I consider the video, or my output, to be my artwork, and the victim and the savior are the artists. The victim drizzles the piece with their identity and the fortune of the piece is in the hands of the savior. 

The video starts with a robotic sound describing the situation of the victim and the savior. To create that sound, I used gtts for text-to-speech conversion. Using a robotic sound added to the theme of anonymity and hidden identity. A photo of the victim is then displayed for a few seconds to give the audience an idea of the victims external identity (age, gender, race), then immediately after is the chat determining their fate and unveiling their internal identity. I used a time ticking sound effect that keeps going throughout the chat and increasingly gets faster creating tension and keeping the audience focused. 

