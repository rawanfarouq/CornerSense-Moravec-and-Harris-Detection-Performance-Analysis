import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the chess image
image = cv2.imread('chess.png', cv2.IMREAD_GRAYSCALE)

# Function: Moravec Corner Detection
def moravec_corner_detection(image, threshold=100):
    corners = []
    height, width = image.shape
    window_size = 3
    offset = window_size // 2

    for y in range(offset, height - offset):
        for x in range(offset, width - offset):
            region = image[y-offset:y+offset+1, x-offset:x+offset+1]
            intensities = [
                np.sum((region - np.roll(region, shift, axis=axis))**2)
                for shift, axis in [(1, 0), (-1, 0), (1, 1), (-1, 1)]
            ]
            if min(intensities) > threshold:
                corners.append((x, y))
    return corners

# Function: Harris Corner Detection
def harris_corner_detection(image, k=0.04, threshold=1e6):
    # Compute gradients
    Ix = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    Iy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    
    # Compute structure tensor components
    Ixx = Ix**2
    Iyy = Iy**2
    Ixy = Ix * Iy

    # Apply Gaussian filter to smooth
    Ixx = cv2.GaussianBlur(Ixx, (3, 3), 1)
    Iyy = cv2.GaussianBlur(Iyy, (3, 3), 1)
    Ixy = cv2.GaussianBlur(Ixy, (3, 3), 1)

    # Harris response calculation
    harris_response = (Ixx * Iyy - Ixy**2) - k * (Ixx + Iyy)**2
    
    # Threshold and extract corners
    corners = np.argwhere(harris_response > threshold)
    return corners[:, [1, 0]]  # Reverse (y, x) to (x, y)

# Detect corners using both methods
moravec_corners = moravec_corner_detection(image, threshold=100)
harris_corners = harris_corner_detection(image, threshold=1e6)

# Visualization: Moravec Corners
plt.figure(figsize=(10, 10))
plt.imshow(image, cmap='gray')
plt.scatter(*zip(*moravec_corners), color='red', s=10, label='Moravec Corners')
plt.legend()
plt.title('Moravec Corner Detection')
plt.show()

# Visualization: Harris Corners
plt.figure(figsize=(10, 10))
plt.imshow(image, cmap='gray')
plt.scatter(harris_corners[:, 0], harris_corners[:, 1], color='green', s=10, label='Harris Corners')
plt.legend()
plt.title('Harris Corner Detection')
plt.show()

# Visualization: Both Corners Together
plt.figure(figsize=(10, 10))
plt.imshow(image, cmap='gray')
plt.scatter(*zip(*moravec_corners), color='red', s=10, label='Moravec Corners')
plt.scatter(harris_corners[:, 0], harris_corners[:, 1], color='green', s=10, label='Harris Corners')
plt.legend()
plt.title('Corner Detection (Moravec: Red, Harris: Green)')
plt.show()
