import os

script_path = os.path.abspath('main.py')
startup_folder = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
shortcut_path = os.path.join(startup_folder, 'my_assistant.lnk')

if not os.path.exists(startup_folder):
    os.makedirs(startup_folder)

if not os.path.exists(shortcut_path):
    bat_path = os.path.join(os.path.dirname(script_path), 'my_assistant.bat')
    with open(bat_path, 'w') as bat_file:
        bat_file.write(f'@echo off\npython {script_path}\npause')
    os.startfile(bat_path, 'run', shortcut_path)
    os.remove(bat_path)