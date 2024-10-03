# This code detect a water level only for images

import cv2
import numpy as np

# Load the image of the bottle
image = cv2.imread('images/bottle.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply thresholding to create a binary image
_, thresholded = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Calculate the water level by finding the largest contour area (assuming water is the largest area)
if contours:
    largest_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), ( 0, 0, 255), 2)

    # Water level as a percentage of the bottle height
    water_level_percentage = (image.shape[0] - y - h) / image.shape[0] * 100
    print(f'Water Level: {water_level_percentage:.2f}%')

# Display the result
cv2.imshow('Water Level Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
