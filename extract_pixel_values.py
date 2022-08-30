from Pillow import Image

im = Image.open('chunk'+ each +'.png')


#   pixval returns a list of sets [(R,G,B,A), (R,G,B,A),...] with one set per pixel
pixval = list(im.getdata())

#   pixval_flat returns a list of values [R, G, B, A, R, G, B, A,...] for all pixels in line
#       pixval_flat = [x in sets for pixval for x in sets]




