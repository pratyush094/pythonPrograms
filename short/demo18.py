from PIL import Image as im
from PIL import ImageFilter as ift
i = im.open("winners.jpg")
im = i.filter(ift.FIND_EDGES)
im.show()
