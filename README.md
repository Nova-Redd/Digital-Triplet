# Digital-Triplet (2021)
Virtual assistants for Digital Twin systems
https://youtu.be/dw2gzlr3fnk
https://youtu.be/FU8_GesplGM

# Task
Its 2020 and the world is in the fourth insustrial revolution!
Engineering Cyber-Physical systems are evolving from Digital Twin models to Digital Triplet.
At Dedan Kimathi University of Technology (DeKUT) SIEMENS Mechatronics Systems training centre, we are tasked to add Face-Recogniton security access and Voice assistants to the Digital Twin models of the Analytic and Thermal Process Control stations.
This repository outlines the approaches we took to achieve this

# Analytic and Thermal Process Control stations
![image](https://user-images.githubusercontent.com/83555928/116885724-0e3e0600-abdd-11eb-81c9-bcb157bec205.png)
![image](https://user-images.githubusercontent.com/83555928/116886682-39752500-abde-11eb-9f44-d28c2f63cf82.png)

Both of these stations are developed by Amatrol to teach and train on process control which is a vital part of major industries, including: power generation; petrochemicals; food processing and bottling; chemical manufacturing; biotechnology; pharmaceuticals and refineries.

The Analytic process control station monitors and regulates the pH of a process fluid. The station runs on PID Controller Module – Single Loop (T5554-C1-A) or PID Controller Module – Dual Loop (T5554-C2-A)

The Thermal process control station, on the other hand, regulates temperature. The controller for this station is PID Controller Module – Dual Loop (T5553-C2-A).

Here is a link to Amatrol's site if you wish to know more on Process control machines
https://amatrol.com/product/process-control-training/

In 2018, the team of Isaiah Nassiuma, Emanuel Sunguti, Langat KIpkoech Rogers and Timothy Kimari proposed a new control method based on the Siemens S7 1200 PLC PID control functionality.

In 2020, the controller used for both stations was the Siemens S7 1200 PLC (CPU 1214C DC/DC/DC)

# Criteria
1. Digital Twin models for the stations
2. Real time Face recognition
3. Intelligent voice assistant

# Tech Stack Summary
We used Siemens NX software to build the digital twin models. With the software, we could design and simulate realizing the best from the digital twins

PLC programs were written in the TIA portal(Totally Integrated Automation)

Face recognition and voice assistant programmes were written in Python. We chose Python due to its popularity in Artificial intelligence implementation. our face and voice recognition models had to be intelligent. Secondly, and full disclosure I believe this is one of the major reasons, we didnt have a lot of experience programming. Python has a very huge community, which is only growing, and growing😊 since the introduction of deep learning. We joined the community and keep learining so much! From basic programming, through machine-learning and deep learning fundamentals to deep learning APIs (Keras and a bit of Pytorch)

The models were created in Tensorflow Keras API

Communication between client machine and server computer was done through OPC UA protocol(Open Platform Communications Unified Architecture)

The Snap7 library was used to interface Python programs with the S7 1200 PLC

# Tech stack
1. Siemens NX
2. Siemens TIA portal
3. Python 
4. Tensorflow Keras API
5. OPC UA protocol
6. Snap7 library

# Functionality
1. Real time digital twin model
2. Realtime face recognition
3. General conversation with the machine
4. Specify the setpoints using voice in English
5. Control different components (pumps, motors, chiller) of the stations using speech 

# Breakdown of Work done



