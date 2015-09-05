title: dd 操作进度显示
date: 2014-12-21
modified: 2015-9-5
slug: dd-progress-monitoring
tags: Linux, CLI
author: Fonzie


最近在帮朋友从 U 盘安装 Linux，这么好的推广自由软件的机会，怎么能放过。但在 Windows 尝试了 n 个方法之后，依然没能做出一个可作为安装介质的 U 盘，然后只能依靠好老（Good old）的 dd 咯。但使用 `dd` 命令操作时，在命令完成以前，默认没有任何输出信息，看不到执行的进度，不太方便。那句话怎么说来着：["All mail clients suck. This one just sucks less."](http://www.mutt.org/)，这里应该说 All other tools suck. dd just suck less。在网上查找了一下怎么给 dd 加进度显示，让 dd 用户体验更好些。

这次我第二次需要这么做了，本着 DRY（Don't Repeat Yourself，不要重复学习）的原则，把方法记录在博客里，以防以后再次用到。

可以使用 `pv`（Pipe Viewer）来查看 Unix [管道](https://zh.wikipedia.org/zh/管道_(Unix))的数据传输情况，把 dd 的输入输出部分分开。此方法需要系统里安装有 pv，然后执行如下命令：

    dd if=/dev/urandom | pv | dd of=/dev/null

输出类似：

    记录了131452+0 的读入MiB/s] [    <=>            ]
    记录了131452+0 的写出
    记录了131453+0 的读入
    记录了131452+0 的写出
    67303424字节(67 MB)已复制67303424字节(67 MB)已复 制，5.92668 秒，11.4 MB/秒

延伸一下，`pv` 可以用于其他情况，比如查看校验码检测的进度：

    pv /home/user/bigfile.iso | md5sum

以下方法，可以在 dd 命令已经启动后，在一个新的终端里执行，dd 的操作进度会在原终端更新：

    sudo kill -USR1 $(pgrep ^dd)

比如，执行：

    dd if=/dev/zero of=/dev/null count=10MB

输出如下：

    记录了9509217+0 的读入
    记录了9509216+0 的写出
    4868718592字节(4.9 GB)已复制，5.17436 秒，941 MB/秒
    记录了10000000+0 的读入
    记录了10000000+0 的写出
    5120000000字节(5.1 GB)已复制，5.44257 秒，941 MB/秒

还可以用 `watch` 命令直接观察输出文件的大小变化：

    watch ls -l /pathtofile/filename

更华丽的办法是配合使用 `dialog`，显示一个字符界面的进度条对话框：

    (pv -n /dev/sdx | dd of=/dev/sdy bs=128M conv=notrunc,noerror) 2>&1 | dialog --gauge "正在使用 dd 克隆，请稍候…" 10 70 0

参考文章：

* [How do you monitor the progress of dd?](http://askubuntu.com/questions/215505/how-do-you-monitor-the-progress-of-dd)

* [Linux dd Command Show Progress Copy Bar With Status](http://www.cyberciti.biz/faq/linux-unix-dd-command-show-progress-while-coping/)
