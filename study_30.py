"""
ValueError
IndexError




"""


def retuen_int():
    try:
        1/0

        i = 1
        a = input()
        return i
    except IndexError:
        print("IndexError")
    except Exception as error:
        print(error)  # 应当在所有异常之前
    else:
        i = 2
        print("无异常执行else")
    finally:
        i = 3
        print("不管代码是否有问题均执行finally")


print(retuen_int())

# __main__模块