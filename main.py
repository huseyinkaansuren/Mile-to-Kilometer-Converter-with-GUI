import tkinter

def miles_to_km():
    miles = float(mile_input.get())
    km= miles * 1.609
    km_result.config(text=f"{km}")

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=150)
window.maxsize(width=300,height=150)
window.config(padx=20,pady=20)

equal_label = tkinter.Label(text="is equal to", font=("Arial",13,"normal"))
equal_label.grid(column=0,row=1)
equal_label.config(padx=10)

mile_input = tkinter.Entry(width=10)
mile_input.insert(tkinter.END, string="0")
mile_input.grid(column=1, row=0)

km_result = tkinter.Label(text="0")
km_result.grid(column=1, row=1)
km_result.config(padx=10)

calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1,row=2)
calculate_button.config(padx=10)

mile_label = tkinter.Label(text="Miles", font=("Arial",13,"normal"))
mile_label.grid(column=2,row=0)
mile_label.config(padx=10)

km_label = tkinter.Label(text="Km", font=("Arial",13,"normal"))
km_label.grid(column=2,row=1)
km_label.config(padx=10)





window.mainloop()