import os

#display size
try:
    dispHeight, dispSize = os.popen('stty size', 'r').read().split()
    dispSize = int(dispSize)
    dispHeight = int(dispHeight)
except:
    dispHeight = 60
    dispSize = 100
################################################################


#background layer
bgHeight = dispHeight
bgWidth = 10*dispSize
bgStarCount = int(bgWidth*bgHeight/100)
#################################################################