# import 与 from...import
# 在 python 用 import 或者 from...import 来导入相应的模块。
#
# 将整个模块(somemodule)导入，格式为： import somemodule
#
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
#
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#
# 将某个模块中的全部函数导入，格式为： from somemodule import *
import sys
print('--------------------------')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path, '\n')

from sys import argv, path # 导入特定的成员

print('--------------------------')
print('path:', argv)
print('path:', path)

