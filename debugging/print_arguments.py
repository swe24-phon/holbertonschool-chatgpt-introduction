#!/usr/bin/python3
import sys
import os

# Print the script name
print(os.path.basename(sys.argv[0]))

# Print each argument on a new line
for arg in sys.argv[1:]:
    print(arg)
