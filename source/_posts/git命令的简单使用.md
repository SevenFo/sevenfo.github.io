---
title: git命令的简单使用
date: 2019-10-03 21:05:57
tags:
categories:
---
{% note default %}
之前一直弄不清楚git那些命令，今天终于花了一个多小时的时间熟悉了一边git的一些简单命令，并且解决的一些常见的冲突
{% endnote %}
---
<!--more--> 
# git使用的基本流程
## 方法一
1. 在创建远程仓库

    以GitHub为例，右上角加号的菜单中选择 new repository,填写相关信息后 create repository,即成功创建仓库.
2. 初始化本地工作区

    在git bash 进入到某个文件夹使用命令
    ``` bash
    git init
    ```
    初始化本地工作区
3. 链接远程仓库

    ``` bash
    git remote add 该远程仓库名的别称(通常为origin) https://github.com/username/repositoryName
    ```
    与remote 相关的命令还有
    ``` bash
    git remote #查看所有远程仓库名的别称
    git remote remove #删除某个别称
    ...
    ```
4. 提交改动到暂存区(index)

    ``` bash
    git add fileName
    git add .
    ```
5. 提交改动至本地仓库(local repository)

    ``` bash
    git commit -m 'message'
    ```
    4~5两步一可以采用一个命令
    ``` bash
    git commit -a -m 'message'
    ```
6. 提交改动至远程仓库(remote repository)

    ```bash
    git push origin(远程仓库别称) master(local branch) master(remote branch) # the remote branchName can be omitted when the local branchName is as same as the remote branchName
    ```
    注意:此方法因为远程仓库与本地仓库不同因此提交修改到远程仓库时会发生冲突，其解决方案便是先 拉取远程仓库到本地 后再提交修改
    ``` bash
    git getch origin <branchName(can be omitted)>
    git merge origin/master #merge 参数 ：将该分支与本地分支合并
    ```
    or
    ``` bash
    git pull origin master
    ```
## 方法二

初始化本地仓库后直接pull远程仓库到本地，后提交修改方法同上，命令同上