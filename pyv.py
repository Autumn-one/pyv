import os
import sys
import re
from colorama import init, Fore, Back, Style

init(autoreset=True) # 初始化 windows必须
args = sys.argv
if len(args) >= 2:
    arg = args[1]
    if arg == 'ls' or arg == 'list':
        os.system("py -0")
    elif re.match(r"[23]\.\d+", arg):
        os.system(f"setx PY_PYTHON {args[1]}")
        print(Fore.GREEN + f"python版本设置完成, 重启命令行生效! 版本号: {args[1]}")
    else:
        print(Fore.RED + "无法识别的指令!")



