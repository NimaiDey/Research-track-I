import time
import sys

message = "Welcome"
for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.2)  # Adjust speed of animation

print()  # Move to a new line after animation

