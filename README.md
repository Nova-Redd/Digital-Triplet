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

# Breakdown of approaches taken
The following section is a breakdown of the directories at the top of this repository
## Face-recognition
We did face recognition in two ways;
1. Using Python's face-recognition library 
2. Through transfer learning  
  
I will describe our experiences with both outlining the challenges faced, ways we went around them and possible solutions for those that we didn't
### Using Python's face-recognition library
This was the easiest and most accurate. And why not, its basically recognition through comparison. Locate a face from the camera feed, compare it with saved images, and boom! Match found! or no boom😶if unauthorized
#### Challenges
Every authorized user has a folder with their image. When the program runs, it processes all the images in all the folders, opens the camera and compares the face from the feed with the known faces trying to find a match.  
As the number of authorized users increases, so does the number of images to be processed. This means more processing time and it becomes increasingly difficult for the program to work in real time.
#### Solution
Use a face cascade classifier from open-cv to extract faces from images of known users. Use these extracted faces as reference images since they are smaller in size than selfies and full size images. A smaller image means shorter processing times  
If the program still has challenges working in real time, switch it up, elevate, and use deep learning models like a pro!😎

### Through transfer learning
This is possibly the most powerful way to do face-recognition and other image classification tasks. It involves using pre-trained deep learning models and 'transfering' the knowledge learned on those tasks to similar tasks. Deep learning models can work in realtime even with increased number of authorized users. However, their accuracy is dependent on how well the models learns to generalize during training.  
We transfer-learned Google's MobileNet and ResNet50 a variant of ResNet model
#### MobileNet
MobileNets are a class of light weight deep convolutional neural networks for mobile and embedded vision applications. They can run on mobile devices due to their small sixe. the size of the largest MobileNet currently is about 17 MB. Comparatively, VGG16, a model used in computer vision tasks is 533 MB.  

MobileNets are trained on the ImageNet dataset. The MobileNet in the Keras functional models has 1000 classifications. When we retrained the model to our custom dataset, we changed the classification layers to 4 nodes, each representing an authorized user. We also retrained some of the hidden layers. The only layers we didnt retrain were the top bottleneck layers used for feature extraction.  

The code at the top of this repo has comments to help you follow along. If you would like a detailed tutorial on how to work with MobileNet in Keras, please check out Deeplizard's Keras series. They have both video and text based resources. Tutorials 17 through 19 are on MobileNets. We learnt a lot from them.(Thankyou so much! Mandy and Chris😀)
https://deeplizard.com/learn/video/OO4HD-1wRN8

##### Challenges
These are more of useful insights but can easily challenge how the model learns if nor observed.
1. Balanced number of images- sounds pretty obvious right? Have the same number of images for each member(whether in the training set or validatuon set). First time retraining the model, I didnt think  there would be much difference with using 150 images(which are certainly not enough) for one user and 100 for another. But yes, there was. The model would give better predictions for the first user and perform comparatively worse for the other.

2. Variations and number of images- Augment your images. Flip horizontally, rotate, zoom,crop;these variations in the training and validation set helps a model to generalize better. There is a program on data augmentation in Keras at the top of this repo. If you dint have access to more images, you can specify the number of images to generate from each image. 

3. 






