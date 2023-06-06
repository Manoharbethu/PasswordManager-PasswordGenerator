import tkinter as tk
import random
import string
import csv
from tkinter import messagebox
from tkinter import *

root = tk.Tk()
root.title("Password Generator")
root.geometry("600x600")
root.configure(bg="#2E86C1")

#Adding photo 
photo1 = PhotoImage(file = "image1.png")
#Adding photo
photo2 = PhotoImage(file = "image2.png")
    
#This function created for newwindow1    
def new_window_gp():
    #window1 is created for opening another window
    window1 = tk.Tk()
    window1.title("Password Generator")
    window1.geometry("600x600")
    window1.configure(bg="#5499C7")
    
    #Label1 and Entry1 for length label and entry box
    label1 = tk.Label(
        window1, text="Length:", font='Arial', bg="#5499C7", fg='white')
    label1.place(x=275, y=40)
    entry1 = tk.Entry(window1, width=50)
    entry1.place(x=157, y=80)

    #Label2 and Entry2 for Passoword label and textbox
    label2 = tk.Label(window1, text="Password:", font='Arial', bg="#5499C7", fg='white')
    label2.place(x=265, y=120)
    text_box1 = tk.Text(window1, width=46)
    text_box1.place(x=125, y=160)

    #This function created for generating password
    def generate_password():
        #Exception Handling
        try:
            length = int(entry1.get())
        except ValueError:
            #If we didn't type any length it will popups the error and prints the 
            #above statement
            messagebox.showinfo("status","Please enter the length of password")
            return
        
        "Random generation of password that includes all the uppercase, lowercase, punctuation, digits will suggests a strong password"
        password = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
        text_box1.insert(tk.END, password + '\n')
    
    #Button for clicking generate password
    button = tk.Button(window1, text="Generate Password", command=generate_password, font=('Arial', 10), width=15, height=1, bg='#1B4F72', fg='white')
    button.place(x=258, y=560)
    
#This function created for newwindow2    
def new_window_pm():
    #window1 is created for opening another window
    window2 = tk.Tk()
    window2.title("Password Manage")
    window2.geometry("600x600")
    window2.configure(bg='#5499C7')
    
    #Label3 and Entry2 for Username label and entry box
    label3 = tk.Label(window2, text="Username: ", font='Arial', bg='#5499C7', fg='white')
    label3.place(x=120, y=200)
    entry2 = tk.Entry(window2)
    entry2.place(x=250, y=198, width=200, height=30)

    #Label4 and Entry3 for Password label and entry box
    label4 = tk.Label(window2, text="Password: ", font='Arial', bg='#5499C7', fg='white')
    label4.place(x=120, y=260)
    entry3 = tk.Entry(window2)
    entry3.place(x=250, y=258, width=200, height=30)
    
    #Label5 is small note
    label5 = tk.Label(window2, text="*The password you save here will be automatically saved to the CSV file*", bg='#5499C7', fg='white')
    label5.place(x=108, y=370)
    
    #This function is created for saving data to the csv file
    def save_data():
        username = entry2.get()
        password = entry3.get()
      
        "with the below logic the written data is saved into the csv file and permanently saved"
        with open('File.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        
        messagebox.showinfo("status", "Username and Password successfully saved")
        
        #This deletes all the entered data after we click on save button
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        
    #Button1 for Saving password
    button1 = tk.Button(window2, text="Save", command=save_data, bg='#1B4F72', fg='white', width=10, height=1, font=('Arial', 10))
    button1.place(x=260, y=310)
    
#Button2 for Clicking password generator option
button2=tk.Button(root, image=photo1, command=new_window_gp, height=150, width=200, bg='#3498DB')
button2.place(x=205, y=100)

#Button3 for clicking password manager option
button3=tk.Button(root, image=photo2, command=new_window_pm, height=150, width=200, bg='#3498DB')
button3.place(x=205, y=300)

root.mainloop()