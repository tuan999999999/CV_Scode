import cv2

# Đọc ảnh từ tệp tin
input_image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Kiểm tra xem ảnh đã đọc có tồn tại không
if input_image is None:
    print("Không thể đọc ảnh. Hãy đảm bảo rằng tệp tin 'input.jpg' tồn tại.")
else:
    # Áp dụng bộ lọc Sobel
    sobel_x = cv2.Sobel(input_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(input_image, cv2.CV_64F, 0, 1, ksize=3)

    # Tính toán biểu đồ gradient và hợp nhất biểu đồ gradient
    gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)
    gradient_magnitude = cv2.convertScaleAbs(gradient_magnitude)

    # Hiển thị ảnh gốc và biểu đồ gradient
    cv2.imshow('Ảnh Gốc', input_image)
    cv2.imshow('Biểu đồ Gradient', gradient_magnitude)

    # Lưu biểu đồ gradient thành một tệp tin mới
    cv2.imwrite('output_sobel.jpg', gradient_magnitude)

    # Chờ người dùng nhấn phím bất kỳ để thoát
    cv2.waitKey(0)
    cv2.destroyAllWindows()

