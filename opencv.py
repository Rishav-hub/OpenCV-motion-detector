import cv2
import glob

images=glob.glob("*.jpg")
print(images)
for image in images:
    img=cv2.imread(image,0)

    resized_image=cv2.resize(img,(100,100))
    cv2.imshow("Galaxy",resized_image)
    cv2.waitKey(4000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,resized_image)
