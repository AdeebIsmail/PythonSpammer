import time
from tkinter import *
from tkinter import messagebox

from pynput.keyboard import Key, Controller


def spam(string, how_long, pause, one_word_at_a_time):
    keyboard = Controller()
    word = string + ' '
    end_time = time.time() + 60 * how_long
    time.sleep(5)
    while time.time() <= end_time:
        if one_word_at_a_time:
            for letter in word:
                keyboard.type(letter)
                time.sleep(pause)
                if letter == " ":
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
        else:
            keyboard.type(word)
            time.sleep(pause)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)


def start_button():
    send_one_word = False

    if one_word_at_a_time_msg.get() == "True" or one_word_at_a_time_msg.get() == "true":
        send_one_word = True

    if spam_msg.get() == " " or time_msg.get() == 0.0 or pause_msg.get() == 0.0:
        messagebox.showerror("Error", "Missing Fields")
    else:
        spam(spam_msg.get(), time_msg.get(), pause_msg.get(), send_one_word)


window = Tk()
window.title("Spammer text")
window.geometry('500x300')

spam_msg = StringVar()
time_msg = DoubleVar()
pause_msg = DoubleVar()
one_word_at_a_time_msg = StringVar()

time_msg.set(2)
pause_msg.set(.9)
one_word_at_a_time_msg.set("False")

btn_start = Button(window,
                   text='Start',
                   width=25,
                   height=5,
                   bg="grey",
                   borderwidth=0,
                   command=start_button
                   )
btn_start.place(x=0, y=215)

btn_stop = Button(window,
                  text='Stop',
                  width=25,
                  height=5,
                  bg="grey",
                  borderwidth=0,
                  command=window.destroy
                  )
btn_stop.place(x=320, y=215)

text_spam = Entry(window,
                  textvariable=spam_msg
                  )
text_spam.place(x=0, y=25)

how_long_spam = Entry(window,
                      textvariable=time_msg
                      )
how_long_spam.place(x=0, y=75)

pause_spam = Entry(window,
                   textvariable=pause_msg
                   )
pause_spam.place(x=0, y=125)

is_space = Entry(window,
                 textvariable=one_word_at_a_time_msg
                 )
is_space.place(x=0, y=175)

script_label = Label(window,
                     text="Script"
                     )
script_label.place(x=100, y=25)

how_long_label = Label(window,
                       text="Message timer"
                       )
how_long_label.place(x=100, y=75)

pause_label = Label(window,
                    text="How long between words being sent")
pause_label.place(x=100, y=125)

is_space_label = Label(window,
                       text="True if you want to send words one at a time")
is_space_label.place(x=100, y=175)

window.mainloop()
