from multiprocessing import Process


def func():
    print(12345)


if __name__ == '__main__': 
    p = Process(target=func,)
    p.start() 
    print('*' * 10) 
'''
windows下必须写__name__ ==__'main',这和系统创建进程的机制有关系，不用深究，记着windows下要写就好;
首先运行当前这个.py文件，运行这个文件的程序，那么就产生了进程，这个进程我们称为主进程;
p=Process（target=func,）:将函数注册到一个进程中，p是一个进程对象，此时还没有启动进程，只是创建了一个进程对象。并且func是
    不加括号的，因为加上括号这个函数就直接运行了。
告诉操作系统，给我开启一个进程，func这个函数就被我们新开的这个进程执行了，而这个进程是我主进程运行过程中创建出来的，
所以称这个新创建的进程为主进程的子进程，而主进程又可以称为这个新进程的父进程。
而这个子进程中执行的程序，相当于将现在这个.py文件中的程序copy到一个你看不到的python文件中去执行了，就相当于
当前这个文件，被另外一个py文件import过去并执行了。
start()并不是直接就去执行了，我们知道进程有三个状态，进程会进入进程的三个状态，就绪，（被调度，也就是时间片切换
到它的时候）执行，阻塞，并且在这个三个状态之间不断的转换，等待cpu执行时间片到了。
print() 这是主进程的程序，上面开启的子进程的程序是和主进程的程序同时运行的，我们称为异步
'''
