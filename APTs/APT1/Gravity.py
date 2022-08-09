"""
Created on 9/3/21

@author: cartercribbs
"""

def falling(time, velo):
    t = time
    v = velo
    g = 9.8
    d = v*t + 0.5*g*(t**2)
    return d



