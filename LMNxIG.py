import os,sys,platform,time
limon = platform.architecture()[0]
if limon == '64bit':import LMNxIG
elif limon == '32bit':
    os.system("clear")
    os.system('xdg-open http://t.me/+Q06RbESuEsE2MDFl')
    time.sleep(3)
    sys.exit("\n</> Your Device Is Not Supported For Run This Tool..!")
else:
    os.system("clear")
    sys.exit("\n</> Something Went Wrong..! Try Again")
    