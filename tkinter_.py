#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self._input = Entry(self)
        self._input.pack()
        self._btn = Button(self,text="Hello",command=self.hello)
        self._btn.pack()

    def hello(self):
        name = self._input.get() or 'World'
        messagebox.showinfo('Hello','Hello %s' % name)

app = Application()
app.master.title('hell0')
app.mainloop()