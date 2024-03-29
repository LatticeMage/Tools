import os
import json
import tkinter as tk
from tkinter import ttk, PhotoImage
import subprocess


def launch_exe(exe_path, args=[]):
    """Function to launch an executable with arguments."""
    try:
        cmd = [os.path.expandvars(exe_path)] + args
        subprocess.run(cmd)
    except Exception as e:
        print(f"Error executing {exe_path}: {e}")

def main():
    # Load JSON data
    with open('setting.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Set up the main window
    root = tk.Tk()
    root.title("Shortcut Panel")

    # Apply a dark theme
    root.configure(bg='#2E2E2E')
    
    style = ttk.Style()
    style.theme_use('alt')
    style.configure('TButton', 
                    background='#333333',
                    foreground='white',
                    bordercolor='#555555',
                    padding=10)

    style.map('TButton',
              background=[('pressed', '#555555'), ('active', '#666666')],
              foreground=[('pressed', 'white'), ('active', 'white')])

    basesize = data['basesize']  # Load basesize from JSON

    # For each shortcut in the JSON data, create a button
    for shortcut in data['shortcuts']:
        exe_path = os.path.expandvars(shortcut['exe_path'])  # Handle environment variables in the path
        args = shortcut.get('args', [])


        # Check if "icon" field exists, otherwise use the default naming scheme
        icon_path = shortcut.get('icon', None)
        if not icon_path:
            icon_path = os.path.splitext(os.path.basename(exe_path))[0] + '.png'

        # Create button with image
        img = PhotoImage(file=icon_path)
        
        # Resize the image based on basesize and shortcut's size
        size_multiplier = shortcut['size']
        new_width = basesize * size_multiplier
        new_height = basesize * size_multiplier

        img = img.subsample(int(img.width() // new_width), int(img.height() // new_height))
        
        # Create the button with the adjusted width, height, and no text
        btn = ttk.Button(root, image=img, 
                         command=lambda exe_path=exe_path, args=args: launch_exe(exe_path, args))
        btn.image = img  # To prevent garbage collection of the image

        # Calculate rowspan and columnspan based on shortcut size
        rowspan = columnspan = shortcut['size']

        # Position button based on position in JSON, and account for rowspan/columnspan
        x, y = shortcut['position']
        btn.grid(row=y, column=x, padx=5, pady=5, rowspan=rowspan, columnspan=columnspan)

    # Assume taskbar width
    TASKBAR_WIDTH = 66

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Update window to ensure it's drawn and we can get its dimensions
    root.update_idletasks()

    # Get the window width and height
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    # Calculate x coordinate for the window to be close to the right side (before the taskbar) 
    x = screen_width - window_width - TASKBAR_WIDTH - 10  # 10 is a small margin

    # Set y to a small margin from the top
    y = 0

    # Set the position of the window
    root.geometry(f'+{x}+{y}')
    root.mainloop()

if __name__ == '__main__':
    main()
