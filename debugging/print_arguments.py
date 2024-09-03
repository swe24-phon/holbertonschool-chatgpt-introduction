import sys
import os

try:
    print(os.path.basename(sys.argv[0]))
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
