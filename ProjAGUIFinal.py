#----------------  HIT F5 TO RUN PROGRAM !!! -------------



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

ProjAGUI.py - A Simple GUI program developed for Project A of the authors dissertation

__author__       = "Andrew Berston"
__contact__      = "andrewberston@live.co.uk"

__date__         = "10/04/2016"
__version__      = "Submission"


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



#!/usr/bin/env python       # Ensures correct version of python is used


#Headers

from Tkinter import *       # Imports certain sub-commands for Tkinter
import Tkinter              # Imports 'Tkinter' GUI Library
import os                   # Imports the 'OS' library - Allows the use of terminal commands, in this case, 'raspistill' and 'raspivid' for camera control
import time                 # Imports the 'time' library


top = Tkinter.Tk()          # Creates the 'top' Tkinter window
top.title("Camera Menu")    # Set's the name of the window to 'Camera Menu'



# Command Definitions

def LaunchPreview10():                                           # Begins the definition of the LaunchPreview10 command
    os.system("raspistill -t 10000")                             # Launches a camera preview window for 10,000ms (10s)

def LaunchPreview100():                                          # Begins the definition of the LaunchPreview100 command
    os.system("raspistill -t 100000")                            # Launches a camera preview window for 100,000ms (100s)

def TakePhoto():                                                 # Begins the definition of the TakePhoto command
    timestr = time.strftime("%d-%m-%Y_%H:%M:%S")                 # Sets the variable 'timestr' as the current date and time in the format; DD-MM-YYYY_HH:MM:SS
    filenamephoto = 'Image_' + timestr + '.jpg'                  # Sets the filename for the image, and sets the image type a s a jpeg - Image_currenttime.jpg
    cmdp = 'raspistill -o ' + filenamephoto + ' -t 1000'         # Creates variable cmdp - containing the raspistill command, inserts the filename, and the time to display the preview window for
    os.system("%s" %cmdp)                                        # Executes cmdp -  Takes a photo, names it the date and time, with a 1s preview

def TakeVideo10():                                               # Begins the definition of the TakeVideo10 command
    timestr = time.strftime("%d-%m-%Y_%H:%M:%S")                 # Sets the variable 'timestr' as the current date and time in the format; DD-MM-YYYY_HH:MM:SS
    filenamevideo = '10sVideo_' + timestr + '.h264'              # Sets the filename for the 10s video, and sets the file type as a H264 - Video_currenttime.h264
    cmdV1 = 'raspivid -o ' + filenamevideo + ' -t 10000 '        # Creates variable cmdV2 - containing the raspivid command, inserts the filename, and the time to record for
    os.system("%s" %cmdV1)                                       # Executes cmdV1 -  Starts Video capture for 10,000ms (10s)

def TakeVideo100():                                              # Begins the definition of the TakeVideo100 command
    timestr = time.strftime("%d-%m-%Y_%H:%M:%S")                 # Sets the variable 'timestr' as the current date and time in the format; DD-MM-YYYY_HH:MM:SS
    filenamevideo = '100sVideo_' + timestr + '.h264'             # Sets the filename for the 100s video, and sets the file type as a H264 - Video_currenttime.H264
    cmdV2 = 'raspivid -o ' + filenamevideo + ' -t 100000 '       # Creates variable cmdV1 - containing the raspivid command, inserts the filename, and the time to record for
    os.system("%s" %cmdV2)                                       # Executes cmdV2 - Starts Video capture for 100,000ms (100s) and titles files as filenamevideo

def EXIT():                                                      # Begins the definition of the EXIT command
    top.destroy()                                                # Will destroy 'top' window, i.e. will close the menu


# Widgets
    
    
J = Tkinter.Canvas(top, bg="white", height=440, width=800)                                                                                  # Sets properties of the 'top' Tkinter window
I = Tkinter.Button(top, text ="Preview 10", bg="white", activebackground="white", activeforeground="grey", command = LaunchPreview10)       # Sets properties of the 'Preview 10' button
Ilabel = Tkinter.Label(top, text=" - Starts a 10 second preview window.", bg="White", anchor = "w")                                         # Sets properties of 'Preview 10''s label
K = Tkinter.Button(top, text ="Preview 100", bg="white", activebackground="white", activeforeground="grey", command = LaunchPreview100)     # Sets properties of the 'Preview 100' button
Klabel = Tkinter.Label(top, text=" - Starts a 100 second preview window.", bg="White", anchor = "w")                                        # Sets properties of 'Preview 100''s label
F = Tkinter.Button(top, text ="Photo", bg="white", activebackground="white", activeforeground="grey", command = TakePhoto)                  # Sets properties of the 'Photo' button
Flabel = Tkinter.Label(top, text=" - Takes a Photo after a 1 second preview.", bg="White", anchor = "w")                                    # Sets properties of 'Photo''s label
G = Tkinter.Button(top, text ="Video 10", bg="white", activebackground="white", activeforeground="grey", command = TakeVideo10)             # Sets properties of the 'Video 10' button
Glabel = Tkinter.Label(top, text=" - Starts a 10 second video capture (with preview).", bg="White", anchor = "w")                           # Sets properties of 'Video 10''s label
L = Tkinter.Button(top, text ="Video 100", bg="white", activebackground="white", activeforeground="grey", command = TakeVideo100)           # Sets properties of the 'Video 100' button
Llabel = Tkinter.Label(top, text=" - Starts a 100 second video capture (with preview).", bg="White", anchor = "w")                          # Sets properties of 'Video 100''s label
E = Tkinter.Button(top, text ="EXIT?", bg="white", activebackground="white", activeforeground="grey", command = EXIT)                       # Sets properties of the 'EXIT?' button
Elabel = Tkinter.Label(top, text=" - Exits the program (Any previews / captures will continue till timed out).", bg="White", anchor = "w")  # Sets properties of 'EXIT?''s label


# Widget Properties

J.pack()                                                                            # Creates 'top' window
I.pack()                                                                            # Creates 'Preview 10' button
I.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.1, relx=0, rely=0.1)         #Establishes size and position for the 'Preview 10' button
Ilabel.pack()                                                                       # Creates 'Preview 10''s label 
Ilabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.8, relx=0.2, rely=0.1)  #Establishes size and position for the 'Preview 10''s label
K.pack()                                                                            # Creates 'Preview 100' button
K.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.1, relx=0, rely=0.2)         #Establishes size and position for the 'Preview 100' button
Klabel.pack()                                                                       # Creates 'Preview 100''s label 
Klabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.8, relx=0.2, rely=0.2)  #Establishes size and position for the 'Preview 100''s label
F.pack()                                                                            # Creates 'Photo' button
F.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.1, relx=0, rely=0.4)         #Establishes size and position for the 'Photo' button
Flabel.pack()                                                                       # Creates 'Photo''s label 
Flabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.8, relx=0.2, rely=0.4)  #Establishes size and position for the 'Photo''s label
G.pack()                                                                            # Creates 'Video 10' button
G.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.1, relx=0, rely=0.6)         #Establishes size and position for the 'Video 10' button
Glabel.pack()                                                                       # Creates 'Video 10''s label 
Glabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.8, relx=0.2, rely=0.6)  #Establishes size and position for the 'Video 10''s label
L.pack()                                                                            # Creates 'Video 100' button
L.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.1, relx=0, rely=0.7)         #Establishes size and position for the 'Video 100' button
Llabel.pack()                                                                       # Creates 'Video 100''s label 
Llabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.8, relx=0.2, rely=0.7)  #Establishes size and position for the 'Video 100''s label
E.pack()                                                                            # Creates 'EXIT?' button
E.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.1, relx=0, rely=0.9)         #Establishes size and position for the 'EXIT?' button
Elabel.pack()                                                                       # Creates 'EXIT?''s label 
Elabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.8, relx=0.2, rely=0.9)  #Establishes size and position for the 'EXIT?''s label


#End

top.mainloop() 
