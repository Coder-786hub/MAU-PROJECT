
from tkinter import * 
import joblib

model = joblib.load("Salary_predicter.joblib")

def predicter():
    input_ = float(input_entry.get())
    print(type(input_))
    predicted_value = model.predict([[input_]])

    output_.config(text = f"The predicted salary = {str(predicted_value)[1:10]}")
    




app = Tk()
app.geometry("700x500")
app.title("Salary Predicter")
app.config(bg = "green")

heading = Label(app, text = "SALARY PREDICTER", font = "robot 35 italic", fg = "blue", bg = "green")
heading.pack(fill = "x", pady = 20)

input_label = Label(app, text = "Enter your Year of Experience", fg = "red", bg = "green", font = "arial 20 bold")
input_label.pack(pady = 20)

input_entry = Entry(app, font = "arial 20 bold", justify = "center")
input_entry.pack(pady = 10)

btn = Button(app, text = "Predicter", fg = "red", bg = "blue", font = "robot 25 bold", command = predicter)
btn.pack(pady = 10)

output_ = Label(app, fg = "red", font = "arial 18 bold", bg = "green")
output_.pack()

app.mainloop()
