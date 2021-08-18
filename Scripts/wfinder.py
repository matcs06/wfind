import sys
import os
from pathlib import Path

root_dir = sys.argv[1]
searched_file = sys.argv[2]

print("\n --- Searching for files containg string: " + searched_file + "----\n")

def loopdirs(folder):
   try:
      for root, subFolder, files in os.walk(folder):
         for file in files:
            if searched_file in file:
               print(root + "\\" + file)
   except:   
      print("\nExecultion stopped!\n")

loopdirs(root_dir)
