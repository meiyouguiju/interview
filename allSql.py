import os

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from datetime import datetime

# 初始化字典来存储数据
data = {'ck2': [], 'ck4': [], 'ck6': []}

# 指定全局字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# 根据当前日期动态生成日志文件的路径
current_date = datetime.now().strftime("%Y%m%d")
# log_file_path = f"/home/gnckbase/dae/select/logs/job_hour.sh.{current_date}.log"
log_file_path = f"D:\需求\绿网clickhouse\log文件/job_hour.sh.{current_date}.log"
# output_dir = "/home/gncktest/pic"
output_dir = "D:\需求\绿网clickhouse\log文件"

# 读取日志文件
with open(log_file_path, 'r') as file:
    for line in file:
        # 分割每行以逗号分隔
        parts = line.strip().split(',')
        if len(parts) > 2:
            # 解析时间
            timestamp = parts[0]
            date_format = "%a %b %d %H:%M:%S CST %Y"  # 注意：这里假设的日期格式可能需要根据实际日志进行调整
            dt = datetime.strptime(timestamp, date_format)
            # 转换为matplotlib可识别的格式
            x = matplotlib.dates.date2num(dt)

            # 获取ck和cost
            ck = parts[1]
            cost = float(parts[2].split(':')[1])

            # 将数据添加到相应的列表中
            data[ck].append((x, cost))

        # 准备绘图数据
x_values_ck2 = []
y_values_ck2 = []
x_values_ck3 = []
y_values_ck3 = []
x_values_ck6 = []
y_values_ck6 = []

# 提取每个ck的x和y值
for key, values in data.items():
    x_values = []
    y_values = []
    for x, y in values:
        x_values.append(x)
        y_values.append(y)
    if key == 'ck2':
        x_values_ck2, y_values_ck2 = x_values, y_values
    elif key == 'ck4':
        x_values_ck3, y_values_ck3 = x_values, y_values
    elif key == 'ck6':
        x_values_ck6, y_values_ck6 = x_values, y_values

    # 绘图
plt.figure(figsize=(10, 6))
plt.plot(x_values_ck2, y_values_ck2, label='ck2 鲲鹏5220')
plt.plot(x_values_ck3, y_values_ck3, label='ck4 鲲鹏5250')
plt.plot(x_values_ck6, y_values_ck6, label='ck6 Intel 4316')

# 设置x轴为时间格式
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m月%d日\n%H:%M:%S'))

# 设置图例和标题
plt.legend()
date_month_day_str = datetime.now().strftime("%m月%d日")
plt.title(f"{date_month_day_str}查询总耗时", fontsize=16)
plt.xlabel("时间", fontsize=16)
plt.ylabel("查询耗时", fontsize=16)

# 显示网格
plt.grid(True)

# 自动调整子图参数，以便填充整个图像区域
plt.tight_layout()

# 保存图形到指定的目录
timestamp = datetime.now().strftime("%Y%m%d%H%M")
output_file_path = os.path.join(output_dir, f"{timestamp}_sqlall.jpg")
plt.savefig(output_file_path)

# 显示图形
plt.show()