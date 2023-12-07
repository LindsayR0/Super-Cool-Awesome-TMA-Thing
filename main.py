from vpython import *
import winsound
import time

scene.background = vector(77/255,102/255,75/255) #colors the background a desaturated green
scene.center = vector(-1,3,2) #positions the camera
scene.camera.axis = vector(1.5, -6, -5) #rotates the camera

#VARIABLES FOR COLORS
#color picked from image found at https://en.wikipedia.org/wiki/The_Magnus_Archives
player_clr = vector(2/255,6/255,4/255)
speaker_clr = vector(0.5,0.5,0.5)
#color picked from image found at https://en.wikipedia.org/wiki/The_Magnus_Archives
handle_clr = vector(13/255, 85/255, 53/255)
button_clr1 = color.red
button_clr2 = vector(66/255,74/255,64/255)
screw_clr = vector(49/255,55/255,47/255)

class Tape: #creates a class for the tape
    def __init__(self, tape_pos): #constuctor method with the parmamiter for the tape's position
        #COLORS AND TEXTURES USED FOR THE TAPE
        self.base_clr = color.yellow
        #color picked from image found at https://en.wikipedia.org/wiki/The_Magnus_Archives
        self.side_clr = vector(195/255,197/255,196/255)
        #color picked from image found at https://en.wikipedia.org/wiki/The_Magnus_Archives
        self.sticker_clr = vector(29/255,124/255,59/255)
        self.label_clr = color.white
        self.left_wheel_txr = 'assets/test_txr.png'
        self.center_wheel_txr = 'assets/test_txr.png'
        self.right_wheel_txr = 'assets/test_txr.png'
        
        #OJECTS FOR SHELL OF TAPE
        #creates the base of the tape
        self.base = box(size = vector(0.9, 0.001, 0.4), color = self.base_clr,
            pos = (vector(0, -0.1045, 0) + tape_pos))
        #creates the left side of the tape
        self.left = box(size = vector(0.3, 0.2, 0.8), color = self.side_clr,
            pos = (vector(-0.6, 0, 0) + tape_pos))
        #creates right side of the tape
        self.right = box(size = vector(0.3, 0.2, 0.8), color = self.side_clr,
            pos = (vector(0.6, 0, 0) + tape_pos))
        #creates top side of the tape
        self.top = box(size = vector(0.9, 0.2, 0.2), color = self.side_clr,
            pos = (vector(0, 0, -0.3) + tape_pos))
        #creates bottom side of the tape
        self.bottom = box(size = vector(0.9, 0.2, 0.2), color = self.side_clr,
            pos = (vector(0, 0, 0.3) + tape_pos))
        
        #OBJECTS FOR STICKER ON TAPE
        #creates the left edge of the sticker on the tape
        self.stickerL = box(size = vector(0.2, 0.01, 0.6), color = self.sticker_clr,
            pos = (vector(-0.55, 0.105, 0) + tape_pos))
        #creates the right edge of the sticer on the tape
        self.stickerR = box(size = vector(0.2, 0.01, 0.6), color = self.sticker_clr,
            pos = (vector(0.55, 0.105, 0) + tape_pos))
        #creates label on the tape
        self.sticker_label = box(size = vector(0.9, 0.01, 0.2), color = self.label_clr,
            pos = (vector(0, 0.105, -0.2) + tape_pos))
        #creates bottom of the sticker on the tape
        self.sticker_bottom = box(size = vector(0.9, 0.01, 0.1), color = self.sticker_clr,
            pos = (vector(0, 0.105, 0.25) + tape_pos))
        #creates a middle section on the sticker on the tape
        self.sticker_mid = box(size = vector(0.9, 0.01, 0.02), color = self.sticker_clr,
            pos = (vector(0, 0.105, -0.09) + tape_pos))
        
        #OBJECTS FOR LEFT WHEEL
        #base of left wheel
        self.wheel_baseL = cylinder(radius = 0.3, length = 0.18, texture = self.left_wheel_txr,
            pos = (vector(-0.3,-0.1,0.06) + tape_pos))
        self.wheel_baseL.rotate(axis = vector(0,0,1), angle = 0.5*pi)
        #top of left wheel
        self.wheel_topL = cylinder(radius = 0.08, length = 0.2, texture = self.center_wheel_txr,
            pos = (vector(-0.3, -0.1, 0.06) + tape_pos))
        self.wheel_topL.rotate(axis = vector(0,0,1), angle = 0.5*pi)

        #OBJECTS FOR RIGHT WHEEL
        #base of right wheel
        self.wheel_baseR = cylinder(radius = 0.24, length = 0.18, texture = self.right_wheel_txr,
            pos = (vector(0.3,-0.1,0.06) + tape_pos))
        self.wheel_baseR.rotate(axis = vector(0,0,1), angle = 0.5*pi)
        #top of right wheel
        self.wheel_topR = cylinder(radius = 0.08, length = 0.2, texture = self.center_wheel_txr,
            pos = (vector(0.3, -0.1, 0.06) + tape_pos))
        self.wheel_topR.rotate(axis = vector(0,0,1), angle = 0.5*pi)
    
    def Spin(self, spn): #creates method that spins the wheels on the tape
        #rotates left wheel
        self.wheel_baseL.rotate(angle = (spn/50))
        self.wheel_topL.rotate(angle = (spn/50))

        #rotates right wheel
        self.wheel_baseR.rotate(angle = (spn/50))
        self.wheel_topR.rotate(angle = (spn/50))

#OBJECTS FOR PLAYER
#creates the top of the player base
player_base_top = box(size = vector(2,1,2), pos = vector(0, 0, -0.5), color = player_clr)
#creates the left side of the player base
player_baseL = box(size = vector(0.35, 1, 0.8), pos = vector(-0.825, 0, 0.9), color = player_clr)
#creates the right side of the player base
player_baseR = box(size = vector(0.35, 1, 0.8), pos = vector(0.825, 0, 0.9), color = player_clr)
#creates the bottom of the player base
player_base_bottom = box(size = vector(2, 1, 0.2), pos = vector(0, 0, 1.4), color = player_clr)
#extends the casset player to the end of the buttons on the left side
Lbutton_edge = box(size = vector(0.125, 0.75, 0.5), pos = vector(-0.9375, 0.125, 1.75), color = player_clr)
#extends the casset player to the end of the buttons on the right side
Rbutton_edge = box(size = vector(0.125, 0.75, 0.5), pos = vector(0.9375, 0.125, 1.75), color = player_clr)
#extends the bottom of the casset player to be sligthly longer than the end of the buttons
player_bottom = box(size = vector(2,0.75,3), pos = vector(0,-0.125,0.6), color = player_clr)

#creates the speaker
speaker = box(size = vector(1.5,0.2,1.5), pos = vector(0,0.5,-0.5), color = speaker_clr)
#creates the tape by calling the Tape class and gives the positon for the tape
tape_player = Tape(vector(0, 0.445, 0.9))

#OBJECTS FOR HANDLE
#creates left side of handle
handle_left = box(size = vector(0.1,0.3,1), pos = vector(-1.05,-0.125,2.3), color = handle_clr)
#creates right side of handle
handle_right = box(size = vector(0.1,0.3,1), pos = vector(1.05,-0.125,2.3), color = handle_clr)
#creates top of handle
handle_top = box(size = vector(2, 0.3, 0.1), pos = vector(0,-0.125,2.75), color = handle_clr)

#SCREWS
#creates left screw for the handle
screw_left = cylinder(radius = 0.05, length = 0.02, pos = vector(-1.12,-0.125,1.925),
    color = screw_clr)
#creates right screw for the handle
screw_right = cylinder(radius = 0.05, length = 0.02, pos = vector(1.12,-0.125,1.925),
    color = screw_clr)

#dictonary of buttons
buttons = {
    'button1': box(size = vector(0.25,0.75,0.5), pos = vector(-0.75, 0.125, 1.75), color = button_clr1),
    'button2': box(size = vector(0.25,0.75,0.5), pos = vector(-0.45, 0.125, 1.75), color = button_clr2),
    'button3': box(size = vector(0.25,0.75,0.5), pos = vector(-0.15, 0.125, 1.75), color = button_clr2),
    'button4': box(size = vector(0.25,0.75,0.5), pos = vector(0.15, 0.125, 1.75), color = button_clr2),
    'button5': box(size = vector(0.25,0.75,0.5), pos = vector(0.45, 0.125, 1.75), color = button_clr2),
    'button6': box(size = vector(0.25,0.75,0.5), pos = vector(0.75, 0.125, 1.75), color = button_clr2) 
    }

#function that is run whenever the mouse is down
def buttonPress():
    i = 0
    for b in buttons: #itterates through each item in the dictionary buttons
        if scene.mouse.pick == buttons[b]: #if the mouse is pointing at one of the buttons
            buttons[b].pos.y = 0.025 #moves the button down
            if b == 'button1': #if the button pushed is button1
                #INDEPENDENT RESEARCH
                #learned how to use the winsound library here:
                #https://www.geeksforgeeks.org/python-winsound-module/
                #audio pulled from epiosode 160 of The Magnus Archives ("MAG160 - The Eye Opens"),
                #which can be found at https://youtu.be/riLljv93IqQ?si=D-5vH8Gxl0ngLPzo
                winsound.PlaySound('audios/HelloJon.wav', winsound.SND_ASYNC) #plays sound "Hello Jon" when the first button is pressed
                time.sleep(30) #waits length of audio +2 extra seconds to put button back up
            else:
                if b == 'button2': #if the button pushed is button2
                    #audio pulled from epiosode 160 of The Magnus Archives ("MAG160 - The Eye Opens"),
                    #which can be found at https://youtu.be/riLljv93IqQ?si=D-5vH8Gxl0ngLPzo
                    winsound.PlaySound('audios/I_OPEN_THE_DOOR.wav', winsound.SND_ASYNC) #playes sound "I OPEN THE DOOR" when the second button is pressed
                    time.sleep(51) #waits length of audio +2 extra seconds to put button back up
                else:
                    if b == 'button3': #if the button pushed is button3
                        #audio pulled from epiosode 001 of The Magnus Archives ("MAG001 - Angelerfish"),
                        #which can be found at https://www.youtube.com/watch?v=AdiUHYacaRI
                        winsound.PlaySound('audios/TestTest123.wav', winsound.SND_ASYNC) #playes sound "Test Test 123" when the third button is pressed
                        time.sleep(8) #waits length of audio +2 extra seconds to put button back up
                    else:
                        if b == 'button4': #if the button pushed is button4
                            #audio pulled from epiosode 001 of The Magnus Archives ("MAG001 - Angelerfish"),
                            #which can be found at https://www.youtube.com/watch?v=AdiUHYacaRI
                            winsound.PlaySound('audios/StatementBegins.wav', winsound.SND_ASYNC) #playes the sound "Statement Begins" when the fourth button is pressed
                            time.sleep(11) #waits length of audio +2 extra seconds to put button back up
                        else:
                            if b == 'button5': #if the button pushed is button5
                                #audio pulled from epiosode 001 of The Magnus Archives ("MAG001 - Angelerfish"),
                                #which can be found at https://www.youtube.com/watch?v=AdiUHYacaRI
                                winsound.PlaySound('audios/EndRecording.wav', winsound.SND_ASYNC) #plays the sound "End Recording" when the fifth button is pressed
                                time.sleep(4) #waits length of audio +2 extra seconds to put button back up
                            else: #functinoaly : if the button pushed is button6
                                #audio pulled from episode 180 of The Madnus Archives ("MAG180 - Moving On"),
                                #which can be found at https://www.youtube.com/watch?v=s9K_6B3RKBs
                                winsound.PlaySound('audios/EyeSpy.wav', winsound.SND_ASYNC) #playes the sound "Eye Spy" when the sixth button is pressed
                                time.sleep(35) #waits length of audio +2 extra seconds to put button back up
        buttons[b].pos.y = 0.125 #puts button back up in origonal position

fr = 20 #defines the framerate as 20 fps
frame = 0 #initializes the frame number as 0

#function that keeps track of the time left until the buttons will stop working in seconds
def CountDown(countdown_frames, current_frame, framerate):
    #calculates the time left by using the frames that there are until it stops working, the current frame number, and the framerate
    time_left = floor((countdown_frames-current_frame)/framerate)
    return(time_left) #returns the value for the amount of time left

while frame <= 1800: #functionaly: until 90 seconds have passed
    rate(fr) #sets frame rate according to fr
    secs_left = CountDown(1800, frame, fr) #sets the varable "secs_left" to the ammount of seconds left as determined by the CountDown function
    #creates a timer that displayes the ammount of seconds left
    timer = label(text = str(secs_left), pos = vector(7,-0.2,-2.7), box = False)
    scene.bind('click', buttonPress) #runs buttonPress function whenever the mouse is clicked
    tape_player.Spin(2) #spins the wheels on the tape
    frame += 1 #adds one to the current frame number

scene.unbind('click', buttonPress) #makes it so that the user can no longer click any of the buttons anymore