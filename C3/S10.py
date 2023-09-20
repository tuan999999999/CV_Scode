import cv2

# Đọc ảnh đầu vào
image = cv2.imread('input.jpg')

# Tạo một danh sách (list) để lưu trữ các phiên bản thu nhỏ của ảnh
image_pyramid = [image]

# Tạo image pyramid bằng cách thu nhỏ ảnh theo tỷ lệ giảm dần
while True:
    image = cv2.pyrDown(image)  # Thu nhỏ ảnh
    if image.shape[0] < 30 or image.shape[1] < 30:
        break  # Dừng khi kích thước ảnh quá nhỏ
    image_pyramid.append(image)

# Hiển thị các ảnh trong image pyramid
for i, img in enumerate(image_pyramid):
    cv2.imshow(f'Level {i}', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
