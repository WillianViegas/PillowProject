from PIL import Image, ImageFilter, ImageDraw, ImageFont

im = Image.open("199174.png")

print(im.format, im.size, im.mode)

# im.show()
#
# im = im.rotate(45)
# im.show()
#
# print(im.palette)
#
# im.thumbnail((200, 200))
#
# im.show()

#Read the two images
# image1 = Image.open('wp5728306.jpg')
# image1.show()
# image2 = Image.open('download.jpg')
# image2.show()
#
# #resize, first image
# image1 = image1.resize((426, 240))
# image1_size = image1.size
# image2_size = image2.size
# new_image = Image.new('RGB', (2 * image1_size[0], image1_size[1]), (250,250,250))
# new_image.paste(image1, (0,0))
# new_image.paste(image2, (image1_size[0], 0))
# new_image.save("merged_image", "JPEG")
# new_image.show()

#blur image
# oriImage = Image.open('199174.png')
# blurImage = oriImage.filter(ImageFilter.GaussianBlur(2))
# blurImage.show()

#cropped img
# img = Image.open('wp5728306.jpg')
# cropped = img.crop((1,2,800,800))
# cropped.show()

#water mark
# img_h = Image.open('199174.png')
# width, height = im.size
#
# draw = ImageDraw.Draw(img_h)
# text = "sample WaterMark"
#
# font = ImageFont.truetype('arial.ttf', 36)
# textwidth, textheight = draw.textsize(text, font)
#
# margin = 10
# x = width - textwidth - margin
# y = height - textheight - margin
#
# draw.text((x, y), text, font=font)
# img_h.show()

img = Image.open("wp5728306.jpg")
im3 = im.filter(ImageFilter.MinFilter)
im3.show()