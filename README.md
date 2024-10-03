
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

## Requirements

To run this code, you'll need the following:

- Python 3.x
- OpenCV (`cv2`)
- Numpy (`numpy`)

Install the required libraries using:

```bash
pip install opencv-python numpy

# How It Works
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
