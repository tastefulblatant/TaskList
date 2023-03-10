from tkinter import *
import customtkinter


window = customtkinter.CTk()
window.title("Seznam úkolů")
window.geometry("650x430 ")
window.resizable(False,False)
customtkinter.set_appearance_mode("Dark")

main_font = ("Arial", "12")
button_color = "#ffaf44"

#Functions
def add_text():
    list_box.insert(END, user_input.get())
    user_input.delete(0, END)

def delete_text_item():
    list_box.delete(ANCHOR)

def clear_all_text():
    list_box.delete(0, END)

def save():
    with open("task.txt", "w") as file:
        tasks = list_box.get(0, END)
        for one_task in tasks:
            file.write(f"{one_task}\n")

def open_tasks():
    try:
        with open("task.txt", "r") as file:
            for one_line in file:
                list_box.insert(END, one_line)
    except:
        print("Chyba ve funkci otevirani souboru task.txt")

input_frame = customtkinter.CTkFrame(window)
text_frame = customtkinter.CTkFrame(window)
button_frame = customtkinter.CTkFrame(window)
input_frame.pack(pady=5)
text_frame.pack(pady=5)
button_frame.pack(pady=5)

#Input_frame
user_input = customtkinter.CTkEntry(input_frame, width=400)
add_button = customtkinter.CTkButton(input_frame, text="Add", border_width=2, command=add_text)

user_input.grid(row=0,column=0, padx=5,pady=5)
add_button.grid(row=0, column=1, padx=5, pady=5)

text_scrollbar = customtkinter.CTkScrollbar(text_frame)

#Text_frame
list_box = Listbox(text_frame, width=60, height=15, borderwidth=2, font=main_font, yscrollcommand=text_scrollbar.set)
list_box.grid(row=0, column=0)
text_scrollbar.grid(row=0, column=1, sticky=NS) 



#Button_frame
remove_button = customtkinter.CTkButton(button_frame, text="Remove", command=delete_text_item, border_width=2)
clear_button = customtkinter.CTkButton(button_frame, text="Clear", command=clear_all_text, border_width=2)
save_button = customtkinter.CTkButton(button_frame, text="Save", command=save, border_width=2)
quit_button = customtkinter.CTkButton(button_frame, text="Quit", command=window.destroy, border_width=2)

remove_button.grid(row=0, column=0, padx=2, pady=10, ipadx=8)
clear_button.grid(row=0, column=1, padx=2, pady=10, ipadx=8)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=8)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=8)

open_tasks()

window.mainloop()