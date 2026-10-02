import cv2

# print("OpenCV:", cv2.__version__)
video = cv2.VideoCapture("video1.mp4")
if(video.isOpened()):
    print("video Open succesfully")
else:
    print("video Not found")

# print(
# "FPS:",video.get(cv2.CAP_PROP_FPS),'\n',
# "FRAME WIDTH:",video.get(cv2.CAP_PROP_FRAME_WIDTH),'\n',

# "FRAME HEIGHT:",video.get(cv2.CAP_PROP_FRAME_HEIGHT),'\n',
# "FRAME COUNT:",video.get(cv2.CAP_PROP_FRAME_COUNT)
# )
# duration = video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS)
# print("duration" , duration)

fps = video.get(cv2.CAP_PROP_FPS)

frames_to_skip = int(fps*2) # number of frames to read in every 5 second 

current_frame = 0
# delay =  int(1000/fps)
# # framse corresponding to video duration
# framseCount = fps*duration
# frams_to_skip = int(fps*5)
while True:

    # Jump to the frame we want
    video.set(cv2.CAP_PROP_POS_FRAMES, current_frame)

    # Read that frame
    success, frame = video.read()

    if not success:
        break

    # Display the sampled frame
    cv2.imshow("CCTV Sampling", frame)

    # Print which frame we are looking at
    print("Frame:", current_frame)

    # Wait for a key
    key = cv2.waitKey(5000)

    # Press q to quit
    if key == ord("q"):
        break

    # Move 5 seconds forward
    current_frame += frames_to_skip

video.release()
cv2.destroyAllWindows()


