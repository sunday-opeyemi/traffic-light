# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:13:51 2019

@author: YEMI
"""

import tkinter as tk
from PIL import Image, ImageTk

class TrafficLight(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master=None)
        self.canv = tk.Canvas(height= 300, width= 200)
        self.canv.pack()
        self.red = self.canv.create_oval(50, 10, 100, 50, fill= "grey", tag= "red")
        self.yellow = self.canv.create_oval(50, 60, 100, 100, fill= "grey", tag= "yellow")
        self.green = self.canv.create_oval(50, 110, 100, 150, fill= "grey", tag= "green")
        self.imgplay = Image.open("sim/bplay.png")
        self.imgstart = ImageTk.PhotoImage(self.imgplay)
        self.startbtn = tk.Button(self, image= self.imgstart, command= self.start_traffic)
        self.startbtn.pack()
        self.imgpus = Image.open("sim/bpause.png")
        self.imgpause = ImageTk.PhotoImage(self.imgpus)
        self.stopbtn = tk.Button(self, image= self.imgpause, command= self.stop_traffic)
        self.stopbtn.pack()
              
    def show_red(self):
        self.canv.itemconfigure(self.green, fill="gray")
        self.canv.itemconfigure(self.red, fill="red")
        
    def show_yellow(self):
        self.canv.itemconfigure(self.red, fill="gray")
        self.canv.itemconfigure(self.yellow, fill="yellow")
        self.delay = self.canv.after(2000, self.show_green)
        
    def show_green(self):
        self.canv.itemconfigure(self.yellow, fill="gray")
        self.canv.itemconfigure(self.green, fill="green")
        self.delay = self.canv.after(2000, self.start_traffic)

    def start_traffic(self):
        self.show_red()
        self.delay = self.canv.after(2000, self.show_yellow)
    
    def stop_traffic(self):
        self.canv.after_cancel(self.delay)
        self.canv.itemconfigure(self.red, fill="gray")
        self.canv.itemconfigure(self.yellow, fill="gray")
        self.canv.itemconfigure(self.green, fill="gray")

if __name__ == "__main__":
    root= tk.Tk()
    traffic = TrafficLight(root)
    traffic.pack()
    root.mainloop()