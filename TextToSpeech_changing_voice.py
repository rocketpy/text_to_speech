# pip install pyttsx3
# pip install pypiwin32

import pyttsx3
  

converter = pyttsx3.init()

# Sets speed percent Can be more than 100
converter.setProperty('rate', 150)
# Set volume 0-1
converter.setProperty('volume', 0.7)
  
# Queue the entered text 
# There will be a pause between
# each one like a pause in 
# a sentence
converter.say("Hello")
converter.say("I'm a robot")
  
# Empties the say() queue
# Program will not continue
# until all speech is done talking
converter.runAndWait()

#  Changing Voice


