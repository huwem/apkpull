# -*- coding: utf-8 -*-
# python3
import sys
import subprocess

#默认值
SourceDir ="/system/priv-app"
DestDir = "."
APKDir = "/data/local/tmp/APKs"

if len(sys.argv)>4 or len(sys.argv)==2:
    print("参数数量错误，正在退出...")
    exit(1)

#读取命令行参数
if len(sys.argv) >= 3 :
    SourceDir = sys.argv[1]
    DestDir = sys.argv[2]
if len(sys.argv) == 4:
    APKDir = "/"+sys.argv[3]+"/APKs"

#命令字符串
Pullcmd = "adb pull "+APKDir+" "+DestDir
cmd = ["adb shell","su","cd "+SourceDir,"mkdir "+APKDir,'''find . -name "*.apk" -type f -exec cp {} '''+APKDir+''' \\;''',"exit","exit"]
Clrcmd=["adb shell","su","rm -rf "+APKDir]

def PullFile(pullcmd):
    print(pullcmd)
    print("start pulling")
    s = subprocess.Popen(str(pullcmd+"\r\n"), stderr=subprocess.PIPE, stdin=subprocess.PIPE,stdout=subprocess.PIPE, shell=True)
    stderrinfo, stdoutinfo = s.communicate()
    if str(stderrinfo,encoding="utf-8").split(":")[1] == " error":
        print(str(stderrinfo, encoding="utf-8"))
        print("发生错误，正在退出...")
        exit(1)
    s.wait()
    return s.returncode

def Run():
    print(cmd[0])
    s = subprocess.Popen(str(cmd[0]+"\r\n"), stderr=subprocess.PIPE, stdin=subprocess.PIPE,stdout=subprocess.PIPE, shell=True)
    
    for i in range(1,len(cmd)):
        print(cmd[i])
        s.stdin.write(str(cmd[i]+"\r\n").encode())
        s.stdin.flush() 
     
    stderrinfo, stdoutinfo = s.communicate()
    print(str(stderrinfo,encoding="utf-8")+"\n"+str(stdoutinfo,encoding="utf-8"))
    return s.returncode

def Clear():
    print(cmd[0])
    s = subprocess.Popen(str(Clrcmd[0]+"\r\n"), stderr=subprocess.PIPE, stdin=subprocess.PIPE,stdout=subprocess.PIPE, shell=True)
    
    for i in range(1,len(Clrcmd)):
        print(Clrcmd[i])
        s.stdin.write(str(Clrcmd[i]+"\r\n").encode())
        s.stdin.flush() 
     
    stderrinfo, stdoutinfo = s.communicate()
    print(str(stderrinfo,encoding="utf-8")+"\n"+str(stdoutinfo,encoding="utf-8"))
    return s.returncode


if __name__ == "__main__":
    Run()
    PullFile(Pullcmd)
    print("pull finished")
    Choice = input("是否清理缓存文件夹（y/n)")
    while Choice!= "n":
        if Choice == "y":
            Clear()
            print("clear finished")
            exit(0)
        Choice = input("是否清理缓存文件夹（y/n)")
    print("正在退出...")
    exit(0)
