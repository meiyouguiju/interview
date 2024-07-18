import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import os

# 指定全局字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# 根据当前日期动态生成日志文件的路径
current_date = datetime.now().strftime("%Y%m%d")
# log_file_path = f"/home/gnckbase/dae/select/logs/job_hour.sh.{current_date}.log.detail"
log_file_path = f"D:\需求\绿网clickhouse\log文件/job_hour.sh.{current_date}.log.detail"
# output_dir = "/home/gncktest/pic"
output_dir = "D:\需求\绿网clickhouse\log文件"

# 读取文件内容
with open(log_file_path, "r") as file:
    lines = file.readlines()

# 初始化数据结构
data = {"ck2": [], "ck4": [], "ck6": []}
times = []
sqls = ["sql1", "sql2", "sql3", "sql4", "sql5"]

# 解析文件内容
for i in range(0, len(lines), 16):
    time_str = lines[i].strip()
    time_obj = datetime.strptime(time_str, "%a %b %d %H:%M:%S CST %Y")
    times.append(time_obj)
    for j in range(5):
        data["ck2"].append(float(lines[i + 1 + j].strip()))
        data["ck4"].append(float(lines[i + 6 + j].strip()))
        data["ck6"].append(float(lines[i + 11 + j].strip()))

# 生成折线图
for i in range(5):
    fig, ax = plt.subplots(figsize=(10, 6))  # 增加图形的大小
    ax.plot_date(times, [data["ck2"][j] for j in range(i, len(data["ck2"]), 5)], '-', label="ck2 鲲鹏5220")
    ax.plot_date(times, [data["ck4"][j] for j in range(i, len(data["ck4"]), 5)], '-', label="ck4 鲲鹏5250")
    ax.plot_date(times, [data["ck6"][j] for j in range(i, len(data["ck6"]), 5)], '-', label="ck6 Intel 4316")
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m月%d日\n%H:%M:%S'))  # 修改时间格式
    ax.set_xlabel("时间", fontsize=16)
    date_month_day_str = datetime.now().strftime("%m月%d日")
    ax.set_ylabel("查询耗时", fontsize=16)
    ax.set_title(f"{date_month_day_str} {sqls[i]}查询耗时", fontsize=16)
    ax.legend()
    ax.grid(True)

    # 保存图形到指定的目录
    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    output_file_path = os.path.join(output_dir, f"{timestamp}_sql{i+1}.jpg")
    plt.savefig(output_file_path)

plt.show()
