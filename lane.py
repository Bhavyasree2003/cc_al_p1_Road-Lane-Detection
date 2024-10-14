# Install OpenCV if not already installed
!pip install opencv-python-headless

# Import necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()
image_path = list(uploaded.keys())[0] 
def color_selection(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 25, 255])
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    mask_white = cv2.inRange(hsv, lower_white, upper_white)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask = cv2.bitwise_or(mask_white, mask_yellow)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result
def detect_lanes(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    return edges
def region_of_interest(image):
    height, width = image.shape[:2]
    mask = np.zeros_like(image)
    polygon = np.array([[(0, height), (width, height), (width, height // 2), (0, height // 2)]])
    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image
def hough_lines(image):
    lines = cv2.HoughLinesP(image, 1, np.pi / 180, threshold=50, minLineLength=100, maxLineGap=50)
    line_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 3)  
    return line_image
def process_image(image_path):
    image = cv2.imread(image_path)
    color_selected = color_selection(image)
    edges = detect_lanes(color_selected)
    masked_image = region_of_interest(edges)
    line_image = hough_lines(masked_image)
    result = cv2.addWeighted(image, 1, line_image, 1, 0)
    plt.figure(figsize=(15, 10))
    plt.subplot(231)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')
    plt.subplot(232)
    plt.imshow(cv2.cvtColor(color_selected, cv2.COLOR_BGR2RGB))
    plt.title("Color Selected Image")
    plt.axis('off')
    
    plt.subplot(233)
    plt.imshow(edges, cmap='gray')
    plt.title("Canny Edge Detection")
    plt.axis('off')
    
    plt.subplot(234)
    plt.imshow(masked_image, cmap='gray')
    plt.title("Masked Image")
    plt.axis('off')
    
    plt.subplot(235)
    plt.imshow(cv2.cvtColor(line_image, cv2.COLOR_BGR2RGB))
    plt.title("Detected Lane Lines")
    plt.axis('off')
    
    plt.subplot(236)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title("Result with Lane Lines")
    plt.axis('off')
    
    plt.show()
process_image(image_path)
