from PIL import Image as im
from PIL import ImageOps as io
i = im.open("winners.jpg")
img = io.autocontrast(i,20)
img.show()
