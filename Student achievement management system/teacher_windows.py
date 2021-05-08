import tkinter as tk
import data_porcess as dao
from tkinter import ttk
import os
import tkinter.messagebox

def teacher_windows(data):
    teacher_windows = tk.Tk()
    teacher_windows.attributes("-alpha", 1)
    teacher_windows.title('XXXXXXXX学校学生成绩管理系统')
    teacher_windows.geometry('1000x500')
    data = data[0]
    tip1 = tk.Label(teacher_windows, text=data[0], font=('Arial', 25)).place(x=100, y=50)
    tip2 = tk.Label(teacher_windows, text=data[1], font=('Arial', 25)).place(x=100, y=150)
    tip3 = tk.Label(teacher_windows, text=data[2], font=('Arial', 25)).place(x=100, y=250)
    tip4 = tk.Label(teacher_windows, text=data[3], font=('Arial', 25)).place(x=100, y=350)
    scores = dao.get_scores_by_lesson_and_classname(lesson=data[3], classname=data[1])
    style = ttk.Style()

    def fixed_map(option):
        return [elm for elm in style.map("Treeview", query_opt=option)
                if elm[:2] != ("!disabled", "!selected")]

    style.map("Treeview",
              foreground=fixed_map("foreground"),
              background=fixed_map("background"))
    tree = ttk.Treeview(teacher_windows, columns=['1', '2', '3', '4', '5'], show='headings')

    def set_cell_value(event):  # 双击进入编辑状态
        for item in tree.selection():
            item_text = tree.item(item, "values")
        column = tree.identify_column(event.x)  # 列
        row = tree.identify_row(event.y)  # 行
        cn = int(str(column).replace('#', ''))
        rn = int(str(row).replace('I', ''))
        entryedit = tk.Text(teacher_windows, width=20, height=1)
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

        okb = ttk.Button(teacher_windows, text='OK', width=8, command=saveedit)
        okb1 = ttk.Button(teacher_windows, text='Cancer', width=8, command=cancer)
        okb.place(x=650, y=20)
        okb1.place(x=750, y=20)

    tree.bind('<Double-1>', set_cell_value)
    style.configure("Treeview", font=(None, 15), rowheight=int(25))
    tree.column('1', width=100, anchor='center')
    tree.column('2', width=100, anchor='center')
    tree.column('3', width=200, anchor='center')
    tree.column('4', width=100, anchor='center')
    tree.column('5', width=100, anchor='center')
    tree.heading('1', text='姓名')
    tree.heading('2', text='学号')
    tree.heading('3', text='班级')
    tree.heading('4', text='课程')
    tree.heading('5', text='成绩')
    tree.tag_configure('evenColor', background='red')
    for i in scores:
        if int(i[4]) < 60:
            tree.insert('', 'end', values=i, tags=("evenColor",))
        else:
            tree.insert('', 'end', values=i, )
    tree.place(x=350, y=50)

    def back_index(win):
        win.destroy()
        os.system('python login_windows.py')

    tk.Button(teacher_windows, text='退出', font=('Arial', 15), command=lambda: back_index(teacher_windows)).place(
        x=850, y=420)

    teacher_windows.mainloop()



# if __name__ == '__main__':
#     teacher_windows([('张三', 123456, '高三（1）班', '语文', 91)])
