import tkinter as tk
import data_porcess as dao
from tkinter import ttk
import tkinter.messagebox
import os


def manager_windows():
    manager_windows = tk.Tk()
    manager_windows.attributes("-alpha", 1)
    manager_windows.title('XXXX学校学生成绩管理系统')
    manager_windows.geometry('1000x500')

    tk.Label(manager_windows, text='姓名', font=('Arial', 10)).place(x=20, y=90)
    s_name = tk.Entry(manager_windows, font=('Arial', 10), width=10)
    s_name.place(x=60, y=90)
    tk.Button(manager_windows, text='查询', font=('Arial', 10), command=lambda: select(1)).place(x=140, y=90)

    tk.Label(manager_windows, text='学号', font=('Arial', 10)).place(x=220, y=90)
    s_id = tk.Entry(manager_windows, font=('Arial', 10), width=10)
    s_id.place(x=260, y=90)
    tk.Button(manager_windows, text='查询', font=('Arial', 10), command=lambda: select(2)).place(x=340, y=90)

    tk.Label(manager_windows, text='姓名', font=('Arial', 10)).place(x=520, y=90)
    t_name = tk.Entry(manager_windows, font=('Arial', 10), width=10)
    t_name.place(x=560, y=90)
    tk.Button(manager_windows, text='查询', font=('Arial', 10), command=lambda: select(3)).place(x=640, y=90)

    tk.Label(manager_windows, text='教工号', font=('Arial', 10)).place(x=720, y=90)
    t_id = tk.Entry(manager_windows, font=('Arial', 10), width=10)
    t_id.place(x=780, y=90)
    tk.Button(manager_windows, text='查询', font=('Arial', 10), command=lambda: select(4)).place(x=840, y=90)

    def select(num):
        if num == 1:
            name = s_name.get()
            student_list = dao.find_like('username', name, 1)
            tk.messagebox.showinfo('结果', student_list)
            score_windows(student_list)
        elif num == 2:
            student_id = s_id.get()
            student_list = dao.find_like('id', student_id, 1)
            tk.messagebox.showinfo('结果', student_list)

        elif num == 3:
            teacher_name = t_name.get()
            teacher_list = dao.find_like('username', teacher_name, 2)
            tk.messagebox.showinfo('结果', teacher_list)

        else:
            teacher_id = t_id.get()
            teacher_list = dao.find_like('id', teacher_id, 2)
            tk.messagebox.showinfo('结果', teacher_list)

    tk.Label(manager_windows, text='学生', font=('Arial', 25)).place(x=100, y=40)
    tk.Label(manager_windows, text='教师', font=('Arial', 25)).place(x=700, y=40)

    # tree
    style = ttk.Style()

    def fixed_map(option):
        return [elm for elm in style.map("Treeview", query_opt=option)
                if elm[:2] != ("!disabled", "!selected")]

    style.map("Treeview",
              foreground=fixed_map("foreground"),
              background=fixed_map("background"))
    tree = ttk.Treeview(manager_windows, columns=['1', '2', '3'], show='headings')

    def set_cell_value(event):  # 双击进入编辑状态
        for item in tree.selection():
            item_text = tree.item(item, "values")
        column = tree.identify_column(event.x)  # 列
        row = tree.identify_row(event.y)  # 行
        cn = int(str(column).replace('#', ''))
        rn = int(str(row).replace('I', ''))
        entryedit = tk.Text(manager_windows, width=20, height=1)
        entryedit.place(x=500, y=20)

        def saveedit():
            tree.set(item, column=column, value=entryedit.get(0.0, "end"))
            print(tree.item(item, 'values'))
            dao.update_score(tree.item(item, 'values'))
            entryedit.destroy()
            okb.destroy()
            okb1.destroy()

        def cancer():
            entryedit.destroy()
            okb.destroy()
            okb1.destroy()

        okb = ttk.Button(manager_windows, text='OK', width=8, command=saveedit)
        okb1 = ttk.Button(manager_windows, text='Cancer', width=8, command=cancer)
        okb.place(x=650, y=20)
        okb1.place(x=750, y=20)

    # 双击事件
    style.configure("Treeview", font=(None, 15), rowheight=int(25))
    tree.column('1', width=100, anchor='center')
    tree.column('2', width=100, anchor='center')
    tree.column('3', width=150, anchor='center')
    tree.heading('1', text='姓名')
    tree.heading('2', text='学号')
    tree.heading('3', text='班级')
    students = dao.find_all_students()
    for i in students:
        tree.insert('', 'end', values=i, )
    tree.place(x=30, y=120)

    def delete_tree1():
        curltem = tree.focus()
        item = tree.item(curltem)['values']
        flag = tk.messagebox.askyesno('提示', '要删除' + item[0] + '同学的信息吗？')
        if flag:
            dao.delete_user(item[1], True)
            tree.delete(curltem)
            tk.messagebox.showinfo('提示', '删除成功')

    tk.Button(manager_windows, text='删除学生信息', font=('Arial', 15), command=delete_tree1).place(x=150, y=420)

    # lesson tree
    score_tree = ttk.Treeview(manager_windows, columns=['1', '2', '3', '4'], show='headings')

    def set_cell_value1(event):  # 双击进入编辑状态
        for item in score_tree.selection():
            item_text = score_tree.item(item, "values")
        column = score_tree.identify_column(event.x)  # 列
        row = score_tree.identify_row(event.y)  # 行
        cn = int(str(column).replace('#', ''))
        rn = int(str(row).replace('I', ''))
        entryedit = tk.Text(manager_windows, width=20, height=1)
        entryedit.place(x=500, y=20)

        def saveedit():
            score_tree.set(item, column=column, value=entryedit.get(0.0, "end"))
            dao.update_lesson(score_tree.item(item, 'values'))
            entryedit.destroy()
            okb.destroy()
            okb1.destroy()

        def cancer():
            entryedit.destroy()
            okb.destroy()
            okb1.destroy()

        okb = ttk.Button(manager_windows, text='OK', width=8, command=saveedit)
        okb1 = ttk.Button(manager_windows, text='Cancer', width=8, command=cancer)
        okb.place(x=650, y=20)
        okb1.place(x=750, y=20)

    score_tree.bind('<Double-1>', set_cell_value1)
    style.configure("Treeview", font=(None, 15), rowheight=int(25))
    score_tree.column('1', width=100, anchor='center')
    score_tree.column('2', width=150, anchor='center')
    score_tree.column('3', width=100, anchor='center')
    score_tree.column('4', width=100, anchor='center')
    score_tree.heading('1', text='教工号')
    score_tree.heading('2', text='授课班级')
    score_tree.heading('3', text='教工姓名')
    score_tree.heading('4', text='所授课程')
    score_tree.tag_configure('evenColor', background='red')
    lesson = dao.fina_all_teacher_info()
    for i in lesson:
        score_tree.insert('', 'end', values=i, )
    score_tree.place(x=500, y=120)

    def delete_tree2():
        curltem = score_tree.focus()
        item = score_tree.item(curltem)['values']
        flag = tk.messagebox.askyesno('提示', '要删除' + item[2] + '老师吗')
        if flag:
            dao.delete_lesson(item[0], lesson=item[3])
            score_tree.delete(curltem)
            tk.messagebox.showinfo('提示', '已删除')

    tk.Button(manager_windows, text='删除教工信息', font=('Arial', 15), command=delete_tree2).place(x=700, y=420)

    def back_index(win):
        win.destroy()
        os.system('python login_windows.py')

    tk.Button(manager_windows, text='退出', font=('Arial', 15), command=lambda: back_index(manager_windows)).place(
        x=850, y=420)
    manager_windows.mainloop()


def score_windows(students):
    score_window = tk.Tk()
    score_window.attributes("-alpha", 1)
    score_window.title('Student achievement management system')
    score_window.geometry('1000x500')
    style = ttk.Style()

    def fixed_map(option):
        return [elm for elm in style.map("Treeview", query_opt=option)
                if elm[:2] != ("!disabled", "!selected")]

    style.map("Treeview",
              foreground=fixed_map("foreground"),
              background=fixed_map("background"))

    def set_cell_value(event):  # 双击进入编辑状态
        for item in tree.selection():
            item_text = tree.item(item, "values")
        column = tree.identify_column(event.x)  # 列
        row = tree.identify_row(event.y)  # 行
        cn = int(str(column).replace('#', ''))
        rn = int(str(row).replace('I', ''))
        entryedit = tk.Text(score_window, width=20, height=1)
        entryedit.place(x=500, y=20)

        def saveedit():
            tree.set(item, column=column, value=entryedit.get(0.0, "end"))
            dao.update_score(tree.item(item, 'values'))
            score_window.destroy()
            score_windows(students)

        def cancer():
            entryedit.destroy()
            okb.destroy()
            okb1.destroy()

        okb = ttk.Button(score_window, text='OK', width=8, command=saveedit)
        okb1 = ttk.Button(score_window, text='Cancer', width=8, command=cancer)
        okb.place(x=650, y=20)
        okb1.place(x=750, y=20)

    # 双击事件
    tree = ttk.Treeview(score_window, columns=['1', '2', '3', '4', '5'], show='headings')
    style.configure("Treeview", font=(None, 16), rowheight=int(25))
    tree.column('1', width=100, anchor='center')
    tree.column('2', width=100, anchor='center')
    tree.column('3', width=150, anchor='center')
    tree.column('4', width=150, anchor='center')
    tree.column('5', width=150, anchor='center')
    tree.heading('1', text='姓名')
    tree.heading('2', text='学号')
    tree.heading('3', text='班级')
    tree.heading('4', text='科目')
    tree.heading('5', text='成绩')

    for student in students:
        scores = dao.get_score_by_id(student[0])
        for score in scores:
            item = [student[1], student[0], student[2], score[0], score[1]]
            tree.insert('', 'end', values=item, )

    tree.bind('<Double-1>', set_cell_value)

    tree.place(x=150, y=80)
    score_window.mainloop()


if __name__ == '__main__':
    manager_windows()
