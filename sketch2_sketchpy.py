# I created this sketch 2 from png image using sketch_from_image() function in Sketchpy.

from sketchpy import canvas

obj = canvas.sketch_from_image(r'images/image2.png')
obj.draw(threshold=190)