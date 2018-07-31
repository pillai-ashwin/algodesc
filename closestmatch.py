import sys
import difflib
import os
from os import listdir, environ
directory = sys.argv[1]
filename = sys.argv[2]
fileslist = os.listdir(directory)
print("\nMaybe the file name that you are looking for is : ",difflib.get_close_matches(filename, fileslist))