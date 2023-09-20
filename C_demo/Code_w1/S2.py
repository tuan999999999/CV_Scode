import cv2
import numpy as np

# Đọc ảnh từ tệp tin
input_image = cv2.imread('input.jpg')

# Kiểm tra xem ảnh đã đọc có tồn tại không
if input_image is None:
    print("Không thể đọc ảnh. Hãy đảm bảo rằng tệp tin 'input.jpg' tồn tại.")
else:
    # Kích thước của kernel Gaussian
    kernel_size = (5, 5)

    # Độ lệch chuẩn (sigma) của kernel Gaussian
    sigma = 1.0

    # Áp dụng bộ lọc Gaussian
    output_image = cv2.GaussianBlur(input_image, kernel_size, sigma)

    # Hiển thị ảnh gốc và ảnh sau khi áp dụng bộ lọc Gaussian
    cv2.imshow('Ảnh Gốc', input_image)
    cv2.imshow('Ảnh sau khi áp dụng bộ lọc Gaussian', output_image)

    # Lưu ảnh sau khi áp dụng bộ lọc Gaussian thành một tệp tin mới
    cv2.imwrite('output_gaussian.jpg', output_image)

    # Chờ người dùng nhấn phím bất kỳ để thoát
    cv2.waitKey(0)
    cv2.destroyAllWindows()
