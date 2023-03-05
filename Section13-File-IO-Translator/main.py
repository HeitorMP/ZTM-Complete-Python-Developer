from file_utils.check_files import *
from translate import Translator
import sys

text = get_myfile(sys.argv)
if not text:
    no_permission_routine()

try:
    with open("test-pt.txt", mode='w') as my_file2:
        translator = Translator(to_lang="pt")
        print(translator.translate(text))
        my_file2.write(translator.translate(text))
except IOError as err:
    no_permission_routine()
