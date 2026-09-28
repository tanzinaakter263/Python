""" install an external module and use
 it to make your computer speak.
 """

import pyttsx3
engine = pyttsx3.init()
engine.say("Hi!!! I am Tanzina")
engine.runAndWait()