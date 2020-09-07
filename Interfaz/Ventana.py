import tkinter as tk


class Window(tk.Frame):

    def __init__(self, *args, **kwargs):
        
        
        self.text = tk.Text()


if __name__ == "__main__":
    root = tk.Tk()

    root.mainloop()