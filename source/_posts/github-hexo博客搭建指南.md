---
title: github+hexo博客搭建指南
date: 2019-10-03 18:08:33
tags:
categories:
---
{% note default %}
{% endnote %}
---

 # 工具的准备与环境配置
- ## 安装visual studio code
VS code 是一款由微软出品（好东西！）的轻量级的强大编辑器，通过其强大的插件系统可以很友好地编辑包括JavaScript、python、c++等在内的各种语言的代码文件。在这里我们将用其来编辑后续的hexo配置文件以及书写博客(.md文件)。
下载链接：https://code.visualstudio.com/
下载->安装->成功

* ## 安装git工具
下载链接: https://git-scm.com/download/win
下载后运行安装程序，按照默认配置一路next（其中有一步选择git的默认编辑器可以选择VScode）即可完成安装。
* ## 安装Node.js
node.js作为hexo的依赖环境
下载链接：https://nodejs.org/zh-cn/
同样一路Next即可
* ## 安装hexo
打开git bash，进入你想要安装hexo的文件目录（以后的博客文件也将存放于此）运行如下代码

``` bash
npm install -g hexo #安装hexo
cd you_blog #进入目录
hexo init #初始化，即下载hexo的相关文件到该目录
hexo g #g :generate 生产网页文件
hexo s #s: server 开启本地预览
```
此时在浏览器中打开 http://localhost:4000 就可以

* ## github的配置
    1. ### 注册GitHub账户
            网址:https://github.com/    
            进入网站->填写用户名等相关信息->sign up->完成新手引导熟悉GitHub->成功

    2. ### 为博客配置GitHub
        1. new repository （新建仓库）

            鼠标移至右上角加号即可在菜单中找到该选项。打开后填写相关信息。注意repository name为 user_name.github.io,其余选项保持默认，点击create repository即可！
        2. 


<!--more--> 