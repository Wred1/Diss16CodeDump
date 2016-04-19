



                  #----------------  HIT F5 TO RUN PROGRAM !!! -------------





"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

ProjBGUI.py - A Simple GUI program developed for Project B of the authors dissertation

__author__       = "Andrew Berston"
__contact__      = "andrewberston@live.co.uk"

__date__         = "18/04/2016"
__version__      = "Submission"


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""







#------------------------------LIBRARIES--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


from Tkinter import *                         # Imports Tkinter sub-commands
import Tkinter as Tk                          # Imports Tkinter library, as tk. for simpler/shorter commands
import RPi.GPIO as gp                         # Imports RPi.GPIO library as gp. for simpler/shorter commands
import os                                     # Imports OS library for terminal commands
import picamera                               # Imports picamera library for extended camera control
import time                                   # Imports time library, for delays, and converting clock time to integr for file names
import Tkconstants                            # Allows Tkinter extra abilities in controlling variables
import tkFileDialog                           # Gives Tkinter ability to simply control file directorys **not used**
import tkMessageBox                           # Gives Tkinter simple commands for creating pop up boxes
import tkFont


#---------------------------------SETUP------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

previewint = 0                          # Sets previewint (is preview live?) integer up as 0

gp.setwarnings(False)                   # Sets up GPIO pins
gp.setmode(gp.BOARD)                    #    "

gp.setup(7, gp.OUT)                     # Sets up pin 7 as an output pin (multiplexer control)
gp.setup(11, gp.OUT)                    #    "
gp.setup(12, gp.OUT)                    #    "
gp.setup(31, gp.OUT)                    # Sets up pin 11 as an output pin (stepper control)
gp.setup(32, gp.OUT)                    #    "
gp.setup(36, gp.OUT)                    #    "
gp.setup(37, gp.OUT)                    #    "

gp.output(7, False)                     #\
gp.output(11, False)                    ## Sets Multiplexer to channel A
gp.output(12, True)                     #/

gp.setup(33, gp.OUT)                    #\
ledpwm = gp.PWM(33, 50)                 ## Sets up led pwm pin, and turns led off
ledpwm.start(100)                       #/
 

#-----------------------------------START CLASS--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 
class MyApp(object):                    # Entire program is ran in a class, as a more efficient way to run multiple tk windows

 import RPi.GPIO as gp             # Reimport Rpi.GPIO within class to set as gp. for simpler commands          

#----------------------------------MAIN WINDOW----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
 def __init__(self, parent):

        global f                         # Globalises new font f
        
        self.root = parent               # Establishes this window as the parent
        self.root.title("Main Menu")     # Sets root window position
        self.root.geometry("+0+0")       # Sets position of root window

        self.frame = Tk.Canvas(parent, bg = "White", height = 420, width = 80) # Sets up root window properties
        self.frame.pack()                                                      # Starts root window
        
        PREVIEW = Tk.Button(self.frame, text="Preview?",bg="white", activebackground="white", activeforeground="grey", command=self.preview)         ##\
        PREVIEW.pack()                                                                                                                               #  # Sets up the 'Preview?' buttons properties and position
        PREVIEW.place(relheight=0.05, relwidth=1, relx=0.0, rely=0.1)                                                                                ##/
        PHOTO = Tk.Button(self.frame, text="Photo", bg="white", activebackground="white", activeforeground="grey", command=self.photo)               ##\
        PHOTO.pack()                                                                                                                                 #  # Sets up the 'Photo' buttons properties and position
        PHOTO.place(relheight=0.05, relwidth=1, relx=0.0, rely=0.25)                                                                                 ##/    
        TIMELAPSE = Tk.Button(self.frame, text="Timelapse", bg="white", activebackground="white", activeforeground="grey", command=self.timelapse)   ##\
        TIMELAPSE.pack()                                                                                                                             #  # Sets up the 'Timelapse' buttons properties and position
        TIMELAPSE.place(relheight=0.05, relwidth=1, relx=0.0, rely=0.34)                                                                             ##/   
        VIDEO = Tk.Button(self.frame, text="Video", bg="white", activebackground="white", activeforeground="grey", command=self.video)               ##\
        VIDEO.pack()                                                                                                                                 #  # Sets up the 'Video' buttons properties and position
        VIDEO.place(relheight=0.05, relwidth=1, relx=0.0, rely=0.43)                                                                                 ##/ 
        LED = Tk.Button(self.frame, text="LED", bg="white", activebackground="white", activeforeground="grey", command=self.led)                     ##\
        LED.pack()                                                                                                                                   #  # Sets up the 'LED' buttons properties and position
        LED.place(relheight=0.05, relwidth=1, relx=0.0, rely=0.6)                                                                                    ##/   
        STEPPER = Tk.Button(self.frame, text="Stepper", bg="white", activebackground="white", activeforeground="grey", command=self.stepper)         ##\
        STEPPER.pack()                                                                                                                               #  # Sets up the 'Stepper' buttons properties and position
        STEPPER.place(relheight=0.05, relwidth=1, relx=0.0, rely=0.69)                                                                               ##/  
        SETTINGS = Tk.Button(self.frame, text="Settings", bg="white", activebackground="white", activeforeground="grey", command=self.settings)      ##\
        SETTINGS.pack()                                                                                                                              #  # Sets up the 'Settings' buttons properties and position
        SETTINGS.place(relheight=0.05, relwidth=1, relx=0.0, rely=0.84)                                                                              ##/  
        EXIT = Tk.Button(self.frame, text="EXIT?", bg="white", activebackground="white", activeforeground="grey", command=self.destroy)              ##\
        EXIT.pack()                                                                                                                                  #  # Sets up the 'Exit?' buttons properties and position
        EXIT.place(relheight = 0.05, relwidth=1, relx = 0.0, rely=0.93)                                                                              ##/    

        Menulabel = Tk.Label(self.frame, text="Main Menu", bg="White", anchor = "center")                             #\                
        Menulabel.pack()                                                                                              ## Sets up the label properties and position for button D
        Menulabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=1, relx=0.0, rely=0.0)                           #/
        f = tkFont.Font(Menulabel, Menulabel.cget("font"))                                                            # Creates new font, takes properties from font used in Menulabel
        f.configure(underline = True)                                                                                 # Make new font underlined
        Menulabel.configure(font = f)                                                                                 # Sets Menulabelfont to new font 'f'

        #Geometry
        self.frame.create_line(0, 30, 80, 30, fill = "#8cf")           # Creates line between menu buttons
        self.frame.create_line(0, 85, 80, 85, fill ="#8cf")            #  "
        self.frame.create_line(0, 230, 80, 230, fill ="#8cf")          #  "
        self.frame.create_line(0, 332, 80, 332, fill ="#8cf")          #  "
      

#-------------------------------SECONDARY WINDOWS------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #-------------------Preview Toggle--------------------------------------------------------------------------------------------------------------------
 def preview(self):                                            # Preview button command
      global previewint                                     
      if previewint == 0:                                      #\ 
            self.camera=picamera.PiCamera()                    ##\
            self.camera.resolution = (2592, 1944)              ###\
            self.camera.preview_fullscreen = False             ##### Checks if preview is live,if not, sets it live with these properties
            self.camera.preview_window = (80,0,640,480)        ###/
            self.camera.start_preview()                        ##/
            previewint = 1                                     #/
      else :
            previewint = 0                                     #\
            self.camera.stop_preview()                         ## If preview is live, stops preview, and ends camera processes
            self.camera.close()                                #/


        
 #----------------------------Photo Options-------------------------------------------------------------------------------------------------------------

 def photo(self):

        global DNP, Lb1, cnp, cdp, cfp
        

        self.cnp = Tk.IntVar()                              # Sets variable PA as an intger
        self.cdp = Tk.IntVar()                              # Sets variable PA as an intger
        self.cfp = Tk.IntVar()                              # Sets variable PA as an intger
        self.typep = Tk.IntVar()
        
        # self.hide()                                # Leftover code from 'hiding' sub-menus
        otherFrame = Tk.Toplevel(bg = "White")       # Sets Sub-Menu background colour to white
        otherFrame.geometry("720x420")               # Sets Sub-Menu window size
        otherFrame.geometry("+80+40")                # Sets Sub-Menu window position
        otherFrame.title("Photo")                    # Sets Sub-Menu title bar to say 'Photo'
        otherFramecanvas = Tk.Canvas(otherFrame, bg = "White") # Sets up root window properties
        otherFramecanvas.pack(expand=Tk.YES, fill=Tk.BOTH)     # Starts root window

         #-- Right Menu
        
        A = Tk.Button(otherFrame, text ="A", bg="white", activebackground="white", activeforeground="grey", command=self.gpioa)     ##\
        A.pack()                                                                                                                    #  # Sets up the 'A' buttons properties and position
        A.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.15)                                                                ##/
        B = Tk.Button(otherFrame, text ="B", bg="white", activebackground="white", activeforeground="grey", command=self.gpiob)     ##\
        B.pack()                                                                                                                    #  # Sets up the 'B' buttons properties and position
        B.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.25)                                                                ##/
        C = Tk.Button(otherFrame, text ="C", bg="white", activebackground="white", activeforeground="grey", command =self.gpioc)    ##\
        C.pack()                                                                                                                    #  # Sets up the 'C' buttons properties and position
        C.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.35)                                                                ##/
        D = Tk.Button(otherFrame, text ="D", bg="white", activebackground="white", activeforeground="grey", command =self.gpiod)    ##\
        D.pack()                                                                                                                    #  # Sets up the 'D' buttons properties and position
        D.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.45)                                                                ##/

        Alabel = Tk.Label(otherFrame, text="Selects Camera A. - ", bg="White", anchor = "e")                       #\                
        Alabel.pack()                                                                                              ## Sets up the label properties and position for button A
        Alabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.15)                      #/
        Blabel = Tk.Label(otherFrame, text="Selects Camera B. - ", bg="White", anchor = "e")                       #\                
        Blabel.pack()                                                                                              ## Sets up the label properties and position for button B
        Blabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.25)                      #/
        Clabel = Tk.Label(otherFrame, text="Selects Camera C. - ", bg="White", anchor = "e")                       #\                
        Clabel.pack()                                                                                              ## Sets up the label properties and position for button C
        Clabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.35)                      #/
        Dlabel = Tk.Label(otherFrame, text="Selects Camera D. - ", bg="White", anchor = "e")                       #\                
        Dlabel.pack()                                                                                              ## Sets up the label properties and position for button D
        Dlabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.45)                      #/
       
        Capture = Tk.Button(otherFrame, text ="Capture?", bg="white", activebackground="white", activeforeground="grey", command =self.capture)     ##\
        Capture.pack()                                                                                                                              #  # Sets up the 'Capture' buttons properties and position
        Capture.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.9)                                                                           ##/
        Capturelabel = Tk.Label(otherFrame, text="Captures image from selected camera. - ", bg="White", anchor = "e")                               ##\                
        Capturelabel.pack()                                                                                                                         #  # Sets up the label properties and position for capture
        Capturelabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.885, relx=0.0, rely=0.9)                                                  ##/

         #-- Titles

        Photolabelmain = Tk.Label(otherFrame, text="Photo Menu", bg="White", anchor = "center")                            #\                
        Photolabelmain.pack()                                                                                              ## Sets up the label properties and position for button D
        Photolabelmain.place(bordermode=OUTSIDE, relheight=0.15, relwidth=0.885, relx=0.0, rely=0.0)                       #/
        f = tkFont.Font(Photolabelmain, Photolabelmain.cget("font"))                                                       # Creates new font, takes properties from font used in Menulabel
        f.configure(underline = True, size = 30)                                                                           # Make new font underlined
        Photolabelmain.configure(font = f)                                                                                 # Sets Menulabelfont to new font 'f'

        Photolabel = Tk.Label(otherFrame, text="Photo", bg="White", anchor = "center")                                     #\                
        Photolabel.pack()                                                                                                  ## Sets up the label properties and position for the photo label
        Photolabel.place(bordermode=OUTSIDE, relheight=0.1, relwidth=0.1, relx=0.895, rely=0.0)                            #/
        g = tkFont.Font(Photolabel, Photolabel.cget("font"))                                                               # Creates new font, takes properties from font used in Photolabel
        g.configure(underline = True,)                                                                                     # Makes font underlind
        Photolabel.configure(font = g)                                                                                     # Sets title to use new font 'g'

         #-- Settings

        CNP = Tk.Checkbutton(otherFrame, text = "Custom Name", variable = self.cnp, onvalue = 1, offvalue = 0, height = 5, width = 20, bg="white", activebackground="white", activeforeground="grey" )
        CNP.pack()                                                              ## Sets up checkbutton for custom name's properties and position
        CNP.place(relheight=0.07, relwidth=0.4, relx=0.005, rely=0.25)          #/

        CNPL = Label(otherFrame, text="i.e. - Experiment 6, Print 5, etc...", bg = "White")               #\
        CNPL.pack()                                                                                       ##\
        CNPL.place(relheight=0.05, relwidth=0.2, relx=0.205, rely=0.335)                                  ###\ 
        CNPL2 = Label(otherFrame, text="(Deafult = Date + Time)", bg = "White")                           ####\
        CNPL2.pack()                                                                                      ##### Sets up info labels and entry box for custom name
        CNPL2.place(relheight=0.05, relwidth=0.2, relx=0.205, rely=0.385)                                 ####/
        self.CNPE = Entry(otherFrame, bg = "White", bd=5)                                                 ###/ 
        self.CNPE.pack()                                                                                  ##/
        self.CNPE.place(relheight=0.07, relwidth=0.2, relx=0.005, rely=0.35)                              #/

        CDP = Tk.Checkbutton(otherFrame, text = "Custom Directory", variable = self.cdp, onvalue = 1, offvalue = 0, height = 5, width = 20, bg="white", activebackground="white", activeforeground="grey" )  
        CDP.pack()                                                               ## Sets up checkbutton for custom directorie's properties and position  
        CDP.place(relheight=0.07, relwidth=0.4, relx=0.005, rely=0.45)           #/

        CDPL = Label(otherFrame, text="i.e. - /media/pi/MyMemoryStick", bg = "White")                     #\
        CDPL.pack()                                                                                       ##\
        CDPL.place(relheight=0.05, relwidth=0.2, relx=0.205, rely=0.535)                                  ###\ 
        CDPL2 = Label(otherFrame, text="(Default = Desktop)", bg = "White")                               ####\
        CDPL2.pack()                                                                                      ##### Sets up info labels and entry box for custom name
        CDPL2.place(relheight=0.05, relwidth=0.2, relx=0.205, rely=0.585)                                 ####/ 
        self.CDPE = Entry(otherFrame, bg = "White", bd=5)                                                 ###/ 
        self.CDPE.pack()                                                                                  ##/
        self.CDPE.place(relheight=0.07, relwidth=0.2, relx=0.005, rely=0.55)                              #/

        CFP = Tk.Checkbutton(otherFrame, text = "Save as PNG?", variable = self.typep, onvalue = 1, offvalue = 0, height = 5, width = 20, bg="white", activebackground="white", activeforeground="grey" ) 
        CFP.pack()                                                               ## Sets up checkbutton for custom file type's properties and position  
        CFP.place(relheight=0.07, relwidth=0.4, relx=0.005, rely=0.65)           #/
        Typeplabel = Label(otherFrame, text="(Deafault = Jpeg)", bg = "White")                            #\
        Typeplabel.pack()                                                                                 ## Sets up properties and position of info label
        Typeplabel.place(relheight=0.05, relwidth=0.2, relx=0.105, rely=0.755)                            #/

        h = tkFont.Font(CNP, CNP.cget("font"))                                                           # Creates new font, takes properties from font used in CNP
        h.configure(size = 6)                                                                            # Makes new font size 6
        CNPL.configure(font = h)                                                                         # Sets label CNPL to use new font 'h'
        CDPL.configure(font = h)                                                                         # Sets label CDPL to use new font 'h'
        CNPL2.configure(font = h)                                                                        # Sets label CNPL2 to use new font 'h'  
        CDPL2.configure(font = h)                                                                        # Sets label CDPL2 to use new font 'h'
        Typeplabel.configure(font = h)                                                                   # Sets label Listlabel to use new font 'h'

        #-- Geometry

        otherFramecanvas.create_line(640, 0, 640, 480, fill ="#8cf")                                     # Inserts line to define border of preview


    #------Photo Option Sub-Section----

 def gpioa(self):                              # gpioa button command
        self.gp.output(7, False)               #\
        self.gp.output(11, False)              ## GPIO config for channel A camera selection
        self.gp.output(12, True)               #/
      
 def gpiob(self):                              # gpiob button command
        self.gp.output(7, True)                #\
        self.gp.output(11, False)              ## GPIO config for channel B camera selection
        self.gp.output(12, True)               #/
   
 def gpioc(self):                              # gpioc button command
        self.gp.output(7, False)               #\
        self.gp.output(11, True)               ## GPIO config for channel C camera selection
        self.gp.output(12, False)              #/
  
 def gpiod(self):                              # gpiod button command
        self.gp.output(7, True)                #\
        self.gp.output(11, True)               ## GPIO config for channel D camera selection
        self.gp.output(12, False)              #/

 def capture(self) :

      namequery = self.cnp.get()
      directoryquery = self.cdp.get()
      filetypequery = self.typep.get()

      filenamep = self.CNPE.get()
      directorypstr = self.CDPE.get()
      self.directoryp = str(directorypstr)

      timestr = time.strftime("%d-%m-%Y_%H:%M:%S")      # Gets current date and time in the set format, and assigns str to variable timestr                      
      millis = int(round(time.time() * 1000))           # Gets current milliseconds (based off equation) and sets int to variable milis
      timenamep = timestr + ':' + str(millis)           # Sets variable timenamep as the date/time followed by the milliseconds

      if namequery == 1:                                # If the custom name checkbox is ticked
          namepp = filenamep                            # the file name will be the box entry
      else:                                             #
          namepp = timenamep                            # If not, name is set as the date/time
    
      if filetypequery == 1:                            # If the .png filetype checkbox is ticked
          filetypepp = '.png'                           # The file will have the suffix .png
      else:                                             #
          filetypepp = '.jpg'                           # If not, will be .jpg

      if directoryquery == 1:                                      # If the custom directory box is checked
          cap =  self.directoryp + ', ' + namepp + filetypepp      # The final capture command is the directory, then the name followed by the filetype
      else:                                                        #
          cap = namepp + filetypepp                                # Otherwise the final capture command is the name followed by the filetype

      global previewint                                         # Imports the 'preview' integer                            
      
      if previewint == 0:
            self.camera=picamera.PiCamera()                     #\
            self.camera.resolution = (2592, 1944)               ##\
            self.camera.preview_fullscreen = False              ### Checks if the preview is currently live
            self.camera.preview_window = (80,70,640,480)        ### If not, sets up camera, and preview, set previewint to 2
            self.camera.start_preview()                         ##/
            previewint = 2                                      #/

      self.camera.capture(cap)                                  # Image capture command, based off earlier set variable cap
         
   
      if previewint == 2:                                       #\
            self.camera.stop_preview()                          ## If previewint = 2, i.e. preview wasnt on before capture was pressed
            self.camera.close()                                 ## After capture is done, preview is closed again, i.e. returns to state 0
            previewint = 0                                      #/


 #----------------------------Timelapse Options----------------------------------------------------------------------------------------------------------------

 def timelapse(self):
        # self.hide()                                      # Leftover code from 'hiding' sub-menus
        # otherFrame.hide()                                # Leftover code from 'hiding' sub-menus
        otherFrame = Tk.Toplevel(bg = "White")             # Sets Sub-Menu background colour to white
        otherFrame.geometry("720x420")                     # Sets Sub-Menu window size
        otherFrame.geometry("+80+40")                      # Sets Sub-Menu window position
        otherFrame.title("Timelapse")                      # Sets Sub-Menu window title to 'Timelapse'
        otherFramecanvas = Tk.Canvas(otherFrame, bg = "White") # Sets up root window properties
        otherFramecanvas.pack(expand=Tk.YES, fill=Tk.BOTH)     # Starts root window

       #Setup Integers
  
        global PA, PB, PC, PD                              # Makes PA PB PC and PD available globally


        self.cnt = Tk.IntVar()
        self.cdt = Tk.IntVar()
        self.typet = Tk.IntVar()

        self.PA = Tk.IntVar()                              # Sets variable PA as an intger
        self.PB = Tk.IntVar()                              # Sets variable PB as an intger
        self.PC = Tk.IntVar()                              # Sets variable PC as an intger
        self.PD = Tk.IntVar()                              # Sets variable PD as an intger

       #Checkboxes
        PAC = Tk.Checkbutton(otherFrame, text = "Cam A", variable = self.PA, onvalue = 1, offvalue = 0, height = 5, width = 20, bg="white", activebackground="white", activeforeground="grey" )   ##\
        PBC = Tk.Checkbutton(otherFrame, text = "Cam B", variable = self.PB, onvalue = 1, offvalue = 0, height = 5, width = 20, bg="white", activebackground="white", activeforeground="grey" )   ### Sets the checkboxes properties
        PCC = Tk.Checkbutton(otherFrame, text = "Cam C", variable = self.PC, onvalue = 1, offvalue = 0, height = 5, width = 20, bg="white", activebackground="white", activeforeground="grey" )   ##/
        PDC = Tk.Checkbutton(otherFrame, text = "Cam D", variable = self.PD, onvalue = 1, offvalue = 0, height = 5, width = 20, bg="white", activebackground="white", activeforeground="grey" )   #/
        PAC.pack()    ##\
        PBC.pack()    ### Sets up the checkboxes
        PCC.pack()    ##/
        PDC.pack()    #/
        PAC.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.15)        ##\
        PBC.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.25)        ### Sets the checkboxes positions
        PCC.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.35)        ##/
        PDC.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.45)        #/

        PAClabel = Tk.Label(otherFrame, text="Selects Camera A. - ", bg="White", anchor = "e")                         #\                
        PAClabel.pack()                                                                                                ## Sets up the label properties and position for chackbox A
        PAClabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.15)                        #/
        PBClabel = Tk.Label(otherFrame, text="Selects Camera B. - ", bg="White", anchor = "e")                         #\                
        PBClabel.pack()                                                                                                ## Sets up the label properties and position for chackbox B
        PBClabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.25)                        #/
        PCClabel = Tk.Label(otherFrame, text="Selects Camera C. - ", bg="White", anchor = "e")                         #\                
        PCClabel.pack()                                                                                                ## Sets up the label properties and position for chackbox C
        PCClabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.35)                        #/
        PDClabel = Tk.Label(otherFrame, text="Selects Camera D. - ", bg="White", anchor = "e")                         #\                
        PDClabel.pack()                                                                                                ## Sets up the label properties and position for checkbox D
        PDClabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.45)                        #/

        Infolabel = Tk.Label(otherFrame, text="(Multiple Cameras can be selected.)", bg="White", anchor = "w")         #\                
        Infolabel.pack()                                                                                               ## Sets up the label properties and position for informational label
        Infolabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.4, relx=0.05, rely=0.85)                        #/

       #Data Entry
        BETL = Label(otherFrame, text="Time (s)", bg = "White")               #\
        BETL.pack()                                                           ##\
        BETL.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.55)       #### Sets up 'time between captures' entry box, and label
        self.BETE = Entry(otherFrame, bg = "White", bd=5)                     #### Sets properties and positions
        self.BETE.pack()                                                      ##/
        self.BETE.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.62)  #/
        REPL = Label(otherFrame, text="Repeat?", bg = "White")                #\
        REPL.pack()                                                           ##\
        REPL.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.70)       #### Sets up 'time between captures' entry box, and label
        self.REPE = Entry(otherFrame, bg = "White", bd=5)                     #### Sets properties and positions)
        self.REPE.pack()                                                      ##/
        self.REPE.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.77)  #/


        Timelabel = Tk.Label(otherFrame, text="Time between captures (non-zero value). - ", bg="White", anchor = "e")                 #\                
        Timelabel.pack()                                                                                                              ## Sets up the label properties and position for entry box time
        Timelabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.485, relx=0.4, rely=0.57)                                      #/
        Timelabel2 = Tk.Label(otherFrame, text="(Does not account for time taken to capture). - ", bg="White", anchor = "e")          #\                
        Timelabel2.pack()                                                                                                             ## Sets up the label properties and position for entry box time2
        Timelabel2.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.485, relx=0.4, rely=0.64)                                     #/               
        Repeatlabel = Tk.Label(otherFrame, text="The number of times a photo will be captured. - ", bg="White", anchor = "e")         #\                
        Repeatlabel.pack()                                                                                                            ## Sets up the label properties and position for entry box repeat
        Repeatlabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.485, relx=0.4, rely=0.77)                                    #/


       #Start Timelapse Button
        StartT = Tk.Button(otherFrame, text ="Start?", bg="white", activebackground="white", activeforeground="grey", command =self.starttimelapse)  #\
        StartT.pack()                                                                                                                                ##Sets up button for starting timelapse, properties and positions
        StartT.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.9)                                                                             #/
        Repeatlabel = Tk.Label(otherFrame, text="Starts timelapse. - ", bg="White", anchor = "e")                                                    #\                
        Repeatlabel.pack()                                                                                                                           ## Sets up the label properties and position for button start
        Repeatlabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.8, relx=0.0, rely=0.9)                                                      #/

       #Titles

        Timelapselabelmain = Tk.Label(otherFrame, text="Timelapse Menu", bg="White", anchor = "center")                        #\                
        Timelapselabelmain.pack()                                                                                              ## Sets up the label properties and position for menu title
        Timelapselabelmain.place(bordermode=OUTSIDE, relheight=0.15, relwidth=0.885, relx=0.0, rely=0.0)                       #/
        f = tkFont.Font(Timelapselabelmain, Timelapselabelmain.cget("font"))                                                   # Creates new font, takes properties from font used in Timelapselabel
        f.configure(underline = True, size = 30)                                                                               # Make new font underlined
        Timelapselabelmain.configure(font = f)                                                                                 # Sets Menulabelfont to new font 'f'

        Timelapselabel = Tk.Label(otherFrame, text="Timelapse", bg="White", anchor = "center")                                 #\                
        Timelapselabel.pack()                                                                                                  ## Sets up the label properties and position for the timelapse label
        Timelapselabel.place(bordermode=OUTSIDE, relheight=0.1, relwidth=0.1, relx=0.895, rely=0.0)                            #/
        g = tkFont.Font(Timelapselabel, Timelapselabel.cget("font"))                                                           # Creates new font, takes properties from font used in Timelapselabel
        g.configure(underline = True,)                                                                                         # Makes font underlind
        Timelapselabel.configure(font = g)                                                                                     # Sets title to use new font 'g'

       #Settings

        CNT = Tk.Checkbutton(otherFrame, text = "Custom Name", variable = self.cnt, onvalue = 1, offvalue = 0, height = 5, width = 20, bg="white", activebackground="white", activeforeground="grey" )
        CNT.pack()                                                              ## Sets up checkbutton for custom name's properties and position
        CNT.place(relheight=0.07, relwidth=0.4, relx=0.005, rely=0.25)          #/

        CNTL = Label(otherFrame, text="i.e. - Experiment 6, Print 5, etc...", bg = "White")               #\
        CNTL.pack()                                                                                       ##\
        CNTL.place(relheight=0.05, relwidth=0.2, relx=0.205, rely=0.335)                                  ###\ 
        CNTL2 = Label(otherFrame, text="(Deafult = Date + Time)", bg = "White")                           ####\
        CNTL2.pack()                                                                                      ##### Sets up info labels and entry box for custom name
        CNTL2.place(relheight=0.05, relwidth=0.2, relx=0.205, rely=0.385)                                 ####/
        self.CNTE = Entry(otherFrame, bg = "White", bd=5)                                                 ###/ 
        self.CNTE.pack()                                                                                  ##/
        self.CNTE.place(relheight=0.07, relwidth=0.2, relx=0.005, rely=0.35)                              #/

        CDT = Tk.Checkbutton(otherFrame, text = "Custom Directory", variable = self.cdt, onvalue = 1, offvalue = 0, height = 5, width = 20, bg="white", activebackground="white", activeforeground="grey" )  
        CDT.pack()                                                               ## Sets up checkbutton for custom directorie's properties and position  
        CDT.place(relheight=0.07, relwidth=0.4, relx=0.005, rely=0.45)           #/

        CDTL = Label(otherFrame, text="i.e. - /media/pi/MyMemoryStick", bg = "White")                     #\
        CDTL.pack()                                                                                       ##\
        CDTL.place(relheight=0.05, relwidth=0.2, relx=0.205, rely=0.535)                                  ###\ 
        CDTL2 = Label(otherFrame, text="(Default = Desktop)", bg = "White")                               ####\
        CDTL2.pack()                                                                                      ##### Sets up info labels and entry box for custom name
        CDTL2.place(relheight=0.05, relwidth=0.2, relx=0.205, rely=0.585)                                 ####/ 
        self.CDTE = Entry(otherFrame, bg = "White", bd=5)                                                 ###/ 
        self.CDTE.pack()                                                                                  ##/
        self.CDTE.place(relheight=0.07, relwidth=0.2, relx=0.005, rely=0.55)                              #/

        CFT = Tk.Checkbutton(otherFrame, text = "Save as PNG?", variable = self.typet, onvalue = 1, offvalue = 0, height = 5, width = 20, bg="white", activebackground="white", activeforeground="grey" ) 
        CFT.pack()                                                               ## Sets up checkbutton for custom file type's properties and position  
        CFT.place(relheight=0.07, relwidth=0.4, relx=0.005, rely=0.65)           #/
        TypeTlabel = Label(otherFrame, text="(Deafault = Jpeg)", bg = "White")                            #\
        TypeTlabel.pack()                                                                                 ## Sets up properties and position of info label
        TypeTlabel.place(relheight=0.05, relwidth=0.2, relx=0.105, rely=0.755)                            #/

        h = tkFont.Font(CNT, CNT.cget("font"))                                                           # Creates new font, takes properties from font used in CNT
        h.configure(size = 6)                                                                            # Makes new font size 6
        CNTL.configure(font = h)                                                                         # Sets label CNPL to use new font 'h'
        CDTL.configure(font = h)                                                                         # Sets label CDPL to use new font 'h'
        CNTL2.configure(font = h)                                                                        # Sets label CNPL2 to use new font 'h'  
        CDTL2.configure(font = h)                                                                        # Sets label CDPL2 to use new font 'h'
        TypeTlabel.configure(font = h)                                                                   # Sets label Listlabel to use new font 'h'

        #Geometry

        otherFramecanvas.create_line(640, 0, 640, 480, fill ="#8cf")                                     # Inserts line to define border of preview


   #------Timelapse Sub-Section----

 def starttimelapse(self):

        global previewint

        namequery = self.cnt.get()
        directoryquery = self.cdt.get()
        filetypequery = self.typet.get()
        
        filenamet = self.CNTE.get()
        directorypstrt = self.CDTE.get()
        self.directoryt = str(directorypstrt)

        repe = self.REPE.get()     #\
        bete = self.BETE.get()     ##\
                                   ### Imports value entered in sub-menu for time between, and number of images captured, and converts to integer
        repeat = int(repe)         ##/
        between = int(bete)        #/

        PA = self.PA.get()         # Imports value of PA (is checkbox checked?)
        PB = self.PB.get()         # Imports value of PB (is checkbox checked?)
        PC = self.PC.get()         # Imports value of PC (is checkbox checked?)
        PD = self.PD.get()         # Imports value of PD (is checkbox checked?)


        if filetypequery == 1:                            # If the .png filetype checkbox is ticked
          filetypett = '.png'                             # The file will have the suffix .png
        else:                                             #
          filetypett = '.jpg'                             # If not, will be .jpg

          
        if directoryquery == 1:                                      # If the custom directory box is checked
          directorytt = self.directoryt+ + ', '                      # The final capture command is the directory, then the name followed by the filetype
        else:                                                        #
          directorytt = ''                                           # If not, the directory slot will be blank
        

        if repeat == 0:                                                          # If value of repeat is 0 (i.e. take no photographs)
            tkMessageBox.showinfo("ERROR!!", "Not a valid number of repeats!")   # A error message box will appear warining of this     
        if between == 0:                                                         # If value of time between is 0 (i.e. repeat photo taking)
            tkMessageBox.showinfo("ERROR!!", "Not a valid amount of time!")      # A error message box will appear warining of this 

        else :                                                                   # If neither repeat or time are 0, then it will proceed to taking photos
          if previewint == 0:                                                    #\                          
            self.camera=picamera.PiCamera()                                      ##\
            self.camera.resolution = (2592, 1944)                                #### Will check if preview is live
            self.camera.preview_fullscreen = False                               #### If not, same process as photo capture section
            self.camera.preview_window = (80,70,640,480)                         ###/
            self.camera.start_preview()                                          ##/
            previewint = 2                                                       #/
          else :
            time.sleep(1)                                                        # Program pauses for 1s


          for i in range(0,repeat, 1):                                           # For loop, will loop 'repeat' number of times

            if PA == 1:                                                          # If Camera A checkbox is ticked
               self.gp.output(7, False)                                          #\
               self.gp.output(11, False)                                         ## Sets multiplexer to channel A
               self.gp.output(12, True)                                          #/
               timestr = time.strftime("%d-%m-%Y_%H:%M:%S")                      #\                
               millis = int(round(time.time() * 1000))                           ## Sets timenamep according to date/time + milliseconds
               timenamet = timestr + ':' + str(millis)                           #/
               if namequery == 1:                                                # If the custom name checkbox is ticked
                 namett = filenamet  + '_' + timenamet                           # the file name will be the box entry
               else:                                                             #
                 namett = timenamet                                              # If not, name is set as the date/time
               cap = directorytt + 'CamA_' + namett + filetypett                 # Sets capture command with camera A, name, and file extension prefix and suffix
               self.camera.capture(cap)                                          # Captures image, with cap command         

            if PB == 1:                                                          # If Camera B checkbox is ticked
               self.gp.output(7, False)                                          #\
               self.gp.output(11, False)                                         ## Sets multiplexer to channel B
               self.gp.output(12, True)                                          #/
               timestr = time.strftime("%d-%m-%Y_%H:%M:%S")                      #\     
               millis = int(round(time.time() * 1000))                           ## Sets timenamep according to date/time + milliseconds                          ##
               timenamet = timestr + ':' + str(millis)                           #/
               if namequery == 1:                                                # If the custom name checkbox is ticked
                 namett = filenamet + '_' + timenamet                            # the file name will be the box entry
               else:                                                             #
                 namett = timenamet                                              # If not, name is set as the date/time
               cap = directorytt + 'CamB_' + namett + filetypett                 # Sets capture command with camera B, name, and file extension prefix and suffix
               self.camera.capture(cap)                                          # Captures image, with cap command

            if PC == 1:                                                          # If Camera C checkbox is ticked
               self.gp.output(7, False)                                          #\
               self.gp.output(11, False)                                         ## Sets multiplexer to channel C
               self.gp.output(12, True)                                          #/
               timestr = time.strftime("%d-%m-%Y_%H:%M:%S")                      #\                 
               millis = int(round(time.time() * 1000))                           ## Sets timenamep according to date/time + milliseconds
               timenamet = timestr + ':' + str(millis)                           #/
               if namequery == 1:                                                # If the custom name checkbox is ticked
                 namett = filenamet + '_' + timenamet                            # the file name will be the box entry
               else:                                                             #
                 namett = timenamet                                              # If not, name is set as the date/time
               cap = directorytt + 'CamC_' + namett + filetypett                 # Sets capture command with camera C, name, and file extension prefix and suffix
               self.camera.capture(cap)                                          # Captures image, with cap command

            if PD == 1:                                                          # If Camera D checkbox is ticked
               self.gp.output(7, False)                                          #\
               self.gp.output(11, False)                                         ## Sets multiplexer to channel D
               self.gp.output(12, True)                                          #/
               timestr = time.strftime("%d-%m-%Y_%H:%M:%S")                      #\               
               millis = int(round(time.time() * 1000))                           ## Sets timenamep according to date/time + milliseconds
               timenamet = timestr + ':' + str(millis)                           #/
               if namequery == 1:                                                # If the custom name checkbox is ticked
                 namett = filenamet + '_' + timenamet                            # the file name will be the box entry
               else:                                                             #
                 namett = timenamet                                              # If not, name is set as the date/time
               cap = directorytt + 'CamD_' + namett + filetypett                 # Sets capture command with camera D, name, and file extension prefix and suffix
               self.camera.capture(cap)                                          # Captures image, with cap command        

            if PA == 0 :                                                                #\
               if PB == 0:                                                              ##\
                  if PC == 0:                                                           ### If no checkboxes are ticked, displays message warning of such
                     if PD == 0:                                                        ### Then breaks for loop
                        tkMessageBox.showinfo("ERROR!!", "No Cameras Selected!")        ##/
                        break                                                           #/

            time.sleep(between)                                                         # Delay for time 'between' loops
   
        if previewint == 2:                                     #\
            self.camera.stop_preview()                          ## Once loop finishes, if prevew int = 2, i.e. preview was not on before, preview turns off
            self.camera.close()                                 ## I.e. returns to state 0
            previewint = 0                                      #/






 #----------------------------Video Options----------------------------------------------------------------------------------------------------------------------------

 def video(self):
        # self.hide()
        otherFrame = Tk.Toplevel(bg = "White") # Sets Sub-Menu window background colour
        otherFrame.geometry("720x420")         # Sets Sub-Menu window size
        otherFrame.geometry("+80+40")          # Sets Sub-Menu window position
        otherFrame.title("Video")              # Sets Sub-Menu window title
        otherFramecanvas = Tk.Canvas(otherFrame, bg = "White") # Sets up root window properties
        otherFramecanvas.pack(expand=Tk.YES, fill=Tk.BOTH)     # Starts root window


        self.cnv = Tk.IntVar()
        self.cdv = Tk.IntVar()        
       
        A = Tk.Button(otherFrame, text ="A", bg="white", activebackground="white", activeforeground="grey", command=self.gpioa)  #\
        A.pack()                                                                                                                 ## Sets A button properties and position
        A.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.15)                                                             #/
        B = Tk.Button(otherFrame, text ="B", bg="white", activebackground="white", activeforeground="grey", command=self.gpiob)  #\
        B.pack()                                                                                                                 ## Sets B button properties and position
        B.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.25)                                                             #/
        C = Tk.Button(otherFrame, text ="C", bg="white", activebackground="white", activeforeground="grey", command =self.gpioc) #\
        C.pack()                                                                                                                 ## Sets C button properties and position
        C.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.35)                                                             #/
        D = Tk.Button(otherFrame, text ="D", bg="white", activebackground="white", activeforeground="grey", command =self.gpiod) #\
        D.pack()                                                                                                                 ## Sets D button properties and position
        D.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.45)                                                             #/ 

        Alabelv = Tk.Label(otherFrame, text="Selects Camera A. - ", bg="White", anchor = "e")                       #\                
        Alabelv.pack()                                                                                              ## Sets up the label properties and position for button A
        Alabelv.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.15)                      #/
        Blabelv = Tk.Label(otherFrame, text="Selects Camera B. - ", bg="White", anchor = "e")                       #\                
        Blabelv.pack()                                                                                              ## Sets up the label properties and position for button B
        Blabelv.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.25)                      #/
        Clabelv = Tk.Label(otherFrame, text="Selects Camera C. - ", bg="White", anchor = "e")                       #\                
        Clabelv.pack()                                                                                              ## Sets up the label properties and position for button C
        Clabelv.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.35)                      #/
        Dlabelv = Tk.Label(otherFrame, text="Selects Camera D. - ", bg="White", anchor = "e")                       #\                
        Dlabelv.pack()                                                                                              ## Sets up the label properties and position for button D
        Dlabelv.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.45)                      #/

        Infolabelv = Tk.Label(otherFrame, text="Cameras cannot be switched duing capture!", bg="White", anchor = "center")      #\                
        Infolabelv.pack()                                                                                                       ## Sets up the label properties and position for informational label
        Infolabelv.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.4, relx=0.005, rely=0.7)                                #/
        Infolabelv2 = Tk.Label(otherFrame, text="Capture may temporarily drop USB power!", bg="White", anchor = "center")       #\                
        Infolabelv2.pack()                                                                                                      ## Sets up the label properties and position for informational label
        Infolabelv2.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.4, relx=0.005, rely=0.8)                               #/

       #Titles

        Videolabelmain = Tk.Label(otherFrame, text="Video Menu", bg="White", anchor = "center")                            #\                
        Videolabelmain.pack()                                                                                              ## Sets up the label properties and position for main title
        Videolabelmain.place(bordermode=OUTSIDE, relheight=0.15, relwidth=0.885, relx=0.0, rely=0.0)                       #/
        f = tkFont.Font(Videolabelmain, Videolabelmain.cget("font"))                                                       # Creates new font, takes properties from font used in Videolabel
        f.configure(underline = True, size = 30)                                                                           # Make new font underlined
        Videolabelmain.configure(font = f)                                                                                 # Sets Menulabelfont to new font 'f'

        Videolabel = Tk.Label(otherFrame, text="Video", bg="White", anchor = "center")                                     #\                
        Videolabel.pack()                                                                                                  ## Sets up the label properties and position for the video label
        Videolabel.place(bordermode=OUTSIDE, relheight=0.1, relwidth=0.1, relx=0.895, rely=0.0)                            #/
        g = tkFont.Font(Videolabel, Videolabel.cget("font"))                                                               # Creates new font, takes properties from font used in PVideolabel
        g.configure(underline = True,)                                                                                     # Makes font underlind
        Videolabel.configure(font = g)                                                                                     # Sets title to use new font 'g'

       #Settings

        CNV = Tk.Checkbutton(otherFrame, text = "Custom Name", variable = self.cnv, onvalue = 1, offvalue = 0, height = 5, width = 20, bg="white", activebackground="white", activeforeground="grey" )
        CNV.pack()                                                              ## Sets up checkbutton for custom name's properties and position
        CNV.place(relheight=0.07, relwidth=0.4, relx=0.005, rely=0.25)          #/

        CNVL = Label(otherFrame, text="i.e. - Experiment 6, Print 5, etc...", bg = "White")               #\
        CNVL.pack()                                                                                       ##\
        CNVL.place(relheight=0.05, relwidth=0.2, relx=0.205, rely=0.335)                                  ###\ 
        CNVL2 = Label(otherFrame, text="(Deafult = Date + Time)", bg = "White")                           ####\
        CNVL2.pack()                                                                                      ##### Sets up info labels and entry box for custom name
        CNVL2.place(relheight=0.05, relwidth=0.2, relx=0.205, rely=0.385)                                 ####/
        self.CNVE = Entry(otherFrame, bg = "White", bd=5)                                                 ###/ 
        self.CNVE.pack()                                                                                  ##/
        self.CNVE.place(relheight=0.07, relwidth=0.2, relx=0.005, rely=0.35)                              #/

        CDV = Tk.Checkbutton(otherFrame, text = "Custom Directory", variable = self.cdv, onvalue = 1, offvalue = 0, height = 5, width = 20, bg="white", activebackground="white", activeforeground="grey" )  
        CDV.pack()                                                               ## Sets up checkbutton for custom directory's properties and position  
        CDV.place(relheight=0.07, relwidth=0.4, relx=0.005, rely=0.45)           #/

        CDVL = Label(otherFrame, text="i.e. - /media/pi/MyMemoryStick", bg = "White")                     #\
        CDVL.pack()                                                                                       ##\
        CDVL.place(relheight=0.05, relwidth=0.2, relx=0.205, rely=0.535)                                  ###\ 
        CDVL2 = Label(otherFrame, text="(Default = Desktop)", bg = "White")                               ####\
        CDVL2.pack()                                                                                      ##### Sets up info labels and entry box for custom directory
        CDVL2.place(relheight=0.05, relwidth=0.2, relx=0.205, rely=0.585)                                 ####/ 
        self.CDVE = Entry(otherFrame, bg = "White", bd=5)                                                 ###/ 
        self.CDVE.pack()                                                                                  ##/
        self.CDVE.place(relheight=0.07, relwidth=0.2, relx=0.005, rely=0.55)                              #/

        h = tkFont.Font(CNV, CNV.cget("font"))                                                           # Creates new font, takes properties from font used in CNP
        h.configure(size = 6)                                                                            # Makes new font size 6
        CNVL.configure(font = h)                                                                         # Sets label CNPL to use new font 'h'
        CDVL.configure(font = h)                                                                         # Sets label CDPL to use new font 'h'
        CNVL2.configure(font = h)                                                                        # Sets label CNPL2 to use new font 'h'  
        CDVL2.configure(font = h)                                                                        # Sets label CDPL2 to use new font 'h'

        #Geometry

        otherFramecanvas.create_line(640, 0, 640, 480, fill ="#8cf")                                     # Inserts line to define border of preview

        #Data entry

        VIDL = Label(otherFrame, text="Time (s)", bg = "White")               #\
        VIDL.pack()                                                           ##\
        VIDL.place(relheight=0.07, relwidth=0.1, relx=0.89, rely=0.60)        ### Sets up entry box and label
        self.VIDE = Entry(otherFrame, bg = "White", bd=5)                     ### Properties and positions
        self.VIDE.pack()                                                      ##/
        self.VIDE.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.67)  #/

        videlabelv = Tk.Label(otherFrame, text="Length of video (seconds). - ", bg="White", anchor = "e")                #\                
        videlabelv.pack()                                                                                                ## Sets up the label properties and position for label for time entry
        videlabelv.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.67)                        #/


        #Start capture button

        CaptureV = Tk.Button(otherFrame, text ="Capture?", bg="white", activebackground="white", activeforeground="grey", command =self.capturevid)    #\
        CaptureV.pack()                                                                                                                                ## Sets start capture button properties and position
        CaptureV.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.9)                                                                             #/ 
        Capturevl = Tk.Label(otherFrame, text="Starts Video Capture. - ", bg="White", anchor = "e")                     #\                
        Capturevl.pack()                                                                                                ## Sets up the label properties and position for capture button
        Capturevl.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.9)                         #/



     # -------Video Sub-Section------


 def capturevid(self) :

      namequery = self.cnv.get()                       # Collects iteger values
      directoryquery = self.cdv.get()

      filenamev = self.CNVE.get()
      directorypstr = self.CDVE.get()
      self.directoryv = str(directorypstr)

      timestr = time.strftime("%d-%m-%Y_%H:%M:%S")     #\               
      millis = int(round(time.time() * 1000))          ## Sets up video name, with prefix video, date/time, and .h264 file extension
      timenamev = timestr + ':' + str(millis)          ## much like in previous sections

      if namequery == 1:                                # If the custom name checkbox is ticked
          namevv = filenamev                            # the file name will be the box entry
      else:                                             #
          namevv = timenamev                            # If not, name is set as the date/time
    
      if directoryquery == 1:                           # If the custom directory box is checked
          directoryvv =  self.directoryv+ + ', '        # The final capture command is the directory, then the name followed by the filetype
      else:                                             #
          directoryvv = ''                              # Otherwise the final capture command is the name followed by the filetype

      global previewint

      vid = directoryvv + 'Video_' + namevv + '.h264'            # vid command is Video_ prefix, followed by custom name, then filetype

      VidLength = self.VIDE.get()               # Gets variable entered for video length
      videolength = int(VidLength)              # in video sub-menu
 
      if videolength == 0:                                                       # If videolength = 0, (or nothing input into box)
            tkMessageBox.showinfo("ERROR!!", "Not a valid amount of time!")      # Will show error window, instead of starting recording

      else:
      
      
        if previewint == 0:                                    #\                        
            self.camera=picamera.PiCamera()                    ##\
            self.camera.preview_fullscreen = False             ### Checks if preview is live,
            self.camera.preview_window = (80,70,640,480)       ### If not, same procress as photo capture section
            self.camera.start_preview()                        ##/
            previewint = 2                                     #/

        self.camera.resolution = (1920, 1080)                  # Sets camera resolution or 1080p video
        self.camera.start_recording(vid)                       # Starts video recording
        self.camera.wait_recording(videolength)                # Delays for integer inputted 'videolength'
        self.camera.stop_recording()                           # Stops video recording
        self.camera.resolution = (2592, 1944)                  # Sets the cameras resolution back to 2592x1944 (max) for larger preview size
   
        if previewint == 2:                                    #\
            self.camera.stop_preview()                         ## If preview was not live before recording start
            self.camera.close()                                ## Closes preview
            previewint = 0                                     #/




         
  #----------------------------LED Control-----------------------------------------------------------------------------------------------------------------------------
                                                                    
 def led(self):                                                     

        global ledcheckval
        self.ledcheckval = Tk.IntVar() 

        # self.hide()                                                   # Sets up window properties
        otherFrame = Tk.Toplevel(bg = "White")                          #
        otherFrame.geometry("720x420")                                  #
        otherFrame.geometry("+80+40")                                   #
        otherFrame.title("LED")                                         #
        otherFramecanvas = Tk.Canvas(otherFrame, bg = "White") # Sets up root window properties
        otherFramecanvas.pack(expand=Tk.YES, fill=Tk.BOTH)     # Starts root window




        self.ledslider = Scale(otherFrame, from_=0, to=100, bg="white", activebackground="white", resolution = 1)
        self.ledslider.coords(60)                                                                                       # Sets up properties and position for slider
        self.ledslider.pack()
        self.ledslider.place(relheight=0.5, relwidth=0.1, relx=0.895, rely=0.30)
        self.ledslider.set(100)
        
        ledcheck = Tk.Checkbutton(otherFrame, text = "Enable?", variable = self.ledcheckval, onvalue = 1, offvalue = 0, height = 5, width = 20, bg="white", activebackground="white", activeforeground="grey" )
        ledcheck.pack()                                                            ### Sets up position and properties for checkbox
        ledcheck.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.15)        ##/
 
        ledupdate = Tk.Button(otherFrame, text ="Update", bg="white", activebackground="white", activeforeground="grey", command =self.LEDUPDATE)   #\
        ledupdate.pack()                                                                                                                            ## Sets start update button properties and position
        ledupdate.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.9)                                                                         #/ 

        sliderlabel = Tk.Label(otherFrame, text="Varys light brightness. - ", bg="White", anchor = "e")                  #\                
        sliderlabel.pack()                                                                                               ## Sets up the label properties and position for slider
        sliderlabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.485, relx=0.4, rely=0.5)                        #/
        sliderlabel2 = Tk.Label(otherFrame, text="(Number refers to duty cycle, not brightness). - ", bg="White", anchor = "e")              
        sliderlabel2.pack()                                                                                              ## Sets up the label properties and position for slider
        sliderlabel2.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.485, relx=0.4, rely=0.6)                       #/
        checklabel = Tk.Label(otherFrame, text="Enables light. - ", bg="White", anchor = "e")                            #\                
        checklabel.pack()                                                                                                ## Sets up the label properties and position for checkbox
        checklabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.15)                        #/
        updatelabel = Tk.Label(otherFrame, text="Updates light brightness. - ", bg="White", anchor = "e")                #\                
        updatelabel.pack()                                                                                               ## Sets up the label properties and position for button update
        updatelabel.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.285, relx=0.6, rely=0.9)                        #/
        

       #Titles

        LEDmain = Tk.Label(otherFrame, text="LED Menu", bg="White", anchor = "center")                                   #\                
        LEDmain.pack()                                                                                                   ## Sets up the label properties and position for main title
        LEDmain.place(bordermode=OUTSIDE, relheight=0.15, relwidth=0.885, relx=0.0, rely=0.0)                            #/
        f = tkFont.Font(LEDmain, LEDmain.cget("font"))                                                                   # Creates new font, takes properties from font used in LEDlabel
        f.configure(underline = True, size = 30)                                                                         # Make new font underlined
        LEDmain.configure(font = f)                                                                                      # Sets Menulabelfont to new font 'f'

        LEDlabel = Tk.Label(otherFrame, text="LED", bg="White", anchor = "center")                                       #\                
        LEDlabel.pack()                                                                                                  ## Sets up the label properties and position for the LED label
        LEDlabel.place(bordermode=OUTSIDE, relheight=0.1, relwidth=0.1, relx=0.895, rely=0.0)                            #/
        g = tkFont.Font(LEDlabel, LEDlabel.cget("font"))                                                                 # Creates new font, takes properties from font used in LEDlabel
        g.configure(underline = True,)                                                                                   # Makes font underlined
        LEDlabel.configure(font = g)                                                                                     # Sets title to use new font 'g'


        #Geometry

        otherFramecanvas.create_line(640, 0, 640, 480, fill ="#8cf")                                                      # Inserts line to define border of preview


 def LEDUPDATE(self):                                        # Update LED brightness
     
        global ledcheckval, ledslider

        ledon = self.ledcheckval.get()                 
  
        if ledon == 1:                                       # Checks if LED enable checkbox ticked
              sliderval = self.ledslider.get()               # If is, gets value of slider
              ledpwm.ChangeDutyCycle(sliderval)              # Applies value
        else:
              ledpwm.ChangeDutyCycle(100)                    # Othewise urns off LED
             

 #----------------------------Stepper Options--------------------------------------------------------------------------------------------------------------------------

 def stepper(self):
        # self.hide()                              # Leftover code from 'hiding' sub-menus
        otherFrame = Tk.Toplevel(bg = "White")     # Sets Sub-Menu window background colour
        otherFrame.geometry("720x420")             # Sets Sub-Menu window size
        otherFrame.geometry("+80+40")              # Sets Sub-Menu window position
        otherFrame.title("Stepper")                # Sets Sub-Menu window title
        otherFramecanvas = Tk.Canvas(otherFrame, bg = "White")  # Sets up root window properties
        otherFramecanvas.pack(expand=Tk.YES, fill=Tk.BOTH)      # Starts root window

        SForward = Tk.Button(otherFrame, text ="Forward", bg="white", activebackground="white", activeforeground="grey", command =self.stepf)   #\
        SForward.pack()                                                                                                                         ## Sets forward button properties and position
        SForward.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.4)                                                                      #/
        SBack = Tk.Button(otherFrame, text ="Back", bg="white", activebackground="white", activeforeground="grey", command =self.stepb)         #\
        SBack.pack()                                                                                                                            ## Sets backward button properties and position
        SBack.place(relheight=0.07, relwidth=0.1, relx=0.895, rely=0.5)                                                                         #/



        flabels = Tk.Label(otherFrame, text="Makes motor go forward. - ", bg="White", anchor = "e")         #\                
        flabels.pack()                                                                                      ## Sets up the label properties and position for button forward
        flabels.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.8, relx=0.0, rely=0.4)                 #/
        flabels = Tk.Label(otherFrame, text="Makes motor go backward. - ", bg="White", anchor = "e")        #\                
        flabels.pack()                                                                                      ## Sets up the label properties and position for button backward
        flabels.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.8, relx=0.0, rely=0.5)                 #/

       #Titles

        Steppermain = Tk.Label(otherFrame, text="Stepper Menu", bg="White", anchor = "center")              #\                
        Steppermain.pack()                                                                                  ## Sets up the label properties and position for Stepper title
        Steppermain.place(bordermode=OUTSIDE, relheight=0.15, relwidth=0.885, relx=0.0, rely=0.0)           #/
        f = tkFont.Font(Steppermain, Steppermain.cget("font"))                                              # Creates new font, takes properties from font used in stepper
        f.configure(underline = True, size = 30)                                                            # Make new font underlined
        Steppermain.configure(font = f)                                                                     # Sets Menulabelfont to new font 'f'

        Stepperlabel = Tk.Label(otherFrame, text="Stepper", bg="White", anchor = "center")                  #\                
        Stepperlabel.pack()                                                                                 ## Sets up the label properties and position for the stepper
        Stepperlabel.place(bordermode=OUTSIDE, relheight=0.1, relwidth=0.1, relx=0.895, rely=0.0)           #/
        g = tkFont.Font(Stepperlabel, Stepperlabel.cget("font"))                                            # Creates new font, takes properties from font used in Stepperlabel
        g.configure(underline = True,)                                                                      # Makes font underlind
        Stepperlabel.configure(font = g)                                                                    # Sets title to use new font 'g'


         #Geometry

        otherFramecanvas.create_line(640, 0, 640, 480, fill ="#8cf")                                        # Inserts line to define border of preview
        

  #------Stepper Sub-section----


 def stepf(self):
      
        self.gp.output(31, True)    # If the forward button is pressed. The pins assigned by the selection buttons will go high in order, causing the stepper motor to go forwards one unit / turn of the stepper.
        self.gp.output(32, False)
        self.gp.output(36, True)
        self.gp.output(37, False)
        time.sleep(0.01)
        self.gp.output(31, False)
        self.gp.output(32, True)
        self.gp.output(36, True)
        self.gp.output(37, False)
        time.sleep(0.01)
        self.gp.output(31, False)
        self.gp.output(32, True)
        self.gp.output(36, False)
        self.gp.output(37, True)
        time.sleep(0.01)
        self.gp.output(31, True)
        self.gp.output(32, False)
        self.gp.output(36, False)
        self.gp.output(37, True)
        time.sleep(0.01)
  
 def stepb(self):
 
        self.gp.output(31, True)    # If the backward button is pressed. The pins assigned by the selection buttons will go high in reverse order, causing the stepper motor to go backwards one unit / turn of the stepper.
        self.gp.output(32, False)
        self.gp.output(36, False)
        self.gp.output(37, True)
        time.sleep(0.01)
        self.gp.output(31, False)
        self.gp.output(32, True)
        self.gp.output(36, False)
        self.gp.output(37, True)
        time.sleep(0.01)
        self.gp.output(31, False)
        self.gp.output(32, True)
        self.gp.output(36, True)
        self.gp.output(37, False)
        time.sleep(0.01)
        self.gp.output(31, True)
        self.gp.output(32, False)
        self.gp.output(36, True)
        self.gp.output(37, False)
        time.sleep(0.01)



#############################################################################      
        
  #---------------------------------Settings------------------------------------------------------------------------------------------------------------------------------
                                                                            #
 def settings(self):                                                        #
        # self.hide()                                                       #  # This section opens the Settings sub-menu.
        # otherFrame.hide()                                                 #  # The settings sub menu has not been completed.
        otherFrame = Tk.Toplevel(bg = "White")                              #
        otherFrame.geometry("720x420")                                      #
        otherFrame.geometry("+80+40")                                       #
        otherFrame.title("Settings")                                        #
        otherFramecanvas = Tk.Canvas(otherFrame, bg = "White")                                                      # Sets up root window properties
        otherFramecanvas.pack(expand=Tk.YES, fill=Tk.BOTH)                                                          # Starts root window
        Infolabelsettings = Tk.Label(otherFrame, text="Section Is Not Complete!", bg="White", anchor = "center")    #\                
        Infolabelsettings.pack()                                                                                    ## Sets up the label properties and position for informational label
        Infolabelsettings.place(bordermode=OUTSIDE, relheight=0.07, relwidth=0.6, relx=0.15, rely=0.4)              #/

       #Titles

        Settingsmain = Tk.Label(otherFrame, text="Settings Menu", bg="White", anchor = "center")                         #\                
        Settingsmain.pack()                                                                                              ## Sets up the label properties and position for Settinga
        Settingsmain.place(bordermode=OUTSIDE, relheight=0.15, relwidth=0.885, relx=0.0, rely=0.0)                       #/
        f = tkFont.Font(Settingsmain, Settingsmain.cget("font"))                                                         # Creates new font, takes properties from font used in Settingsmai
        f.configure(underline = True, size = 30)                                                                         # Make new font underlined
        Settingsmain.configure(font = f)                                                                                 # Sets Settingsfont to new font 'f'

        Settingslabel = Tk.Label(otherFrame, text="Settings", bg="White", anchor = "center")                             #\                
        Settingslabel.pack()                                                                                             ## Sets up the label properties and position for the settings label
        Settingslabel.place(bordermode=OUTSIDE, relheight=0.1, relwidth=0.1, relx=0.895, rely=0.0)                       #/
        g = tkFont.Font(Settingslabel, Settingslabel.cget("font"))                                                       # Creates new font, takes properties from font used in Settingslabel
        g.configure(underline = True,)                                                                                   # Makes font underlined
        Settingslabel.configure(font = g)                                                                                # Sets title to use new font 'g'


        #Geometry

        otherFramecanvas.create_line(640, 0, 640, 480, fill ="#8cf")                                     # Inserts line to define border of preview
 
#############################################################################



#-------------------------------------------------------EXTRA COMMANDS-----------------------------------------------------------------------------------------------------------------------------------------------------------


#############################################################################
#                                                                           #
#   #-------------------------Close other frame-----------------------      #
# def onCloseOtherFrame(self, otherFrame):                                  #
#        otherFrame.destroy()                                               #
#        self.show()                                                        # # These commands were intended for closing one sub-menu,
#                                                                           # # when the other opened, or hiding the window rather then destroying
#   #-----------------------Change new frame to root-----------------       # # it to retain variables.
# def show(self):                                                           # # This section of code was not completed.
#        self.root.update()                                                 #
#        self.root.deiconify()                                              #
#                                                                           #
#   #---------------------Hide window (not destroy)------------------       #
# def hide(self):                                                           #
#      self.root.withdraw()                                                 #
#                                                                           #
#############################################################################

   #--------------------Destroy Window -----------------                      # This section is sent to by the 'EXIT?' button
 def destroy(self):
        global previewint                              
        if previewint == 1:                                                   # Checks if preview is open
            self.camera.stop_preview()                                        # If yes, closes preview
            self.camera.close()                                               #         Then terminates any camera processes (cleans buffers)
        
        gp.cleanup()
        root.destroy()                                                        # Then destroys root window, therefore closing subwindows, and ending entire process
 
 
#----------------------------END-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
if __name__ == "__main__":    #\
                              ##\
    root = Tk.Tk()            ### Setup for class. If root is ended (destroyed) process cant loop, therefore ends
    app = MyApp(root)         ##/
    root.mainloop()           #/
    
