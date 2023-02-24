#TODO: Imports
import cv2
import numpy as np

#TODO: Variable defs
cubecolor = (255,255,255) #Cube template colour
cubelineSize = 2
color = "Undefined"
colorString = ""

class CubeTemplateDimensions:
    
  def __init__(self, Image, Size, matrixType, StartPointCoordinates):
    self.Image = Image
    self.Size = Size

    self.matrixType = matrixType
    self.StartPointCoordinates = StartPointCoordinates

#TODO: Object defs
cubeTemp = CubeTemplateDimensions(np.zeros((400,640)),180,3,(100,60))
cubeTemp.Image = np.zeros((400,640)) #np.zeros((400,640)) -  #Creates a 400 by 640 matrix
cubeTemp.Size = 240 #180
cubeTemp.matrixType = 3 #3

#cubeTemp.StartPointCoordinates = (int(1280/2)-int(cubeTemp.Size/2), int(720/2)-int(cubeTemp.Size/2)) #(100,60)

cubeDimenstions = int(cubeTemp.Size/3)

def drawCube(img, cubeSize, cubeMatrix, start_point): # start_poing (100, 60)
    cubecell = int(cubeSize / cubeMatrix)
    # draw horizontal lines first
    for i in range(cubeMatrix + 1):
        start_line = (start_point[0], start_point[1] + i * cubecell)
        end_line = (start_point[0] + cubeSize, start_point[1] + i * cubecell)
        cv2.line(img, start_line, end_line, cubecolor, cubelineSize)
        
    
    for i in range(cubeMatrix + 1):
        start_line = (start_point[0] + i * cubecell, start_point[1])
        end_line = (start_point[0] + i * cubecell, start_point[1] + cubeSize)
        cv2.line(img, start_line, end_line, cubecolor, cubelineSize)

    #cv2.line(img, (100,60), (280,240), (0,255,0), 9)
    #cv2.putText(img, "X - The coordinates here are: " + str(cubeTemp.StartPointCoordinates), (100,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    return img


cap = cv2.VideoCapture(0) #Sets cap to the video capture of the camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    cubeTemp.Image = frame
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Converts the colours on the fram to hsv
    height, width, _ = frame.shape
    cv2.waitKey(1)
    drawCube(cubeTemp.Image,cubeTemp.Size,cubeTemp.matrixType,cubeTemp.StartPointCoordinates)


    cx = int(width / 2)
    cy = int(height / 2)

    # Pick pixel value
    pixel_center = hsv_frame[cy, cx] #The Hue Saturation and Visibility value at point of the circle
    cv2.waitKey(10)
    hue_value = pixel_center[0]
    xMiddle = (cubeTemp.StartPointCoordinates[0] + int(cubeDimenstions/2))
    yMiddle = (cubeTemp.StartPointCoordinates[1] + int(cubeDimenstions/2))    

    if cv2.waitKey(1) == ord("c"):
        for y in range(yMiddle,yMiddle + (3*cubeDimenstions), cubeDimenstions):
            for x in range(xMiddle,xMiddle + (3*cubeDimenstions), cubeDimenstions):
                hsv_square = cv2.mean(hsv_frame[y:y+cubeDimenstions, x:x+cubeDimenstions])[0] #Finding the mean of the HSV Values in the blocks
                hue_value = hsv_square

                
                
                color = "Undefined"
                
                if hue_value < 11:
                    color = "B" #Orange
                elif hue_value < 33:
                    color = "U" #Yellow
                elif hue_value < 78:
                    color = "R" #Green
                elif hue_value < 131:
                    color = "L" #Blue
                elif hue_value < 180:
                    color = "F" #Red
                else:
                    color = "D" #White
                colorString += color
        colorString += ","
        print(colorString)

    cv2.imshow("Frame", frame) #To convert to an HSV frame use "hsv_frame"
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#TODO:Scrap code
'''
    #FIXME Using rgb colors
    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    #FIXME Putting circles in the middle of the squares
    #cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    #cv2.putText(frame, color, (cx - 200, 100), 0, 3, (0, 0, 0), 5)


    FIXME Code for getting the white in colours
    if cv2.mean(hsv_frame[y:y+cubeDimenstions, x:x+cubeDimenstions])[1] < 100:
        color = "D" #White
                    
    #FIXME COde for knowign where coords are
    #cv2.putText(frame, "X - The coordinates here are: ", (cubeTemp.StartPointCoordinates[0] + cubeDimenstions,cubeTemp.StartPointCoordinates[1]+ cubeDimenstions), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    #FIXME Code for colour bondaries 2
    if cv2.waitKey(1) == ord("c"):
        for y in range(yMiddle,yMiddle + (3*cubeDimenstions), cubeDimenstions):
            for x in range(xMiddle,xMiddle + (3*cubeDimenstions), cubeDimenstions):
                cv2.circle(frame, (x,y), 5, (25, 25, 25), 3)
                pixel_center = cv2.mean(hsv_frame[y:y+cubeDimenstions, x:x+cubeDimenstions])[0] #Finding the mean of the HSV Values in the blocks
                hue_value = pixel_center
                
                color = "Undefined"
                if hue_value < 5:
                    color = "F" #Red
                elif hue_value < 22:
                    color = "B" #Orange
                elif hue_value < 33:
                    color = "U" #Yellow
                elif hue_value < 78:
                    color = "R" #Green
                elif hue_value < 131:
                    color = "L" #Blue
                else:
                    color = "D" #White
                colorString += color
        colorString += ","
        print(colorString)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
'''
