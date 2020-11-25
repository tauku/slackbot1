def still():
    import subprocess
    from subprocess import PIPE
    import cv2
    
    savedir = "/home/pi/slack-bot/slackbot/still_f"
    subprocess.run("sudo pkill -f motion", shell=True,)
    cam = cv2.VideoCapture(0)
    
    ret, stream = cam.read()
    stream = cv2.resize(stream, (320,240))
    
    #cv2.startWindowThread()
    #cv2.imshow("camera", stream)
    path = "./still_f/" + "data" + ".png"
    cv2.imwrite(path, stream) # ファイル保存
    cam.release()
    cv2.destroyAllWindows()
    
