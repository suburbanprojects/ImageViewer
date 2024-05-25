import tkinter as tk
from tkinter import *
from tkinter import filedialog, ttk
from PIL import Image, ImageTk

class ImageViewer2():
    def __init__(self,app):
        self.root = app
        self.viewer_layout()
    
    def viewer_layout(self):
        #create toolbar for a border between label and toolbar
        self.tool_bar = ttk.Label(app) 
        self.tool_bar.pack(side=BOTTOM, fill=BOTH)
        #put the button in the toolbar
        self.button = ttk.Button(self.tool_bar, text='Open Image', command=self.OpenImage) 
        self.button.pack()
        # Create a label to display the image, have to use tk so the image stays centered
        self.label = tk.Label(app)
        self.label.pack(fill=tk.BOTH, expand=True)

    def OpenImage(self):
        self.file = filedialog.askopenfilename(filetype =
        (("PNG files","*.png"),("JPG files","*.jpg"),("all files","*.*")) )
        if self.file:
            image = Image.open(self.file)
            photo = ImageTk.PhotoImage(image)
            self.label.config(image=photo)
            self.label.image = photo

if __name__ == "__main__":
    app = Tk()
    app.title("Image Viewer")
    app.geometry("800x600")
    app2 = ImageViewer2(app)
    app.mainloop()
