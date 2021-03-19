---
title: 给butterfly的valine评论添加emoji
date: 2021-01-04 12:34:03
tags:
---
# 导语
最近换了butterfly主题，想起之前我的博客都没有什么评论留言系统，于是加了valine评论，一不做二不休，顺便把emoji也加了！

# 操作
主要参考了[butterfly主题配置文档](https://butterfly.js.org/posts/ceeb73f/)
主要需要的就是找一个或者建一个emojiCDN出来，这里我白嫖了https://github.com/volantis-x/cdn-emoji
因此其实只需要在butterfly的config页面的的emojiCDN添加以下即可，这里我用的贴吧的表情，如果要用其他的也类似。
```
valine:
  emojiCDN: 'https://cdn.jsdelivr.net/gh/volantis-x/cdn-emoji/tieba/'
```
然后再去source/_data/valine.json（不论是文件夹还是文件，如果没有就创一个，这是butterfly默认的寻找emojimap的地方）配置好emojimap。我用的贴吧的，可以变成
```
{
"haha": "haha.png",
"OK": "OK.png",
"what": "what.png",
"不高兴": "不高兴.png",
"乖": "乖.png",
"你懂的": "你懂的.png",
"便便": "便便.png",
"勉强": "勉强.png",
"吐": "吐.png",
"吐舌": "吐舌.png",
"呀咩爹": "呀咩爹.png",
"呵呵": "呵呵.png",
"哈哈": "哈哈.png",
"啊": "啊.png",
"喷": "喷.png",
"大拇指": "大拇指.png",
"太开心": "太开心.png",
"太阳": "太阳.png",
"委屈": "委屈.png",
"小乖": "小乖.png",
"小红脸": "小红脸.png",
"彩虹": "彩虹.png",
"心碎": "心碎.png",
"怒": "怒.png",
"惊哭": "惊哭.png",
"惊讶": "惊讶.png",
"懒得理": "懒得理.png",
"手纸": "手纸.png",
"挖鼻": "挖鼻.png",
"捂嘴笑": "捂嘴笑.png",
"星星月亮": "星星月亮.png",
"汗": "汗.png",
"沙发": "沙发.png",
"泪": "泪.png",
"滑稽": "滑稽.png",
"爱心": "爱心.png",
"犀利": "犀利.png",
"狂汗": "狂汗.png",
"玫瑰": "玫瑰.png",
"疑问": "疑问.png",
"真棒": "真棒.png",
"睡觉": "睡觉.png",
"礼物": "礼物.png",
"笑尿": "笑尿.png",
"笑眼": "笑眼.png",
"红领巾": "红领巾.png",
"胜利": "胜利.png",
"花心": "花心.png",
"茶杯": "茶杯.png",
"药丸": "药丸.png",
"蛋糕": "蛋糕.png",
"蜡烛": "蜡烛.png",
"鄙视": "鄙视.png",
"酷": "酷.png",
"酸爽": "酸爽.png",
"钱币": "钱币.png",
"阴险": "阴险.png",
"音乐": "音乐.png",
"香蕉": "香蕉.png",
"黑线": "黑线.png"
}
```
（捯饬这玩意还花了我点功夫来着）
这个emojimap就是 名称：文件的格式，因此也可以直接进行拼接而不设置emojicdn，类似下面这样
```
"haha": "https://cdn.jsdelivr.net/gh/volantis-x/cdn-emoji/tieba/haha.png"
```
这样也可以拼起来好几个不同CDN的emoji了，真不错。

效果就是这样的
![](1.jpg)
（讲道理在下面好像就能看到了呢）