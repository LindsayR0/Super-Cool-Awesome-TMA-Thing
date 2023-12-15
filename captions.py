from vpython import *
import time

#creates label for the current caption to be displayed in (currently invisable)
caption = label(text = "", box = False, pos = vector(0.5,-9,0), opacity = 0)

#function that displays the captions for the audio "Statement Begins"
#captions taken from official transcript of episode 1 of The Magnus Archives ("MAG001 - Anglerfish"):
#https://snarp.github.io/magnus_archives_transcripts/episode/001.html
def StatementBegins():
    caption.opacity = 0.66 #makes background box behind caption semi-transparent
    caption.text = "JON: Audio recording by Jonathan Sims."
    time.sleep(3) #after 3 total seconds elapesd since audio started, run next line
    caption.text = "Head Archivist of the Magnus Institute, London."
    time.sleep(5) #after 7 total seconds elapesd since audio started, run next line
    caption.text = "Statement begins."
    time.sleep(2) #after 10 total seconds elapesd since audio started, run next line
    caption.opacity = 0 #makes background box around caption invisable
    caption.text = "" #gets rid of caption text

#function that displays the captions for the audio "End Recording"
#captions taken from official transcript of episode 1 of The Magnus Archives ("MAG001 - Anglerfish"):
#https://snarp.github.io/magnus_archives_transcripts/episode/001.html
def EndRecording():
    caption.opacity = 0.66 #makes background box behind caption semi-transparent
    caption.text = """JON: End recording.
    [TAPE CLICKS]"""
    time.sleep(2) #after 2 total seconds elapesd since audio started, run next line
    caption.opacity = 0 #makes background box around caption invisable
    caption.text = "" #gets rid of caption text

#function that displays the captions for the audio "Test Test Test 123"
#captions taken from official transcript of episode 1 of The Magnus Archives ("MAG001 - Anglerfish"):
#https://snarp.github.io/magnus_archives_transcripts/episode/001.html
def TestTest123():
    caption.opacity = 0.66 #makes background box behind caption semi-transparent
    caption.text = """[TAPE CLICKS]
    JON: Test... Test... Test..."""
    time.sleep(4) #after 4 total seconds elapesd since audio started, run next line
    caption.text = """1, 2, 3...
    Right."""
    time.sleep(4) #after 8 total seconds elapesd since audio started, run next line
    caption.opacity = 0 #makes background box around caption invisable
    caption.text = "" #gets rid of caption text

#captions taken from official transcript of episode 160 of The Magnus Archives ("MAG160 - The Eye Opens"):
#https://snarp.github.io/magnus_archives_transcripts/episode/160.html
def HelloJon():
    caption.opacity = 0.66 #makes background box behind caption semi-transparent
    caption.text = """JON <i>(STATEMENT)</i>: Hello, Jon
    appologies for the deception"""
    time.sleep(4) #after 4 total seconds elapesd since audio started, run next line
    caption.text = """but I rather wanted to make sure you started reading,
    so I thought it best not to announce myself."""
    time.sleep(6) #after 10 total seconds elapesd since audio started, run next line
    caption.text = """I'm assuming you're alone
    you always did prefer to read your statements in private."""
    time.sleep(5) #after 15 total seconds elapesd since audio started, run next line
    caption.text = """I wouldn't try to hard to stop reading
    there's every likelihood you'll just hurt yourself."""
    time.sleep(8) #after 23 total seconds elapesd since audio started, run next line
    caption.text = "So just listen."
    time.sleep(3) #after 26 total seconds elapesd since audio started, run next line
    caption.text = "Now, shall we turn the page and try again?"
    time.sleep(4) #after 30 total seconds elapesd since audio started, run next line
    caption.opacity = 0 #makes background box around caption invisable
    caption.text = "" #gets rid of caption text

#captions taken from official transcript of episode 180 of The Magnus Archives ("MAG180 - Moving On"):
#https://snarp.github.io/magnus_archives_transcripts/episode/180.html
def EyeSpy():
    caption.opacity = 0.66 #makes background box behind caption semi-transparent
    caption.text = "MARTIN: In fact, this time, when you start to… intone"
    time.sleep(4) #after 4 total seconds elapesd since audio started, run next line
    caption.text = "I'm going to find a nice soundproof mausoleum"
    time.sleep(4) #after 8 total seconds elapesd since audio started, run next line
    caption.text = """<i>(cont'd)</i>: and just, just chill with whatever
    horrors they've got lurking in there."""
    time.sleep(3) #after 11 total seconds elapesd since audio started, run next line
    caption.text = "Y'know. Maybe play a bit of I Spy or something."
    time.sleep(4) #after 15 total seconds elapesd since audio started, run next line
    caption.text = """I-I'll start.
    I spy with my little eye..."""
    time.sleep(2) #after 17 total seconds elapesd since audio started, run next line
    caption.text = """<i>(cont'd)</i>: something beginning with... T-
    JON: Tombs."""
    time.sleep(4) #after 21 total seconds elapesd since audio started, run next line
    caption.text = """MARTIN: Cheater.
    JON: I did not!"""
    time.sleep(3) #after 24 total seconds elapesd since audio started, run next line
    caption.text = "MARTIN: Your turn."
    time.sleep(2) #after 26 total seconds elapesd since audio started, run next line
    caption.text = "JON: Fine. I spy with my little eye..."
    time.sleep(3) #after 29 total seconds elapesd since audio started, run next line
    caption.text = "<i>(cont'd)</i>: Literally everything."
    time.sleep(3) #after 32 total seconds elapesd since audio started, run next line
    caption.text = "[MARTIN LAUGHS]"
    time.sleep (2) #after 34 total seconds elapesd since audio started, run next line
    caption.opacity = 0 #makes background box around caption invisable
    caption.text = "" #gets rid of caption text

#captions taken from official transcript of episode 39 of The Magnus Archives ("MAG039 - Infestation"):
#https://snarp.github.io/magnus_archives_transcripts/episode/039.html
def NotAGhost():
    caption.opacity = 0.66 #makes background box behind caption semi-transparent
    caption.text = """JON: You've been living in the Archives for four months,
    constant threat of... this."""
    time.sleep(6) #after 6 total seconds elapesd since audio started, run next line
    caption.text = "Sleeping with a fire extinguisher and a corkscrew."
    time.sleep(4) #after 10 total seconds elapesd since audio started, run next line
    caption.text = """Even you must be aware that that's not normal
    for an archiving job?"""
    time.sleep(4) #after 14 total seconds elapesd since audio started, run next line
    caption.text = "Why are you still here?"
    time.sleep(3) #after 17 total seconds elapesd since audio started, run next line
    caption.text = "MARTIN: Don't really know. I just am."
    time.sleep(5) #after 22 total seconds elapesd since audio started, run next line
    caption.text = "It didn't feel right to just leave."
    time.sleep(3) #after 25 total seconds elapesd since audio started, run next line
    caption.text = """I've typed up a few resignation letters,
    but I just couldn't bring myself to hand them in."""
    time.sleep(6) #after 31 total seconds elapesd since audio started, run next line
    caption.text = "I'm trapped here."
    time.sleep(3) #after 34 total seconds elapesd since audio started, run next line
    caption.text = """It's like I can't… move on and the more
    I struggle, the more I'm stuck."""
    time.sleep(7) #after 40 total seconds elapesd since audio started, run next line
    caption.text = """JON: Martin...
    You're not, uh..."""
    time.sleep(7) #after 47 total seconds elapesd since audio started, run next line
    caption.text = "You didn't die here, did you?"
    time.sleep(3) #after 50 total seconds elapesd since audio started, run next line
    caption.text = """MARTIN: What? What? N-No... what?!
    JON: No, I just… No, just the way you phrased that..."""
    time.sleep(5) #after 55 total seconds elapesd since audio started, run next line
    caption.text = """MARTIN: Made you think I was a <i>ghost?<i>
    JON: No... it's-"""
    time.sleep(3) #after 58 total seconds elapesd since audio started, run next line
    caption.text = """MARTIN: No, no... it's just that whatever
    web these statements have caught you in"""
    time.sleep(4) #after 62 total seconds elapesd since audio started, run next line
    caption.text = "<i>(cont'd)</i>: well, I'm there too. We all are, I think."
    time.sleep(5) #after 67 total seconds elapesd since audio started, run next line
    caption.text = "[MARTIN SIGHS]"
    time.sleep(5) #after 72 total seconds elapesd since audio started, run next line
    caption.text = """MARTIN: A ghost? Really?
    JON: Shut up, Martin."""
    time.sleep(4) #after 76 total seconds elapesd since audio started, run next line
    caption.text = "[TAPE CLICKS]"
    time.sleep(3) #after 79 total seconds elapesd since audio started, run next line
    caption.opacity = 0 #makes background box around caption invisable
    caption.text = "" #gets rid of caption text

def OhHello():
    caption.opacity = 0.66 #makes background box behind caption semi-transparent
    caption.text = "[TAPE CLICKS]"
    time.sleep(2) #after 2 total seconds elapesd since audio started, run next line
    caption.text = "MARTIN: Oh hello."
    time.sleep(4) #after 6 total seconds elapesd since audio started, run next line
    caption.text = "Are you still listining?"
    time.sleep(4) #after 10 total seconds elapesd since audio started, run next line
    caption.text = "Huh..."
    time.sleep(3) #after 13 total seconds elapesd since audio started, run next line
    caption.text = "[TAPE CLICKS]"
    time.sleep(3) #after 16 total seconds elapesd since audio started, run next line
    caption.opacity = 0 #makes background box around caption invisable
    caption.text = "" #gets rid of caption text