import tkinter as tk
import tkinter.messagebox
import data_porcess as dao
import hashlib
import student_windows
import teacher_windows
import manager_windows


def MD5_demo(str):
    md = hashlib.md5()  # 创建md5对象
    md.update(str.encode(encoding='utf - 8'))
    return md.hexdigest()


def login():
    identity_var = int(identity.get())
    id = userE.get()
    password = passwordE.get()
    password = MD5_demo(password)
    print("passwordByH:" + password)
    tag, data = dao.login(id, password, identity_var)
    print("id", identity_var)
    print(tag, data)
    if tag == 1:
        windows.destroy()
        if identity_var == 0:
            manager_windows.manager_windows()
        elif identity_var == 1:
            student_windows.student_windows(data)
        else:
            data = dao.get_lesson_by_teacher_id(id)
            teacher_windows.teacher_windows(data)
    else:
        tk.messagebox.showerror("Error", "用户名、密码错误或用户不存在")


def register():
    register_windows = tk.Toplevel(master=windows)
    register_windows.title('Insert interface')
    register_windows.attributes("-alpha", 0.95, '-topmost', True)
    register_windows.geometry('600x400')
    entry2 = tk.Entry(register_windows, font=('Arial', 12))
    entry2.place(x=200, y=80)
    entry3 = tk.Entry(register_windows, font=('Arial', 12))
    entry3.place(x=200, y=110)
    entry4 = tk.Entry(register_windows, font=('Arial', 12))
    entry4.place(x=200, y=140)
    entry5 = tk.Entry(register_windows, font=('Arial', 12), show='*')
    entry5.place(x=200, y=170)
    entry6 = tk.Entry(register_windows, font=('Arial', 12))
    entry6.place(x=200, y=200)

    # Label
    label1 = tk.Label(register_windows, text='Choose ID ；')
    label1.place(x=50, y=50)
    label2 = tk.Label(register_windows, text='Class :')
    label2.place(x=50, y=80)
    label3 = tk.Label(register_windows, text='Name:')
    label3.place(x=50, y=110)
    label3 = tk.Label(register_windows, text='Id:')
    label3.place(x=50, y=140)
    label3 = tk.Label(register_windows, text='Password:')
    label3.place(x=50, y=170)
    label4 = tk.Label(register_windows, text='Lesson:')
    label4.place(x=50, y=200)
    # Radiobutton
    user_type_var = tk.StringVar()
    # student 1
    user_type_var.set(1)
    rad1 = tk.Radiobutton(register_windows, text='Student', variable=user_type_var, value=1, font=('Arial', 12), )
    rad1.place(x=200, y=50)
    rad2 = tk.Radiobutton(register_windows, text='Teacher', variable=user_type_var, value=2, font=('Arial', 12), )
    rad2.place(x=400, y=50)

    def update_command():
        user_type_int = user_type_var.get()
        class_name = entry2.get()
        name = entry3.get()
        id = entry4.get()
        password = entry5.get()
        print(password)
        password = MD5_demo(password)
        print(password)
        lesson = entry6.get()
        dao.register(username=name, id=id, classname=class_name, password=password, type=user_type_int, lesson=lesson)
        tk.messagebox.showinfo('register', "注册成功")
        register_windows.destroy()

    # Button
    button1 = tk.Button(register_windows, text='register',
                        command=update_command)
    button1.place(x=220, y=220)
    register_windows.mainloop()


if __name__ == '__main__':
    windows = tk.Tk()
    windows.attributes("-alpha", 0.8)
    windows.title('Student achievement management system')
    windows.geometry('1000x500')
    # Label
    tip1 = tkinter.Label(windows, text='Welcome to Student achievement management system', font=('Arial', 25)) \
        .place(x=100, y=50)
    tip2 = tkinter.Label(windows, text='User Id  :', font=('Arial', 15)).place(x=250, y=150)
    tip3 = tkinter.Label(windows, text='Password   :', font=('Arial', 15)).place(x=250, y=210)
    # Entry
    userE = tkinter.Entry(windows, font=('Arial', 14))
    userE.place(x=400, y=150)
    passwordE = tkinter.Entry(windows, show='*', font=('Arial', 14))
    passwordE.place(x=400, y=210)
    # Radiobutton
    identity = tkinter.StringVar()
    identity.set(1)
    tip5 = tkinter.Label(windows, text='Choose Identity :', font=('Arial', 12)).place(x=300, y=280)
    id1 = tkinter.Radiobutton(windows, text='Student', variable=identity, value=1, font=('Arial', 12)).place(x=450,
                                                                                                             y=280)
    id2 = tkinter.Radiobutton(windows, text='Teacher', variable=identity, value=2, font=('Arial', 12)).place(x=550,
                                                                                                             y=280)
    id3 = tkinter.Radiobutton(windows, text='Manager', variable=identity, value=0, font=('Arial', 12)).place(x=650,
                                                                                                             y=280)
    # login Button
    loginButton = tkinter.Button(windows, text='Login', font=('Arial', 20), command=login).place(x=400, y=350)
    # register Button
    registerButton = tkinter.Button(windows, text='register', font=('Arial', 20), command=register).place(x=500, y=350)
    # windows loop refresh
    windows.mainloop()
