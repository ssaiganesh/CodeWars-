"""
Complete rgb function so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
"""
#My Solution

def rgb(r, g, b):
    if r> 255: 
        r = 255
    if g>255: 
        g = 255
    if b>255:  
        b = 255
    if r<0: 
        r = 0
    if g<0: 
        g = 0
    if b<0: 
        b = 0
    x = str(hex(r))[2:].upper()
    if len(x) == 1:
        x = '0'+ x
    y = str(hex(g))[2:].upper()
    if len(y) == 1:
        y = '0'+ y
    z = str(hex(b))[2:].upper()
    if len(z) == 1:
        z = '0'+ z

    return f'{x}{y}{z}'
    


#Recommended Solution:
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))