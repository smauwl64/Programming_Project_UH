import customtkinter as cus

def button_pressed():
    print("entalla")

app = cus.CTk()
app.title("testing")
app.geometry("400x150")
app.grid_columnconfigure(0, weight=1)

button = cus.CTkButton(app, text="averaver", command=button_pressed)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

app.mainloop()


