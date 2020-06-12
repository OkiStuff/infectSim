from ursina import *
from main import addText

app = Ursina()


def changeText(s, a, b):

    

    t = dedent( str(s) )
    Text.default_resoluation = 1080 * Text.size
    test = Text(origin=(a,b), text=t)
    
if addText == True:
    
    aa -= .5
    bb -= .5

    changeText("Hello", aa, bb)
