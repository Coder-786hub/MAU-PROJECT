from tkinter import *
app = Tk()
app.geometry("1200x700")
app.config(bg = "#B1EFF2")

frame1 = LabelFrame(app, text = "Details", fg = "red", bg = "#CFE3C7", font = "arial 18 bold", width = 580, height = 400)
frame1.place(x = 10, y = 10)

name_label = Label(frame1, text = "Full Name", font = "arial 16 bold", bg = "#CFE3C7")
name_label.place(x = 10, y = 20)

father_entry = Entry(frame1, font = "arial 16 bold")
father_entry.place(x = 160, y = 20)

name_label = Label(frame1, text = "Father Name", font = "arial 16 bold", bg = "#CFE3C7")
name_label.place(x = 10, y = 60)

father_entry = Entry(frame1, font = "arial 16 bold")
father_entry.place(x = 160, y = 60)

mother_label = Label(frame1, text = "Mother Name", font = "arial 16 bold", bg = "#CFE3C7")
mother_label.place(x = 10, y = 100)

mother_entry = Entry(frame1, font = "arial 16 bold")
mother_entry.place(x = 160, y = 100)

frame2 = LabelFrame(app, text = "Contact", fg = "red", bg = "white", font = "arial 18 bold", width = 580, height = 400)
frame2.place(x = 600, y = 10)

app.mainloop()