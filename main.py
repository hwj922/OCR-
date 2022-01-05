import  pytesseract
from PIL import Image
from translate import Translator

im=Image.open(r'C:\Users\user\OneDrive\桌面\sentence.jpg')
text = pytesseract.image_to_string(im,lang='eng')

translator = Translator ( to_lang = "zh-tw" )
translation = translator.translate(text)
print(translation)