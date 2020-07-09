---
title: i春秋-DoYouKnowUpload
date: 2020-05-31 17:11:22
tags: [ctf,web]
---
# 导语
[点击这里去答题](https://www.ichunqiu.com/battalion?q=4581)
<!-- more -->
# main
打开看到是一个图片上传
![](https://img-blog.csdnimg.cn/20200522085836321.png)
首先假设它妹有拓展名过滤，直接传个一句话。
![](https://img-blog.csdnimg.cn/20200522085940832.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Jic3poZW5zaHVhaQ==,size_16,color_FFFFFF,t_70)
假设不成立。把一句话的拓展名改为.jpg，打开burpsuit，在发的时候再把jpg改成php

![](https://img-blog.csdnimg.cn/20200522090246740.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Jic3poZW5zaHVhaQ==,size_16,color_FFFFFF,t_70)
会返回给你它的路径。
![](https://img-blog.csdnimg.cn/2020052209032766.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Jic3poZW5zaHVhaQ==,size_16,color_FFFFFF,t_70)
访问一下看看是不是就是那个路径
![](https://img-blog.csdnimg.cn/20200522090522781.png)
发现确实如此。用蚁剑连接，可以看到html目录下有一个config.php
![](https://img-blog.csdnimg.cn/20200522090632419.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Jic3poZW5zaHVhaQ==,size_16,color_FFFFFF,t_70)内容如下
![](https://img-blog.csdnimg.cn/20200522090705213.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Jic3poZW5zaHVhaQ==,size_16,color_FFFFFF,t_70)
所以直接去连数据库
![](https://img-blog.csdnimg.cn/20200522090746726.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Jic3poZW5zaHVhaQ==,size_16,color_FFFFFF,t_70)
然后一顿找，就找到了flag
![](https://img-blog.csdnimg.cn/20200522090831288.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Jic3poZW5zaHVhaQ==,size_16,color_FFFFFF,t_70)
