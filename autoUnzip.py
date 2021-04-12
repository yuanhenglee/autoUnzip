import zipfile
from unrar import rarfile
import fnmatch,os,sys

def main(argv):
    # rootPath = r"C:\Users\user\Documents\1092\TA_PY\HW\1092_046001041_程式設計概論-【實作練習】檔案上傳區-329447"
    try:
        rootPath = argv[1] 
    except:
        print("PATH PLEASE~")

    print("input dir:",rootPath)

    # * DONE: fixing rar support
    for root, dirs, files in os.walk(rootPath):
        # for filename in fnmatch.filter(files, '*.zip'):
        for filename in files:
            filePath = os.path.join(root, filename)
            os.rename( filePath, filePath.encode('utf-8') )

            if zipfile.is_zipfile( filePath ):
                print("Extract ZIP:",filePath)
                try:
                    zipfile.ZipFile(filePath).extractall(root)
                    print( "SUCCESS!" )
                except Exception as e:
                    print(e)
                    _ = input( "FAIL...PRESS ANY KEY TO CONTINUE...")

            if rarfile.is_rarfile( filePath ):
                print("Extract RAR:",filePath)
                try:
                    rarfile.RarFile( filePath ).extractall( root )
                    print( "SUCCESS!" )
                except Exception as e:
                    print(e)
                    _ = input( "FAIL...PRESS ANY KEY TO CONTINUE...")

if __name__ == '__main__':
    main(sys.argv)