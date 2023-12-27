# Напиши программу для вычисления индекса массы тела (ИМТ), используя Tkinter.
# Пользователь вводит рост (в см), вес (в кг) и нажимает кнопку Рассчитать ИМТ. Программа выводит ИМТ, с точностью
# до двух знаков после запятой.

from tkinter import Tk, Button, Label, Entry


def action():
    imt = int(weight_input.get()) / (int(height_input.get()) / 100) ** 2
    imt_label['text'] = f'Ваш ИМТ: {imt:.2f}'


root = Tk()
root.geometry('400x100+500+100')
root.title('Hello!!!')

height_label = Label(text='Введите ваш рост в см.')
height_input = Entry()
weight_label = Label(text='Введите ваш вес в кг.')
weight_input = Entry()
imt_label = Label(text='Ваш ИМТ:')
button = Button(text='Рассчитать ИМТ', command=action)

height_label.place(x=20, y=20)
height_input.place(x=200, y=20)
weight_label.place(x=20, y=40)
weight_input.place(x=200, y=40)
button.place(x=20, y=60)
imt_label.place(x=200, y=60)

root.mainloop()
