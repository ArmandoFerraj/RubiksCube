
#CONTROLS

# To change the view of the cube use: "i", "j", "k", "l", "u", "p"
# To reset the view of the cube use: "q"

# To turn WHITE face: Hold "w" and then press the "right arrow key". (left arrow key for anticlcockwise)
# To turn BLUE face: Hold "b" and then press the "right arrow key"
# To turn ORANGE face: Hold "o" and then press the "right arrow key"
# To turn RED face: Hold "r" and then press the "right arrow key"
# To turn GREEN face: Hold "g" and then press the "right arrow key"
# To turn YELLOW face: Hold "y" and then press the "right arrow key"

import pygame
from math import *
import numpy as np
import TurnAnimation as alg
import AbstractCube

pygame.init()

WINDOW_SIZE = 800
ROTATE_SPEED = .08
degree90 = list(range(100))
phi_step = (2*pi)/(len(degree90)*4)
scale = 100
angle_x = angle_y = angle_z = 0
theta_x = theta_y = theta_z = 0
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,165,0)
white = (255,255,255)
yellow = (255,255,0)

window = pygame.display.set_mode( (WINDOW_SIZE, WINDOW_SIZE) )
clock = pygame.time.Clock()




cube_points = [n for n in range(56)]
cube_points[0] = [[-1.5],[-1.5],[1.5]]
cube_points[1] = [[1.5],[-1.5],[1.5]]
cube_points[2] = [[1.5],[1.5],[1.5]]
cube_points[3] = [[-1.5],[1.5],[1.5]]
cube_points[4] = [[-1.5],[-1.5],[-1.5]]
cube_points[5] = [[1.5],[-1.5],[-1.5]]
cube_points[6] = [[1.5],[1.5],[-1.5]]
cube_points[7] = [[-1.5],[1.5],[-1.5]]

cube_points[8] = [[-.5],[-1.5],[1.5]]
cube_points[9] = [[-1.5],[-.5],[1.5]]
cube_points[10] = [[-1.5],[-1.5],[.5]]

cube_points[11] = [[.5],[-1.5],[1.5]]
cube_points[12] = [[1.5],[-.5],[1.5]]
cube_points[13] = [[1.5],[-1.5],[.5]]

cube_points[14] = [[.5],[1.5],[1.5]]
cube_points[15] = [[1.5],[.5],[1.5]]
cube_points[16] = [[1.5],[1.5],[.5]]

cube_points[17] = [[-.5],[1.5],[1.5]]
cube_points[18] = [[-1.5],[.5],[1.5]]
cube_points[19] = [[-1.5],[1.5],[.5]]

cube_points[20] = [[-.5],[-1.5],[-1.5]]
cube_points[21] = [[-1.5],[-.5],[-1.5]]
cube_points[22] = [[-1.5],[-1.5],[-.5]]

cube_points[23] = [[.5],[-1.5],[-1.5]]
cube_points[24] = [[1.5],[-.5],[-1.5]]
cube_points[25] = [[1.5],[-1.5],[-.5]]

cube_points[26] = [[.5],[1.5],[-1.5]]
cube_points[27] = [[1.5],[.5],[-1.5]]
cube_points[28] = [[1.5],[1.5],[-.5]]

cube_points[29] = [[-.5],[1.5],[-1.5]]
cube_points[30] = [[-1.5],[.5],[-1.5]]
cube_points[31] = [[-1.5],[1.5],[-.5]]

#top midpoints
cube_points[32] = [[-.5],[-1.5],[.5]]
cube_points[33] = [[.5],[-1.5],[.5]]
cube_points[34] = [[-.5],[-1.5],[-.5]]
cube_points[35] = [[.5],[-1.5],[-.5]]

#front midpoints
cube_points[36] = [[-.5],[-.5],[-1.5]]
cube_points[37] = [[.5],[-.5],[-1.5]]
cube_points[38] = [[-.5],[.5],[-1.5]]
cube_points[39] = [[.5],[.5],[-1.5]]

# left midpoints
cube_points[40] = [[-1.5],[-.5],[.5]]
cube_points[41] = [[-1.5],[-.5],[-.5]]
cube_points[42] = [[-1.5],[.5],[.5]]
cube_points[43] = [[-1.5],[.5],[-.5]]

#right midpoint
cube_points[44] = [[1.5],[-.5],[.5]]
cube_points[45] = [[1.5],[-.5],[-.5]]
cube_points[46] = [[1.5],[.5],[.5]]
cube_points[47] = [[1.5],[.5],[-.5]]

#back midpoint
cube_points[48] = [[-.5],[-.5],[1.5]]
cube_points[49] = [[.5],[-.5],[1.5]]
cube_points[50] = [[-.5],[.5],[1.5]]
cube_points[51] = [[.5],[.5],[1.5]]

#bottom midpoints
cube_points[52] = [[-.5],[1.5],[.5]]
cube_points[53] = [[.5],[1.5],[.5]]
cube_points[54] = [[-.5],[1.5],[-.5]]
cube_points[55] = [[.5],[1.5],[-.5]]

projection_matrix = [[1,0,0],
                     [0,1,0]]

def getcolor(cubelist, cubie_loc):
    global cubie_color
    if cubelist[cubie_loc] in range(0,9):
        cubie_color = white
    elif cubelist[cubie_loc] in range(9,18):
        cubie_color = blue
    elif cubelist[cubie_loc] in range(18,27):
        cubie_color = orange
    elif cubelist[cubie_loc] in range(27,36):
        cubie_color = red
    elif cubelist[cubie_loc] in range(36,45):
        cubie_color = green
    else: 
        cubie_color = yellow
    

def Nmaxelements(list1, N, zcoord):
    final_list = []
 
    for i in range(0, N):
        max1 = 0
         
        for j in range(len(list1)):    
            if list1[j] > max1:
                max1 = list1[j];
                 
        list1.remove(max1);
        final_list.append(max1)
    
    global colorkey
    colorkey = 'nothing'
    
    if final_list[0] == zcoord[0]:
        colorkey = 'YOB'
    elif final_list[0] == zcoord[1]:
        colorkey = 'YBR'
    elif final_list[0] == zcoord[2]:
        colorkey = 'RWB'
    elif final_list[0] == zcoord[3]:
        colorkey = 'WOB'
    elif final_list[0] == zcoord[4]:
        colorkey = 'YOG'
    elif final_list[0] == zcoord[5]:
        colorkey = 'YRG'
    elif final_list[0] == zcoord[6]:
        colorkey = 'WGR'
    elif final_list[0] == zcoord[7]:
        colorkey = 'WOG'

    
    
def connect_points(i, j, points):
    pygame.draw.line(window, (0, 0, 0), (points[i][0], points[i][1]) , (points[j][0], points[j][1]))
    



while True:
    AbstractCube.cube.create_cube
    temp_list = []
    points3d = []
    clock.tick(60)
    i=0
    window.fill((0,0,0))
    
    rotation_z = [[cos(angle_z), -sin(angle_z), 0],
                  [sin(angle_z), cos(angle_z), 0],
                  [0, 0, 1]]
    rotation_y = [[cos(angle_y), 0, sin(angle_y)],
                  [0, 1, 0],
                  [-sin(angle_y), 0, cos(angle_y)]]
    rotation_x = [[1, 0, 0],
                  [0, cos(angle_x), -sin(angle_x)],
                  [0, sin(angle_x), cos(angle_x)]]

    points = [0 for _ in range(len(cube_points))]


    for point in cube_points:
    
        rotate_x = np.dot(rotation_x, point)
        rotate_y = np.dot(rotation_y, rotate_x)
        rotate_z = np.dot(rotation_z, rotate_y)
        points3d.append(rotate_z)
        point_2d = np.dot(projection_matrix, rotate_z)
        x = (point_2d[0][0] * scale) + WINDOW_SIZE/2
        y = (point_2d[1][0] * scale) + WINDOW_SIZE/2
        temp_list.append(point_2d)
        points[i] = (x,y)
        i += 1
        pygame.draw.circle(window, (0, 0, 0), (x,y), 4)

    # add if statements for the heiarchy of prints

    zcoord = [points3d[0][2][0],points3d[1][2][0],points3d[2][2][0], points3d[3][2][0], points3d[4][2][0], points3d[5][2][0], points3d[6][2][0], points3d[7][2][0]]
    zcoord1 = [points3d[0][2][0],points3d[1][2][0],points3d[2][2][0], points3d[3][2][0], points3d[4][2][0], points3d[5][2][0], points3d[6][2][0], points3d[7][2][0]]
    Nmaxelements(zcoord1, 4, zcoord)
    
            

    if colorkey == 'RWB':

        #outside edges
        connect_points(2, 3, points)
        connect_points(1, 2, points)
        connect_points(2, 6, points)
        
        #vertical lines
        connect_points(8, 17, points)
        connect_points(11, 14, points)
        connect_points(13, 16, points)
        
        connect_points(25, 28, points)

        #top horizontal lines
        
        #side horizontal lines
        connect_points(12, 24, points)
        connect_points(15, 27, points)

        connect_points(18, 15, points)
        connect_points(9, 12, points)

        #bottom horizontal
        connect_points(26, 14, points)
        connect_points(29, 17, points)
        connect_points(19, 16, points)
        connect_points(31, 28, points)

        #if RWB then these are the last things printed

        # 6 cubies x 3 faces = 18 polygons and they need 6 if statements each for the colors
        
        pygame.draw.polygon(window,red,((points[0]),(points[3]),(points[7]),(points[4])))
    
        pygame.draw.polygon(window,blue,((points[4]),(points[5]),(points[6]),(points[7])))


        getcolor(AbstractCube.cube.create_cube,0)
        pygame.draw.polygon(window,cubie_color,((points[0]),(points[8]),(points[32]),(points[10])))

        getcolor(AbstractCube.cube.create_cube,1)
        pygame.draw.polygon(window,cubie_color,((points[8]),(points[11]),(points[33]),(points[32])))
        
        getcolor(AbstractCube.cube.create_cube,2)
        pygame.draw.polygon(window,cubie_color,((points[11]),(points[1]),(points[13]),(points[33])))

        getcolor(AbstractCube.cube.create_cube,3)
        pygame.draw.polygon(window,cubie_color,((points[10]),(points[32]),(points[34]),(points[22])))

        getcolor(AbstractCube.cube.create_cube,4)
        pygame.draw.polygon(window,cubie_color,((points[32]),(points[33]),(points[35]),(points[34])))

        getcolor(AbstractCube.cube.create_cube,5)
        pygame.draw.polygon(window,cubie_color,((points[33]),(points[13]),(points[25]),(points[35])))

        getcolor(AbstractCube.cube.create_cube,6)
        pygame.draw.polygon(window,cubie_color,((points[22]),(points[34]),(points[20]),(points[4])))

        getcolor(AbstractCube.cube.create_cube,7)
        pygame.draw.polygon(window,cubie_color,((points[34]),(points[35]),(points[23]),(points[20])))

        getcolor(AbstractCube.cube.create_cube,8)
        pygame.draw.polygon(window,cubie_color,((points[25]),(points[5]),(points[23]),(points[35])))



        getcolor(AbstractCube.cube.create_cube,9)
        pygame.draw.polygon(window,cubie_color,((points[4]),(points[20]),(points[36]),(points[21])))

        getcolor(AbstractCube.cube.create_cube,10)
        pygame.draw.polygon(window,cubie_color,((points[20]),(points[23]),(points[37]),(points[36])))

        getcolor(AbstractCube.cube.create_cube,11)
        pygame.draw.polygon(window,cubie_color,((points[23]),(points[5]),(points[24]),(points[37])))

        getcolor(AbstractCube.cube.create_cube,12)
        pygame.draw.polygon(window,cubie_color,((points[21]),(points[36]),(points[38]),(points[30])))

        getcolor(AbstractCube.cube.create_cube,13)
        pygame.draw.polygon(window,cubie_color,((points[36]),(points[37]),(points[39]),(points[38])))

        getcolor(AbstractCube.cube.create_cube,14)
        pygame.draw.polygon(window,cubie_color,((points[37]),(points[24]),(points[27]),(points[39])))

        getcolor(AbstractCube.cube.create_cube,15)
        pygame.draw.polygon(window,cubie_color,((points[30]),(points[38]),(points[29]),(points[7])))

        getcolor(AbstractCube.cube.create_cube,16)
        pygame.draw.polygon(window,cubie_color,((points[38]),(points[39]),(points[26]),(points[29])))

        getcolor(AbstractCube.cube.create_cube,17)
        pygame.draw.polygon(window,cubie_color,((points[39]),(points[27]),(points[6]),(points[26])))



        getcolor(AbstractCube.cube.create_cube,27)
        pygame.draw.polygon(window,cubie_color,((points[0]),(points[10]),(points[40]),(points[9])))

        getcolor(AbstractCube.cube.create_cube,28)
        pygame.draw.polygon(window,cubie_color,((points[10]),(points[22]),(points[41]),(points[40])))

        getcolor(AbstractCube.cube.create_cube,29)
        pygame.draw.polygon(window,cubie_color,((points[22]),(points[4]),(points[21]),(points[41])))

        getcolor(AbstractCube.cube.create_cube,30)
        pygame.draw.polygon(window,cubie_color,((points[9]),(points[40]),(points[42]),(points[18])))

        getcolor(AbstractCube.cube.create_cube,31)
        pygame.draw.polygon(window,cubie_color,((points[40]),(points[41]),(points[43]),(points[42])))

        getcolor(AbstractCube.cube.create_cube,32)
        pygame.draw.polygon(window,cubie_color,((points[41]),(points[21]),(points[30]),(points[43])))

        getcolor(AbstractCube.cube.create_cube,33)
        pygame.draw.polygon(window,cubie_color,((points[18]),(points[42]),(points[19]),(points[3])))

        getcolor(AbstractCube.cube.create_cube,34)
        pygame.draw.polygon(window,cubie_color,((points[42]),(points[43]),(points[31]),(points[19])))

        getcolor(AbstractCube.cube.create_cube,35)
        pygame.draw.polygon(window,cubie_color,((points[43]),(points[30]),(points[7]),(points[31])))
        

        connect_points(0, 4, points)
        connect_points(4, 7, points)
        connect_points(7, 3, points)
        connect_points(3, 0, points)

        connect_points(0, 1, points)
        connect_points(1, 5, points)
        connect_points(5, 4, points)
        connect_points(4, 0, points)

        connect_points(4, 5, points)
        connect_points(5, 6, points)
        connect_points(6, 7, points)
        connect_points(7, 4, points)

        connect_points(13, 10, points)
        connect_points(22, 25, points)
        connect_points(8, 20, points)
        connect_points(11, 23, points)

        connect_points(10, 19, points)
        connect_points(22, 31, points)
        connect_points(9, 21, points)
        connect_points(18, 30, points)

        connect_points(21, 24, points)
        connect_points(30, 27, points)
        connect_points(20, 29, points)
        connect_points(23, 26, points)
        
    elif colorkey == 'WOB':

        #Background Colors
        pygame.draw.polygon(window,red,((points[0]),(points[3]),(points[7]),(points[4])))
        pygame.draw.polygon(window,green,((points[0]),(points[1]),(points[2]),(points[3])))
        pygame.draw.polygon(window,yellow,((points[3]),(points[2]),(points[6]),(points[7])))    
        
        #background perimeter
        connect_points(0, 3, points)
        connect_points(2, 3, points)
        connect_points(3, 7, points)
        
        #back midpoints
        connect_points(8, 17, points)
        connect_points(11, 14, points)
        connect_points(9, 12, points)
        connect_points(18, 15, points)
        
        #Left midpoints
        connect_points(9, 21, points)
        connect_points(18, 30, points)
        connect_points(10, 19, points)
        connect_points(22, 31, points)

        #bottom Midpoints
        connect_points(26, 14, points)
        connect_points(29, 17, points)
        connect_points(19, 16, points)
        connect_points(31, 28, points)

        #WOB colors
        pygame.draw.polygon(window,white,((points[0]),(points[1]),(points[5]),(points[4])))
        pygame.draw.polygon(window,blue,((points[4]),(points[5]),(points[6]),(points[7])))
        pygame.draw.polygon(window,orange,((points[1]),(points[5]),(points[6]),(points[2])))

        getcolor(AbstractCube.cube.create_cube,0)
        pygame.draw.polygon(window,cubie_color,((points[0]),(points[8]),(points[32]),(points[10])))

        getcolor(AbstractCube.cube.create_cube,1)
        pygame.draw.polygon(window,cubie_color,((points[8]),(points[11]),(points[33]),(points[32])))
        
        getcolor(AbstractCube.cube.create_cube,2)
        pygame.draw.polygon(window,cubie_color,((points[11]),(points[1]),(points[13]),(points[33])))

        getcolor(AbstractCube.cube.create_cube,3)
        pygame.draw.polygon(window,cubie_color,((points[10]),(points[32]),(points[34]),(points[22])))

        getcolor(AbstractCube.cube.create_cube,4)
        pygame.draw.polygon(window,cubie_color,((points[32]),(points[33]),(points[35]),(points[34])))

        getcolor(AbstractCube.cube.create_cube,5)
        pygame.draw.polygon(window,cubie_color,((points[33]),(points[13]),(points[25]),(points[35])))

        getcolor(AbstractCube.cube.create_cube,6)
        pygame.draw.polygon(window,cubie_color,((points[22]),(points[34]),(points[20]),(points[4])))

        getcolor(AbstractCube.cube.create_cube,7)
        pygame.draw.polygon(window,cubie_color,((points[34]),(points[35]),(points[23]),(points[20])))

        getcolor(AbstractCube.cube.create_cube,8)
        pygame.draw.polygon(window,cubie_color,((points[25]),(points[5]),(points[23]),(points[35])))



        getcolor(AbstractCube.cube.create_cube,9)
        pygame.draw.polygon(window,cubie_color,((points[4]),(points[20]),(points[36]),(points[21])))

        getcolor(AbstractCube.cube.create_cube,10)
        pygame.draw.polygon(window,cubie_color,((points[20]),(points[23]),(points[37]),(points[36])))

        getcolor(AbstractCube.cube.create_cube,11)
        pygame.draw.polygon(window,cubie_color,((points[23]),(points[5]),(points[24]),(points[37])))

        getcolor(AbstractCube.cube.create_cube,12)
        pygame.draw.polygon(window,cubie_color,((points[21]),(points[36]),(points[38]),(points[30])))

        getcolor(AbstractCube.cube.create_cube,13)
        pygame.draw.polygon(window,cubie_color,((points[36]),(points[37]),(points[39]),(points[38])))

        getcolor(AbstractCube.cube.create_cube,14)
        pygame.draw.polygon(window,cubie_color,((points[37]),(points[24]),(points[27]),(points[39])))

        getcolor(AbstractCube.cube.create_cube,15)
        pygame.draw.polygon(window,cubie_color,((points[30]),(points[38]),(points[29]),(points[7])))

        getcolor(AbstractCube.cube.create_cube,16)
        pygame.draw.polygon(window,cubie_color,((points[38]),(points[39]),(points[26]),(points[29])))

        getcolor(AbstractCube.cube.create_cube,17)
        pygame.draw.polygon(window,cubie_color,((points[39]),(points[27]),(points[6]),(points[26])))




        getcolor(AbstractCube.cube.create_cube,18)
        pygame.draw.polygon(window,cubie_color,((points[5]),(points[25]),(points[45]),(points[24])))

        getcolor(AbstractCube.cube.create_cube,19)
        pygame.draw.polygon(window,cubie_color,((points[25]),(points[13]),(points[44]),(points[45])))

        getcolor(AbstractCube.cube.create_cube,20)
        pygame.draw.polygon(window,cubie_color,((points[13]),(points[1]),(points[12]),(points[44])))

        getcolor(AbstractCube.cube.create_cube,21)
        pygame.draw.polygon(window,cubie_color,((points[24]),(points[45]),(points[47]),(points[27])))

        getcolor(AbstractCube.cube.create_cube,22)
        pygame.draw.polygon(window,cubie_color,((points[45]),(points[44]),(points[46]),(points[47])))

        getcolor(AbstractCube.cube.create_cube,23)
        pygame.draw.polygon(window,cubie_color,((points[44]),(points[12]),(points[15]),(points[46])))

        getcolor(AbstractCube.cube.create_cube,24)
        pygame.draw.polygon(window,cubie_color,((points[27]),(points[47]),(points[28]),(points[6])))

        getcolor(AbstractCube.cube.create_cube,25)
        pygame.draw.polygon(window,cubie_color,((points[47]),(points[46]),(points[16]),(points[28])))

        getcolor(AbstractCube.cube.create_cube,26)
        pygame.draw.polygon(window,cubie_color,((points[46]),(points[15]),(points[2]),(points[16])))

        

        #Connect perimeter
        connect_points(0, 1, points)
        connect_points(1, 5, points)
        connect_points(4, 5, points)
        connect_points(0, 4, points)

        connect_points(2, 6, points)
        connect_points(6, 5, points)
        connect_points(1, 2, points)
        connect_points(6, 7, points)
        connect_points(4, 7, points)

        #top midpoints
        connect_points(13, 10, points)
        connect_points(22, 25, points)
        connect_points(8, 20, points)
        connect_points(11, 23, points)
        

        #middle midpoint
        connect_points(20, 29, points)
        connect_points(23, 26, points)
        connect_points(21, 24, points)
        connect_points(30, 27, points)

        #right midpoint
        connect_points(13, 16, points)
        connect_points(25, 28, points)
        connect_points(12, 24, points)
        connect_points(15, 27, points)
        

    elif colorkey == 'WOG':
        #Background Colors
        pygame.draw.polygon(window,red,((points[0]),(points[3]),(points[7]),(points[4])))
        pygame.draw.polygon(window,blue,((points[4]),(points[5]),(points[6]),(points[7])))
        pygame.draw.polygon(window,yellow,((points[3]),(points[2]),(points[6]),(points[7])))    
        
        #background perimeter
        connect_points(3, 7, points)
        connect_points(4, 7, points)
        connect_points(6, 7, points)

        #front midpoint
        connect_points(20, 29, points)
        connect_points(23, 26, points)
        connect_points(21, 24, points)
        connect_points(30, 27, points)
        
        #Left midpoints
        connect_points(9, 21, points)
        connect_points(18, 30, points)
        connect_points(10, 19, points)
        connect_points(22, 31, points)

        #bottom Midpoints
        connect_points(26, 14, points)
        connect_points(29, 17, points)
        connect_points(19, 16, points)
        connect_points(31, 28, points)

        #WOG colors
        #pygame.draw.polygon(window,white,((points[0]),(points[1]),(points[5]),(points[4])))
        #pygame.draw.polygon(window,green,((points[0]),(points[1]),(points[2]),(points[3])))
        #pygame.draw.polygon(window,orange,((points[1]),(points[5]),(points[6]),(points[2])))

        #pygame.draw.polygon(window,white,((points[0]),(points[1]),(points[5]),(points[4])))
        #pygame.draw.polygon(window,blue,((points[4]),(points[5]),(points[6]),(points[7])))
        #pygame.draw.polygon(window,orange,((points[1]),(points[5]),(points[6]),(points[2])))

        getcolor(AbstractCube.cube.create_cube,0)
        pygame.draw.polygon(window,cubie_color,((points[0]),(points[8]),(points[32]),(points[10])))

        getcolor(AbstractCube.cube.create_cube,1)
        pygame.draw.polygon(window,cubie_color,((points[8]),(points[11]),(points[33]),(points[32])))
        
        getcolor(AbstractCube.cube.create_cube,2)
        pygame.draw.polygon(window,cubie_color,((points[11]),(points[1]),(points[13]),(points[33])))

        getcolor(AbstractCube.cube.create_cube,3)
        pygame.draw.polygon(window,cubie_color,((points[10]),(points[32]),(points[34]),(points[22])))

        getcolor(AbstractCube.cube.create_cube,4)
        pygame.draw.polygon(window,cubie_color,((points[32]),(points[33]),(points[35]),(points[34])))

        getcolor(AbstractCube.cube.create_cube,5)
        pygame.draw.polygon(window,cubie_color,((points[33]),(points[13]),(points[25]),(points[35])))

        getcolor(AbstractCube.cube.create_cube,6)
        pygame.draw.polygon(window,cubie_color,((points[22]),(points[34]),(points[20]),(points[4])))

        getcolor(AbstractCube.cube.create_cube,7)
        pygame.draw.polygon(window,cubie_color,((points[34]),(points[35]),(points[23]),(points[20])))

        getcolor(AbstractCube.cube.create_cube,8)
        pygame.draw.polygon(window,cubie_color,((points[25]),(points[5]),(points[23]),(points[35])))



        getcolor(AbstractCube.cube.create_cube,18)
        pygame.draw.polygon(window,cubie_color,((points[5]),(points[25]),(points[45]),(points[24])))

        getcolor(AbstractCube.cube.create_cube,19)
        pygame.draw.polygon(window,cubie_color,((points[25]),(points[13]),(points[44]),(points[45])))

        getcolor(AbstractCube.cube.create_cube,20)
        pygame.draw.polygon(window,cubie_color,((points[13]),(points[1]),(points[12]),(points[44])))

        getcolor(AbstractCube.cube.create_cube,21)
        pygame.draw.polygon(window,cubie_color,((points[24]),(points[45]),(points[47]),(points[27])))

        getcolor(AbstractCube.cube.create_cube,22)
        pygame.draw.polygon(window,cubie_color,((points[45]),(points[44]),(points[46]),(points[47])))

        getcolor(AbstractCube.cube.create_cube,23)
        pygame.draw.polygon(window,cubie_color,((points[44]),(points[12]),(points[15]),(points[46])))

        getcolor(AbstractCube.cube.create_cube,24)
        pygame.draw.polygon(window,cubie_color,((points[27]),(points[47]),(points[28]),(points[6])))

        getcolor(AbstractCube.cube.create_cube,25)
        pygame.draw.polygon(window,cubie_color,((points[47]),(points[46]),(points[16]),(points[28])))

        getcolor(AbstractCube.cube.create_cube,26)
        pygame.draw.polygon(window,cubie_color,((points[46]),(points[15]),(points[2]),(points[16])))


        getcolor(AbstractCube.cube.create_cube,36)
        pygame.draw.polygon(window,cubie_color,((points[1]),(points[11]),(points[49]),(points[12])))

        getcolor(AbstractCube.cube.create_cube,37)
        pygame.draw.polygon(window,cubie_color,((points[11]),(points[8]),(points[48]),(points[49])))

        getcolor(AbstractCube.cube.create_cube,38)
        pygame.draw.polygon(window,cubie_color,((points[8]),(points[0]),(points[9]),(points[48])))

        getcolor(AbstractCube.cube.create_cube,39)
        pygame.draw.polygon(window,cubie_color,((points[12]),(points[49]),(points[51]),(points[15])))

        getcolor(AbstractCube.cube.create_cube,40)
        pygame.draw.polygon(window,cubie_color,((points[49]),(points[48]),(points[50]),(points[51])))

        getcolor(AbstractCube.cube.create_cube,41)
        pygame.draw.polygon(window,cubie_color,((points[48]),(points[9]),(points[18]),(points[50])))

        getcolor(AbstractCube.cube.create_cube,42)
        pygame.draw.polygon(window,cubie_color,((points[15]),(points[51]),(points[14]),(points[2])))

        getcolor(AbstractCube.cube.create_cube,43)
        pygame.draw.polygon(window,cubie_color,((points[51]),(points[50]),(points[17]),(points[14])))

        getcolor(AbstractCube.cube.create_cube,44)
        pygame.draw.polygon(window,cubie_color,((points[50]),(points[18]),(points[3]),(points[17])))

        #Connect perimeter
        connect_points(1, 5, points)
        connect_points(5, 6, points)
        connect_points(6, 2, points)
        connect_points(2, 1, points)

        connect_points(0, 1, points)
        connect_points(0, 3, points)
        connect_points(2, 3, points)

        connect_points(4, 5, points)
        connect_points(0, 4, points)
       
        #top midpoints
        connect_points(13, 10, points)
        connect_points(22, 25, points)
        connect_points(8, 20, points)
        connect_points(11, 23, points)
    
        #right midpoint
        connect_points(13, 16, points)
        connect_points(25, 28, points)
        connect_points(12, 24, points)
        connect_points(15, 27, points)

        #back midpoints
        connect_points(8, 17, points)
        connect_points(11, 14, points)
        connect_points(9, 12, points)
        connect_points(18, 15, points)



    elif colorkey == 'WGR':
        #Background Colors
        pygame.draw.polygon(window,blue,((points[4]),(points[5]),(points[6]),(points[7])))
        pygame.draw.polygon(window,yellow,((points[3]),(points[2]),(points[6]),(points[7])))
        pygame.draw.polygon(window,orange,((points[1]),(points[5]),(points[6]),(points[2])))
        
        #background perimeter
        connect_points(6, 7, points)
        connect_points(6, 2, points)
        connect_points(5, 6, points)
        
        #front midpoint
        connect_points(20, 29, points)
        connect_points(23, 26, points)
        connect_points(21, 24, points)
        connect_points(30, 27, points)

        #right midpoint
        connect_points(13, 16, points)
        connect_points(25, 28, points)
        connect_points(12, 24, points)
        connect_points(15, 27, points)
        
        #bottom Midpoints
        connect_points(26, 14, points)
        connect_points(29, 17, points)
        connect_points(19, 16, points)
        connect_points(31, 28, points)

        #WGR colors
        pygame.draw.polygon(window,white,((points[0]),(points[1]),(points[5]),(points[4])))
        pygame.draw.polygon(window,green,((points[0]),(points[1]),(points[2]),(points[3])))
        pygame.draw.polygon(window,red,((points[0]),(points[3]),(points[7]),(points[4])))

        getcolor(AbstractCube.cube.create_cube,0)
        pygame.draw.polygon(window,cubie_color,((points[0]),(points[8]),(points[32]),(points[10])))

        getcolor(AbstractCube.cube.create_cube,1)
        pygame.draw.polygon(window,cubie_color,((points[8]),(points[11]),(points[33]),(points[32])))
        
        getcolor(AbstractCube.cube.create_cube,2)
        pygame.draw.polygon(window,cubie_color,((points[11]),(points[1]),(points[13]),(points[33])))

        getcolor(AbstractCube.cube.create_cube,3)
        pygame.draw.polygon(window,cubie_color,((points[10]),(points[32]),(points[34]),(points[22])))

        getcolor(AbstractCube.cube.create_cube,4)
        pygame.draw.polygon(window,cubie_color,((points[32]),(points[33]),(points[35]),(points[34])))

        getcolor(AbstractCube.cube.create_cube,5)
        pygame.draw.polygon(window,cubie_color,((points[33]),(points[13]),(points[25]),(points[35])))

        getcolor(AbstractCube.cube.create_cube,6)
        pygame.draw.polygon(window,cubie_color,((points[22]),(points[34]),(points[20]),(points[4])))

        getcolor(AbstractCube.cube.create_cube,7)
        pygame.draw.polygon(window,cubie_color,((points[34]),(points[35]),(points[23]),(points[20])))

        getcolor(AbstractCube.cube.create_cube,8)
        pygame.draw.polygon(window,cubie_color,((points[25]),(points[5]),(points[23]),(points[35])))





        getcolor(AbstractCube.cube.create_cube,36)
        pygame.draw.polygon(window,cubie_color,((points[1]),(points[11]),(points[49]),(points[12])))

        getcolor(AbstractCube.cube.create_cube,37)
        pygame.draw.polygon(window,cubie_color,((points[11]),(points[8]),(points[48]),(points[49])))

        getcolor(AbstractCube.cube.create_cube,38)
        pygame.draw.polygon(window,cubie_color,((points[8]),(points[0]),(points[9]),(points[48])))

        getcolor(AbstractCube.cube.create_cube,39)
        pygame.draw.polygon(window,cubie_color,((points[12]),(points[49]),(points[51]),(points[15])))

        getcolor(AbstractCube.cube.create_cube,40)
        pygame.draw.polygon(window,cubie_color,((points[49]),(points[48]),(points[50]),(points[51])))

        getcolor(AbstractCube.cube.create_cube,41)
        pygame.draw.polygon(window,cubie_color,((points[48]),(points[9]),(points[18]),(points[50])))

        getcolor(AbstractCube.cube.create_cube,42)
        pygame.draw.polygon(window,cubie_color,((points[15]),(points[51]),(points[14]),(points[2])))

        getcolor(AbstractCube.cube.create_cube,43)
        pygame.draw.polygon(window,cubie_color,((points[51]),(points[50]),(points[17]),(points[14])))

        getcolor(AbstractCube.cube.create_cube,44)
        pygame.draw.polygon(window,cubie_color,((points[50]),(points[18]),(points[3]),(points[17])))


        getcolor(AbstractCube.cube.create_cube,27)
        pygame.draw.polygon(window,cubie_color,((points[0]),(points[10]),(points[40]),(points[9])))

        getcolor(AbstractCube.cube.create_cube,28)
        pygame.draw.polygon(window,cubie_color,((points[10]),(points[22]),(points[41]),(points[40])))

        getcolor(AbstractCube.cube.create_cube,29)
        pygame.draw.polygon(window,cubie_color,((points[22]),(points[4]),(points[21]),(points[41])))

        getcolor(AbstractCube.cube.create_cube,30)
        pygame.draw.polygon(window,cubie_color,((points[9]),(points[40]),(points[42]),(points[18])))

        getcolor(AbstractCube.cube.create_cube,31)
        pygame.draw.polygon(window,cubie_color,((points[40]),(points[41]),(points[43]),(points[42])))

        getcolor(AbstractCube.cube.create_cube,32)
        pygame.draw.polygon(window,cubie_color,((points[41]),(points[21]),(points[30]),(points[43])))

        getcolor(AbstractCube.cube.create_cube,33)
        pygame.draw.polygon(window,cubie_color,((points[18]),(points[42]),(points[19]),(points[3])))

        getcolor(AbstractCube.cube.create_cube,34)
        pygame.draw.polygon(window,cubie_color,((points[42]),(points[43]),(points[31]),(points[19])))

        getcolor(AbstractCube.cube.create_cube,35)
        pygame.draw.polygon(window,cubie_color,((points[43]),(points[30]),(points[7]),(points[31])))
        
        #Connect perimeter
        connect_points(3, 7, points)
        connect_points(4, 7, points)
        connect_points(1, 5, points)
        connect_points(2, 1, points)

        connect_points(0, 1, points)
        connect_points(0, 3, points)
        connect_points(2, 3, points)

        connect_points(4, 5, points)
        connect_points(0, 4, points)
       
        #top midpoints
        connect_points(13, 10, points)
        connect_points(22, 25, points)
        connect_points(8, 20, points)
        connect_points(11, 23, points)

        #Left midpoints
        connect_points(9, 21, points)
        connect_points(18, 30, points)
        connect_points(10, 19, points)
        connect_points(22, 31, points)

        #back midpoints
        connect_points(8, 17, points)
        connect_points(11, 14, points)
        connect_points(9, 12, points)
        connect_points(18, 15, points)


    elif colorkey == 'YBR':
        #Background Colors
        pygame.draw.polygon(window,white,((points[0]),(points[1]),(points[5]),(points[4])))
        pygame.draw.polygon(window,green,((points[0]),(points[1]),(points[2]),(points[3])))
        pygame.draw.polygon(window,orange,((points[1]),(points[5]),(points[6]),(points[2])))
        
        #background perimeter
        connect_points(1, 5, points)
        connect_points(2, 1, points)
        connect_points(0, 1, points)

        #top midpoints
        connect_points(13, 10, points)
        connect_points(22, 25, points)
        connect_points(8, 20, points)
        connect_points(11, 23, points)
        
        #right midpoint
        connect_points(13, 16, points)
        connect_points(25, 28, points)
        connect_points(12, 24, points)
        connect_points(15, 27, points)

        #back midpoints
        connect_points(8, 17, points)
        connect_points(11, 14, points)
        connect_points(9, 12, points)
        connect_points(18, 15, points)
        
        #YBR colors
        pygame.draw.polygon(window,blue,((points[4]),(points[5]),(points[6]),(points[7])))
        pygame.draw.polygon(window,yellow,((points[3]),(points[2]),(points[6]),(points[7])))
        pygame.draw.polygon(window,red,((points[0]),(points[3]),(points[7]),(points[4])))

        getcolor(AbstractCube.cube.create_cube,45)
        pygame.draw.polygon(window,cubie_color,((points[29]),(points[7]),(points[31]),(points[54])))

        getcolor(AbstractCube.cube.create_cube,46)
        pygame.draw.polygon(window,cubie_color,((points[26]),(points[29]),(points[54]),(points[55])))

        getcolor(AbstractCube.cube.create_cube,47)
        pygame.draw.polygon(window,cubie_color,((points[6]),(points[26]),(points[55]),(points[28])))

        getcolor(AbstractCube.cube.create_cube,48)
        pygame.draw.polygon(window,cubie_color,((points[31]),(points[19]),(points[52]),(points[54])))

        getcolor(AbstractCube.cube.create_cube,49)
        pygame.draw.polygon(window,cubie_color,((points[55]),(points[54]),(points[52]),(points[53])))

        getcolor(AbstractCube.cube.create_cube,50)
        pygame.draw.polygon(window,cubie_color,((points[28]),(points[55]),(points[53]),(points[16])))

        getcolor(AbstractCube.cube.create_cube,51)
        pygame.draw.polygon(window,cubie_color,((points[52]),(points[19]),(points[3]),(points[17])))

        getcolor(AbstractCube.cube.create_cube,52)
        pygame.draw.polygon(window,cubie_color,((points[53]),(points[52]),(points[17]),(points[14])))

        getcolor(AbstractCube.cube.create_cube,53)
        pygame.draw.polygon(window,cubie_color,((points[16]),(points[53]),(points[14]),(points[2])))

        



        getcolor(AbstractCube.cube.create_cube,9)
        pygame.draw.polygon(window,cubie_color,((points[4]),(points[20]),(points[36]),(points[21])))

        getcolor(AbstractCube.cube.create_cube,10)
        pygame.draw.polygon(window,cubie_color,((points[20]),(points[23]),(points[37]),(points[36])))

        getcolor(AbstractCube.cube.create_cube,11)
        pygame.draw.polygon(window,cubie_color,((points[23]),(points[5]),(points[24]),(points[37])))

        getcolor(AbstractCube.cube.create_cube,12)
        pygame.draw.polygon(window,cubie_color,((points[21]),(points[36]),(points[38]),(points[30])))

        getcolor(AbstractCube.cube.create_cube,13)
        pygame.draw.polygon(window,cubie_color,((points[36]),(points[37]),(points[39]),(points[38])))

        getcolor(AbstractCube.cube.create_cube,14)
        pygame.draw.polygon(window,cubie_color,((points[37]),(points[24]),(points[27]),(points[39])))

        getcolor(AbstractCube.cube.create_cube,15)
        pygame.draw.polygon(window,cubie_color,((points[30]),(points[38]),(points[29]),(points[7])))

        getcolor(AbstractCube.cube.create_cube,16)
        pygame.draw.polygon(window,cubie_color,((points[38]),(points[39]),(points[26]),(points[29])))

        getcolor(AbstractCube.cube.create_cube,17)
        pygame.draw.polygon(window,cubie_color,((points[39]),(points[27]),(points[6]),(points[26])))



        getcolor(AbstractCube.cube.create_cube,27)
        pygame.draw.polygon(window,cubie_color,((points[0]),(points[10]),(points[40]),(points[9])))

        getcolor(AbstractCube.cube.create_cube,28)
        pygame.draw.polygon(window,cubie_color,((points[10]),(points[22]),(points[41]),(points[40])))

        getcolor(AbstractCube.cube.create_cube,29)
        pygame.draw.polygon(window,cubie_color,((points[22]),(points[4]),(points[21]),(points[41])))

        getcolor(AbstractCube.cube.create_cube,30)
        pygame.draw.polygon(window,cubie_color,((points[9]),(points[40]),(points[42]),(points[18])))

        getcolor(AbstractCube.cube.create_cube,31)
        pygame.draw.polygon(window,cubie_color,((points[40]),(points[41]),(points[43]),(points[42])))

        getcolor(AbstractCube.cube.create_cube,32)
        pygame.draw.polygon(window,cubie_color,((points[41]),(points[21]),(points[30]),(points[43])))

        getcolor(AbstractCube.cube.create_cube,33)
        pygame.draw.polygon(window,cubie_color,((points[18]),(points[42]),(points[19]),(points[3])))

        getcolor(AbstractCube.cube.create_cube,34)
        pygame.draw.polygon(window,cubie_color,((points[42]),(points[43]),(points[31]),(points[19])))

        getcolor(AbstractCube.cube.create_cube,35)
        pygame.draw.polygon(window,cubie_color,((points[43]),(points[30]),(points[7]),(points[31])))
        
        #Connect perimeter
        connect_points(3, 7, points)
        connect_points(4, 7, points)
        connect_points(6, 7, points)
        connect_points(6, 2, points)

        connect_points(5, 6, points)
        connect_points(0, 3, points)
        connect_points(2, 3, points)

        connect_points(4, 5, points)
        connect_points(0, 4, points)

        #front midpoint
        connect_points(20, 29, points)
        connect_points(23, 26, points)
        connect_points(21, 24, points)
        connect_points(30, 27, points)
       
        #Left midpoints
        connect_points(9, 21, points)
        connect_points(18, 30, points)
        connect_points(10, 19, points)
        connect_points(22, 31, points)

        #bottom Midpoints
        connect_points(26, 14, points)
        connect_points(29, 17, points)
        connect_points(19, 16, points)
        connect_points(31, 28, points)


        

    elif colorkey == 'YRG':
        #Background Colors
        pygame.draw.polygon(window,white,((points[0]),(points[1]),(points[5]),(points[4])))
        pygame.draw.polygon(window,blue,((points[4]),(points[5]),(points[6]),(points[7])))
        pygame.draw.polygon(window,orange,((points[1]),(points[5]),(points[6]),(points[2])))
        
        #background perimeter
        connect_points(1, 5, points)
        connect_points(4, 5, points)
        connect_points(5, 6, points)
        
        #top midpoints
        connect_points(13, 10, points)
        connect_points(22, 25, points)
        connect_points(8, 20, points)
        connect_points(11, 23, points)
        
        #right midpoint
        connect_points(13, 16, points)
        connect_points(25, 28, points)
        connect_points(12, 24, points)
        connect_points(15, 27, points)

        #front midpoint
        connect_points(20, 29, points)
        connect_points(23, 26, points)
        connect_points(21, 24, points)
        connect_points(30, 27, points)
        
        #YGR colors
        pygame.draw.polygon(window,green,((points[0]),(points[1]),(points[2]),(points[3])))
        pygame.draw.polygon(window,yellow,((points[3]),(points[2]),(points[6]),(points[7])))
        pygame.draw.polygon(window,red,((points[0]),(points[3]),(points[7]),(points[4])))

        getcolor(AbstractCube.cube.create_cube,45)
        pygame.draw.polygon(window,cubie_color,((points[29]),(points[7]),(points[31]),(points[54])))

        getcolor(AbstractCube.cube.create_cube,46)
        pygame.draw.polygon(window,cubie_color,((points[26]),(points[29]),(points[54]),(points[55])))

        getcolor(AbstractCube.cube.create_cube,47)
        pygame.draw.polygon(window,cubie_color,((points[6]),(points[26]),(points[55]),(points[28])))

        getcolor(AbstractCube.cube.create_cube,48)
        pygame.draw.polygon(window,cubie_color,((points[31]),(points[19]),(points[52]),(points[54])))

        getcolor(AbstractCube.cube.create_cube,49)
        pygame.draw.polygon(window,cubie_color,((points[55]),(points[54]),(points[52]),(points[53])))

        getcolor(AbstractCube.cube.create_cube,50)
        pygame.draw.polygon(window,cubie_color,((points[28]),(points[55]),(points[53]),(points[16])))

        getcolor(AbstractCube.cube.create_cube,51)
        pygame.draw.polygon(window,cubie_color,((points[52]),(points[19]),(points[3]),(points[17])))

        getcolor(AbstractCube.cube.create_cube,52)
        pygame.draw.polygon(window,cubie_color,((points[53]),(points[52]),(points[17]),(points[14])))

        getcolor(AbstractCube.cube.create_cube,53)
        pygame.draw.polygon(window,cubie_color,((points[16]),(points[53]),(points[14]),(points[2])))




        getcolor(AbstractCube.cube.create_cube,27)
        pygame.draw.polygon(window,cubie_color,((points[0]),(points[10]),(points[40]),(points[9])))

        getcolor(AbstractCube.cube.create_cube,28)
        pygame.draw.polygon(window,cubie_color,((points[10]),(points[22]),(points[41]),(points[40])))

        getcolor(AbstractCube.cube.create_cube,29)
        pygame.draw.polygon(window,cubie_color,((points[22]),(points[4]),(points[21]),(points[41])))

        getcolor(AbstractCube.cube.create_cube,30)
        pygame.draw.polygon(window,cubie_color,((points[9]),(points[40]),(points[42]),(points[18])))

        getcolor(AbstractCube.cube.create_cube,31)
        pygame.draw.polygon(window,cubie_color,((points[40]),(points[41]),(points[43]),(points[42])))

        getcolor(AbstractCube.cube.create_cube,32)
        pygame.draw.polygon(window,cubie_color,((points[41]),(points[21]),(points[30]),(points[43])))

        getcolor(AbstractCube.cube.create_cube,33)
        pygame.draw.polygon(window,cubie_color,((points[18]),(points[42]),(points[19]),(points[3])))

        getcolor(AbstractCube.cube.create_cube,34)
        pygame.draw.polygon(window,cubie_color,((points[42]),(points[43]),(points[31]),(points[19])))

        getcolor(AbstractCube.cube.create_cube,35)
        pygame.draw.polygon(window,cubie_color,((points[43]),(points[30]),(points[7]),(points[31])))





        getcolor(AbstractCube.cube.create_cube,36)
        pygame.draw.polygon(window,cubie_color,((points[1]),(points[11]),(points[49]),(points[12])))

        getcolor(AbstractCube.cube.create_cube,37)
        pygame.draw.polygon(window,cubie_color,((points[11]),(points[8]),(points[48]),(points[49])))

        getcolor(AbstractCube.cube.create_cube,38)
        pygame.draw.polygon(window,cubie_color,((points[8]),(points[0]),(points[9]),(points[48])))

        getcolor(AbstractCube.cube.create_cube,39)
        pygame.draw.polygon(window,cubie_color,((points[12]),(points[49]),(points[51]),(points[15])))

        getcolor(AbstractCube.cube.create_cube,40)
        pygame.draw.polygon(window,cubie_color,((points[49]),(points[48]),(points[50]),(points[51])))

        getcolor(AbstractCube.cube.create_cube,41)
        pygame.draw.polygon(window,cubie_color,((points[48]),(points[9]),(points[18]),(points[50])))

        getcolor(AbstractCube.cube.create_cube,42)
        pygame.draw.polygon(window,cubie_color,((points[15]),(points[51]),(points[14]),(points[2])))

        getcolor(AbstractCube.cube.create_cube,43)
        pygame.draw.polygon(window,cubie_color,((points[51]),(points[50]),(points[17]),(points[14])))

        getcolor(AbstractCube.cube.create_cube,44)
        pygame.draw.polygon(window,cubie_color,((points[50]),(points[18]),(points[3]),(points[17])))
        
        #Connect perimeter
        connect_points(3, 7, points)
        connect_points(4, 7, points)
        connect_points(6, 7, points)
        connect_points(6, 2, points)

        connect_points(2, 1, points)
        connect_points(0, 1, points)
        connect_points(0, 3, points)

        connect_points(2, 3, points)
        connect_points(0, 4, points)
    
        #Left midpoints
        connect_points(9, 21, points)
        connect_points(18, 30, points)
        connect_points(10, 19, points)
        connect_points(22, 31, points)

        #back midpoints
        connect_points(8, 17, points)
        connect_points(11, 14, points)
        connect_points(9, 12, points)
        connect_points(18, 15, points)

        #bottom Midpoints
        connect_points(26, 14, points)
        connect_points(29, 17, points)
        connect_points(19, 16, points)
        connect_points(31, 28, points)


    elif colorkey == 'YOG':
        #Background Colors
        pygame.draw.polygon(window,white,((points[0]),(points[1]),(points[5]),(points[4])))
        pygame.draw.polygon(window,blue,((points[4]),(points[5]),(points[6]),(points[7])))
        pygame.draw.polygon(window,red,((points[0]),(points[3]),(points[7]),(points[4])))
        
        #background perimeter
        connect_points(0, 4, points)
        connect_points(4, 7, points)
        connect_points(4, 5, points)
        
        
        #top midpoints
        connect_points(13, 10, points)
        connect_points(22, 25, points)
        connect_points(8, 20, points)
        connect_points(11, 23, points)

        #Left midpoints
        connect_points(9, 21, points)
        connect_points(18, 30, points)
        connect_points(10, 19, points)
        connect_points(22, 31, points)

        #front midpoint
        connect_points(20, 29, points)
        connect_points(23, 26, points)
        connect_points(21, 24, points)
        connect_points(30, 27, points)
        
        #YOG colors
        pygame.draw.polygon(window,green,((points[0]),(points[1]),(points[2]),(points[3])))
        pygame.draw.polygon(window,yellow,((points[3]),(points[2]),(points[6]),(points[7])))
        pygame.draw.polygon(window,orange,((points[1]),(points[5]),(points[6]),(points[2])))

        getcolor(AbstractCube.cube.create_cube,45)
        pygame.draw.polygon(window,cubie_color,((points[29]),(points[7]),(points[31]),(points[54])))

        getcolor(AbstractCube.cube.create_cube,46)
        pygame.draw.polygon(window,cubie_color,((points[26]),(points[29]),(points[54]),(points[55])))

        getcolor(AbstractCube.cube.create_cube,47)
        pygame.draw.polygon(window,cubie_color,((points[6]),(points[26]),(points[55]),(points[28])))

        getcolor(AbstractCube.cube.create_cube,48)
        pygame.draw.polygon(window,cubie_color,((points[31]),(points[19]),(points[52]),(points[54])))

        getcolor(AbstractCube.cube.create_cube,49)
        pygame.draw.polygon(window,cubie_color,((points[55]),(points[54]),(points[52]),(points[53])))

        getcolor(AbstractCube.cube.create_cube,50)
        pygame.draw.polygon(window,cubie_color,((points[28]),(points[55]),(points[53]),(points[16])))

        getcolor(AbstractCube.cube.create_cube,51)
        pygame.draw.polygon(window,cubie_color,((points[52]),(points[19]),(points[3]),(points[17])))

        getcolor(AbstractCube.cube.create_cube,52)
        pygame.draw.polygon(window,cubie_color,((points[53]),(points[52]),(points[17]),(points[14])))

        getcolor(AbstractCube.cube.create_cube,53)
        pygame.draw.polygon(window,cubie_color,((points[16]),(points[53]),(points[14]),(points[2])))



        getcolor(AbstractCube.cube.create_cube,18)
        pygame.draw.polygon(window,cubie_color,((points[5]),(points[25]),(points[45]),(points[24])))

        getcolor(AbstractCube.cube.create_cube,19)
        pygame.draw.polygon(window,cubie_color,((points[25]),(points[13]),(points[44]),(points[45])))

        getcolor(AbstractCube.cube.create_cube,20)
        pygame.draw.polygon(window,cubie_color,((points[13]),(points[1]),(points[12]),(points[44])))

        getcolor(AbstractCube.cube.create_cube,21)
        pygame.draw.polygon(window,cubie_color,((points[24]),(points[45]),(points[47]),(points[27])))

        getcolor(AbstractCube.cube.create_cube,22)
        pygame.draw.polygon(window,cubie_color,((points[45]),(points[44]),(points[46]),(points[47])))

        getcolor(AbstractCube.cube.create_cube,23)
        pygame.draw.polygon(window,cubie_color,((points[44]),(points[12]),(points[15]),(points[46])))

        getcolor(AbstractCube.cube.create_cube,24)
        pygame.draw.polygon(window,cubie_color,((points[27]),(points[47]),(points[28]),(points[6])))

        getcolor(AbstractCube.cube.create_cube,25)
        pygame.draw.polygon(window,cubie_color,((points[47]),(points[46]),(points[16]),(points[28])))

        getcolor(AbstractCube.cube.create_cube,26)
        pygame.draw.polygon(window,cubie_color,((points[46]),(points[15]),(points[2]),(points[16])))



        getcolor(AbstractCube.cube.create_cube,36)
        pygame.draw.polygon(window,cubie_color,((points[1]),(points[11]),(points[49]),(points[12])))

        getcolor(AbstractCube.cube.create_cube,37)
        pygame.draw.polygon(window,cubie_color,((points[11]),(points[8]),(points[48]),(points[49])))

        getcolor(AbstractCube.cube.create_cube,38)
        pygame.draw.polygon(window,cubie_color,((points[8]),(points[0]),(points[9]),(points[48])))

        getcolor(AbstractCube.cube.create_cube,39)
        pygame.draw.polygon(window,cubie_color,((points[12]),(points[49]),(points[51]),(points[15])))

        getcolor(AbstractCube.cube.create_cube,40)
        pygame.draw.polygon(window,cubie_color,((points[49]),(points[48]),(points[50]),(points[51])))

        getcolor(AbstractCube.cube.create_cube,41)
        pygame.draw.polygon(window,cubie_color,((points[48]),(points[9]),(points[18]),(points[50])))

        getcolor(AbstractCube.cube.create_cube,42)
        pygame.draw.polygon(window,cubie_color,((points[15]),(points[51]),(points[14]),(points[2])))

        getcolor(AbstractCube.cube.create_cube,43)
        pygame.draw.polygon(window,cubie_color,((points[51]),(points[50]),(points[17]),(points[14])))

        getcolor(AbstractCube.cube.create_cube,44)
        pygame.draw.polygon(window,cubie_color,((points[50]),(points[18]),(points[3]),(points[17])))
        
        #Connect perimeter
        connect_points(3, 7, points)
        connect_points(6, 7, points)
        connect_points(6, 2, points)
        connect_points(2, 1, points)

        connect_points(5, 6, points)
        connect_points(1, 5, points)
        connect_points(0, 1, points)
        
        connect_points(0, 3, points)
        connect_points(2, 3, points)

        #right midpoint
        connect_points(13, 16, points)
        connect_points(25, 28, points)
        connect_points(12, 24, points)
        connect_points(15, 27, points)
        
        #back midpoints
        connect_points(8, 17, points)
        connect_points(11, 14, points)
        connect_points(9, 12, points)
        connect_points(18, 15, points)

        #bottom Midpoints
        connect_points(26, 14, points)
        connect_points(29, 17, points)
        connect_points(19, 16, points)
        connect_points(31, 28, points)

    elif colorkey == 'YOB':
        #Background Colors
        pygame.draw.polygon(window,white,((points[0]),(points[1]),(points[5]),(points[4])))
        pygame.draw.polygon(window,green,((points[0]),(points[1]),(points[2]),(points[3])))
        pygame.draw.polygon(window,red,((points[0]),(points[3]),(points[7]),(points[4])))
        
        #background perimeter
        connect_points(0, 4, points)
        connect_points(0, 1, points)
        connect_points(0, 3, points)
        
        #top midpoints
        connect_points(13, 10, points)
        connect_points(22, 25, points)
        connect_points(8, 20, points)
        connect_points(11, 23, points)

        #Left midpoints
        connect_points(9, 21, points)
        connect_points(18, 30, points)
        connect_points(10, 19, points)
        connect_points(22, 31, points)

        #back midpoints
        connect_points(8, 17, points)
        connect_points(11, 14, points)
        connect_points(9, 12, points)
        connect_points(18, 15, points)
        
        #YOB colors
        pygame.draw.polygon(window,yellow,((points[3]),(points[2]),(points[6]),(points[7])))
        pygame.draw.polygon(window,orange,((points[1]),(points[5]),(points[6]),(points[2])))
        pygame.draw.polygon(window,blue,((points[4]),(points[5]),(points[6]),(points[7])))

        getcolor(AbstractCube.cube.create_cube,45)
        pygame.draw.polygon(window,cubie_color,((points[29]),(points[7]),(points[31]),(points[54])))

        getcolor(AbstractCube.cube.create_cube,46)
        pygame.draw.polygon(window,cubie_color,((points[26]),(points[29]),(points[54]),(points[55])))

        getcolor(AbstractCube.cube.create_cube,47)
        pygame.draw.polygon(window,cubie_color,((points[6]),(points[26]),(points[55]),(points[28])))

        getcolor(AbstractCube.cube.create_cube,48)
        pygame.draw.polygon(window,cubie_color,((points[31]),(points[19]),(points[52]),(points[54])))

        getcolor(AbstractCube.cube.create_cube,49)
        pygame.draw.polygon(window,cubie_color,((points[55]),(points[54]),(points[52]),(points[53])))

        getcolor(AbstractCube.cube.create_cube,50)
        pygame.draw.polygon(window,cubie_color,((points[28]),(points[55]),(points[53]),(points[16])))

        getcolor(AbstractCube.cube.create_cube,51)
        pygame.draw.polygon(window,cubie_color,((points[52]),(points[19]),(points[3]),(points[17])))

        getcolor(AbstractCube.cube.create_cube,52)
        pygame.draw.polygon(window,cubie_color,((points[53]),(points[52]),(points[17]),(points[14])))

        getcolor(AbstractCube.cube.create_cube,53)
        pygame.draw.polygon(window,cubie_color,((points[16]),(points[53]),(points[14]),(points[2])))



        getcolor(AbstractCube.cube.create_cube,18)
        pygame.draw.polygon(window,cubie_color,((points[5]),(points[25]),(points[45]),(points[24])))

        getcolor(AbstractCube.cube.create_cube,19)
        pygame.draw.polygon(window,cubie_color,((points[25]),(points[13]),(points[44]),(points[45])))

        getcolor(AbstractCube.cube.create_cube,20)
        pygame.draw.polygon(window,cubie_color,((points[13]),(points[1]),(points[12]),(points[44])))

        getcolor(AbstractCube.cube.create_cube,21)
        pygame.draw.polygon(window,cubie_color,((points[24]),(points[45]),(points[47]),(points[27])))

        getcolor(AbstractCube.cube.create_cube,22)
        pygame.draw.polygon(window,cubie_color,((points[45]),(points[44]),(points[46]),(points[47])))

        getcolor(AbstractCube.cube.create_cube,23)
        pygame.draw.polygon(window,cubie_color,((points[44]),(points[12]),(points[15]),(points[46])))

        getcolor(AbstractCube.cube.create_cube,24)
        pygame.draw.polygon(window,cubie_color,((points[27]),(points[47]),(points[28]),(points[6])))

        getcolor(AbstractCube.cube.create_cube,25)
        pygame.draw.polygon(window,cubie_color,((points[47]),(points[46]),(points[16]),(points[28])))

        getcolor(AbstractCube.cube.create_cube,26)
        pygame.draw.polygon(window,cubie_color,((points[46]),(points[15]),(points[2]),(points[16])))




        getcolor(AbstractCube.cube.create_cube,9)
        pygame.draw.polygon(window,cubie_color,((points[4]),(points[20]),(points[36]),(points[21])))

        getcolor(AbstractCube.cube.create_cube,10)
        pygame.draw.polygon(window,cubie_color,((points[20]),(points[23]),(points[37]),(points[36])))

        getcolor(AbstractCube.cube.create_cube,11)
        pygame.draw.polygon(window,cubie_color,((points[23]),(points[5]),(points[24]),(points[37])))

        getcolor(AbstractCube.cube.create_cube,12)
        pygame.draw.polygon(window,cubie_color,((points[21]),(points[36]),(points[38]),(points[30])))

        getcolor(AbstractCube.cube.create_cube,13)
        pygame.draw.polygon(window,cubie_color,((points[36]),(points[37]),(points[39]),(points[38])))

        getcolor(AbstractCube.cube.create_cube,14)
        pygame.draw.polygon(window,cubie_color,((points[37]),(points[24]),(points[27]),(points[39])))

        getcolor(AbstractCube.cube.create_cube,15)
        pygame.draw.polygon(window,cubie_color,((points[30]),(points[38]),(points[29]),(points[7])))

        getcolor(AbstractCube.cube.create_cube,16)
        pygame.draw.polygon(window,cubie_color,((points[38]),(points[39]),(points[26]),(points[29])))

        getcolor(AbstractCube.cube.create_cube,17)
        pygame.draw.polygon(window,cubie_color,((points[39]),(points[27]),(points[6]),(points[26])))
        
        #Connect perimeter
        connect_points(3, 7, points)
        connect_points(6, 7, points)
        connect_points(6, 2, points)
        connect_points(2, 1, points)

        connect_points(5, 6, points)
        connect_points(1, 5, points)
        

        connect_points(4, 7, points)
        connect_points(4, 5, points)
        connect_points(2, 3, points)

        #right midpoint
        connect_points(13, 16, points)
        connect_points(25, 28, points)
        connect_points(12, 24, points)
        connect_points(15, 27, points)

        #front midpoint
        connect_points(20, 29, points)
        connect_points(23, 26, points)
        connect_points(21, 24, points)
        connect_points(30, 27, points)

        #bottom Midpoints
        connect_points(26, 14, points)
        connect_points(29, 17, points)
        connect_points(19, 16, points)
        connect_points(31, 28, points)
        
    
#######################################  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            angle_y = angle_x = angle_z = 0
        if keys[pygame.K_j]:
            angle_y += ROTATE_SPEED
        if keys[pygame.K_l]:
            angle_y -= ROTATE_SPEED
        if keys[pygame.K_k]:
            angle_x += ROTATE_SPEED
        if keys[pygame.K_i]:
            angle_x -= ROTATE_SPEED
        if keys[pygame.K_u]:
            angle_z -= ROTATE_SPEED
        if keys[pygame.K_p]:
            angle_z += ROTATE_SPEED
            
        if keys[pygame.K_b] and keys[pygame.K_RIGHT]:
            face_points = [cube_points[4],cube_points[20],cube_points[23],cube_points[5],cube_points[21],cube_points[36],cube_points[37],cube_points[24],cube_points[30],cube_points[38],cube_points[39],cube_points[27],cube_points[7],cube_points[29],cube_points[26],cube_points[6],cube_points[22],cube_points[34],cube_points[35],cube_points[25],cube_points[41],cube_points[45],cube_points[43],cube_points[47],cube_points[31],cube_points[54],cube_points[55],cube_points[28]]
            theta_y = angle_y 
            theta_x = angle_x
            theta_z = angle_z
            direction = 'clockwise'
            alg.turn('f', phi_step, degree90, theta_z, theta_x, theta_y, window, face_points, projection_matrix, scale, WINDOW_SIZE, colorkey, white, blue, orange, red, green, yellow, points, connect_points, AbstractCube.cube.create_cube, direction)
            AbstractCube.cube.turn('f')

        if keys[pygame.K_b] and keys[pygame.K_LEFT]:
            face_points = [cube_points[4],cube_points[20],cube_points[23],cube_points[5],cube_points[21],cube_points[36],cube_points[37],cube_points[24],cube_points[30],cube_points[38],cube_points[39],cube_points[27],cube_points[7],cube_points[29],cube_points[26],cube_points[6],cube_points[22],cube_points[34],cube_points[35],cube_points[25],cube_points[41],cube_points[45],cube_points[43],cube_points[47],cube_points[31],cube_points[54],cube_points[55],cube_points[28]]
            theta_y = angle_y
            theta_x = angle_x
            theta_z = angle_z
            direction = 'anticlockwise'
            alg.turn('f prime', phi_step, degree90, theta_z, theta_x, theta_y, window, face_points, projection_matrix, scale, WINDOW_SIZE, colorkey, white, blue, orange, red, green, yellow, points, connect_points, AbstractCube.cube.create_cube, direction)
            AbstractCube.cube.turn('f')
            AbstractCube.cube.turn('f')
            AbstractCube.cube.turn('f')
            
        if keys[pygame.K_o] and keys[pygame.K_RIGHT]:
            face_points = [cube_points[1],cube_points[2],cube_points[5],cube_points[6]]         
            theta_y = angle_y 
            theta_x = angle_x
            theta_z = angle_z
            AbstractCube.cube.turn('r')
            #alg.turn('r', phi_step, degree90, theta_z, theta_x, theta_y, window, face_points, projection_matrix, scale, WINDOW_SIZE, colorkey, white, blue, orange, red, green, yellow, points, connect_points)
            
        if keys[pygame.K_o] and keys[pygame.K_LEFT]:
            face_points = [cube_points[1],cube_points[2],cube_points[5],cube_points[6]]       
            theta_y = angle_y 
            theta_x = angle_x
            theta_z = angle_z
            AbstractCube.cube.turn('r')
            AbstractCube.cube.turn('r')
            AbstractCube.cube.turn('r')
            #alg.turn('r prime', phi_step, degree90, theta_z, theta_x, theta_y, window, face_points, projection_matrix, scale, WINDOW_SIZE, colorkey, white, blue, orange, red, green, yellow, points, connect_points)
            
        if keys[pygame.K_g] and keys[pygame.K_RIGHT]:
            face_points = [cube_points[0],cube_points[1],cube_points[2],cube_points[3]]
            theta_y = angle_y 
            theta_x = angle_x
            theta_z = angle_z
            AbstractCube.cube.turn('b')
            #alg.turn('b', phi_step, degree90, theta_z, theta_x, theta_y, window, face_points, projection_matrix, scale, WINDOW_SIZE, colorkey, white, blue, orange, red, green, yellow, points, connect_points)

        if keys[pygame.K_g] and keys[pygame.K_LEFT]:
            face_points = [cube_points[0],cube_points[1],cube_points[2],cube_points[3]]
            theta_y = angle_y 
            theta_x = angle_x
            theta_z = angle_z
            AbstractCube.cube.turn('b')
            AbstractCube.cube.turn('b')
            AbstractCube.cube.turn('b')
            #alg.turn('b prime', phi_step, degree90, theta_z, theta_x, theta_y, window, face_points, projection_matrix, scale, WINDOW_SIZE, colorkey, white, blue, orange, red, green, yellow, points, connect_points)
            
        if keys[pygame.K_r] and keys[pygame.K_RIGHT]:
            face_points = [cube_points[0],cube_points[4],cube_points[3],cube_points[7]]
            theta_y = angle_y 
            theta_x = angle_x
            theta_z = angle_z
            AbstractCube.cube.turn('l')
            #alg.turn('l', phi_step, degree90, theta_z, theta_x, theta_y, window, face_points, projection_matrix, scale, WINDOW_SIZE, colorkey, white, blue, orange, red, green, yellow, points, connect_points)
            
        if keys[pygame.K_r] and keys[pygame.K_LEFT]:
            face_points = [cube_points[0],cube_points[4],cube_points[3],cube_points[7]]
            theta_y = angle_y 
            theta_x = angle_x
            theta_z = angle_z
            AbstractCube.cube.turn('l')
            AbstractCube.cube.turn('l')
            AbstractCube.cube.turn('l')
            #alg.turn('l prime', phi_step, degree90, theta_z, theta_x, theta_y, window, face_points, projection_matrix, scale, WINDOW_SIZE, colorkey, white, blue, orange, red, green, yellow, points, connect_points)
        
        if keys[pygame.K_w] and keys[pygame.K_RIGHT]:
            face_points = [cube_points[0],cube_points[1],cube_points[4],cube_points[5]]
            theta_y = angle_y 
            theta_x = angle_x
            theta_z = angle_z
            AbstractCube.cube.turn('u')
            #alg.turn('u', phi_step, degree90, theta_z, theta_x, theta_y, window, face_points, projection_matrix, scale, WINDOW_SIZE, colorkey, white, blue, orange, red, green, yellow, points, connect_points)
            
        if keys[pygame.K_w] and keys[pygame.K_LEFT]:
            face_points = [cube_points[0],cube_points[1],cube_points[4],cube_points[5]]
            theta_y = angle_y 
            theta_x = angle_x
            theta_z = angle_z
            AbstractCube.cube.turn('u')
            AbstractCube.cube.turn('u')
            AbstractCube.cube.turn('u')
            #alg.turn('u prime', phi_step, degree90, theta_z, theta_x, theta_y, window, face_points, projection_matrix, scale, WINDOW_SIZE, colorkey, white, blue, orange, red, green, yellow, points, connect_points)

        if keys[pygame.K_y] and keys[pygame.K_RIGHT]:
            face_points = [cube_points[2],cube_points[3],cube_points[6],cube_points[7]]
            theta_y = angle_y 
            theta_x = angle_x
            theta_z = angle_z
            AbstractCube.cube.turn('d')
            #alg.turn('d', phi_step, degree90, theta_z, theta_x, theta_y, window, face_points, projection_matrix, scale, WINDOW_SIZE, colorkey, white, blue, orange, red, green, yellow, points, connect_points)
            
        if keys[pygame.K_y] and keys[pygame.K_LEFT]:
            face_points = [cube_points[2],cube_points[3],cube_points[6],cube_points[7]]
            theta_y = angle_y 
            theta_x = angle_x
            theta_z = angle_z
            AbstractCube.cube.turn('d')
            AbstractCube.cube.turn('d')
            AbstractCube.cube.turn('d')
            #alg.turn('d prime', phi_step, degree90, theta_z, theta_x, theta_y, window, face_points, projection_matrix, scale, WINDOW_SIZE, colorkey, white, blue, orange, red, green, yellow, points, connect_points)

        

    pygame.display.update()






    
    
