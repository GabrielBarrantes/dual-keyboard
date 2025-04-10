import os, sys
import keyboard
from evdev import InputDevice, categorize, ecodes, UInput

event_number = sys.argv[1]
device_path = f'/dev/input/event{event_number}'
dev = InputDevice(device_path)
dev.grab()

print(f'Listening for key presses on {device_path}...')

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key = categorize(event)
        print("key code:", key.keycode)
        if key.keystate == key.key_down:
            if key.keycode == 'KEY_LEFTSHIFT':
                keyboard.press_and_release('ctrl+c')
            elif key.keycode == 'KEY_LEFTCTRL':
                keyboard.press_and_release('ctrl+v')
            elif key.keycode == 'KEY_CAPSLOCK':
                keyboard.press_and_release('ctrl+s')
            elif key.keycode == 'KEY_LEFTMETA':
                keyboard.press_and_release('up')
                keyboard.press_and_release('enter')
            elif key.keycode == 'KEY_S':
                keyboard.press_and_release('up')
                keyboard.press_and_release('up')
                keyboard.press_and_release('enter')
            elif key.keycode == 'KEY_SPACE':
                keyboard.press_and_release('ctrl+x')
                keyboard.press_and_release('y')
                keyboard.press_and_release('enter')
            elif key.keycode == 'KEY_A':
                keyboard.press_and_release('ctrl+minus')
            elif key.keycode == 'KEY_F1':
                keyboard.press_and_release('ctrl+w')
            elif key.keycode == 'KEY_GRAVE':
                keyboard.write('git status')
                keyboard.press_and_release('enter')
            elif key.keycode == 'KEY_1':
                keyboard.write('git checkout ')
            elif key.keycode == 'KEY_2':
                keyboard.write('git checkout -b ')
            elif key.keycode == 'KEY_3':
                keyboard.write('git add .')
                keyboard.press_and_release('enter')
            elif key.keycode == 'KEY_4':
                keyboard.write('git commit --amend')
                keyboard.press_and_release('enter')
            elif key.keycode == 'KEY_5':
                keyboard.write('git commit')
                keyboard.press_and_release('enter')
            elif key.keycode == 'KEY_ESC':
                keyboard.press_and_release('escape')
            elif key.keycode == 'KEY_TAB':
                keyboard.press_and_release('ctrl+z')
            elif key.keycode == 'KEY_102ND':
                keyboard.press_and_release('ctrl+f')
            elif key.keycode == 'KEY_BACKSPACE':
                keyboard.write("git push origin ")
            elif key.keycode == 'KEY_RIGHTCTRL':
                keyboard.write('--force')
            elif key.keycode == 'KEY_Z':
                keyboard.press(125)
                keyboard.press_and_release('minus')
                keyboard.release(125)
            elif key.keycode == 'KEY_LEFTALT':
                keyboard.press(125)
                keyboard.press_and_release('equal')
                keyboard.release(125)





