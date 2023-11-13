from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300 ,height=100)

def miles_to_km():
    try:
        miles = float(label_entry.get())
        km = round(miles * 1.609, 2)  # Use float conversion and round to 2 decimal places
        label2.config(text=f"{km} Km")
    except ValueError:
        label2.config(text="Invalid input")

label_entry = Entry()
label_entry.grid(column=2, row=1)


label = Label(text='Miles')
label1  = Label(text='is equal to')
label2 = Label(text='Km')



label.grid(column=1,row=1)
label1.grid(column=3,row=1)
label2.grid(column=2,row=2)


button = Button(text='calculate',command=miles_to_km)
button.grid(column=2,row=3)


window.mainloop()