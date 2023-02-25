# import the required library
import cv2

# define a function to display the coordinates of

# of the points clicked on the image
def click_event(event, x, y, flags, params):
   
   if event == cv2.EVENT_LBUTTONDOWN:
      print(f'({x},{y})')
      
      # put coordinates as text on the image
      cv2.putText(frame, f'({x},{y})',(x,y),
      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
      
      # draw point on the image
      cv2.circle(frame, (x,y), 3, (0,255,255), -1)
 
# read the input image
#img = cv2.imread('back2school.jpg')

# create a window
cv2.namedWindow('Point Coordinates')
cap = cv2.VideoCapture(0) #Sets cap to the video capture of the camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# bind the callback function to window
cv2.setMouseCallback('Point Coordinates', click_event)

# display the image
while True:
   _, frame = cap.read()
   cv2.imshow('Point Coordinates',frame)
   k = cv2.waitKey(1) & 0xFF 
   if k == ord("q"):
      break
   
cap.release()
cv2.destroyAllWindows()