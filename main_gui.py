# Jack Tench 2023

# Imports
import time
import tkinter as tk

# Define Counter class.
class Counter:

    # Init method.
    def __init__(self):
        self.count = 0
    
    # Methods for counter up and down.
    def up(self):
        self.count += 1
    def down(self):
        self.count -= 1
    
    # Method to reset counter to 0.
    def reset(self):
        self.count = 0

    # Method to return current count.
    def getCount(self):
        return self.count

# Functions
def get_counters_amount():
    global countersToCreate
    countersToCreate = countersToCreateEntry.get()
    time.sleep(0.5)
    setupWindow.destroy() # the application has been destroyed!

def update():
    dynamicLabels = []
    for i in range(countersToCreateInt):
        label = tk.Label(text = str(i+1) + ": " + str(counters[i].getCount()))
        label.pack()
        dynamicLabels.append(label)

def upBtnPress():
    selectedCounterToChange = toChange.get()
    selectedCounterToChangeIndex = int(selectedCounterToChange) - 1
    counters[selectedCounterToChangeIndex].up()
    update()

def downBtnPress():
    selectedCounterToChange = toChange.get()
    selectedCounterToChangeIndex = int(selectedCounterToChange) - 1
    counters[selectedCounterToChangeIndex].down()
    update()

def resetBtnPress():
    selectedCounterToChange = toChange.get()
    selectedCounterToChangeIndex = int(selectedCounterToChange) - 1
    counters[selectedCounterToChangeIndex].reset()
    update()

winTitle = "ScoreTallyPy"

# Setup init window.
setupWindow = tk.Tk()
setupWindow.title(winTitle)

# Populate init window.
header1 = tk.Label(text = "ScoreTallyPy")
header1.pack()
countersToCreateLabel = tk.Label(text = "Select how many counters:")
countersToCreateLabel.pack()
countersToCreateEntry = tk.Entry()
countersToCreateEntry.pack()
countersToCreateButton = tk.Button(text = "Go!", command = get_counters_amount)
countersToCreateButton.pack()

setupWindow.mainloop()

# Create array/list? of counters * amount selected.
if countersToCreate == "":
    countersToCreateInt = 1
else:
    countersToCreateInt = int(countersToCreate)
counters = [Counter() for i in range(countersToCreateInt)]

# Setup main window.
mainWindow = tk.Tk()
mainWindow.title(winTitle)

# Populate main window.
header2 = tk.Label(text = "ScoreTallyPy")
header2.pack()

# Create dynamic amount of labels.
update()

# Create list of readable names for counters.
counterNamesHuman = []
for i in range(countersToCreateInt):
    counterNamesHuman.append(str(i+1))

# Drop down menu.
toChange = tk.StringVar(mainWindow)
toChange.set(counterNamesHuman[0])
selectCounter = tk.OptionMenu(mainWindow, toChange, *counterNamesHuman)
selectCounter.pack()

# Plus and minus buttons.
upBtn = tk.Button(text = "+", command = upBtnPress)
upBtn.pack()
downBtn = tk.Button(text = "-", command  = downBtnPress)
downBtn.pack()
# Reset button.
resetBtn = tk.Button(text = "Reset", command = resetBtnPress)
resetBtn.pack()

mainWindow.mainloop()
