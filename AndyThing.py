import time, sys

# Put this at the beginning of both files
def print_out(text):
    i = 0
    while i < len(text):
        print(text[i], end="")
        # time is in seconds. This is pretty fast, feel free to adjust
        time.sleep(0.01)
        i += 1
        sys.stdout.flush()