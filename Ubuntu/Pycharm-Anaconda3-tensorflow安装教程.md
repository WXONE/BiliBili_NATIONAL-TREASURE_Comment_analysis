\## Pycharm-Anaconda3-tensorflow安装教程

\### 1.Pycharm安装

我使用的方法是从官网下载

下面是官网网址

\>http://www.jetbrains.com/pycharm/download/#section=linux



下载成功后解压



解压后进入 “pycharm-professional-2018.2.3/pycharm-2018.2.3/bin” 目录下

打开命令窗口输入



\``` sh ./pycharm.sh ```





然后选择“Do not import settings”，一路ok下去就好



在Tool 点击第三项生成快捷栏。



\### 2.Anaconda安装。

下载：



官方下载地址：https://www.continuum.io/downloads



所有安装包地址：https://repo.continuum.io/archive/



安装：



在文件目录下执行：

\``` bash Anaconda3-4.2.0-Linux-x86_64.sh```



（里面的版本号自己变一下）



之后就是一路回车，遇见yes,no这种就选yes,



安装完anaconda后，你可以再开启一个终端输入conda list，如果显示没有该命令，就说明你的环境变量没有配置好（里面的一些变量改成自己的）



方法一：在终端中输入



\```sudo gedit ~/.bashrc ```



然后在末端输入



\```export PATH="/home/coder/anaconda3/bin:$PATH"```



方法二：

\```echo 'export PATH="/home/hqy/anaconda2/bin:$PATH"' >> ~/.bashrc```



\``` source ~/.bashrc```



检查一下：

conda --version



python --version





如果想打开notebook



终端输入

\``` ipython notebook```



\### 3.tensorflow安装



1、先更改anconda下载镜像为清华仓库镜像（这样舒速度快一点）



\```

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

conda config --set show_channel_urls yes

\```

2、建立一个python环境，python版本为3.6，取名字为tensorflow



\```conda create -n tensorflow python=3.6```

3、这样的话你就拥有了一个自己的环境，然后你激活这个环境就可以使用了，你可以在这个环境下安装一些python模块。



\```source activate tensorflow```

4、激活这个环境后，就可以在里面安装tensorflow，掌握这里使用的是pip方式安装的



\>pip install --upgrade --ignore-installed tensorflow



5.然后进入python，使用import tensorflow进行测试，看是否安装成功



\### 添加opencv

在tf环境里

\```pip install opencv-contrib-python ```



\## 结束

最后如果想在Pycharm里弄的话，把解析器换成Anaconda。