import cv2

cap = cv2.VideoCapture('Videos/Shim_L100_U10-37.mp4')
i = 1
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite(r'C:\Users\usuario\Desktop\Procesamiento\1 Frames\Shim_L100_U10-37\\' + str(i) + '.png', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()