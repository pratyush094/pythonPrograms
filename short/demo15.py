from PIL import Image as im
ref = im.open("winners.jpg")
ref1 = ref.rotate(90)
ref1.show()
