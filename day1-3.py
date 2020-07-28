# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:19:14 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 100.45
y = 0.5
z = 10.5
mc.player.setPos(x,y,z)