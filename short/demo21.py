from PIL import Image as im
from PIL import ImageOps as io
i = im.open("winners.jpg")
img = io.crop(i,20)
img.show()
