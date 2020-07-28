# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:30:12 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
                                                                                                
while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("your location - x:" + str(x) +
    "Y:" + str(y) +
    "Z:" + str(z))