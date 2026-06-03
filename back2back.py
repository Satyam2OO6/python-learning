import cv2
import glob
imges=glob.glob("*.jpg")

for image in imges:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(500,500))
    cv2.imshow("hay",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized"+image,re)

