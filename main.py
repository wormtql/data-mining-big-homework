from dm.big_homework import big_homework
import sys


if len(sys.argv) == 1:
    arg = "big_homework"
else:
    arg = sys.argv[1]

if arg == "big_homework":
    big_homework()
