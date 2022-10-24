# let's start with the Imports 
import cv2 as cv
print( cv.__version__ )

path = 'Photos/candy1.jpg'
  
# Read the image using imread function
image = cv.imread(path)
  
# Naming a window
cv.namedWindow("Resized_Window", cv.WINDOW_NORMAL)

# Using resizeWindow()
cv.resizeWindow("Resized_Window", 427, 427)
  
# Displaying the image
cv.imshow("Resized_Window", image)
cv.waitKey(0)

# Saving the Image as it is with another name
cv.imwrite("my-dog.jpg",image)

# Convert the image to grayscale and save it
gray_image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imwrite("dog-greyscale.jpg",gray_image)

# Change the type of the image file
cv.imwrite("mydog.png",image)

# Resize the image using resize() function (Upscale with resize()
# If providing a value >100 it will upscale the image.)
scale_percent = 35 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv.resize(image, dim, interpolation = cv.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv.imshow("Resized image", resized)
cv.waitKey(0)

# Cropping an image
cropped_image = image[80:280, 150:330]
 
# Display cropped image
# Чтобы разрезать массив, нужно указать начальный и конечный индексы первого, а также второго измерения. 
# The first dimension is always the number of rows or the height of the image.
# The second dimension is the number of columns or the width of the image. 
cv.imshow("cropped", cropped_image) # Slicing to crop the image
 
# Save the cropped image
cv.imwrite("Cropped Image.jpg", cropped_image)
 
cv.waitKey(0)
cv.destroyAllWindows()

#press any key to close the windows
cv.destroyAllWindows()
