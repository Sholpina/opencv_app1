import cv2 as cv
print( cv.__version__ )

# Load an color image in grayscale
# Path
path = 'Photos/candy1.jpg'
  
# Reading an image in default mode
image = cv.imread(path)
  
# Naming a window
cv.namedWindow("Resized_Window", cv.WINDOW_NORMAL)

# Using resizeWindow()
cv.resizeWindow("Resized_Window", 427, 427)
  
# Displaying the image
cv.imshow("Resized_Window", image)
cv.waitKey(0)



