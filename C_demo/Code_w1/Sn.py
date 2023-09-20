import cv2

# Đọc ảnh từ tệp tin
input_image = cv2.imread('input.jpg')

# Kiểm tra xem ảnh đã đọc có tồn tại không
if input_image is None:
    print("Không thể đọc ảnh. Hãy đảm bảo rằng tệp tin 'input.jpg' tồn tại.")
else:
    # Áp dụng bộ lọc Laplacian
    output_image = cv2.Laplacian(input_image, cv2.CV_64F)

    # Chuyển đổi kết quả về ảnh định dạng unsigned 8-bit
    output_image = cv2.convertScaleAbs(output_image)

    # Hiển thị ảnh gốc và ảnh sau khi áp dụng bộ lọc Laplacian
    cv2.imshow('Ảnh Gốc', input_image)
    cv2.imshow('Ảnh sau khi áp dụng bộ lọc Laplacian', output_image)

    # Lưu ảnh sau khi áp dụng bộ lọc Laplacian thành một tệp tin mới
    cv2.imwrite('output_laplacian.jpg', output_image)

    # Chờ người dùng nhấn phím bất kỳ để thoát
    cv2.waitKey(0)
    cv2.destroyAllWindows()
