from p5 import *

w = 3600  # width
h = 3600  # height
frame_rate = 1

"""
params = {
  # map param 0 from 0-255 to 0.1 - 0.4
  radius: mapParam(rawParams[0], 0.1, 0.4),
  # map param 1 from 0-255 to 3-8 as integer
  points: parseInt(mapParam(rawParams[1], 3, 8)),
  # 50% chance to fill
  fill: rawParams[2] < 127,
  # generate a random RGB color
  backgroundColor: "rgb("+rawParams[3]+","+rawParams[4]+","+ rawParams[5]+")"
}"""

def setup():
    size(w, h, P3D) # (width, height)
    frameRate(frame_rate)
    imageMode(CENTER)
    noLoop()

def draw():
    background(params.backgroundColor)
    if params.fill:
        fill('black')
    else :
        noFill()
	r = params.radius * width
    beginShape()
    for (i=0; i < params.points; i++)
        {ang = TWO_PI * i/params.points
        #slightly offset the angle of each point
        angleOffset = range(0, TWO_PI)/10
        x = r*cos(ang+angleOffset)
        y = r*sin(ang+angleOffset)
        vertex(x+width/2, y+height/2)}
    endShape(CLOSE)

run()