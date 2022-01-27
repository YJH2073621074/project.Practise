# 运行时检测python版本
import sys
if not hasattr(sys, "hexversion") or sys.version_info != (2, 7):
    print("sorry, you are not running on python 2.7")
    print("current python version:", sys.version)