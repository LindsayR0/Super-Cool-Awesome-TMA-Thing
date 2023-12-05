from vpython import *

scene.background = vector(77/255,102/255,75/255)
scene.center = vector(-1,3,2) #positions the camera
scene.camera.axis = vector(1.5, -6, -5) #rotates the camera

#color picked from image found at https://en.wikipedia.org/wiki/The_Magnus_Archives
player_clr = vector(2/255,6/255,4/255)
speaker_clr = vector(0.5,0.5,0.5)
#color picked from image found at https://en.wikipedia.org/wiki/The_Magnus_Archives
handle_clr = vector(13/255, 85/255, 53/255)
button_clr1 = color.red
button_clr2 = vector(66/255,74/255,64/255)
screw_clr = vector(49/255,55/255,47/255)

#function that is run whenever the mouse is down
def buttonPress():
    for b in buttons: #itterates through each item in the dictionary buttons
        if scene.mouse.pick == buttons[b]: #if the mouse is pointing at one of the buttons
            if buttons[b].pos.y == 0.125: #functionaly: if the button is up
                buttons[b].pos.y = 0.025 #moves the button down
            else: #functionaly: if the button is down
                buttons[b].pos.y = 0.125 #moves the button up

class Tape: #creates a class for the tape
    def __init__(self, tape_pos): #constuctor method with the parmamiter for the tape's position
        self.base_clr = color.yellow
        #color picked from image found at https://en.wikipedia.org/wiki/The_Magnus_Archives
        self.side_clr = vector(195/255,197/255,196/255)
        #color picked from image found at https://en.wikipedia.org/wiki/The_Magnus_Archives
        self.sticker_clr = vector(29/255,124/255,59/255)
        self.label_clr = color.white
        self.left_wheel_txr = color.green
        self.center_wheel_txr = color.green
        self.right_wheel_txr = color.red
        
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
        #creates a middle section on the tape
        self.sticker_mid = box(size = vector(0.9, 0.01, 0.02), color = self.sticker_clr,
            pos = (vector(0, 0.105, -0.09) + tape_pos))
        #list containing shapes for the left wheel in the tape
        self.wheel_left = [
            #base of left wheel
            cylinder(radius = 0.3, length = 0.18, color = self.left_wheel_txr,
                pos = (vector(-0.3,-0.1,0.06) + tape_pos)).rotate(axis = vector(0,0,1), angle = 0.5*pi),
            #top of left wheel
            cylinder(radius = 0.08, length = 0.2, color = self.center_wheel_txr,
                pos = (vector(-0.3, -0.1, 0.06) + tape_pos)).rotate(axis = vector(0,0,1), angle = 0.5*pi)
            ]

        #list containing shapes for the right wheel in the tape
        self.wheel_right = [
            #base of right wheel
            cylinder(radius = 0.24, length = 0.18, color = self.right_wheel_txr,
                pos = (vector(0.3,-0.1,0.06) + tape_pos)).rotate(axis = vector(0,0,1), angle = 0.5*pi),
            #top of right wheel
            cylinder(radius = 0.08, length = 0.2, color = self.center_wheel_txr,
                pos = (vector(0.3, -0.1, 0.06) + tape_pos)).rotate(axis = vector(0,0,1), angle = 0.5*pi)
            ]

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
Tape(vector(0, 0.445, 0.9))

#creates left side of handle
handle_left = box(size = vector(0.1,0.3,1), pos = vector(-1.05,-0.125,2.3), color = handle_clr)
#creates right side of handle
handle_right = box(size = vector(0.1,0.3,1), pos = vector(1.05,-0.125,2.3), color = handle_clr)
#creates top of handle
handle_top = box(size = vector(2, 0.3, 0.1), pos = vector(0,-0.125,2.75), color = handle_clr)

screw_left = cylinder(radius = 0.05, length = 0.02, pos = vector(-1.12,-0.125,1.925),
    color = screw_clr)
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

while True:
    rate(20)
    scene.bind('click', buttonPress)


#winsound library for audio
#look into sleep