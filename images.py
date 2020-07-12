from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
#blur image 
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("blur.png", 'png')

#sharp image 
# sharp_img = img.filter(ImageFilter.SHARPEN)
# sharp_img.save("sharp_pika.png", 'png')

#greyscale image 
greyscale_img = img.convert('L')
# greyscale_img.save("grey_pika.png", 'png')
# greyscale_img.show()

#rotate image 
crooked = greyscale_img.rotate(90)
crooked.save("rotate_pika.png", 'png')
crooked.show()