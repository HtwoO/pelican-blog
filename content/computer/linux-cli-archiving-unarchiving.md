title: Linux 命令行压缩解压
date: 2015-1-3
modified: 2015-9-5
slug: linux-cli-archiving-unarchiving
lang: zh
tags: Linux, CLI
author: Fonzie


[TOC]

## 压缩解压 zip 归档（压缩包）

由于 rar 有许可证问题，在给使用 Windows 的朋友发送归档文件的时候，我习惯使用 zip 格式。归档有几个方便的用途：打包多个文件和保持文件的时间戳，并有确保文件完整的作用，能解压的文件，通常是完整的，而如果文件不完整，往往归档坏了，就解压不了了。

在 Debian、Mint 或 Ubuntu 上安装 zip 压缩和解压工具，需要管理员权限：

    # apt-get update
    # apt-get install zip unzip

或者：

    $ sudo apt-get update && sudo apt-get install zip unzip

### 以下是一些常见用法的示例：

把 archive 目录里的文件打包到名为 archive.zip 的归档里，归档的名字可不带 zip 后缀：

    zip archive.zip archive/

把 archive 目录里的文件和所有子目录打包到名为 archive.zip 的归档里：

    zip -r archive.zip archive/
    zip --recurse-paths archive.zip archive/

解压 package.zip 文件到当前目录：

    unzip package.zip

检测归档文件完整性，并输出概要信息：

    zip -T package.zip
    zip --test package.zip  # 和以上命令等效
    unzip -tq package.zip
    unzip -t -q package.zip # 和以上命令等效

解压 package.zip 到 newdir 目录：

    unzip package.zip -d newdir/

列出 package.zip 里的文件列表：

    unzip -l package.zip

从归档里解压出名为 README.md 的文件：

    unzip package.zip README.md

其他用法：

    zip -e log.zip *.log    # 使用密码加密归档，会在命令行执行后提示输入
    zip -c log.zip *.log    # 加单行注释，会在命令行执行后提示输入
    zip -z log.zip *.log    # 加多行注释，会在命令行执行后提示输入，Ctrl + D 结束输入
    unzip -z log.zip        # 显示注释

更高级的用法，请查看命令 zip -h、unzip -h，或手册页 man zip、man unzip。

---

## 其他常见 Linux 归档格式

### tar.gz、tar.xz、tar.bz2

Linux 上的 tar.gz、tgz、tar.xz、tar.bz2 等多种归档格式，基本上都可以用 `tar` 来解压，这是几乎每个现代的 Linux 操作系统都有的工具。写本文的时候，Debian 8 里的 tar 版本是 1.27.1，支持 gz、bz2 和 xz 等归档格式。

打包为 tar.gz、tgz、tar.xz、tar.bz2、tbz2，（参数连在一起时？连接符「-」可省略）：

    tar -czvf mail.tar.gz Mail/
    tar czvf mail.tgz Mail/
    tar -cJvf mail.tar.xz Mail/
    tar -cjvf log.tar.bz2 *.log
    tar --create -j -v -f log.tbz2 *.log

解压 tar.gz、tar.xz、tar.bz2 归档：

    tar -xzvf log.tar.gz
    tar -xjvf log.tar.bz2
    tar -xJvf log.tar.xz

列出归档里的内容：

    tar -tjvf log.tar.bz2

tar 的参数比较多，但可以用以下方法记忆，先指定操作模式，再指定要操作的归档格式，后面加上 `vf` 输出操作过程详细信息，单加 `f` 不显示操作过程的输出信息。

可选的操作模式，必须选择其中一项，前面是选项的简写方式，后面是选项完整写法：

    -A, --catenate, --concatenate   追加 tar 文件至归档
    -c, --create               创建一个新归档
    -d, --diff, --compare      找出归档和文件系统的差异
        --delete               从归档(非磁带！)中删除
    -r, --append               追加文件至归档结尾
    -t, --list                 列出归档内容
        --test-label           测试归档卷标并退出
    -u, --update               仅追加比归档中副本更新的文件
    -x, --extract, --get       从归档中解出文件

需要操作的归档格式，选择和要操作的文件对应的选项，前面是选项的简写方式，后面是选项完整写法：

    -j, --bzip2                通过 bzip2 过滤归档
    -J, --xz                   通过 xz 过滤归档
        --lzip                 通过 lzip 过滤归档
        --lzma                 通过 xz 过滤归档
        --lzop
        --no-auto-compress     不使用归档后缀名来决定压缩程序
    -z, --gzip, --gunzip, --ungzip   通过 gzip 过滤归档
    -Z, --compress, --uncompress   通过 compress 过滤归档

### 压缩 gzip 或 bzip2：

    gzip *.pdf
    bzip2 *.pdf

结果会给当前目录每个 pdf 文件生成一个 `.pdf.gz` 或 `.pdf.bz2`（使用 bzip2 时）的归档，并删除原始 pdf 文件。

解压缩 gz 或 bz2：

    gzip *.pdf.gz
    bzip2 *.pdf.bz2

结果会解压缩当前目录每个 `.pdf.gz` 或 `.pdf.bz2`（使用 bzip2 时）归档，并删除原归档文件。

列出 gz 归档里的文件：

    gzip -l foo.gz
    gzip --list foo.gz
    gunzip -l foo.gz

测试 gz 归档完整性：

    gzip -tv foo.gz
    gzip --test --verbose foo.gz # 以上命令的完整版本
    gunzip -tv foo.gz

---

## 7z 和 rar 归档

7z 因其较高的压缩率，在 Windows 平台用的也蛮多的。rar 也因为归档某类文件时比 zip 略高的压缩率，在开始推出时很多人用（鄙人也用过），但因为版权问题，建议尽量避免使用 rar 格式。这里列出它们的压缩解压方式，以便收到人家发的此类归档时不致无法使用。

Debian 系列发行版里解压 7z 归档，需要安装 `p7zip` 软件包。要解压 rar 归档，需要先启用 non-free（非自由）软件仓库，然后安装 `unrar` 软件包。

    $ apt-get update
    $ apt-get install p7zip unrar

常用处理 7z 归档命令：

    7zr a mail.7z Mail/ # 把 Mail 目录归档到 mail.7z
    7zr a log.7z *.log  # 把所有 log 后缀的文件归档到 log.7z
    7zr x foo.7z        # 解压归档，保留归档里的目录结构
    7zr l foo.7z        # 列出归档里的文件列表
    7zr d foo.7z bar    # 删除归档里文件名为 bar 的文件
    7zr t foo.7z        # 检测归档文件完整性

更复杂用法请查看 `7zr --help`。

常用处理 rar 归档命令：

    unrar x foo.rar             # 解压归档，保留归档里的目录结构
    unrar x foo.rar testdir/    # 解压到 testdir 目录
    unrar l foo.rar             # 列出归档里的文件列表
    unrar t foo.rar             # 检测归档文件完整性

更复杂用法请查看 `unrar --help` 或 `unrar h`。

---

## 中文文件名乱码问题

来自 Windows 系统的归档文件解压后，文件名可能会出现乱码，这时可以使用以下命令来尝试改名（转码），`-f` 后是文件名的原始编码，`-t` 后面指定的是要转换成的编码，`-r` 表示递归处理所有子目录里的文件：

    convmv -f gbk -t utf8 -r dir/ # 预览改名效果

以上命令显示转码结果正确后，可加上 `--notest` 选项可实际进行改名（转码）操作：

    convmv --notest -f gbk -t utf8 -r dir/

linux-wiki.cn 的文章示意：「千万不要在 NTFS 或 FAT 文件系统上执行 convmv，否则极可能产生意外结果」，个人没有注意过这个问题。

## 参考资料

* 命令的帮助和手册页（manpage）

* [中文文件名乱码问题](http://linux-wiki.cn/wiki/中文文件名乱码问题)

* [压缩与解压](http://linux-wiki.cn/wiki/压缩与解压)

* [Zipping and Unzipping Files under Linux](http://www.cyberciti.biz/tips/how-can-i-zipping-and-unzipping-files-under-linux.html)

* [Compressing files under Linux or UNIX cheat sheet](http://www.cyberciti.biz/howto/question/general/compress-file-unix-linux-cheat-sheet.php)
