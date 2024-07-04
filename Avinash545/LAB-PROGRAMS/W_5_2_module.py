import numpy as np
import cv2

# Create a blank image
img = np.zeros((400, 400, 3), dtype="uint8")

# Draw a rectangle
cv2.rectangle(img, (30, 30), (300, 200), (0, 20, 200), 10)

# Display the image
cv2.imshow('Window', img)

# Wait for a key press
cv2.waitKey(0)

# Destroy the window
cv2.destroyAllWindows()
