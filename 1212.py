import pyjokes
from googletrans import Translator
translator = Translator()
joke = pyjokes.get_joke()
#a = translator.translate(joke, dest='ru')
#print(a)
print(joke)