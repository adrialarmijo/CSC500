import tkinter as tk

def createWindow(title, background):
    window = tk.Tk()
    window.geometry("600x600")
    window.config(bg=background)
    window.resizable(width=True, height=True)
    window.title(title)
    return window