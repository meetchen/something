import tkinter as tk
import data_porcess as dao
from tkinter import ttk
import tkinter.messagebox
import os


def manager_windows():
    manager_windows = tk.Tk()
    manager_windows.attributes("-alpha", 0.8)
    manager_windows.title('Student achievement management system')
    manager_windows.geometry('1000x500')
    tip1 = tk.Label(manager_windows, text='人员', font=('Arial', 25)).place(x=100, y=50)
    tip3 = tk.Label(manager_windows, text='课程', font=('Arial', 25)).place(x=800, y=50)
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
    tree = ttk.Treeview(manager_windows, columns=['1', '2', '3', '4'], show='headings')

    def set_cell_value(event):  # 双击进入编辑状态
        for item in tree.selection():
            # item = I001
            item_text = tree.item(item, "values")
            # print(item_text[0:2])  # 输出所选行的值
        column = tree.identify_column(event.x)  # 列
        row = tree.identify_row(event.y)  # 行
        cn = int(str(column).replace('#', ''))
        rn = int(str(row).replace('I', ''))
        # entryedit = tk.Text(teacher_windows, width=10 + (cn - 1) * 16, height=1)
        entryedit = tk.Text(manager_windows, width=20, height=1)
        # entryedit.place(x=16 + (cn - 1) * 130, y=6 + rn * 20)
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
        # okb.place(x=90 + (cn - 1) * 242, y=2 + rn * 20)
        okb.place(x=650, y=20)
        okb1.place(x=750, y=20)

    # 双击事件
    # tree.bind('<Double-1>', set_cell_value)
    style.configure("Treeview", font=(None, 15), rowheight=int(25))
    tree.column('1', width=100, anchor='center')
    tree.column('2', width=100, anchor='center')
    tree.column('3', width=200, anchor='center')
    tree.column('4', width=100, anchor='center')
    tree.heading('1', text='Name')
    tree.heading('2', text='Id')
    tree.heading('3', text='ClassName')
    tree.heading('4', text='Type')
    tree.tag_configure('evenColor', background='red')
    users = dao.find_all_user()
    for i in users:
        tree.insert('', 'end', values=i, )
    tree.place(x=30, y=120)

    def delete_tree1():
        curltem = tree.focus()
        item = tree.item(curltem)['values']
        msg = '要删除'
        is_student = True
        if item[3] == '学生':
            msg = msg + '学生' + item[0]
        else:
            msg = msg + '老师' + item[0]
        flag = tk.messagebox.askyesno('提示', msg + '吗？')
        if flag:
            dao.delete_user(item[1], is_student)
            tree.delete(curltem)

    tk.Button(manager_windows, text='deleteUser', font=('Arial', 15), command=delete_tree1).place(x=150, y=420)

    # lesson tree
    score_tree = ttk.Treeview(manager_windows, columns=['1', '2', '3'], show='headings')

    def set_cell_value1(event):  # 双击进入编辑状态
        for item in score_tree.selection():
            # item = I001
            item_text = score_tree.item(item, "values")
            # print(item_text[0:2])  # 输出所选行的值
        column = score_tree.identify_column(event.x)  # 列
        row = score_tree.identify_row(event.y)  # 行
        cn = int(str(column).replace('#', ''))
        rn = int(str(row).replace('I', ''))
        # entryedit = tk.Text(teacher_windows, width=10 + (cn - 1) * 16, height=1)
        entryedit = tk.Text(manager_windows, width=20, height=1)
        # entryedit.place(x=16 + (cn - 1) * 130, y=6 + rn * 20)
        entryedit.place(x=500, y=20)

        def saveedit():
            score_tree.set(item, column=column, value=entryedit.get(0.0, "end"))
            print(score_tree.item(item, 'values'))
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
        # okb.place(x=90 + (cn - 1) * 242, y=2 + rn * 20)
        okb.place(x=650, y=20)
        okb1.place(x=750, y=20)

    score_tree.bind('<Double-1>', set_cell_value1)
    style.configure("Treeview", font=(None, 15), rowheight=int(25))
    score_tree.column('1', width=100, anchor='center')
    score_tree.column('2', width=100, anchor='center')
    score_tree.column('3', width=100, anchor='center')
    score_tree.heading('1', text='lesson')
    score_tree.heading('2', text='TeacherName')
    score_tree.heading('3', text='teacher_id')
    score_tree.tag_configure('evenColor', background='red')
    lesson = dao.find_all_lesson()
    for i in lesson:
        score_tree.insert('', 'end', values=i, )
    score_tree.place(x=650, y=120)

    def delete_tree2():
        curltem = score_tree.focus()
        item = score_tree.item(curltem)['values']
        flag = tk.messagebox.askyesno('提示', '要删除' + item[1] + '的' + item[0] + '课吗？')
        if flag:
            dao.delete_lesson(item[2], lesson=item[0])
            score_tree.delete(curltem)

    tk.Button(manager_windows, text='deleteLesson', font=('Arial', 15), command=delete_tree2).place(x=700, y=420)

    def back_index(win):
        win.destroy()
        os.system('python login_windows.py')

    tk.Button(manager_windows, text='Exit', font=('Arial', 15), command=lambda: back_index(manager_windows)).place(
        x=850, y=420)
    manager_windows.mainloop()

if __name__ == '__main__':
    manager_windows()
