import keyboard
import json


keybinds_json_file = open('keybinds.json')
stop_script_key = 'Esc'

#whenever the key is typed within (timout seconds) followed by a space, the value will replace the text before the space was typed
for key, value in json.load(keybinds_json_file).items():
    keyboard.add_abbreviation(key, value)

#The code will keep running in the background until the command in args is pressed
keyboard.wait(stop_script_key)