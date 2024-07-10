import cv2
import numpy as np
import utils

# 定义不同颜色在HSV空间的阈值
hsv_lower_red = np.array([-20, 70, 100])
hsv_upper_red = np.array([10, 255, 255])
hsv_lower_blue = np.array([110, 70, 100])
hsv_upper_blue = np.array([130, 255, 255])
hsv_lower_yellow = np.array([20, 70, 100])
hsv_upper_yellow = np.array([35, 255, 255])
hsv_lower_green = np.array([40, 70, 100])
hsv_upper_green = np.array([80, 255, 255])

# 创建捕获视频的实例
cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)

while True:
    # 读取一帧
    ret, frame = cap.read()
    if not ret:
        break

    # 颜色空间转换
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 创建掩模
    mask_red = cv2.inRange(hsv, hsv_lower_red, hsv_upper_red)
    mask_blue = cv2.inRange(hsv, hsv_lower_blue, hsv_upper_blue)
    mask_yellow = cv2.inRange(hsv, hsv_lower_yellow, hsv_upper_yellow)
    mask_green = cv2.inRange(hsv, hsv_lower_green, hsv_upper_green)

    # 合并掩模
    mask = cv2.bitwise_or(mask_red, mask_blue)
    mask = cv2.bitwise_or(mask, mask_yellow)
    mask = cv2.bitwise_or(mask, mask_green)

    # 形态学操作
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=0)

    # 轮廓检测
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 轮廓分析和颜色判断
    for contour in contours:
        if cv2.contourArea(contour) > 2000:  # 根据实际情况调整面积阈值
            # 计算边界框
            x, y, w, h = cv2.boundingRect(contour)
            # 计算中心坐标
            center_x, center_y = x + w // 2, y + h // 2
            
            color_bgr = frame[center_y, center_x]

            listRGB = [color_bgr[2], color_bgr[1], color_bgr[0]]
            arrayRGB = np.array(listRGB)
            predict = utils.predict_color(arrayRGB)
            # 输出颜色和坐标
            if predict:
                print(f"Detected {predict} cube at ({center_x}, {center_y})")
                # 绘制边界框
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, predict, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    # 显示结果
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    # 按'q'退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()