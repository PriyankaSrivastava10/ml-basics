import os

c=125
imageList = os.listdir("images\\king")
#print(imageList)
for img in imageList:
    print (img)
    os.rename(os.path.join("images\\king", img), os.path.join("images\\king",str(c)+".jpg"))
    c=c+1
    print (img)
