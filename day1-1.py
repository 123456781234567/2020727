# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:19:14 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

print(mc.player.getTilePos())

