---
title: i春秋-Pretty_good_privacy
date: 2021-01-28 18:05:27
tags: [ctf,misc]
---
# 导语
[点击这里去答题](https://www.ichunqiu.com/battalion?q=2333)
<!-- more -->
![](1.jpg)

# pretty good privacy
看到题目，立刻想到要用pgp。
我没有，因此去https://www.gnupg.org/download/index.html 下载一个Gpg4win。安装的时候默认安装的模块都安装了就完事了。

解压题目，可以看到一个这
![](2.jpg)
打开doc文件，可以看到这样的内容
![](3.jpg)
当然你得先开了word的显示隐藏内容的选项才能看到下面那个TrueCrypt的内容。
然后全选，设置字体颜色为黑色，可以看到这个藏比还多藏了一点，但不多。（？）
![](4.jpg)

看到TrueCrypt，立即推要用TrueCrypt。
我没有，因此去https://sourceforge.net/projects/truecrypt/files/TrueCrypt/TrueCrypt-7.2.exe/download 下一个并且安装。

然后我们就看一下.pgp，由于目前我们没有获得密钥，所以是无法解密的。

看到有TrueCrypt，试着用TrueCrypt挂载CISCN2016
如果你在第一层，用的是第一行的密码，那么你可以看到
![](5.jpg)
那你能帮帮我吗（？）
![](6.jpg)

然而我们老misc选手word可能没有显示隐藏内容吗？使用下面的密码挂载TrueCrypt，即可得到pgp密钥对。
![](7.jpg)
使用pgp加载了两个密钥，即可解密SECRET.docx.pgp
![](8.jpg)
![](9.jpg)
打开docx，即得flag。
![](10.jpg)