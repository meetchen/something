import tkinter as tk
import data_porcess as dao
from tkinter import ttk
import login_windows
import os

def student_windows(data):
    student_windows = tk.Tk()
    student_windows.attributes("-alpha", 1)
    student_windows.title('XXXXXXXX学校学生成绩管理系统')
    student_windows.geometry('1000x500')
    tip1 = tk.Label(student_windows, text=data[0], font=('Arial', 25)).place(x=100, y=50)
    tip2 = tk.Label(student_windows, text=data[1], font=('Arial', 25)).place(x=100, y=150)
    tip3 = tk.Label(student_windows, text=data[2], font=('Arial', 25)).place(x=100, y=250)
    scores = dao.get_score_by_id(data[1])
    style = ttk.Style()

    def fixed_map(option):
        # Returns the style map for 'option' with any styles starting with
        # ("!disabled", "!selected", ...) filtered out

        # style.map() returns an empty list for missing options, so this should
        # be future-safe
        return [elm for elm in style.map("Treeview", query_opt=option)
                if elm[:2] != ("!disabled", "!selected")]

    style.map("Treeview",
              foreground=fixed_map("foreground"),
              background=fixed_map("background"))
    tree = ttk.Treeview(student_windows, columns=['1', '2'], show='headings')
    style.configure("Treeview", font=(None, 15), rowheight=int(25))
    tree.column('1', width=100, anchor='sw')
    tree.column('2', width=100, anchor='sw')
    tree.heading('1', text='课程')
    tree.heading('2', text='成绩')
    tree.tag_configure('evenColor', background='red')
    for i in scores:
        if int(i[1]) < 60:
            tree.insert('', 'end', values=i, tags=("evenColor",))
        else:
            tree.insert('', 'end', values=i, )
    tree.place(x=350, y=50)

    def back_index(win):
        student_windows.destroy()
        os.system('python login_windows.py')

    tk.Button(student_windows, text=' 退出', font=('Arial', 15), command=lambda: back_index(student_windows)).place(
        x=850, y=420)

    student_windows.mainloop()


if __name__ == '__main__':
    student_windows(('张三', 123456, '高三（1）班'))
