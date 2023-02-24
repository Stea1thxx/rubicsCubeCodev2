### This is a small area where I'll place all my references from which I drew inspiration from:

#### Python colour recog:

https://learnopencv.com/color-spaces-in-opencv-cpp-python/   
https://pysource.com/2021/10/19/simple-color-recognition-with-opencv-and-python/   

#### Other stuff:

https://www.markdownguide.org/basic-syntax/

#### Creating the right outputs for the rubics cube solving algorithm:

https://github.com/hkociemba/RubiksCube-TwophaseSolver/blob/master/enums.py    

To understand how the input of the solving algorithm works I had to consult the github page. There I found that the input takes in a long string of data which has all the corresponding faces of the cube. This is in order of:     

U1, U2, U3, U4, U5, U6, U7, U8, U9, R1, R2, R3, R4, R5, R6, R7, R8, R9, F1, F2, F3, F4, F5, F6, F7, F8, F9, D1, D2, D3, D4, D5, D6, D7, D8, D9, L1, L2, L3, L4, L5, L6, L7, L8, L9, B1, B2, B3, B4, B5, B6, B7, B8, B9 of the enum constants.    



                  |************|
                  |*U1**U2**U3*|
                  |************|
                  |*U4**U5**U6*|
                  |************|
                  |*U7**U8**U9*|
                  |************|
     |************|************|************|************|
     |*L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*|
     |************|************|************|************|
     |*L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*|
     |************|************|************|************|
     |*L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*|
     |************|************|************|************|
                  |************|
                  |*D1**D2**D3*|
                  |************|
                  |*D4**D5**D6*|
                  |************|
                  |*D7**D8**D9*|
                  |************|     
                  
![alt text](https://www.codeproject.com/KB/Articles/1199528/RubiksCubeImage3.png)
                  
                  
