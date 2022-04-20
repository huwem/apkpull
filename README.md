# apkpull
用于获取移动设备某文件夹下的全部.apk文件

环境    
python3     
adb连接

usage:    
使用方法：

1.python3 apkpull.py 
寻找文件夹/system/priv-app内的全部.apk文件然后临时保存于移动设备文件夹/data/local/tmp/APKs，并把/data/local/tmp/APKs复制到电脑上当前文件夹。

2.python3 apkpull.py SourceDir DestDir
寻找文件夹SourceDir内的全部.apk文件然后临时保存于移动设备文件夹/data/local/tmp/APKs，并把/data/local/tmp/APKs复制到电脑上的文件夹DestDir。

3.python3 apkpull.py SourceDir DestDir APKDir
寻找文件夹SourceDir内的全部.apk文件然后临时保存于移动设备文件夹APKDir，并把APKDir复制到电脑上文件夹DestDir

最后可以选择是否清除在手机中产生的缓存文件夹，输入y清理，输入n退出
