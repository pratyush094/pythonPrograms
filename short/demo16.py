from PIL import Image as im
ref = im.open("winners.jpg")
ref1 = ref.convert("I")
ref1.show()
