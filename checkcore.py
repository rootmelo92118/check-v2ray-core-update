import os,urllib.request,json,zipfile,argparse,wget

def switchs(resourcePath,executableFilePath,version):
    try:
        with urllib.request.urlopen("https://api.github.com/repos/v2fly/v2ray-core/releases/latest") as url:
            data = json.loads(url.read().decode()) 
        if os.path.isfile(executableFilePath):   
            try:
                localVersion = "v" + os.popen(executableFilePath + " -version").readlines()[0].split(" ")[1]
            except PermissionError:
                print("Permission Error")
                return "Permission Error"
            except Exception as e:
                print(e)
            try:
                if data["tag_name"] == localVersion:
                    print("The v2ray core version is the latest.")
                    return "The v2ray core version is the latest."
                else:
                    updater(resourcePath,executableFilePath,version,data["tag_name"])
            except:
                updater(resourcePath,executableFilePath,version,data["tag_name"])
        else:
            initalize(resourcePath,executableFilePath,version,data["tag_name"])
    except Exception as e:
        print(e)

def initalize(resourcePath,executableFilePath,version,tagName):
    try:
        if "windows" in version and "\\" in executableFilePath:
            pathList = executableFilePath.split("\\")
            del pathList[-1]
            exepath = ""
            for i in pathList:
                exepath = exepath + i + "\\"
        elif "windows" in version:
            pathList = executableFilePath.split("/")
            del pathList[-1]
            exepath = ""
            for i in pathList:
                exepath = exepath + i + "/"
        else:
            pathList = executableFilePath.split("/")
            del pathList[-1]
            exepath = "/"
            for i in pathList:
                exepath = exepath + i + "/"
        os.chdir(exepath)
        if os.path.isfile("v2ray.zip"):
            os.remove("v2ray.zip")
        url = "https://github.com/v2fly/v2ray-core/releases/download/"+tagName+"/"+version+".zip"
        wget.download(url,"v2ray.zip")
        print("")
        compressedFile = zipfile.ZipFile("v2ray.zip")
        compressedFile.extract("geoip-only-cn-private.dat",path=resourcePath)
        if "windows" in version:
            compressedFile.extract("v2ray.exe",path=".")
        else:
            compressedFile.extract("v2ray",path=".")
            os.chmod(executableFilePath,0o755)
        try:
            os.remove("v2ray.zip")
        except:
            pass
        os.chdir(resourcePath)
        geoResourceURL = ["https://github.com/Loyalsoldier/v2ray-rules-dat/releases/latest/download/geosite.dat","https://github.com/Loyalsoldier/v2ray-rules-dat/releases/latest/download/geoip.dat"]
        wget.download(geoResourceURL[0],"geosite.dat")
        print("")
        wget.download(geoResourceURL[1],"geoip.dat")
        print("")
        print("Update successful")
        return "Update successful"
    except Exception as e:
        print(e)

def updater(resourcePath,executableFilePath,version,tagName):
    try:
        if "windows" in version and "\\" in executableFilePath:
            pathList = executableFilePath.split("\\")
            del pathList[-1]
            exepath = ""
            for i in pathList:
                exepath = exepath + i + "\\"
        elif "windows" in version:
            pathList = executableFilePath.split("/")
            del pathList[-1]
            exepath = ""
            for i in pathList:
                exepath = exepath + i + "/"
        else:
            pathList = executableFilePath.split("/")
            del pathList[-1]
            exepath = "/"
            for i in pathList:
                exepath = exepath + i + "/"
        os.remove(resourcePath+"/geoip-only-cn-private.dat")
        os.chdir(exepath)
        if os.path.isfile("v2ray.zip"):
            os.remove("v2ray.zip")
        if "windows" in version:
            os.remove("v2ray.exe")
        else:
            os.remove("v2ray")
        url = "https://github.com/v2fly/v2ray-core/releases/download/"+tagName+"/"+version+".zip"
        wget.download(url,"v2ray.zip")
        print("")
        compressedFile = zipfile.ZipFile("v2ray.zip")
        compressedFile.extract("geoip-only-cn-private.dat",path=resourcePath)
        if "windows" in version:
            compressedFile.extract("v2ray.exe",path=".")
        else:
            compressedFile.extract("v2ray",path=".")
            os.chmod(executableFilePath,0o755)
        try:
            os.remove("v2ray.zip")
        except:
            pass
        os.chdir(resourcePath)
        os.remove("geoite.dat")
        os.remove("geoip.dat")
        geoResourceURL = ["https://github.com/Loyalsoldier/v2ray-rules-dat/releases/latest/download/geosite.dat","https://github.com/Loyalsoldier/v2ray-rules-dat/releases/latest/download/geoip.dat"]
        wget.download(geoResourceURL[0],"geosite.dat")
        print("")
        wget.download(geoResourceURL[1],"geoip.dat")
        print("")
        print("Update successful")
        return "Update successful"
    except Exception as e:
        print(e)

def get_parser():
    parser = argparse.ArgumentParser(description='A script to check and update v2ray-core.')
    parser.add_argument('-r', '--resource', type=str, help="The location you put resource files. (geosite.dat, geoip.dat, etc.)")
    parser.add_argument('-e', '--executableFile', type=str, help="The location you put v2ray-core.")
    parser.add_argument('-v', '--version', type=str, help="The version matches your system and CPU architecture. Please be sure you input the correct version, or it will not be executed successfully. The format is the file name without the \".zip\" suffix download v2ray-core on GitHub. (e.g.: v2ray-windows-64, v2ray-macos-arm64-v8a, etc)")
    return parser
    
try:
    parser = get_parser()
    args = parser.parse_args()
    switchs(args.resource,args.executableFile,args.version)
except Exception as e:
    print(e)
