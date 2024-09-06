import pytesseract
from PIL import Image # pip install Pillow

# set tesseract cmd to the be the path to your tesseract engine executable 
# (where you installed tesseract from above urls)

# IMPORTANT: this should end with '...\tesseract.exe'


# and start doing it

# your saved images on desktop
list_with_many_images = [
  "/home/ep/test/pics/1.png",
  "/home/ep/test/pics/2.png",
  "/home/ep/test/pics/3.png",
  "/home/ep/test/pics/4.png",
  "/home/ep/test/pics/5.png",
  "/home/ep/test/pics/6.png",
  "/home/ep/test/pics/7.png",
  "/home/ep/test/pics/8.png",
  "/home/ep/test/pics/9.png",
  "/home/ep/test/pics/10.png",
  "/home/ep/test/pics/11.png",
  "/home/ep/test/pics/12.png",
  "/home/ep/test/pics/13.png",
  "/home/ep/test/pics/14.png",
  "/home/ep/test/pics/15.png",
  "/home/ep/test/pics/16.png",
  "/home/ep/test/pics/17.png",
  "/home/ep/test/pics/18.png",
  "/home/ep/test/pics/19.png",
  "/home/ep/test/pics/20.png",
  "/home/ep/test/pics/21.png",
  "/home/ep/test/pics/22.png",
  "/home/ep/test/pics/23.png",
  "/home/ep/test/pics/24.png",
  "/home/ep/test/pics/25.png",
  "/home/ep/test/pics/26.png",
  "/home/ep/test/pics/27.png",
  "/home/ep/test/pics/28.png"
]

# create a function that returns the text
def image_to_str(path):
    """ return a string from image """
    return pytesseract.image_to_string(Image.open(path))

# now pure action + csv part
with open("images_content3.csv", "w+", encoding="utf-8") as file:
  file.write("ImagePath, ImageText")
  for image_path in list_with_many_images:
    text = image_to_str(image_path)
    line = f"{image_path}, {text}\n"
    file.write(line)


    