import pytesseract
from PIL import Image
import pyttsx3

try:
    # opening an image from the source path
    img = Image.open(r"D:\IVP_MINI_PROJECT\test7.png").convert('L')
    print(img)  # describes image format in the output
    img.save('greyscale.png')
    # print(img)
    # path where the Tesseract module is installed
    pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"
    # print(pytesseract.pytesseract.tesseract_cmd)
    # converts the image to result and saves it into result variable
    # print(pytesseract)
    result = pytesseract.image_to_string(img)
    print("result: "+result)
    # write text in a text file and save it to source path
    with open('abc.txt', mode='w') as file:
        file.write(result)
    print(result)

    # initializes the text-to-speech engine
    engine = pyttsx3.init()

    # an audio will be played which speaks the text if pyttsx3 recognizes it
    engine.say(result)
    engine.runAndWait()

except Exception as e:
    print("An error occurred:", e)
