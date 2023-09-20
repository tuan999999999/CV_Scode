import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh đầu vào
image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Thực hiện biến đổi Fourier 2D
f_transform = np.fft.fft2(image)
f_transform_shifted = np.fft.fftshift(f_transform)

# Tính biểu đồ phổ (magnitude spectrum)
magnitude_spectrum = 20 * np.log(np.abs(f_transform_shifted))

# Hiển thị ảnh gốc và biểu đồ phổ
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Ảnh gốc'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Biểu đồ phổ'), plt.xticks([]), plt.yticks([])

# Lưu ảnh kết quả
cv2.imwrite('output_Fourier_Transform.jpg', magnitude_spectrum)

plt.show()
