import graph
import random

def noir(height, length):
	for y in range(height):
		for x in range(length):
			graph.plot(y,x)

def bande_noire_gauche(height, length, band_width):
	for y in range(height):
		for x in range(length):
			if x < band_width:
				graph.plot(y,x)
				
def black_rectangle(height, length, y1, y2, x1, x2):
	for y in range(height):
		for x in range(length):
			if x >= x1 and x <= x2 and y >= y1 and y <= y2:
				graph.plot(y,x)
			
def white_rectangle(height, length, y1, y2, x1, x2):
	for y in range(height):
		for x in range(length):
			if x <= x1 or x >= x2 or y <= y1 or y >= y2:
				graph.plot(y,x)

def profMethod_vertical_strip(height, length, band_width):
	for l in range(height):
		for c in range(length):
			if c%(2*band_width) > band_width:
				graph.plot(l,c)
				
def conditional_checkerboard(height, length, box_width):
	for y in range(height):
		for x in range(length):
			if (x%(2*box_width) < box_width or y%(2*box_width) < box_width) and (x%(2*box_width) > box_width or y%(2*box_width) > box_width):
				graph.plot(y,x)
			


def nh(x, box_width):
	whichBand = x//box_width
	
	return whichBand

def nv(y, box_width):
	whichBand = y//box_width
	
	return whichBand

graph.ouvre_fenetre(400, 500)
conditional_checkerboard(400, 500, 20)
graph.attend_fenetre()
