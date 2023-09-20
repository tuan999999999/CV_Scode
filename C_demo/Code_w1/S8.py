import cv2

# Đọc ảnh từ tệp tin
input_image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Kiểm tra xem ảnh đã đọc có tồn tại không
if input_image is None:
    print("Không thể đọc ảnh. Hãy đảm bảo rằng tệp tin 'input.jpg' tồn tại.")
else:
    # Áp dụng bộ lọc Canny
    edges = cv2.Canny(input_image, threshold1=30, threshold2=70)

    # Hiển thị ảnh gốc và ảnh sau khi áp dụng bộ lọc Canny
    cv2.imshow('Ảnh Gốc', input_image)
    cv2.imshow('Biểu đồ Canny', edges)

    # Lưu ảnh biểu đồ Canny thành một tệp tin mới
    cv2.imwrite('output_canny.jpg', edges)

    # Chờ người dùng nhấn phím bất kỳ để thoát
    cv2.waitKey(0)
    cv2.destroyAllWindows()
