---
title: PlayWithAndroidKernel
date: 2020-07-19 12:02:18
tags: [pwn]
---
# 导语
Do you want to hack Android？
<!-- more -->

# 环境配置
初学Android内核漏洞，github上的[AndroidKernelExploitationPlayground](https://github.com/Fuzion24/AndroidKernelExploitationPlayground)是一个很不错的选择，虽然他还是安装4.4.2的内核，但是帮助我们理解的话还是很有价值的。
我在我的Ubuntu16.04上配置，如果你的步骤有出入建议查找其他教程~
配置AndroidKernelExploitationPlayground的环境基本可以分为一下步骤
1. 下载安卓虚拟机goldfish源码
2. 下载AndroidKernelExploitationPlayground
3. 使用AndroidKernelExploitationPlayground的patch将有漏洞的内核模块加到安卓虚拟机源码
4. 安装交叉编译工具arm-linux-androideabi-4.6
5. 编译虚拟机
6. 下载安装Androidsdk
7. 启动虚拟机

## 下载安卓虚拟机goldfish源码
在[AndroidKernelExploitationPlayground](https://github.com/Fuzion24/AndroidKernelExploitationPlayground)的README中，有给我们一个地址，如果有梯子的话直接复制他的命令就成了，速度也比较可观。不过用国内的源速度应该更起飞一点。没梯子的话建议去整一个。
``` bash
git clone https://aosp.tuna.tsinghua.edu.cn/kernel/goldfish.git
```
clone完了你可能会发现里面没有东西，之后的git checkout和git am会把代码放进来的，莫慌。

## 下载AndroidKernelExploitationPlayground
这个也不是很大，速度也还好，直接clone
```
git clone https://github.com/Fuzion24/AndroidKernelExploitationPlayground.git kernel_exploit_challenges
```
 
*注意* goldfish和kernel_exploit_challenges需要放在同一个目录下，如果不在的话你后面的环境变量自己看着改8。

## 使用AndroidKernelExploitationPlayground的patch将有漏洞的内核模块加到安卓虚拟机源码
和项目的README里面说的一样，把命令复制过去就行了（在goldfish上层的目录执行）
``` bash
cd goldfish && git checkout -t origin/android-goldfish-3.4 && \
git am --signoff < ../kernel_exploit_challenges/kernel_build/debug_symbols_and_challenges.patch && \
cd .. && ln -s $(pwd)/kernel_exploit_challenges/ goldfish/drivers/vulnerabilities
```

## 安装交叉编译工具arm-linux-androideabi-4.6
``` bash
git clone https://android.googlesource.com/platform/prebuilts/gcc/linux-x86/arm/arm-linux-androideabi-4.6
```


## 编译虚拟机
``` bash
export ARCH=arm SUBARCH=arm CROSS_COMPILE=arm-linux-androideabi- &&\
export PATH=$(pwd)/arm-linux-androideabi-4.6/bin/:$PATH && \
cd goldfish && make goldfish_armv7_defconfig && make -j8
```
（这里也是在goldfish上层目录）

## 下载安装AndroidSDK
[下载地址](http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz )
使用tar命令解压之后，再将tools添加到环境变量中
（这里最好把这些环境变量全都加到.bashrc下，比较方便）
然后我们启动tools下的android程序。
如果你的电脑没有java环境，那么你就需要装一个，可以使用apt直接装
```
// 安装默认的jre和jdk
sudo apt-get install default-jre
sudo apt-get install default-jdk

// 安装oracle JDK
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update

// 安装JDK8
sudo apt-get install oracle-java8-installer
```
我直接装的默认的
android是android SDK manager程序，在这里我们需要装android 4.4.2API19下的SDK plantform和arm eabi system image
![](1.jpg)
使用`android list targets`可以看到有对应的镜像文件
![](2.jpg)
然后创建模拟器
```
android create avd --force -t "android-19" -n kernel_challenges
```
![](3.jpg)
然后进入 goldfish 目录，使用下面的命令来使用我们的内核来运行模拟器，并在 1234 端口起一个 gdbserver 来方便进行内核调试
```
emulator -show-kernel -kernel arch/arm/boot/zImage -avd kernel_challenges -no-boot-anim -no-skin -no-audio -no-window -qemu -monitor unix:/tmp/qemuSocket,server,nowait -s
```

## 启动虚拟机
在goldfish目录下
```
arm-linux-androideabi-gdb vmlinux
```
这里有可能遇到
```
arm-linux-androideabi-gdb: error while loading shared libraries: libpython2.6.so.1.0: cannot open shared object file: No such file or directory
```
因为我的ubuntu版本默认的是python2.7+3.5的环境，而这个就单纯的去找python2.6的库，于是会报错，所以我们使用ln命令把2.7的库软连接2.6的库。
```
sudo ln -s /usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0 /usr/lib/x86_64-linux-gnu/libpython2.6.so.1.0
```

正常之后是这样额
![](4.jpg)
输入target remote:1234如果是如下显示，就说明环境配置完成辣。





参考
https://github.com/Fuzion24/AndroidKernelExploitationPlayground
https://www.anquanke.com/post/id/86617
https://www.cnblogs.com/louby/p/10837864.html