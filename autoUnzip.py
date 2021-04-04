
import zipfile,fnmatch,os,sys

def main(argv):
    # rootPath = r"C:\Users\user\Documents\1092\TA_PY\HW\1092_046001041_程式設計概論-【實作練習】檔案上傳區-329447"
    try:
        rootPath = (argv[1]) 
    except:
        print("PATH PLEASE~")


    pattern = '*.zip'

    print("input dir:",rootPath)


    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print(os.path.join(root, filename))
            # zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(root, os.path.splitext(filename)[0]))
            zipfile.ZipFile(os.path.join(root, filename)).extractall(root)

if __name__ == '__main__':
    main(sys.argv)