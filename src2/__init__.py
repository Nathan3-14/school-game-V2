
try:
    import rich
except ModuleNotFoundError:
    print("Module 'rich' is needed for project to work\nDownload it from https://github.com/Textualize/rich and place it in the root folder")
    quit()

from .classes import *
from .input_handlers import *
from .common_classes import *
