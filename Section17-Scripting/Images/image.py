from PIL import Image, ImageFilter


"""
print(img)
print(img.format)
print(img.size)
print(img.mode)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')
filtered_img.save("gray.png", "png")
img.show()


.rotate()
.resize()

"""
img = Image.open('astro.jpg')
img.thumbnail((400, 400))
img.save('tb_astro.png')
img.show()
