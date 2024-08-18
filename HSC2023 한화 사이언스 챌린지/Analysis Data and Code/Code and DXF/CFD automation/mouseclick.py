from pynput import mouse, keyboard

# This will keep track if the listener should be running
running = True

def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_press(key):
    global running
    if key == keyboard.Key.esc:
        # Stop listener
        running = False

# Setup the listener threads
mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

# Start the threads and join them so the script doesn't end early
mouse_listener.start()
keyboard_listener.start()

while running:
    pass

mouse_listener.stop()
keyboard_listener.stop()
