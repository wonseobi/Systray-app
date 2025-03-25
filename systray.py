# App that runs on system tray with menu

# Module dependencies
import PIL
import pystray

# Importing packages
from PIL import Image

# Drawing icon from root
image = PIL.Image.open("smile.png")

# Menu feature
def on_clicked(icon, item):
    if str(item) == "Working!":
        print("Hello program")
    elif str(item) == "Exit":
        icon.stop()
    elif str(item) == "Subitem 1":
        print("This is the Submenu 1")
    else:
        print("Feature coming soon...")

icon = pystray.Icon("Neural", image, menu=pystray.Menu(
    pystray.MenuItem("Working!", on_clicked),
    pystray.MenuItem("Exit", on_clicked),
    pystray.MenuItem("Submenu", pystray.Menu(
        pystray.MenuItem("Subitem 1", on_clicked),
        pystray.MenuItem("Subitem 2", on_clicked)
    ))
))

icon.run()