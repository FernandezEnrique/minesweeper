import PIL
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

class Menu:
    def __init__(self, caption, msg, btn1, btn2, btn3, btn4):
        self.win = Tk()
        self.win.title(caption)
        self.win.geometry(f"450x550")
        self.win.config(bg="cornsilk4") 
        self.win.resizable(0,0)
        self.selection = None
        #self.win.iconbitmap('img/icono.ico')

        self.opc1 = btn1
        self.opc2 = btn2
        self.opc3 = btn3
        self.opc4 = btn4
        
        #image = Image.open("img/game-img.png")
        #image = image.resize((200,200), Image.ANTIALIAS)
        #img = ImageTk.PhotoImage(image)

        font_button = font.Font(family='Tahoma', size=16)

        Label(self.win, text=msg, font=font_button, bg="cornsilk3", fg="black").pack(pady=20)
        opc1_button = Button(self.win, text = btn1, font = font_button, bg="cornsilk3", fg="black", command=self.option1).pack(pady=20)
        opc2_button = Button(self.win, text = btn2, font = font_button, bg="cornsilk3", fg="black", command = self.option2).pack(pady=20)
        opc3_button = Button(self.win, text = btn3, font = font_button, bg="cornsilk3", fg="black", command = self.option3).pack(pady=20)
        opc4_button = Button(self.win, text = btn4, font = font_button, bg="cornsilk3", fg="black", command = self.option3).pack(pady=20)


        #lbl_img = Label(self.win, image = img)
        #lbl_img.pack()

        self.screen_width = self.win.winfo_screenwidth()
        self.screen_height = self.win.winfo_screenheight()
        self.x_coordinate = int((self.screen_width/2) - (450/2))
        self.y_coordinate = int((self.screen_height/2) - (550/2))
        self.win.geometry("{}x{}+{}+{}".format(450, 550, self.x_coordinate, self.y_coordinate))

        
        self.win.mainloop()
    
    def option1(self):
        self.selection = self.opc1
        self.win.destroy()
        return self.opc1


    def option2(self):
        self.selection = self.opc2
        self.win.destroy()
        return self.opc2
    
    def option3(self):
        self.selection = self.opc3
        self.win.destroy()
        return self.opc3
    
    def option4(self):
        self.selection = self.opc4
        self.win.destroy()
        return self.opc4