import pygame
import sys
from doomsettings import *
import allgamesclasses as ag
from doommap import *

def main():
    game = ag.Game(res, map,fps)
    game.run()