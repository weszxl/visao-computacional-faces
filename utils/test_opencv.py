import cv2
import numpy as np

image = np.zeros((300, 300, 3), dtype="uint8")
cv2.putText(image, "('-')", (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow("test", image)
cv2.waitKey(0)
cv2.destroyAllWindows()



