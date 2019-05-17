import subprocess as sp
import requests
import cv2
import numpy

x=sp.getoutput("cat /run/media/root/BA66-832E/pd.txt")
y=sp.getoutput("pwd")
url=x

while True:
    data=requests.get(url)
    myphoto=data.content
    myphoto_a=bytearray(myphoto)
    photo_1d=numpy.array(myphoto_a)
    photo_3d=cv2.imdecode(photo_1d, -1)
    cv2.imshow('stream',photo_3d)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()


print(x)
print(y)
