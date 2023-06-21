# cc_al_p1_Road-Lane-Detection
Codeclause: Artificial Intellegence Intern 
# Task-1
 
 Task-1 Road-Lane-Detection
***************************
What is Lane Detection?
Lane detection is the process of identifying the lane boundaries on the road. It is an essential task for autonomous driving systems and driver assistance systems.
These systems use sensors, cameras, and computer vision algorithms to detect lane markings and determine the vehicle’s position relative to the lane boundaries.

Lane Detection Techniques
**************************
Lane detection involves identifying and tracking lanes on the road using computer vision techniques. Here are some commonly used techniques for accurate lane detection:

1.Edge Detection: By detecting the boundaries of objects in an image, edge detection helps distinguish lanes from the surrounding environment. The Canny edge detector is a popular algorithm for this task.

2.Hough Transform: The Hough Transform is used to detect lines in an image. It converts the image space into a parameter space and can accurately detect straight lines. The Probabilistic Hough Transform is often preferred for lane detection due to its efficiency and robustness.

3.Region of Interest (ROI) Selection: Defining a region of interest allows us to focus on the relevant portion of the image where lanes are expected. By limiting the detection process to this area, we improve accuracy and eliminate unwanted features.

4.Perspective Transformation: Perspective transformation provides a bird’s-eye view of the road, improving lane detection accuracy. By applying geometric transformations, we can transform the image from the driver’s viewpoint to a top-down view, removing perspective distortions.

5.Color Filtering and Thresholding: Lanes often have distinct colors compared to the road and surroundings. Color filtering and thresholding techniques isolate the lane markings based on their color properties, making it easier to detect and track them.

6.Machine Learning and Deep Learning: These techniques involve training models on annotated images to learn lane features and patterns. Machine learning algorithms, such as Convolutional Neural Networks (CNNs), have shown promising results in lane detection, achieving high accuracy and robustness.

USAGE
*********
!pip install -q opencv-python

To run the project:
*********************
To run this project in Jupyter Notebook, you can follow these steps:

1.Open Jupyter Notebook in your web browser.

2.Create a new notebook or open an existing one.

3.Copy and paste the code into a code cell in the notebook.

4.Save the image file 'road.jpg' in the same directory as your notebook file.

5.Run the code cell by clicking the "Run" button or using the Shift + Enter keyboard shortcut.

6.The code will be executed, and the output image with the detected lane lines will be displayed below the code cell

7.The code will execute and display the result in the notebook's output. If you encounter any errors or issues, make sure you have the required libraries installed and that the image file is accessible.

Lane Detection using OpenCV and Python
****************************************************************
In this section, we will explore how to detect lanes using OpenCV and Python. We will use edge detection and the Hough transform to detect the lanes.

Step 1: Import Libraries

Step 2: Read the Image

Step 3: Convert Image to Grayscale

Step 4: Apply Gaussian Blur

Step 5: Detect Edge Using Canny

Step 6: Region of Interest

Step 7: Hough Transform

Step 8: Draw Lines on the Image

Step 9: Overlaying the Lines on the Original Image

Step 10: Display Result
