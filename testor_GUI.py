#testor_GUI
import question_generator
import tkinter

from random import randint as rint
from random import choice

from os import getcwd
path=getcwd()

#тут мы случайно выбираем операцию с числами и числа в задании
#и генерируем список по схеме:
#numbers=[a,b,base_a, base_b, result, base_result]
op=choice(['+','-'])
b=rint(20,100)
#меня пугала херня, что ответ может быть отрицательным
#и это вызывает ошибку, так что теперь только положительный
lis=[rint(b,150),b,rint(2,10),rint(2,10)]

if op=='+':
    res=lis[0]+lis[1]
if op=='-':
    res=lis[0]-lis[1]

lis.append(res)
lis.append(rint(2,10))

class Window():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("250x250+0+0")
        self.root.title('Тест')
        exiter = tkinter.Button(self.root, text = 'Завершить тест', command=self.quit)
        global entry_string
        entry_string = tkinter.StringVar()
        self.answer_entry=tkinter.Entry(self.root,textvariable=entry_string)
        ans_check=tkinter.Button(self.root, text = 'Ответить', command=self.next)
        self.question_label = tkinter.Label(self.root, text = question_generator.numsys2_10(lis, op)[0])
        self.question_label.pack(side='top')
        self.answer_entry.pack(side='top')
        ans_check.pack(side='right')
        exiter.pack(side='left')
        self.root.mainloop()
    def next(self):
        global op, b, lis, res

        f=open(path+'//results.txt','a')
        f.write('''
 '''+str(lis)+' '+op+'  Answer: '+ entry_string.get()+ str(str(res)==entry_string.get()))
        f.close()
        op = choice(['+', '-'])
        b = rint(20, 100)
        lis = [rint(b, 150), b, rint(2, 10), rint(2, 10)]

        if op == '+':
            res = lis[0] + lis[1]
        if op == '-':
            res = lis[0] - lis[1]

        lis.append(res)
        lis.append(rint(2, 10))
        self.answer_entry.delete(0, 'end')
        self.question_label.configure(text=question_generator.numsys2_10(lis, op)[0])
        #тест залуплен сам на себе, но это не баг, а фича.
    def quit(self):
        self.root.destroy()
    #Вот этот кусок кода с классами спизжен из инета.
    #может быть, тут эта ошибка

window = Window()
