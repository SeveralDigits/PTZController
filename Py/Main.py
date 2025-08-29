import clr
from pathlib import Path

script_dir = Path(__file__).parent
dll_path = script_dir.parent / "Lib" / "PTZ2.dll"

clr.AddReference(str(dll_path))
from PTZ import PTZDevice, PTZType
from tkinter import *

camera_name = "Logi Group Camera"

device = PTZDevice.GetDevice(camera_name, PTZType.Relative)

print("Zoom range:", device.ZoomMin, "to", device.ZoomMax, "step:", device.ZoomStep)

root = Tk()
root.title("PTZ Controller")
root.geometry('500x200')

labelStep = Label(root, text="Step amount")
entryStep = Entry(root)

def ZoomIn():
    Amnt = int(entryStep.get())
    device.Zoom(Amnt)

def ZoomOut():
    Amnt = int(entryStep.get())
    device.Zoom(-Amnt)

def PanLeft():
    Amnt = int(entryStep.get())
    device.Move(-Amnt, 0)

def PanRight():
    Amnt = int(entryStep.get())
    device.Move(Amnt, 0)

def TiltUp():
    Amnt = int(entryStep.get())
    device.Move(0, -Amnt)

def TiltDown():
    Amnt = int(entryStep.get())
    device.Move(0, Amnt)

buttonUp = Button(root, text="Up", command=TiltUp)
buttonDown = Button(root, text="Down", command=TiltDown)
buttonLeft = Button(root, text="Left", command=PanLeft)
buttonRight = Button(root, text="Right", command=PanRight)

buttonZoomIn = Button(root, text="Zoom in", command=ZoomIn)
buttonZoomOut = Button(root, text="Zoom out", command=ZoomOut)

root.mainloop()
