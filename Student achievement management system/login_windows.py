import tkinter as tk
import tkinter.messagebox
import data_porcess as dao
import student_windows
import teacher_windows
import manager_windows
from PIL import Image, ImageTk


def login():
    identity_var = int(identity.get())
    id = userE.get()
    password = passwordE.get()
    password = dao.MD5_demo(password)
    tag, data = dao.login(id, password, identity_var)
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


def register(windows):
    register_windows = tk.Toplevel(master=windows)
    register_windows.title('注册用户')
    register_windows.attributes("-alpha", 0.95, '-topmost', True)
    register_windows.geometry('600x400')
    entry2 = tk.Entry(register_windows, font=('Arial', 15))
    entry2.place(x=300, y=100)
    entry3 = tk.Entry(register_windows, font=('Arial', 15))
    entry3.place(x=300, y=150)
    entry4 = tk.Entry(register_windows, font=('Arial', 15))
    entry4.place(x=300, y=200)
    entry5 = tk.Entry(register_windows, font=('Arial', 15), show='*')
    entry5.place(x=300, y=250)
    entry6 = tk.Entry(register_windows, font=('Arial', 15))
    entry6.place(x=300, y=300)

    # Label
    label1 = tk.Label(register_windows, text='选择要注册的身份类型 ；',font=('Arial', 15))
    label1.place(x=50, y=50)
    label2 = tk.Label(register_windows, text='班级（授课班级） :',font=('Arial', 15))
    label2.place(x=50, y=100)
    label3 = tk.Label(register_windows, text='姓名:',font=('Arial', 15))
    label3.place(x=50, y=150)
    label3 = tk.Label(register_windows, text='学号（教工号）:',font=('Arial', 15))
    label3.place(x=50, y=200)
    label3 = tk.Label(register_windows, text='密码:',font=('Arial', 15))
    label3.place(x=50, y=250)
    label4 = tk.Label(register_windows, text='授课课程（学生不必填写）:',font=('Arial', 15))
    label4.place(x=50, y=300)
    # Radiobutton
    user_type_var = tk.StringVar()
    # student 1
    user_type_var.set(1)
    rad1 = tk.Radiobutton(register_windows, text='学生', variable=user_type_var, value=1, font=('Arial', 12), )
    rad1.place(x=300, y=50)
    rad2 = tk.Radiobutton(register_windows, text='教师', variable=user_type_var, value=2, font=('Arial', 12), )
    rad2.place(x=400, y=50)

    def update_command():
        user_type_int = user_type_var.get()
        class_name = entry2.get()
        name = entry3.get()
        id = entry4.get()
        password = entry5.get()
        password = dao.MD5_demo(password)
        lesson = entry6.get()
        dao.register(username=name, id=id, classname=class_name, password=password, type=user_type_int, lesson=lesson)
        tk.messagebox.showinfo('注册', "注册成功")
        register_windows.destroy()

    # Button
    button1 = tk.Button(register_windows, text='注册',
                        command=update_command,font=('Arial', 15))
    button1.place(x=220, y=350)
    register_windows.mainloop()


if __name__ == '__main__':
    windows = tk.Tk()
    # 设置透明度
    windows.attributes("-alpha", 1)
    windows.title('XXXXXXXX学校学生成绩管理系统')

    # 设置背景图片
    # image_file = Image.open('30.jpg')
    # photo = ImageTk.PhotoImage(image_file)
    # canvas = tk.Canvas(windows, width=1200, height=700, bd=0, highlightthickness=0)
    # canvas.create_image(700, 500, image=photo)
    # canvas.pack()

    windows.geometry('1000x500')
    # Label
    tip1 = tkinter.Label(windows, text='欢迎使用XXXX学校学生成绩管理系统', font=('Arial', 25)) \
        .place(x=200, y=50)
    tip2 = tkinter.Label(windows, text='学号或教工号 :', font=('Arial', 15)).place(x=250, y=150)
    tip3 = tkinter.Label(windows, text='密码 :', font=('Arial', 15)).place(x=250, y=210)
    # Entry
    userE = tkinter.Entry(windows, font=('Arial', 14))
    userE.place(x=400, y=150)
    passwordE = tkinter.Entry(windows, show='*', font=('Arial', 14))
    passwordE.place(x=400, y=210)
    # Radiobutton
    identity = tkinter.StringVar()
    identity.set(1)
    tip5 = tkinter.Label(windows, text='选择登陆身份 :', font=('Arial', 12)).place(x=220, y=280)
    id1 = tkinter.Radiobutton(windows, text='学生', variable=identity, value=1, font=('Arial', 12)).place(x=400,
                                                                                                             y=280)
    id2 = tkinter.Radiobutton(windows, text='教师', variable=identity, value=2, font=('Arial', 12)).place(x=500,
                                                                                                             y=280)
    id3 = tkinter.Radiobutton(windows, text='管理员', variable=identity, value=0, font=('Arial', 12)).place(x=600,
                                                                                                             y=280)
    # login Button
    loginButton = tkinter.Button(windows, text='登陆', font=('Arial', 20), command=login).place(x=400, y=350)
    # register Button
    registerButton = tkinter.Button(windows, text='注册', font=('Arial', 20),
                                    command=lambda: register(windows)).place(x=500, y=350)
    # windows loop refresh
    windows.mainloop()
