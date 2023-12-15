from captions import *

button_audios = {
    #audio pulled from episode 1 of The Magnus Archives ("MAG001 - Anglerfish"),
    #which can be found at https://www.youtube.com/watch?v=AdiUHYacaRI
    'button1': 'audios/StatementBegins.wav',
    #audio pulled from episode 1 of The Magnus Archives ("MAG001 - Anglerfish"),
    #which can be found at https://www.youtube.com/watch?v=AdiUHYacaRI
    'button2': 'audios/EndRecording.wav',
    #audio pulled from episode 1 of The Magnus Archives ("MAG001 - Anglerfish"),
    #which can be found at https://www.youtube.com/watch?v=AdiUHYacaRI
    'button3': 'audios/TestTest123.wav',
    #audio pulled from episode 160 of The Magnus Archives ("MAG160 - The Eye Opens"),
    #which can be found at https://www.youtube.com/watch?v=riLljv93IqQ&t=443s
    'button4': 'audios/HelloJon.wav',
    #audio pulled from episode 180 of The Magnus Archives ("MAG180 - Moving On"),
    #which can be found at https://www.youtube.com/watch?v=s9K_6B3RKBs&t=18s
    'button5': 'audios/EyeSpy.wav',
    #audio pulled from episode 39 of The Magnus Archives ("MAG039 - Infestation"),
    #which can be found at https://www.youtube.com/watch?v=l8yOc1Tksh8&t=1s
    'button6': 'audios/NotAGhost.wav'
    }

def buttonCaptions(audio):
    #functionaly: runs the function for the captions of "Statement Begins" when that audio is playing
    if audio =='audios/StatementBegins.wav':
        StatementBegins()
    #functionaly: runs the function for the captions of "End Recording" when that audio is playing
    if audio == 'audios/EndRecording.wav':
        EndRecording()
    #functionaly: runs the function for the captions of "Test Test 123" when that audio is playing
    if audio == 'audios/TestTest123.wav':
        TestTest123()
    #functionaly: runs the function for the captions of "Hello Jon" when that audio is playing
    if audio == 'audios/HelloJon.wav':
        HelloJon()
    #functionaly: runs the function for the captions of "Eye Spy" when that audio is playing
    if audio == 'audios/EyeSpy.wav':
        EyeSpy()
    #functionaly: runs the function for the captions of "Not A Ghost" when that audio is playing
    if audio == 'audios/NotAGhost.wav':
        NotAGhost()