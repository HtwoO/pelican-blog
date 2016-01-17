Maya Plugin Development
##########################################################
:date: 2015-8-18
:modified: 2016-1-17
:slug: maya-plugin-development
:lang: zh
:tags: CGI, Maya
:author: Fonzie

Below is compiler requirement for plugin development for the three latest version of Autodesk Maya.

Compiler requirement for Maya 2016

- Linux: gcc 4.4.7, RHEL(CentOS) 6.5, DTS(Developer Toolset) 2.1
 
- Mac OS X: Mavericks 10.9.5, Xcode 6.1.1, SDK 10.9, clang with libstdc++

- Windows: Visual Studio 2012 update 4

For Maya 2015

- Linux: gcc 4.1.2, RHEL(CentOS) 6.2, Fedora 14

- Mac OS X: Mountain Lion 10.8.5, Xcode 5.0.2, SDK 10.8, clang with libstdc++

- Windows: Visual Studio 2012 update 4

For Maya 2014

- Linux: gcc 4.1.2, RHEL(CentOS) 6.0, Fedora 14

- Mac OS X: Snow Leopard 10.6.8, Xcode 3.2.1, gcc 4.2.1

- Windows: Visual Studio 2010 SP1


Steps to setup Visual Studio 2010 Express edition to compile maya plugin.

1. Install vs2010 express.

2. Confirm that there is no newer C++ redistribution/runtime than ones in WinSDK 7.1. If newer ones exists in the system, WinSDK 7.1 will fail when install.

3. Confirm that there is no newer C++ redistribution/runtime than ones in WinSDK 7.1. If newer ones exists in the system, WinSDK 7.1 will fail when install.

4. Install vs2010 sp1

5. Install vs2010 patch `VC-Compiler-KB2519277`_ (1).

::

    Note(1) patch checksum: 
        File: VC-Compiler-KB2519277.exe
        Size: 126887272 bytes
        File Version: 10.0.40219.303
        Modified: 2011.3.15, 12:53:07
        MD5: 485B2C95B20961B031D2CE0A717461DD
        SHA1: 0EF28CF05F9F6AD71167D99BE3446F267686F89B
        CRC32: B0903D05

.. _`VC-Compiler-KB2519277`: https://support.microsoft.com/en-us/kb/2519277

