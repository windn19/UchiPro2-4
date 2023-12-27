from tkinter import Tk, Button, Entry, Label


def action():
    label['text'] = f'Привет, {entry.get()}!'


root = Tk()
root.geometry('400x100')
root.title('Hello!!!')

label = Label(text='Как тебя зовут?')
entry = Entry()
button = Button(text='Нажми меня!', command=action)
#
label.place(x=150, y=10)
entry.place(x=130, y=30)
button.place(x=150, y=60)

root.mainloop()
