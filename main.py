import cv2

# print("OpenCV:", cv2.__version__)
video = cv2.VideoCapture("video1.mp4")
if(video.isOpened()):
    print("video Open succesfully")
else:
    print("video Not found")

print(
"FPS:",video.get(cv2.CAP_PROP_FPS),'\n',
"FRAME WIDTH:",video.get(cv2.CAP_PROP_FRAME_WIDTH),'\n',
"FRAME HEIGHT:",video.get(cv2.CAP_PROP_FRAME_HEIGHT),'\n',
"FRAME COUNT:",video.get(cv2.CAP_PROP_FRAME_COUNT)
)
duration = video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS)
print("duration" , duration)


delay =  int(1000/video.get(cv2.CAP_PROP_FPS))

while True:
     success , frame = video.read()
     if not success:
         break     
     cv2.imshow("window name", frame)
     key  = cv2.waitKey(delay)
     if key == ord('q'):
         
         break
cv2.destroyAllWindows()
    


