import matplotlib.pyplot as plt
import cv2

print("Hello World")

img = cv2.imread("/root/yum.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


plt.figure()
plt.imshow(img)
plt.title("The Most Beautiful Bowl of Noodles")
plt.axis('off')
plt.show()
