import graph

def row_horiz(y, larg):
	for x in range(larg):
		graph.plot(y, x)
		
def segment_horiz(y, x1, x2):
	for x in range(x1, x2):
		graph.plot(y, x)
		
def rectangle(y1, y2, x1, x2):
	for x in range(x1, x2):
		for y in range(y1, y2):
			graph.plot(y,x)

def vertical_strip(image_height, image_width, band_width):
	for rectStart in range (0, image_width, band_width*2):
		rectangle(0, image_height, rectStart, rectStart + band_width)


def checkerboard(image_height, image_width, box_width):
	boxStartX = 0
	boxStartY = 0
	
	for boxStartX in range (0, image_width, box_width*2):
		for boxStartY in range (0, image_height, box_width*2):
			rectangle(boxStartY, boxStartY+box_width, boxStartX, boxStartX+box_width)
			
		for boxStartY in range (0, image_height, box_width*2):
			rectangle(boxStartY+box_width, boxStartY+(2*box_width), boxStartX+box_width, boxStartX+(2*box_width))




graph.ouvre_fenetre(120, 160)



graph.attend_fenetre()

