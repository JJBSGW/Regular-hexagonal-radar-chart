import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, messagebox

plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统
plt.rcParams['axes.unicode_minus'] = False

def draw_hexagon_radar(categories, values, title="六边形分析图"):
    # 参数检查
    if len(categories) != 6 or len(values) != 6:
        raise ValueError("必须提供6个分类和6个值")

    # 将数据转换为极坐标格式
    angles = np.linspace(0, 2*np.pi, 6, endpoint=False).tolist()
    angles += angles[:1]  # 闭合图形
    
    # 设置极坐标图
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, polar=True)
    
    # 绘制数据
    values += values[:1]  # 闭合图形
    ax.plot(angles, values, color='blue', linewidth=2)
    ax.fill(angles, values, color='blue', alpha=0.25)
    
    # 设置刻度标签
    ax.set_theta_offset(np.pi/2)  # 将0度位置设置在顶部
    ax.set_theta_direction(-1)    # 顺时针方向
    
    # 设置轴标签
    ax.set_rlabel_position(0)
    plt.ylim(0, max(values)*1.1)
    
    # 设置分类标签
    label_positions = np.linspace(0, 2*np.pi, 6, endpoint=False)
    ax.set_xticks(label_positions)
    ax.set_xticklabels(categories)
    
    # 美化标签显示
    for label, angle in zip(ax.get_xticklabels(), label_positions):
        if angle in [0, np.pi]:
            label.set_horizontalalignment('center')
        elif 0 < angle < np.pi:
            label.set_horizontalalignment('left')
        else:
            label.set_horizontalalignment('right')
    
    # 设置标题
    plt.title(title, y=1.1)
    
    # 显示图形
    plt.show()

def generate_chart():
    try:
        # 获取用户输入
        categories = [entry_category1.get(), entry_category2.get(), entry_category3.get(),
                      entry_category4.get(), entry_category5.get(), entry_category6.get()]
        values = [float(entry_value1.get()), float(entry_value2.get()), float(entry_value3.get()),
                  float(entry_value4.get()), float(entry_value5.get()), float(entry_value6.get())]
        title = entry_title.get()

        # 调用绘图函数
        draw_hexagon_radar(categories, values, title)
    except ValueError as e:
        messagebox.showerror("输入错误", "请确保所有值为数字，且所有字段已填写！")

# 创建主窗口
root = Tk()
root.title("六边形分析图生成器")
root.geometry("400x400")

# 添加标题输入
Label(root, text="图表标题:").grid(row=0, column=0, padx=10, pady=5)
entry_title = Entry(root)
entry_title.grid(row=0, column=1, padx=10, pady=5)

# 添加分类和程度输入
categories_labels = ["分类1:", "分类2:", "分类3:", "分类4:", "分类5:", "分类6:"]
values_labels = ["程度1:", "程度2:", "程度3:", "程度4:", "程度5:", "程度6:"]

entries_categories = []
entries_values = []

for i in range(6):
    Label(root, text=categories_labels[i]).grid(row=i+1, column=0, padx=10, pady=5)
    entry_category = Entry(root)
    entry_category.grid(row=i+1, column=1, padx=10, pady=5)
    entries_categories.append(entry_category)

    Label(root, text=values_labels[i]).grid(row=i+1, column=2, padx=10, pady=5)
    entry_value = Entry(root)
    entry_value.grid(row=i+1, column=3, padx=10, pady=5)
    entries_values.append(entry_value)

# 全局变量存储输入框
entry_category1, entry_category2, entry_category3, entry_category4, entry_category5, entry_category6 = entries_categories
entry_value1, entry_value2, entry_value3, entry_value4, entry_value5, entry_value6 = entries_values

# 添加生成按钮
Button(root, text="生成图表", command=generate_chart).grid(row=7, column=1, columnspan=2, pady=20)

# 运行主循环
root.mainloop()
