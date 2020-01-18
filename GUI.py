import tkinter


class App():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Системы счисления')
        exiter = tkinter.Button(self.root, text = 'Выход', command=self.quit)
        start = tkinter.Button(self.root, text = 'Начать тест', command=self.start)
        welcome_label = tkinter.Label(self.root, text = 'Добро пожаловать. Введите своё имя и нажмите "Начать тест"')
        welcome_label.pack()
        global text1
        text1=tkinter.Text(self.root,width=7, heigh=2,font='Arial 14')
        text1.pack()
        start.pack()
        exiter.pack()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()
    def start(self):
        name=text1.get('1.0')
        print(name)
        self.quit()
        import testor_GUI

app = App()
