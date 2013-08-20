import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# font = ImageFont.truetype("Arial-Bold.ttf",14)
font = ImageFont.truetype("SIXTY.TTF",250)
img=Image.new("RGB", (250,250),(255,255,255))
#img=Image.new("R")
draw = ImageDraw.Draw(img)
draw.text((0, 0),"B!",(0,0,0),font=font)
draw = ImageDraw.Draw(img)
img.save("a_test.jpg")
