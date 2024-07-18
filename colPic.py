import os

import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib

# 指定全局字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# 根据当前日期动态生成日志文件的路径
current_date = datetime.now().strftime("%Y%m%d")
# log_file_path = f"/home/gnckbase/dae/select/logs/job_hour.sh.{current_date}.log"
log_file_path = f"D:\需求\绿网clickhouse\log文件/job_hour.sh.{current_date}.log"
# output_dir = "/home/gncktest/pic"
output_dir = "D:\需求\绿网clickhouse\log文件"

# 读取文件内容
with open(log_file_path, "r") as file:
    lines = file.readlines()

# 初始化数据结构
data = {"ck2": 0, "ck6": 0, "ck4": 0}
label = {"ck2": "ck2 鲲鹏5220", "ck4": "ck4 鲲鹏5250", "ck6": "ck6 Intel 4316"}

# 解析文件内容
for line in lines:
    parts = line.strip().split(',')
    ck = parts[1]
    cost = float(parts[2].split(':')[1])
    data[ck] += cost

# 计算性能落后百分比
t6 = data["ck6"]
a = round((data["ck2"] - t6) / t6 * 100, 2)
b = round((data["ck4"] - t6) / t6 * 100, 2)

# 生成柱状图
fig, ax = plt.subplots(figsize=(12, 8))  # 增加图形的宽度
colors = ['blue', 'orange', 'green']
for i, ck in enumerate(data.keys()):
    ax.bar(ck, data[ck], color=colors[i], label=label.get(ck), align='center', width=0.4)  # 将x轴的标签设置为ck节点
    ax.text(i, data[ck] + 5, str(data[ck]), ha='center', va='bottom', fontsize=10)
ax.set_xlabel("集群", fontsize=16)
ax.set_ylabel("总耗时", fontsize=16)
date_month_day_str = datetime.now().strftime("%m月%d日")
ax.set_title(f"{date_month_day_str}总耗时", fontsize=16)

# 在图形中添加性能落后百分比的信息
text = f"ck6耗时：{t6}，ck2对比ck6性能落后：{a}%，ck4对比ck6性能落后：{b}%"
plt.figtext(0.5, 0.01, text, ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})  # 增大字体大小

# 添加图例
ax.legend()

# 保存图形到指定的目录
timestamp = datetime.now().strftime("%Y%m%d%H%M")
output_file_path = os.path.join(output_dir, f"{timestamp}_dayall_col.jpg")
plt.savefig(output_file_path)

plt.show()
