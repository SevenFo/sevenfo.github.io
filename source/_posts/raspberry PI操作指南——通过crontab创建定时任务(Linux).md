---
title: raspberry PI操作指南——通过crontab创建定时任务(Linux)
date: 2019-09-02 18:06:07
tags: raspberryPi
---
# 1.单词释义
        cron:定时任务
# 2.使用方式
```bash
(sudo) crontab -e #编辑定时任务
(sudo) crontab -l #列出所有定时任务
(sudo) crontab -r #删除当前用户的所有定时任务
```
加上sudo则针对所有用户，否则只对当前用户生效。

当然你也可以使用 -u 参数来指定特定的用户，这样就无需切换用户了。

```bash
sudo crontab -u 用户名(如 root ) -其他参数
如：
sudo crontab -u pi -l #查看用户pi的所有定时任务
```
注意:若首次编辑crontab文件会提示选择编辑器，推荐使用nano

crontab 命令示例：
```bash
#a.每天8:00运行hello.py文件
0 8 * * * sudo python hello.py
#b.每月1号8:00运行newmonth.py文件
0 8 1 * * sudo python newmonth.py
```
具体使用说明如下:
# 3.官方使用说明
```bash
# Edit this file to introduce tasks to be run bycron.
通过编辑这个文件来使定时程序运行特定的任务。
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
每行只能定义一个任务，并通过一些特定的字段来指示如何运行这个任务。
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
你可以通过如下字段来指定任务运行的时间：
m:分钟，h:小时，dom:每月的第几天，mon:月份，dow:每星期的第几天，
*:任意（分钟，小时等）。
使用格式：m h dom mon dow 命令
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
需要注意的是，
定义在此的所有定时任务的时间都基于当前定时任务系统的时区与时间。
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
除非用户重定向邮件发送对象，
所有定时任务的日志输出（包括错误）
都将通过邮件发送给这个crontab文件所归属的用户
邮件目录：/var/mail/
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
比如，如果你想在每周一的上午五点钟备份你的账户，你可以写下如下代码：
0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# For more information see the manual pages of crontab(5) and cron(8)
更多信息请查找帮助手册
# m h  dom mon dow   command
```

