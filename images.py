from PIL import Image, ImageFilter

img = Image.open('./pokedex/mailchimp-0qnRfgnZIsI-unsplash.jpg')
img.thumbnail((400,400))
filtered_img = img.filter(ImageFilter.DETAIL)

filtered_img.save('blur.png', 'png')

print(dir(img))
filtered_img.show()