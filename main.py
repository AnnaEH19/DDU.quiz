from tkinter import *

questions = ["Who is the Danish queen known for her love of horses and equestrianism?",
             "What is the name of the traditional Danish sweet bread, often served at Christmas and Easter?",
             "Who is the Danish footballer known as 'Lord Bendtner'?",
             "What is the name of the traditional Danish Christmas decoration made of woven hearts?",
             "Which Danish actor starred in the movie 'James Bond: Casino Royale'?",
             "Which Danish toy company is known for its colorful, interlocking building blocks?",
             "Slut"
             ]

correct_answers = ["Queen Margrethe 2", "Kringle", "Nicklas Bendtner",
                   "Julehjerte", "Mads Mikkelsen", "LEGO", "The end"]

first_option = ["Queen Elizabeth 2", "Rye bread", "Peter Schmeichel",
                "Julehjerte", "Nikolaj Coster-Waldau", "LEGO", "Fine"]

second_option = ["Queen Victoria", "Kringle", "Michael Laudrup",
                 "Julestjerne", "Viggo Mortensen", "Playmobil", "El fin"]

third_option = ["Queen Anne", "Cinnamon roll", "Nicklas Bendtner",
                "Julekugle", "Mads Mikkelsen", "Fisher-Price", "O fim"]

fourth_option = ["Queen Margrethe 2", "Croissant", "Christian Eriksen",
                 "Juletræ", "Lars Mikkelsen", "Hasbro", "Das ende"]

root = Tk()

root.geometry('260x560+0+0')
root.title('QUIZ - prototype')

root.config(bg='#E84A58')

dronning = PhotoImage(file='DRONNING.png')

dronningButton = Button(image=dronning, bg='#E84A58', activebackground='#E84A58', bd=0)
dronningButton.place(x=160, y=120)

tale2 = PhotoImage(file='TALE2.png')

tale2Button = Button(image=tale2, bg='#E84A58', activebackground='#E84A58', bd=0)
tale2Button.place(x=10, y=114)

tale1 = PhotoImage(file='TALE1.png')

tale1Button = Button(image=tale1, bg='#E84A58', activebackground='#E84A58', bd=0)
tale1Button.place(x=10, y=20)

SB = PhotoImage(file='SB.png')

Sback = Button(image=SB, bg='#E84A58', activebackground='#E84A58', bd=0, width=240, height=260)
Sback.place(x=10, y=280)

S = PhotoImage(file='S.png')

s1Button = Button(image=S, bg='#F1F2E4', activebackground='#F1F2E4', bd=0, width=200, height=40)
s1Button.place(x=30, y=300)

s2Button = Button(image=S, bg='#F1F2E4', activebackground='#F1F2E4', bd=0, width=200, height=40)
s2Button.place(x=30, y=360)

s3Button = Button(image=S, bg='#F1F2E4', activebackground='#F1F2E4', bd=0, width=200, height=40)
s3Button.place(x=30, y=420)

s4Button = Button(image=S, bg='#F1F2E4', activebackground='#F1F2E4', bd=0, width=200, height=40)
s4Button.place(x=30, y=480)

questionArea = Text(font=('brevia', 10, 'bold'), width=22, height=4, wrap='word', bg='#F0F1E3', bd=0)
questionArea.place(x=45, y=40)

questionArea.insert(END, questions[0])

sv1Button = Button(text=first_option[0], font=('brevia', 10, 'bold'), bg='#35C08F', bd=0,
                   activebackground='#35C08F', activeforeground='black', cursor='hand2')
sv1Button.place(x=55, y=310)

sv2Button = Button(text=second_option[0], font=('brevia', 10, 'bold'), bg='#35C08F', bd=0,
                   activebackground='#35C08F', activeforeground='black', cursor='hand2')
sv2Button.place(x=55, y=370)

sv3Button = Button(text=third_option[0], font=('brevia', 10, 'bold'), bg='#35C08F', bd=0,
                   activebackground='#35C08F', activeforeground='black', cursor='hand2')
sv3Button.place(x=55, y=430)

sv4Button = Button(text=fourth_option[0], font=('brevia', 10, 'bold'), bg='#35C08F', bd=0,
                   activebackground='#35C08F', activeforeground='black', cursor='hand2')
sv4Button.place(x=55, y=490)


def select(event):
    b = event.widget
    value = b['text']
    for i in range(7):
        if value == correct_answers[i]:
            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i+1])

            sv1Button.config(text=first_option[i+1])
            sv2Button.config(text=second_option[i+1])
            sv3Button.config(text=third_option[i+1])
            sv4Button.config(text=fourth_option[i+1])

            rigtig = Label(root, text='Correct answer:)   ', font=('brevia', 10, 'bold'), bg='#E84A58')
            rigtig.place(x=40, y=180)
            rigtig.after(2000, lambda: rigtig.destroy())

    if value not in correct_answers:
        wrong=Label(root, text='Wrong:( Try again.', font=('brevia', 10, 'bold'), bg='#E84A58')
        wrong.place(x=40, y=180)
        wrong.after(2000, lambda: wrong.destroy())


sv1Button.bind('<Button-1>', select)
sv2Button.bind('<Button-1>', select)
sv3Button.bind('<Button-1>', select)
sv4Button.bind('<Button-1>', select)

root.mainloop()