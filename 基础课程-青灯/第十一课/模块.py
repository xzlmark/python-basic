# 模块导入顺序：先导入内置的，后导入地方的，最后导入自己定义的
# 导入的方法有很多种
# 1.import 模块名:这种导入在使用的时候需要用：模块名.函数名 如：import time

# 2.from 模块名 import 函数名: 这种导入在使用的时候可以直接使用 如果：from time import sqrt.在使用的时候就不需要用
# time.sqart(),而直接用sqart()即可。import后面可以是函数，属性或则模块名

# 3.也可以使用from 模块名 import * 这种格式，这其实和第一种导入方法是一样的。

# 总结：如果知道明确使用模块下面的哪个方法，可以用第二种方式，这样可以更加节约内存，如果不知道还需要用模块中的其他方法，
# 则用第一种全部导入的方式

# 别名：当模块名较长时候，则在导入的时候用as 取个别名。如import time as t.注意：这种导入只在当前文件中有用

# 导入自定义模块：也就是自己写的python文件。如果在当前目录下，可以直接用import 模块名；
# 但是在一个项目中的其他目录中，则需要使用from 项目名.文件夹 import 模块名.

# if __name__ == '__main__': 的意义在于：如果这个文件在其他文件中调用后，这个文件中的所有代码都会执行一遍，如果有测试
# 等语句，可以直接放在这个判断语句后，则其他文件调用的时候就不会执行了，主要用于测试。if的意思就是判断这个文件是否是
# 本身调用，如果是则执行，如果不是则不执行里面的内容

# 包与模块的区别：包是一种特殊的目录结构，里面包括一个__init__的文件

