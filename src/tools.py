from tkinter import *    
from callbacks import *

class Window:
    def __init__(self, root, width, height):
        super().__init__()
        self.root = root
        self.width = width
        self.height = height

    def createFrame(self, orientation):
        if(orientation == 'half'):
            self.top_frame = Frame(self.root, width=self.width, height=self.height / 2)
            self.bottom_frame = Frame(self.root, width=self.width, height=self.height / 2)
        elif(orientation == 'corners'):
            self.top_left_frame = Frame(self.root)
            self.top_right_frame = Frame(self.root)
            self.bottom_left_frame = Frame(self.root)
            self.bottom_right_frame = Frame(self.root)
        self.root.grid_propagate(False)

    def createWindow(self, title, size, resize):
        '''
        Create a new window

        root:   Tk() object. main app root
        size:   size (width x height) of window when initialized
        resize: type is boolean. 
                true will initialize window that can change size. 
                false will initialize window that cannot change size
        '''
        self.root.title(title)
        self.root.geometry(size)
        self.root.resizable(resize[0], resize[1])

    def createGrid(self, rows, cols, orientation):
        if(orientation == 'single'):
            if(rows):
                for idx in range(rows['count']):
                    self.root.rowconfigure(idx, weight=rows['weight'][idx])
            if(cols):
                for idx in range(cols['count']):
                    self.root.columnconfigure(idx, weight=cols['weight'][idx])

        elif(orientation == 'half'):
            if(rows):
                self.top_frame.grid(row=0, rowspan=rows['top']['count'])
                self.bottom_frame.grid(row=rows['top']['count'], rowspan=rows['bottom']['count'])
                # for idx in range(rows['top']['count']):
                #     self.top_frame.rowconfigure(idx, weight=rows['top']['weight'][idx])
                # for idx in range(rows['bottom']['count']):
                #     self.bottom_frame.rowconfigure(idx, weight=rows['bottom']['weight'][idx])

            if(cols):
                self.top_frame.grid(column=0, columnspan=3)
                self.bottom_frame.grid(column=0, columnspan=3)

                # for idx in range(cols['top']['count']):
                #     self.top_frame.columnconfigure(idx, weight=cols['top']['weight'][idx])
                # for idx in range(cols['bottom']['count']):
                #     self.bottom_frame.columnconfigure(idx, weight=cols['bottom']['weight'][idx])        
        

    def addLabel(self, text, coords, head=False, frame=None, font_type='Arial'):
        if(head): font_size = 25
        else: font_size = 12

        if not frame: label = Label(self.root, text=text, font=(font_type, font_size))
        elif(frame == 'top'): label = Label(self.top_frame, text=text, font=(font_type, font_size))
        elif(frame == 'bottom'): label = Label(self.bottom_frame, text=text, font=(font_type, font_size))
        label.grid(column=coords[0], row=coords[1])

    def addEntry(self, coords, head=False, frame=None):
        if not frame: entry = Entry(self.root)
        elif(frame == 'top'): entry = Entry(self.top_frame)
        elif(frame == 'bottom'): entry = Entry(self.bottom_frame)
        entry.grid(column=coords[0], row=coords[1], sticky='ew')

    def addButton(self, name, pos, color, command, args, frame=None, wait=False):
        if not frame: button = Button(self.root, text=name, bg=color, command=lambda: command(*args))
        elif(frame == 'top'): button = Button(self.top_frame, text=name, bg=color, command=lambda: command(*args))
        elif(frame == 'bottom'): button = Button(self.bottom_frame, text=name, bg=color, command=lambda: command(*args))
        button.grid(column=pos[0], row=pos[1])

    def addDropDown(self, coords, items, cmd, head=False, frame=None):
        if not frame: 
            val = StringVar(self.root)
            val.set('')
            entry = OptionMenu(self.root, val, *items, command=cmd)
        elif(frame == 'top'): 
            val = StringVar(self.top_frame)
            val.set('')
            entry = OptionMenu(self.top_frame, val, *items, command=cmd)
        elif(frame == 'bottom'): 
            val = StringVar(self.top_frame)
            val.set('')
            entry = OptionMenu(self.bottom_frame, val, *items, command=cmd)
        entry.grid(column=coords[0], row=coords[1], sticky='ew')        

    def clearWindow(self):
        try:
            for widget in self.root.winfo_children():
                widget.destroy()
        except Exception:
            for widget in self.top_frame.winfo_children():
                widget.destroy()

    
