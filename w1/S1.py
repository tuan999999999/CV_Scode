import cv2
import numpy as np

# Đọc ảnh từ tệp tin
input_image = cv2.imread('input.jpg')

# Kiểm tra xem ảnh đã đọc có tồn tại không
if input_image is None:
    print("Không thể đọc ảnh. Hãy đảm bảo rằng tệp tin 'input.jpg' tồn tại.")
else:
    # Kích thước của bộ lọc trung bình (độ lớn của kernel)
    kernel_size = 5

    # Áp dụng bộ lọc trung bình
    output_image = cv2.blur(input_image, (kernel_size, kernel_size))

    # Hiển thị ảnh gốc và ảnh sau khi áp dụng bộ lọc trung bình
    cv2.imshow('Ảnh Gốc', input_image)
    cv2.imshow('Ảnh sau khi áp dụng bộ lọc trung bình', output_image)

    # Lưu ảnh sau khi áp dụng bộ lọc trung bình thành một tệp tin mới
    cv2.imwrite('output1_tb.jpg', output_image)

    # Chờ người dùng nhấn phím bất kỳ để thoát
    cv2.waitKey(0)
    cv2.destroyAllWindows()
