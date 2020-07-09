---
title: python-sys_os
date: 2020-01-14 17:49:12
tags: [python, 操作系统]
---
# 导语
python不多逼逼，大家都懂，sys和os是python非常基础且重要的两个模块，今天就由在下整理一下
[python os docs](https://docs.python.org/3/library/os.html)
[python sys docs](https://docs.python.org/3/library/sys.html)
<!-- more -->
# os
os模块提供了多数操作系统的功能接口函数。当os模块被导入后，它会自适应于不同的操作系统平台，根据不同的平台进行相应的操作，在python编程时，经常和文件、目录打交道，所以离不了os模块。
根据手册，我用ipython在自己的电脑上全部实验了一下。

方法|作用|备注
--|:--:|:--:
os.name|显示当前操作系统的所属的平台|类linux为posix，windows为nt
os.ctermid|显示对于此进程的控制终端的文件名|只适用于unix系统，我没跑出来
os.environ[key]|接受一个参数key，显示目录下的环境变量|如果你不知道你的操作系统接受的参数都有什么，可以用os.environ.keys()。
os.getenv(key,default=None)|同上|接受str，返回str
os.environb|二进制下的os.environb|我的os模块里没有这个。因为如果要使用这个方法必须要os.support_bytes_enivron为True才可，这个值是取决于原生操作系统的环境的数据类型是否是字节型，而windows不是。
os/getenvb(key,default=None)|同上|接受byte，返回byte
os.fsencode(filename)|用文件系统编码文件名|在windows里就是os.fsencode('D:\\1.txt')=>b'D:\\1.txt')
os.fsdecode(filename)|用文件系统编码解码文件名|encode的逆过程
os.fspath(path)|返回path的路径|主要是应对os.PathLike类型的，PathLike类型主要在pathlib中产生，引用也很多，他是一种文件系统路径的替代对象表示。pathlike包含了ducktype思想，就是看着这个挺像路径，那么我们就管他当路径，而使用fspath即可将他转化为标准的路径表达。
os.get_exec_path(env=None)|返回可执行文件的搜索路径|好像就是我设置的环境变量的'PATH'里的值
os.getegid()|返回egid（关于uid、gid、euid、egid的知识有空再写）|只适用于unix
os.setegid(egid)|设置egid|
os.geteuid()|返回euid|只适用unix
os.seteuid(euid)|设置euid|
os.getgid()|返回gid|只使用unix
os.setgid(gid)|设置gid|
os.getgrouplist(user,group)|返回user所在的组里面的所有id,group一般是通过user的密码记录而确定的组id|只适用于unix
os.getgroups()|返回对当前进程提供了支持的组id|只适用于unix
os.setgroups(groups)|设置group|
os.getlogin()|返回当前登录的用户|
os.getpgid(pid)|返回pgid（关于PID、PGID、PPID、SID、TID、TTY的知识有空再写）|只适用于unix
os.setpgid(pid, pgrp)|设置pgid|
os.getpgrp()|返回pgrp|只适用于unix
os.setpgrp()|设置pgrp|
os.getpid()|返回pid|windows也适用
os.getppid()|返回ppid|windows也适用
os.getpriority(which, who)|返回调度优先级|只适用于unix
os.setpriority(which, who, priority)|设置优先级
os.PRIO_PROCESS|getpriority和setpriority的参数|
os.PRIO_PGRP|同上
os.PRIO_USER|同上
os.getresuid()|Return a tuple (rgid, egid, sgid)|三合一奥利给
os.getuid()|返回当前进程的真实用户的uid|只适用于unix
os.os.initgroups(username, gid)|调用系统的initgroups（）函数来初始化user所在的group的group access list|只适用于unix
os.putenv(key,value)|设置环境参数为变量名key|会影响os.system()、popen()、fork()和execv（）
os.setregid(rgid, egid)|设置regid|
os.setresgid(rgid, egid, sgid)|设置resgid|
os.setresuid(ruid, euid, suid)|设置resuid|
os.setreuid(ruid, euid)|设置reuid|
os.getsid(pid)|返回sid|
os.setsid()|设置sid|
os.setuid(uid)|设置uid|
os.strerror(code)|返回code中对应的错误信息|

os.path.abspath(path)|返回path规范化的绝对路径|
os.path.split(path)|将path分割成目录和文件名的二元组返回


os.chdir(path)|改变当前的工作路径为path
os.fchdir(fd)
os.getcwd()|获取当前的工作路径|
