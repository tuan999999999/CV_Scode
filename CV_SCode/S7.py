import cv2
import numpy as np

# Đọc ảnh từ tệp tin
input_image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Kiểm tra xem ảnh đã đọc có tồn tại không
if input_image is None:
    print("Không thể đọc ảnh. Hãy đảm bảo rằng tệp tin 'input.jpg' tồn tại.")
else:
    # Tạo kernel Prewitt theo hướng ngang và dọc
    kernel_x = np.array([[-1, 0, 1],
                         [-1, 0, 1],
                         [-1, 0, 1]])

    kernel_y = np.array([[-1, -1, -1],
                         [0, 0, 0],
                         [1, 1, 1]])

    # Áp dụng bộ lọc Prewitt theo hướng ngang và dọc
    prewitt_x = cv2.filter2D(input_image, -1, kernel_x)
    prewitt_y = cv2.filter2D(input_image, -1, kernel_y)

    # Kết hợp biểu đồ gradient từ cả hai hướng
    gradient_magnitude = cv2.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)

    # Hiển thị ảnh gốc và biểu đồ gradient Prewitt
    cv2.imshow('Ảnh Gốc', input_image)
    cv2.imshow('Biểu đồ Gradient Prewitt', gradient_magnitude)

    # Lưu biểu đồ gradient Prewitt thành một tệp tin mới
    cv2.imwrite('output_prewitt.jpg', gradient_magnitude)

    # Chờ người dùng nhấn phím bất kỳ để thoát
    cv2.waitKey(0)
    cv2.destroyAllWindows()
