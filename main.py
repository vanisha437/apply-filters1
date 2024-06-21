import cv2

inputPath = 'static/img1.jpg'

originalImage = cv2.imread(inputPath)

# ------------Convert image to Grayscale --------------

# Convert the color image to grayscale image
grayscaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

# # ----------------- Convert image to Sketch Image ---------------

# Invert the grayscale image
invertedImg = 255 - grayscaleImage

# Apply Gaussian blur
blurredImg = cv2.GaussianBlur(invertedImg, (21, 21), 0)

# Blend the grayscale image and the blurred image using the color dodge blend mode
sketchImg = cv2.divide(grayscaleImage, 255 - blurredImg, scale=256)

# Save the sketch image to disk
outputPath = 'converted/sketch.png'
cv2.imwrite(outputPath, sketchImg)

# Display the converted image
cv2.imshow('Sketch Image', sketchImg)
cv2.waitKey(0)

# Display a message indicating that the image has been saved