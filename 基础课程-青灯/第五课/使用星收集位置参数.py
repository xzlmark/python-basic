# 在不清楚传入参数是多少个，可以用 * 来收集
# 函数在传参得过程中，使用的元组
# 收集所有的传过来得参数
def f(*args):
    # args 是一个元组
    print(args)
f(6,6,7)
