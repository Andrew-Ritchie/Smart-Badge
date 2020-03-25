import math
import machine

dac1 = machine.Pin(25)
speaker = machine.DAC(dac1)

C4 = 261.626
D4 = 293.665
E4 = 329.628
F4 = 349.228
G4 = 391.995
A4 = 440
B4 = 493.883
C5 = 523.351

max_volume = 127
baselength = 3000

def playNote(note, length=1, volume=max_volume):
    notelength = baselength*length
    for t in range(notelength):
        speaker.write(128 + int(volume * math.sin(2 * math.pi * note * t/baselength)))
        
def playSong(song):
    for note in song:
        playNote(*note)
        
def chordTest():
    for t in range(10000):
        speaker.write(128 + int(0.3 * math.sin(2 * math.pi * C4 * t/5000)) + int(0.3 * math.sin(2 * math.pi * E4 * t/5000)) + int(0.3 * math.sin(2 * math.pi * G4 * t/5000)))

song1 = [(E4,1,max_volume),
         (E4,1,max_volume),
         (F4,1,max_volume),
         (G4,1,max_volume),
         (G4,1,max_volume),
         (F4,1,max_volume),
         (E4,1,max_volume),
         (D4,1,max_volume),
         (C4,1,max_volume),
         (C4,1,max_volume),
         (D4,1,max_volume),
         (E4,1,max_volume),
         (E4,1.5,max_volume),
         (D4,0.5,max_volume),
         (D4,2,max_volume),
         (E4,1,max_volume),
         (E4,1,max_volume),
         (F4,1,max_volume),
         (G4,1,max_volume),
         (G4,1,max_volume),
         (F4,1,max_volume),
         (E4,1,max_volume),
         (D4,1,max_volume),
         (C4,1,max_volume),
         (C4,1,max_volume),
         (D4,1,max_volume),
         (E4,1,max_volume),
         (D4,1.5,max_volume),
         (C4,0.5,max_volume),
         (C4,2,max_volume)]

    








