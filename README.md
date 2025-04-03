# CornerSense-Moravec-and-Harris-Detection-Performance-Analysis
Project Description:
The project implements and compares two corner detection algorithms:

Moravec Corner Detection: Identifies corners by analyzing intensity variations within a small window in four directions (horizontal, vertical, and diagonal). A pixel is marked as a corner if the minimum intensity variation surpasses a predefined threshold.

Harris Corner Detection: Employs image gradients to construct a structure tensor and calculates a "cornerness" measure from eigenvalues. Corners are robustly identified by significant intensity variation in all directions.

Comparison and Analysis include:
Number of Detected Corners: Moravec detects fewer corners due to directional sensitivity; Harris captures more details using eigenvalue analysis.

Corner Distribution: Moravec finds only highly distinctive features; Harris offers a more uniform and detailed corner distribution.

Robustness to Noise: Moravec is sensitive to noise, while Harris is more robust due to gradient smoothing (Gaussian filter).

Computational Efficiency: Moravec is faster and simpler, suitable when speed is prioritized. Harris is computationally heavier but delivers greater accuracy and robustness.

![chess](https://github.com/user-attachments/assets/46cbf5a1-f675-487b-afff-2cce89dd204e)
![harris detection](https://github.com/user-attachments/assets/9b1a67ea-fb43-443a-92f7-6b62d7321e9f)
![detection moravec vs harris](https://github.com/user-attachments/assets/e41667f7-9fe7-4ef3-b528-1a8627a9b812)
![moravec detection](https://github.com/user-attachments/assets/7de2c2ee-f1bb-41e7-8215-81cea07e5371)
