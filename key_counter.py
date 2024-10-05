from pynput import keyboard

# Initialize a variable to count key presses
key_count = 0

def on_press(key):
    global key_count
    key_count += 1
    print(f'Key pressed: {key}, Total keystrokes: {key_count}')

def on_release(key):
    # Stop the listener if the 'Esc' key is pressed
    if key == keyboard.Key.esc:
        return False

# Set up the listener for key presses and releases
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Press keys to count. Press 'Esc' to stop.")
    listener.join()

print(f'Total key presses: {key_count}')
