from vpython import *
#GlowScript 3.1 VPython
scene.width = scene.height = 600
scene.background = color.white
scene.range = 1.3
scene.title = 'A 15000-segment curve object with random segment lengths, radii, and colors'
# Display frames per second and render time:
scene.append_to_title("<div id='fps'/>")

run = True
def Runbutton(b):
    global run
    if b.text == 'Pause':
        run = False
        b.text = 'Run'
    else:
        run = True
        b.text = 'Pause'

button(text='Pause', bind=Runbutton)
scene.append_to_caption("""
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.""")

N = 15000
p = []
last = vec(0,0,0)
for i in range(N):
    next = last+0.1*vec.random()
    while mag(next) > 1: # if next is outside the sphere, try another random value
        next = last+0.1*vec.random()
    p.append({'pos':next, 'radius':0.001+0.03*random(), 'color':(vec(1,1,1)+vec.random())/2})
    last = next
c = curve(p)
while True:
    rate(60)
    if run:
        c.rotate(angle=0.005, axis=vec(0,1,0))