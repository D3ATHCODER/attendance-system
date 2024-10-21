import tkinter as tk
from tkinter import messagebox
import admin_interface
import register_student
import take_attendance
import view_attendance

def login_window():
    def check_login():
        username = entry_user.get()
        password = entry_pass.get()
        
        if admin_interface.admin_login(username, password):
            messagebox.showinfo("Success", "Login successful!")
            login.destroy()
            main_interface()
        else:
            messagebox.showerror("Error", "Invalid login credentials")
    
    login = tk.Tk()
    login.title("Admin Login")
    
    tk.Label(login, text="Username:").grid(row=0)
    entry_user = tk.Entry(login)
    entry_user.grid(row=0, column=1)
    
    tk.Label(login, text="Password:").grid(row=1)
    entry_pass = tk.Entry(login, show="*")
    entry_pass.grid(row=1, column=1)
    
    tk.Button(login, text="Login", command=check_login).grid(row=2, column=1)
    
    login.mainloop()

def main_interface():
    root = tk.Tk()
    root.title("Face Recognition Attendance System")

    def register_student_interface():
        name = entry_name.get()
        roll_number = entry_roll.get()
        if name and roll_number:
            register_student.register_student(name, roll_number)
            messagebox.showinfo("Success", f"Student {name} registered successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter both name and roll number")

    def take_attendance_interface():
        take_attendance.take_attendance()
        messagebox.showinfo("Attendance", "Attendance process completed!")

    def view_attendance_interface():
        records = view_attendance.view_attendance()
        attendance_window = tk.Toplevel(root)
        attendance_window.title("Attendance Records")
        text_area = tk.Text(attendance_window, height=15, width=50)
        text_area.pack()
        for record in records:
            text_area.insert(tk.END, record + '\n')

    tk.Label(root, text="Enter Name:").grid(row=0, column=0)
    entry_name = tk.Entry(root)
    entry_name.grid(row=0, column=1)

    tk.Label(root, text="Enter Roll Number:").grid(row=1, column=0)
    entry_roll = tk.Entry(root)
    entry_roll.grid(row=1, column=1)

    tk.Button(root, text="Register Student", command=register_student_interface).grid(row=2, column=1)
    tk.Button(root, text="Take Attendance", command=take_attendance_interface).grid(row=3, column=1)
    tk.Button(root, text="View Attendance", command=view_attendance_interface).grid(row=4, column=1)

    root.mainloop()

if __name__ == "__main__":
    login_window()