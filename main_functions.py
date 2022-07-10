import os

def messagewebpage(usrmsg, name, usrpfp):
    message = open(os.getcwd() + "/HTTP_Root/text/message.txt", "w")
    message.write(usrmsg)
    message.close()
    usrname = open(os.getcwd() + "/HTTP_Root/text/user.txt", "w")
    usrname.write(name)
    usrname.close()
    avatarurl = open(os.getcwd() + "/HTTP_Root/text/imageurl.txt", "w")
    avatarurl.write(str(usrpfp))
    avatarurl.close()