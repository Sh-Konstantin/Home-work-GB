from tkinter import *

class trafficklight:
    __color = 'ff0000'
    def __init__(self):
        super().__init__()
        self.title('светофор')
        self.canvas = Canvas(self, width = 200, height=200)
        self.red = self.canvas.create_krug (10,10,60,60, fill=self.__color)
        self.yellow = self.canvas.create_krug(10, 70, 60, 120, fill='#808000')
        self.green = self.canvas.create_krug(10, 130, 60, 180, fill='#008000')
        self.canvas.pack()
        self.state = 'red-yellow'
        self.after(7000,self.running)

    def running(self):
        if self.state == 'red-yellow':
            self.canvas.itemconfigure(self.red, fill='800000')
            self.canvas.itemconfigure(self.yellow, fill='ffff00')
            self.state = "yellow-green"
            self.after(2000,self.running)
        elif self.state == 'yellow-green':
            self.canvas.itemconfigure(self.yellow, fill='808000')
            self.canvas.itemconfigure(self.green, fill='00ff00')
            self.state = "green-yellow:"
            self.after(2000, self.running)
        elif self.state == 'green-yellow':
            self.canvas.itemconfigure(self.green, fill='008000')
            self.canvas.itemconfigure(self.yellow, fill='ffff00')
            self.state = "yellow-red:"
            self.after(2000, self.running)
        elif self.state == "yellow-red":
            self.canvas.itemconfigure(self.red, fill=self.__collot)
            self.canvas.itemconfigure(self.yellow, fill='#808000')
            self.state = 'red-yellow'

            a = TfafficLight()
            a.mainloop()