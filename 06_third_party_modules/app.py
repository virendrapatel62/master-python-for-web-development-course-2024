from PIL import Image

img = Image.open("image.jpg")
# img.show()

height = img.height
width = img.width

for index in range(2, 11):
    new_height = int(height/index)
    new_width = int(width/index)
    resized_image = img.resize((new_width, new_height))
    resized_image.save(f"output/resized_image_{new_width}x{new_height}.jpg")
