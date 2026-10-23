"""Day 1 · 第一个 Python 程序

运行方式（在 python-roadmap 目录下）：
    python day01/hello.py

今天只学四件事：
    1. print() 往屏幕输出
    2. input() 从键盘读一行
    3. 变量：name = "张三"
    4. f-string：f"你好，{name}"
"""

from datetime import datetime

name = input("你叫什么名字？")
now = datetime.now().strftime("%Y-%m-%d %H:%M")

print(f"你好，{name}！")
print(f"现在是 {now}，你写下了第一行 Python。")

# ---------- 练手（自己动手改，别只看） ----------
# 1. 再加一行，打印你的专业
# 2. 把 strftime 里的格式改成 "%Y年%m月%d日"，看看输出变成什么样
# 3. 加一个 input 问"今天想学什么"，然后打印出来
