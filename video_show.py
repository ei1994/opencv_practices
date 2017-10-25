import cv2
import matplotlib.pyplot as plt

def camera_(file, SaveVideo):
    # capture frame-by frame
    camera = cv2.VideoCapture(file)
    cv2.namedWindow('', 0)
    _, frame = camera.read()
    height, width, _ = frame.shape
    cv2.resizeWindow('', width, height)
    
    if SaveVideo:
        # define the codec and creat VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        videoWriter = cv2.VideoWriter('video.avi', fourcc, 20.0, (width, height))

    while camera.isOpened():
        ret, frame = camera.read()
        if ret is not True:
            print ('\nEnd of Video')
            break

        if SaveVideo:
            frame1 = cv2.flip(frame,0)
            # write the flipped frame
            videoWriter.write(frame1)
            
        # display the resulting frame
        cv2.imshow('frame', frame)
        choice = cv2.waitKey(10)&0xFF
        if choice == ord('q'): 
            break

    if SaveVideo:
        videoWriter.release()
    # when everything done, release the capture 
    camera.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    camera_('111.mp4',True)

    
