
# Water Level Detection in Images

This project demonstrates a simple method to detect the water level in an image of a water bottle using OpenCV. The script reads an image, processes it to detect contours, and calculates the water level as a percentage of the bottle's height.

## Requirements

To run this code, you'll need the following:

- Python 3.x
- OpenCV (`cv2`)
- Numpy (`numpy`)

Install the required libraries using:

```bash
pip install opencv-python numpy


Share


You said:
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


this code create a readme.md file
ChatGPT said:
ChatGPT
Sure, here's a sample README.md file for your water level detection code:

markdown
Copy code
# Water Level Detection in Images

This project demonstrates a simple method to detect the water level in an image of a water bottle using OpenCV. The script reads an image, processes it to detect contours, and calculates the water level as a percentage of the bottle's height.

## Requirements

To run this code, you'll need the following:

- Python 3.x
- OpenCV (`cv2`)
- Numpy (`numpy`)

Install the required libraries using:

```bash
pip install opencv-python numpy
How It Works
Load Image: The code loads an image of a water bottle.
Convert to Grayscale: It converts the image to grayscale to simplify the processing.
Gaussian Blur: Gaussian blur is applied to reduce noise.
Thresholding: A binary threshold is applied to separate the bottle from the background.
Find Contours: Contours are found in the thresholded image, which represent potential water boundaries.
Calculate Water Level: The largest contour is considered the water. The bounding rectangle of this contour is used to calculate the water level as a percentage of the bottle's height.
Display Result: The detected contour and water level are displayed on the original image.
Usage
Place an image of a bottle in the images/ directory and name it bottle.jpg.

Run the script using:

python capture_img.py

The program will display the original image with the detected water level marked. The percentage of the water level will be printed in the console.
