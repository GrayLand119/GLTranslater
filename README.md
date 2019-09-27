# GLTranslater

使用有道翻译 API 自动读取 txt 文本并逐行长文本的翻译, 生成中英文混排的双语文本.


# Usage

0. 由于是调用有道的文本翻译功能, 需要先去有道平台注册一个账号并`创建应用`然后`添加服务(翻译实例)`, 之后获得请求的 KEY , 并将其填入`GLTranslater.py`中的如下位置:

```python
YOUDAO_URL = 'http://openapi.youdao.com/api'
APP_KEY = '请输入在有道平台注册得到的 APP_KEY'
APP_SECRET = '请输入在有道平台注册得到的 APP_SECRET'
```


1. 将带翻译的文本放入目录`WaitToTranslate`中, 例如: `History Through NSFNet.txt`

```python
So I hope you got from that, that it wasn't trivial. It wasn't like somebody just walked out and said, hey make a network. I mean, there were forces,  powerful forces, the "telecom lobbyists",  that did not want this to happen.
 And we will, we will see these telecom lobbyists a couple times as we progress through this lecture. So Larry Smarr and the folks that made the supercomputers convinced Congress to authorize the, the giving of a grant to build the National Science  Foundation's network.
 It was going to use the TCP/IP protocol that the ARPANET had built. It was supposed to be inclusive,  at least for research academics.

...
```

2. 执行`python GLTranslater.py`, 将会自动请求网络进行翻译.
3. 翻译完成后会生成文件`History Through NSFNet-proccessed.txt`并保存在`Translated`目录中:

效果:
```python
So I hope you got from that, that it wasn't trivial. It wasn't like somebody just walked out and said, hey make a network.
所以我希望你们从中明白，这不是小事。这不像有人走出去说，嘿，建立一个网络。
 I mean, there were forces,  powerful forces, the "telecom lobbyists",  that did not want this to happen.
我的意思是，有力量，强大的力量，“电信说客”，他们不希望这种事情发生。
 And we will, we will see these telecom lobbyists a couple times as we progress through this lecture.
在这堂课的过程中，我们会多次看到这些电信说客。
 So Larry Smarr and the folks that made the supercomputers convinced Congress to authorize the, the giving of a grant to build the National Science  Foundation's network.
所以Larry Smarr和那些制造超级计算机的人说服了国会批准拨款来建立国家科学基金会的网络。
 It was going to use the TCP/IP protocol that the ARPANET had built.
它将使用阿帕网建立的TCP/IP协议。
 It was supposed to be inclusive,  at least for research academics.
它应该是包容性的，至少对研究学者来说是这样。

...

```


# Feature feature...

未来将添加`人工智能本地翻译`功能...


