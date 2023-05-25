import json

from tkinter import *


root = Tk()

lbl = Label(text='Введите текст задания')
text = Entry(root, width=50)

lbl1 = Label(text="Правильный ответ:")
inp1 = Entry()

lbl2 = Label(text='Ответ 2:')
inp2 = Entry()

answers = [inp1, inp2]
lbls = []

lbl.pack()
text.pack()

lbl1.pack()
inp1.pack()

lbl2.pack()
inp2.pack()


def add_ans():
    global ans_id
    global btadd
    global btrem
    global btready

    lbl3 = Label(text=f'Ответ {len(lbls)+3}')
    inp = Entry()
    
    lbls.append(lbl3)
    answers.append(inp)

    lbl3.pack()
    inp.pack()

    
    btadd.destroy()
    btadd = Button(text="Добавить кнопку", command=add_ans)
    btadd.pack()
    
    btrem.destroy()
    btrem = Button(text="Удалить ответ", command=remove_ans)
    btrem.pack()
    
    btready.destroy()
    btready = Button(text='Готово', command=ready)
    btready.pack()
    

def remove_ans():
    if not len(lbls):
        return
    
    l = lbls.pop(-1)
    b = answers.pop(-1)
    
    l.destroy()
    b.destroy()
    


def ready():
    anss = []
    for a in answers:
        t = a.get()
        print(t)
        if len(t.strip()) == 0:
            return
        anss.append(t)
        
    with open('tasks.json') as file:
        j = json.load(file) or []
        
    
    question = {'text': text.get(), 'answers': anss}
    j.append(question)
    
    print(j)
    
    with open('tasks.json', 'w') as file:
        j = json.dump(j, file)
        
    
    for l in lbls:
        b = answers.pop(-1)
        b.destroy()
        l.destroy()
        
    lbls.clear()
                
         
btadd = Button(text="Добавить ответ", command=add_ans)
btadd.pack()

btrem = Button(text="Удалить ответ", command=remove_ans)
btrem.pack()

btready = Button(text='Готово', command=ready)
btready.pack()

root.mainloop()