import os
for i in range(5):
    os.system ("fswebcam -F 5 --fps 20 1280*720 /path")
    print("taken")
