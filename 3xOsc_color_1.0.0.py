"""3xOsc color calculator 1.0.0 - Calculate volumes for colors with Fruity
Loops 3xOsc oscillators.
Copyright (C) 2023  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

def inputRGB():
    global R
    global G
    global B
    global quitcheck
    print ("Input R, G, B values for a color in RGB format."+"\n")
    R=input("R (q to quit): ")
    if R=='q':
        quit()
    if R.isdigit()==False or int(R)<0:
        R=0
    if int(R)>255:
        R=255
    G=input("G (q to quit): ")
    if G=='q':
        quit()
    if G.isdigit()==False or int(G)<0:
        G=0
    if int(G)>255:
        G=255
    B=input("B (q to quit): ")
    if B=='q':
        quit()
    if B.isdigit()==False or int(B)<0:
        B=0
    if int(B)>255:
        B=255
    R=int(R)
    G=int(G)
    B=int(B)
    CalculateVolumes(R,G,B)
    
#GenerateChord

def CalculateVolumes(R,G,B):
    RGB=[R,G,B]
    RGBmax=max(RGB)
    saw=int(50/RGBmax*R)
    square=int(50/RGBmax*G)
    sine=int(50/RGBmax*B)
    osclist=[saw,square,sine]
    maxosc=max(osclist)
    osc_one=False
    print ("\n")
    if saw==maxosc and osc_one==False:
        print ("Saw: Oscillator 1")
        osc_one=True
    else:
        print ("Saw: ",saw)
    if square==maxosc and osc_one==False:
        print ("Square: Oscillator 1")
        osc_one=True
    else:
        print ("Square: ",square)
    if sine==maxosc and osc_one==False:
        print ("Sine: Oscillator 1")
        osc_one=True
    else:
        print ("Sine: ",sine)
    print ("\n")
    RGBscale=[R/255*100,G/255*100,B/255*100]
    RGBvalue=int(100-max(RGBscale))
    print ("Clone synth specified above, pitch it one octave below, invert polarity and set volume on: ", RGBvalue)
    print ("\n")

#main
def main():
    global R
    global G
    global B
    while True:
        inputRGB()

main()
