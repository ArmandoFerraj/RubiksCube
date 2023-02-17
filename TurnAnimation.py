import pygame
from math import *
import numpy as np

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,165,0)
white = (255,255,255)
yellow = (255,255,0)

def getcolor4gui(cubelist, cubie_loc):
    global cubie_color4gui
    if cubelist[cubie_loc] in range(0,9):
        cubie_color4gui = white
    elif cubelist[cubie_loc] in range(9,18):
        cubie_color4gui = blue
    elif cubelist[cubie_loc] in range(18,27):
        cubie_color4gui = orange
    elif cubelist[cubie_loc] in range(27,36):
        cubie_color4gui = red
    elif cubelist[cubie_loc] in range(36,45):
        cubie_color4gui = green
    else: 
        cubie_color4gui = yellow

def turn(face_alg, phi_step, degree90, theta_z, theta_x, theta_y, window, face_points, projection_matrix, scale, WINDOW_SIZE, colorkey, white, blue, orange, red, green, yellow, points, connect_points, abstractcube, direction):
    phi = 0

    
    for degree_increment in degree90:
        if face_alg == 'f':

            parity = 1
            turn_matrix = [[cos(phi), -sin(phi), 0],
                           [sin(phi), cos(phi), 0],
                           [0, 0, 1]]
            drawing_key = 'draw f'
            #pygame.draw.polygon(window,blue,((points[4]),(points[5]),(points[6]),(points[7])))
            
        elif face_alg == 'f prime':
            parity = -1
            turn_matrix = [[cos(phi), -sin(phi), 0],
                           [sin(phi), cos(phi), 0],
                           [0, 0, 1]]
            drawing_key = 'draw f'
            
        elif face_alg == 'r':
            parity = -1
            turn_matrix = [[1, 0, 0],
                           [0, cos(phi), -sin(phi)],
                           [0, sin(phi), cos(phi)]]
            drawing_key = 'draw r'
                
        elif face_alg == 'r prime':
            parity = 1
            turn_matrix = [[1, 0, 0],
                           [0, cos(phi), -sin(phi)],
                           [0, sin(phi), cos(phi)]]
            drawing_key = 'draw r'
                
        elif face_alg == 'b':
            parity = -1
            turn_matrix = [[cos(phi), -sin(phi), 0],
                           [sin(phi), cos(phi), 0],
                           [0, 0, 1]]
            drawing_key = 'draw b'
        elif face_alg == 'b prime':
            parity = 1
            turn_matrix = [[cos(phi), -sin(phi), 0],
                           [sin(phi), cos(phi), 0],
                           [0, 0, 1]]
            drawing_key = 'draw b'
            
        elif face_alg == 'l':
            parity = 1
            turn_matrix = [[1, 0, 0],
                           [0, cos(phi), -sin(phi)],
                           [0, sin(phi), cos(phi)]]
            drawing_key = 'draw l'
        
        elif face_alg == 'l prime':
            parity = -1
            turn_matrix = [[1, 0, 0],
                           [0, cos(phi), -sin(phi)],
                           [0, sin(phi), cos(phi)]]
            drawing_key = 'draw l'
        
        elif face_alg == 'u':
            parity = 1
            turn_matrix = [[cos(phi), 0, sin(phi)],
                           [0, 1, 0],
                           [-sin(phi), 0, cos(phi)]]
            drawing_key = 'draw u'
            
        elif face_alg == 'u prime':
            parity = -1
            turn_matrix = [[cos(phi), 0, sin(phi)],
                           [0, 1, 0],
                           [-sin(phi), 0, cos(phi)]]
            drawing_key = 'draw u'
            
        elif face_alg == 'd':
            parity = 1
            turn_matrix = [[cos(phi), 0, sin(phi)],
                           [0, 1, 0],
                           [-sin(phi), 0, cos(phi)]]
            drawing_key = 'draw d'
            
        elif face_alg == 'd prime':
            parity = -1
            turn_matrix = [[cos(phi), 0, sin(phi)],
                           [0, 1, 0],
                           [-sin(phi), 0, cos(phi)]]
            drawing_key = 'draw d'
        
            
        face_rotation_z = [[cos(theta_z), -sin(theta_z), 0],
                           [sin(theta_z), cos(theta_z), 0],
                           [0, 0, 1]]
        face_rotation_y = [[cos(theta_y), 0, sin(theta_y)],
                           [0, 1, 0],
                           [-sin(theta_y), 0, cos(theta_y)]]
        face_rotation_x = [[1, 0, 0],
                           [0, cos(theta_x), -sin(theta_x)],
                           [0, sin(theta_x), cos(theta_x)]]
        phi = phi + (phi_step*parity)
        window.fill((0,0,0))
        
        h = 0
        face_pts = [0 for _ in range(len(face_points))]
        tfp = []

        for point in face_points:
            face_point = np.dot(turn_matrix,point)
            face_rotate_x = np.dot(face_rotation_x, face_point)
            face_rotate_y = np.dot(face_rotation_y, face_rotate_x)
            face_rotate_z = np.dot(face_rotation_z, face_rotate_y)
            face_point_2d = np.dot(projection_matrix, face_rotate_z)
            x = (face_point_2d[0][0] * scale) + WINDOW_SIZE/2
            y = (face_point_2d[1][0] * scale) + WINDOW_SIZE/2
            #pygame.draw.circle(window, (255, 0, 0), (x,y), 5)
            tfp.append((x,y))
            face_pts[h] = (x,y)
            h += 1
            
        #print(face_pts)
        if drawing_key == 'draw f':

            if colorkey == 'RWB':


                #static red cubies
                
                getcolor4gui(abstractcube,27)
                pygame.draw.polygon(window,cubie_color4gui,((points[0]),(points[10]),(points[40]),(points[9])))

                getcolor4gui(abstractcube,28)
                pygame.draw.polygon(window,cubie_color4gui,((points[10]),(points[22]),(points[41]),(points[40])))

                getcolor4gui(abstractcube,30)
                pygame.draw.polygon(window,cubie_color4gui,((points[9]),(points[40]),(points[42]),(points[18])))

                getcolor4gui(abstractcube,31)
                pygame.draw.polygon(window,cubie_color4gui,((points[40]),(points[41]),(points[43]),(points[42])))

                getcolor4gui(abstractcube,34)
                pygame.draw.polygon(window,cubie_color4gui,((points[42]),(points[43]),(points[31]),(points[19])))

                getcolor4gui(abstractcube,33)
                pygame.draw.polygon(window,cubie_color4gui,((points[18]),(points[42]),(points[19]),(points[3])))



                #static white cubies

                getcolor4gui(abstractcube,0)
                pygame.draw.polygon(window,cubie_color4gui,((points[0]),(points[8]),(points[32]),(points[10])))

                getcolor4gui(abstractcube,1)
                pygame.draw.polygon(window,cubie_color4gui,((points[8]),(points[11]),(points[33]),(points[32])))
                
                getcolor4gui(abstractcube,2)
                pygame.draw.polygon(window,cubie_color4gui,((points[11]),(points[1]),(points[13]),(points[33])))

                getcolor4gui(abstractcube,3)
                pygame.draw.polygon(window,cubie_color4gui,((points[10]),(points[32]),(points[34]),(points[22])))

                getcolor4gui(abstractcube,4)
                pygame.draw.polygon(window,cubie_color4gui,((points[32]),(points[33]),(points[35]),(points[34])))

                getcolor4gui(abstractcube,5)
                pygame.draw.polygon(window,cubie_color4gui,((points[33]),(points[13]),(points[25]),(points[35])))
                

                #red-white static perimeter and lines
                
                connect_points(0, 22, points)
                connect_points(3, 0, points)
                connect_points(3, 31, points)
                

                connect_points(0, 1, points)
                connect_points(1, 25, points)
                

                connect_points(13, 10, points)
                connect_points(22, 25, points)
                connect_points(8, 34, points)
                connect_points(11, 35, points)

                connect_points(10, 19, points)
                connect_points(22, 31, points)
                connect_points(9, 41, points)
                connect_points(18, 43, points)
                
                
                # grey layer (seperates static and dynamic stuff)
                
                pygame.draw.polygon(window,(69,69,69),((points[22]),(points[25]),(points[28]),(points[31])))

                
                if direction == 'clockwise':
    
                    #cubies right of the turning face
                    
                    getcolor4gui(abstractcube,18)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[3]),(face_pts[7]),(face_pts[21]),(face_pts[19])))

                    getcolor4gui(abstractcube,21)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[21]),(face_pts[7]),(face_pts[11]),(face_pts[23])))

                    getcolor4gui(abstractcube,24)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[23]),(face_pts[11]),(face_pts[15]),(face_pts[27])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies top of the turning face
                    
                    getcolor4gui(abstractcube,6)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[17]),(face_pts[1]),(face_pts[0])))

                    getcolor4gui(abstractcube,7)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[17]),(face_pts[18]),(face_pts[2]),(face_pts[1])))

                    getcolor4gui(abstractcube,8)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[18]),(face_pts[19]),(face_pts[3]),(face_pts[2])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[17][0], face_pts[17][1]) , (face_pts[1][0], face_pts[1][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[18][0], face_pts[18][1]) , (face_pts[2][0], face_pts[2][1]))


                    #cubies under the turning face (they are "turning" therfore this is before the color changes)
                
                    getcolor4gui(abstractcube,45)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[24]),(face_pts[25]),(face_pts[13]),(face_pts[12])))

                    getcolor4gui(abstractcube,46)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[25]),(face_pts[26]),(face_pts[14]),(face_pts[13])))

                    getcolor4gui(abstractcube,47)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[26]),(face_pts[27]),(face_pts[15]),(face_pts[14])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies left of the turning face
                    
                    getcolor4gui(abstractcube,29)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[0]),(face_pts[4]),(face_pts[20])))

                    getcolor4gui(abstractcube,32)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[20]),(face_pts[4]),(face_pts[8]),(face_pts[22])))

                    getcolor4gui(abstractcube,35)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[22]),(face_pts[8]),(face_pts[12]),(face_pts[24])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[20][0], face_pts[20][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[22][0], face_pts[22][1]) , (face_pts[8][0], face_pts[8][1]))

                elif direction == 'anticlockwise':
                    
                    #cubies under the turning face (they are "turning" therfore this is before the color changes)
                
                    getcolor4gui(abstractcube,45)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[24]),(face_pts[25]),(face_pts[13]),(face_pts[12])))

                    getcolor4gui(abstractcube,46)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[25]),(face_pts[26]),(face_pts[14]),(face_pts[13])))

                    getcolor4gui(abstractcube,47)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[26]),(face_pts[27]),(face_pts[15]),(face_pts[14])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies right of the turning face
                    
                    getcolor4gui(abstractcube,18)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[3]),(face_pts[7]),(face_pts[21]),(face_pts[19])))

                    getcolor4gui(abstractcube,21)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[21]),(face_pts[7]),(face_pts[11]),(face_pts[23])))

                    getcolor4gui(abstractcube,24)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[23]),(face_pts[11]),(face_pts[15]),(face_pts[27])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies left of the turning face
                    
                    getcolor4gui(abstractcube,29)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[0]),(face_pts[4]),(face_pts[20])))

                    getcolor4gui(abstractcube,32)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[20]),(face_pts[4]),(face_pts[8]),(face_pts[22])))

                    getcolor4gui(abstractcube,35)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[22]),(face_pts[8]),(face_pts[12]),(face_pts[24])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[20][0], face_pts[20][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[22][0], face_pts[22][1]) , (face_pts[8][0], face_pts[8][1]))

                    #cubies top of the turning face
                    
                    getcolor4gui(abstractcube,6)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[17]),(face_pts[1]),(face_pts[0])))

                    getcolor4gui(abstractcube,7)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[17]),(face_pts[18]),(face_pts[2]),(face_pts[1])))

                    getcolor4gui(abstractcube,8)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[18]),(face_pts[19]),(face_pts[3]),(face_pts[2])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[17][0], face_pts[17][1]) , (face_pts[1][0], face_pts[1][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[18][0], face_pts[18][1]) , (face_pts[2][0], face_pts[2][1]))



                # cubies of the turning face

                getcolor4gui(abstractcube,9)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[0]),(face_pts[1]),(face_pts[5]),(face_pts[4])))

                getcolor4gui(abstractcube,10)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[1]),(face_pts[2]),(face_pts[6]),(face_pts[5])))

                getcolor4gui(abstractcube,11)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[2]),(face_pts[3]),(face_pts[7]),(face_pts[6])))

                getcolor4gui(abstractcube,12)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[4]),(face_pts[5]),(face_pts[9]),(face_pts[8])))

                getcolor4gui(abstractcube,13)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[5]),(face_pts[6]),(face_pts[10]),(face_pts[9])))

                getcolor4gui(abstractcube,14)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[6]),(face_pts[7]),(face_pts[11]),(face_pts[10])))

                getcolor4gui(abstractcube,15)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[8]),(face_pts[9]),(face_pts[13]),(face_pts[12])))

                getcolor4gui(abstractcube,16)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[9]),(face_pts[10]),(face_pts[14]),(face_pts[13])))

                getcolor4gui(abstractcube,17)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[10]),(face_pts[11]),(face_pts[15]),(face_pts[14])))


                pygame.draw.line(window, (0, 0, 0), (face_pts[1][0], face_pts[1][1]) , (face_pts[13][0], face_pts[13][1])) 
                pygame.draw.line(window, (0, 0, 0), (face_pts[2][0], face_pts[2][1]) , (face_pts[14][0], face_pts[14][1]))
                pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[7][0], face_pts[7][1]))
                pygame.draw.line(window, (0, 0, 0), (face_pts[8][0], face_pts[8][1]) , (face_pts[11][0], face_pts[11][1]))
                
                
            elif colorkey == 'WOB':

                #static orange cubies
                
                getcolor4gui(abstractcube,19)
                pygame.draw.polygon(window,cubie_color4gui,((points[25]),(points[13]),(points[44]),(points[45])))

                getcolor4gui(abstractcube,20)
                pygame.draw.polygon(window,cubie_color4gui,((points[13]),(points[1]),(points[12]),(points[44])))

                getcolor4gui(abstractcube,22)
                pygame.draw.polygon(window,cubie_color4gui,((points[45]),(points[44]),(points[46]),(points[47])))

                getcolor4gui(abstractcube,23)
                pygame.draw.polygon(window,cubie_color4gui,((points[44]),(points[12]),(points[15]),(points[46])))

                getcolor4gui(abstractcube,25)
                pygame.draw.polygon(window,cubie_color4gui,((points[47]),(points[46]),(points[16]),(points[28])))

                getcolor4gui(abstractcube,26)
                pygame.draw.polygon(window,cubie_color4gui,((points[46]),(points[15]),(points[2]),(points[16])))



                #static white cubies

                getcolor4gui(abstractcube,0)
                pygame.draw.polygon(window,cubie_color4gui,((points[0]),(points[8]),(points[32]),(points[10])))

                getcolor4gui(abstractcube,1)
                pygame.draw.polygon(window,cubie_color4gui,((points[8]),(points[11]),(points[33]),(points[32])))
                
                getcolor4gui(abstractcube,2)
                pygame.draw.polygon(window,cubie_color4gui,((points[11]),(points[1]),(points[13]),(points[33])))

                getcolor4gui(abstractcube,3)
                pygame.draw.polygon(window,cubie_color4gui,((points[10]),(points[32]),(points[34]),(points[22])))

                getcolor4gui(abstractcube,4)
                pygame.draw.polygon(window,cubie_color4gui,((points[32]),(points[33]),(points[35]),(points[34])))

                getcolor4gui(abstractcube,5)
                pygame.draw.polygon(window,cubie_color4gui,((points[33]),(points[13]),(points[25]),(points[35])))
                

                # static perimeter and lines
                
                connect_points(0, 22, points)
                connect_points(22, 25, points)
                connect_points(25, 1, points)
                connect_points(1, 0, points)

                connect_points(1, 2, points)
                connect_points(5, 6, points)
                connect_points(4, 7, points)

                connect_points(13, 10, points)
                connect_points(22, 25, points)
                connect_points(8, 34, points)
                connect_points(11, 35, points)

                connect_points(13, 16, points)
                connect_points(25, 28, points)
                connect_points(12, 45, points)
                connect_points(15, 47, points)


                
                
                # grey layer (seperates static and dynamic stuff)
                
                pygame.draw.polygon(window,(69,69,69),((points[22]),(points[25]),(points[28]),(points[31])))


                if direction == 'clockwise':

                    #cubies under the turning face (they are "turning" therfore this is before the color changes)
                
                    getcolor4gui(abstractcube,45)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[24]),(face_pts[25]),(face_pts[13]),(face_pts[12])))

                    getcolor4gui(abstractcube,46)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[25]),(face_pts[26]),(face_pts[14]),(face_pts[13])))

                    getcolor4gui(abstractcube,47)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[26]),(face_pts[27]),(face_pts[15]),(face_pts[14])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies left of the turning face
                    
                    getcolor4gui(abstractcube,29)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[0]),(face_pts[4]),(face_pts[20])))

                    getcolor4gui(abstractcube,32)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[20]),(face_pts[4]),(face_pts[8]),(face_pts[22])))

                    getcolor4gui(abstractcube,35)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[22]),(face_pts[8]),(face_pts[12]),(face_pts[24])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[20][0], face_pts[20][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[22][0], face_pts[22][1]) , (face_pts[8][0], face_pts[8][1]))

                    #cubies right of the turning face
                    
                    getcolor4gui(abstractcube,18)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[3]),(face_pts[7]),(face_pts[21]),(face_pts[19])))

                    getcolor4gui(abstractcube,21)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[21]),(face_pts[7]),(face_pts[11]),(face_pts[23])))

                    getcolor4gui(abstractcube,24)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[23]),(face_pts[11]),(face_pts[15]),(face_pts[27])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies top of the turning face
                    
                    getcolor4gui(abstractcube,6)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[17]),(face_pts[1]),(face_pts[0])))

                    getcolor4gui(abstractcube,7)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[17]),(face_pts[18]),(face_pts[2]),(face_pts[1])))

                    getcolor4gui(abstractcube,8)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[18]),(face_pts[19]),(face_pts[3]),(face_pts[2])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[17][0], face_pts[17][1]) , (face_pts[1][0], face_pts[1][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[18][0], face_pts[18][1]) , (face_pts[2][0], face_pts[2][1]))

                    

                
                elif direction == 'anticlockwise':

                    #cubies left of the turning face
                    
                    getcolor4gui(abstractcube,29)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[0]),(face_pts[4]),(face_pts[20])))

                    getcolor4gui(abstractcube,32)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[20]),(face_pts[4]),(face_pts[8]),(face_pts[22])))

                    getcolor4gui(abstractcube,35)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[22]),(face_pts[8]),(face_pts[12]),(face_pts[24])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[20][0], face_pts[20][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[22][0], face_pts[22][1]) , (face_pts[8][0], face_pts[8][1]))

                    #cubies under the turning face (they are "turning" therfore this is before the color changes)
                
                    getcolor4gui(abstractcube,45)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[24]),(face_pts[25]),(face_pts[13]),(face_pts[12])))

                    getcolor4gui(abstractcube,46)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[25]),(face_pts[26]),(face_pts[14]),(face_pts[13])))

                    getcolor4gui(abstractcube,47)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[26]),(face_pts[27]),(face_pts[15]),(face_pts[14])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies top of the turning face
                    
                    getcolor4gui(abstractcube,6)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[17]),(face_pts[1]),(face_pts[0])))

                    getcolor4gui(abstractcube,7)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[17]),(face_pts[18]),(face_pts[2]),(face_pts[1])))

                    getcolor4gui(abstractcube,8)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[18]),(face_pts[19]),(face_pts[3]),(face_pts[2])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[17][0], face_pts[17][1]) , (face_pts[1][0], face_pts[1][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[18][0], face_pts[18][1]) , (face_pts[2][0], face_pts[2][1]))
    
                    #cubies right of the turning face
                    
                    getcolor4gui(abstractcube,18)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[3]),(face_pts[7]),(face_pts[21]),(face_pts[19])))

                    getcolor4gui(abstractcube,21)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[21]),(face_pts[7]),(face_pts[11]),(face_pts[23])))

                    getcolor4gui(abstractcube,24)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[23]),(face_pts[11]),(face_pts[15]),(face_pts[27])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[23][0], face_pts[23][1]) , (face_pts[11][0], face_pts[11][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[21][0], face_pts[21][1]) , (face_pts[7][0], face_pts[7][1]))

                # cubies of the turning face

                getcolor4gui(abstractcube,9)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[0]),(face_pts[1]),(face_pts[5]),(face_pts[4])))

                getcolor4gui(abstractcube,10)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[1]),(face_pts[2]),(face_pts[6]),(face_pts[5])))

                getcolor4gui(abstractcube,11)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[2]),(face_pts[3]),(face_pts[7]),(face_pts[6])))

                getcolor4gui(abstractcube,12)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[4]),(face_pts[5]),(face_pts[9]),(face_pts[8])))

                getcolor4gui(abstractcube,13)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[5]),(face_pts[6]),(face_pts[10]),(face_pts[9])))

                getcolor4gui(abstractcube,14)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[6]),(face_pts[7]),(face_pts[11]),(face_pts[10])))

                getcolor4gui(abstractcube,15)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[8]),(face_pts[9]),(face_pts[13]),(face_pts[12])))

                getcolor4gui(abstractcube,16)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[9]),(face_pts[10]),(face_pts[14]),(face_pts[13])))

                getcolor4gui(abstractcube,17)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[10]),(face_pts[11]),(face_pts[15]),(face_pts[14])))


                pygame.draw.line(window, (0, 0, 0), (face_pts[1][0], face_pts[1][1]) , (face_pts[13][0], face_pts[13][1])) 
                pygame.draw.line(window, (0, 0, 0), (face_pts[2][0], face_pts[2][1]) , (face_pts[14][0], face_pts[14][1]))
                pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[7][0], face_pts[7][1]))
                pygame.draw.line(window, (0, 0, 0), (face_pts[8][0], face_pts[8][1]) , (face_pts[11][0], face_pts[11][1]))

            elif colorkey == 'WOG':

                if direction == 'clockwise':

                    #cubies under the turning face (they are "turning" therfore this is before the color changes)
                
                    getcolor4gui(abstractcube,45)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[24]),(face_pts[25]),(face_pts[13]),(face_pts[12])))

                    getcolor4gui(abstractcube,46)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[25]),(face_pts[26]),(face_pts[14]),(face_pts[13])))

                    getcolor4gui(abstractcube,47)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[26]),(face_pts[27]),(face_pts[15]),(face_pts[14])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies left of the turning face
                    
                    getcolor4gui(abstractcube,29)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[0]),(face_pts[4]),(face_pts[20])))

                    getcolor4gui(abstractcube,32)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[20]),(face_pts[4]),(face_pts[8]),(face_pts[22])))

                    getcolor4gui(abstractcube,35)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[22]),(face_pts[8]),(face_pts[12]),(face_pts[24])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[20][0], face_pts[20][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[22][0], face_pts[22][1]) , (face_pts[8][0], face_pts[8][1]))

                    #cubies right of the turning face
                    
                    getcolor4gui(abstractcube,18)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[3]),(face_pts[7]),(face_pts[21]),(face_pts[19])))

                    getcolor4gui(abstractcube,21)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[21]),(face_pts[7]),(face_pts[11]),(face_pts[23])))

                    getcolor4gui(abstractcube,24)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[23]),(face_pts[11]),(face_pts[15]),(face_pts[27])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies top of the turning face
                    
                    getcolor4gui(abstractcube,6)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[17]),(face_pts[1]),(face_pts[0])))

                    getcolor4gui(abstractcube,7)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[17]),(face_pts[18]),(face_pts[2]),(face_pts[1])))

                    getcolor4gui(abstractcube,8)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[18]),(face_pts[19]),(face_pts[3]),(face_pts[2])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[17][0], face_pts[17][1]) , (face_pts[1][0], face_pts[1][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[18][0], face_pts[18][1]) , (face_pts[2][0], face_pts[2][1]))
                
                elif direction == 'anticlockwise':

                    #cubies left of the turning face
                    
                    getcolor4gui(abstractcube,29)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[0]),(face_pts[4]),(face_pts[20])))

                    getcolor4gui(abstractcube,32)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[20]),(face_pts[4]),(face_pts[8]),(face_pts[22])))

                    getcolor4gui(abstractcube,35)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[22]),(face_pts[8]),(face_pts[12]),(face_pts[24])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[20][0], face_pts[20][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[22][0], face_pts[22][1]) , (face_pts[8][0], face_pts[8][1]))

                    #cubies under the turning face (they are "turning" therfore this is before the color changes)
                
                    getcolor4gui(abstractcube,45)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[24]),(face_pts[25]),(face_pts[13]),(face_pts[12])))

                    getcolor4gui(abstractcube,46)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[25]),(face_pts[26]),(face_pts[14]),(face_pts[13])))

                    getcolor4gui(abstractcube,47)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[26]),(face_pts[27]),(face_pts[15]),(face_pts[14])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies top of the turning face
                    
                    getcolor4gui(abstractcube,6)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[17]),(face_pts[1]),(face_pts[0])))

                    getcolor4gui(abstractcube,7)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[17]),(face_pts[18]),(face_pts[2]),(face_pts[1])))

                    getcolor4gui(abstractcube,8)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[18]),(face_pts[19]),(face_pts[3]),(face_pts[2])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[17][0], face_pts[17][1]) , (face_pts[1][0], face_pts[1][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[18][0], face_pts[18][1]) , (face_pts[2][0], face_pts[2][1]))
    
                    #cubies right of the turning face
                    
                    getcolor4gui(abstractcube,18)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[3]),(face_pts[7]),(face_pts[21]),(face_pts[19])))

                    getcolor4gui(abstractcube,21)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[21]),(face_pts[7]),(face_pts[11]),(face_pts[23])))

                    getcolor4gui(abstractcube,24)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[23]),(face_pts[11]),(face_pts[15]),(face_pts[27])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[23][0], face_pts[23][1]) , (face_pts[11][0], face_pts[11][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[21][0], face_pts[21][1]) , (face_pts[7][0], face_pts[7][1]))

                pygame.draw.polygon(window,(69,69,69),((face_pts[16]),(face_pts[19]),(face_pts[27]),(face_pts[24])))
                
                #static white cubies

                getcolor4gui(abstractcube,0)
                pygame.draw.polygon(window,cubie_color4gui,((points[0]),(points[8]),(points[32]),(points[10])))

                getcolor4gui(abstractcube,1)
                pygame.draw.polygon(window,cubie_color4gui,((points[8]),(points[11]),(points[33]),(points[32])))
                    
                getcolor4gui(abstractcube,2)
                pygame.draw.polygon(window,cubie_color4gui,((points[11]),(points[1]),(points[13]),(points[33])))

                getcolor4gui(abstractcube,3)
                pygame.draw.polygon(window,cubie_color4gui,((points[10]),(points[32]),(points[34]),(points[22])))

                getcolor4gui(abstractcube,4)
                pygame.draw.polygon(window,cubie_color4gui,((points[32]),(points[33]),(points[35]),(points[34])))

                getcolor4gui(abstractcube,5)
                pygame.draw.polygon(window,cubie_color4gui,((points[33]),(points[13]),(points[25]),(points[35])))

                #static orange cubies
                
                getcolor4gui(abstractcube,19)
                pygame.draw.polygon(window,cubie_color4gui,((points[25]),(points[13]),(points[44]),(points[45])))

                getcolor4gui(abstractcube,20)
                pygame.draw.polygon(window,cubie_color4gui,((points[13]),(points[1]),(points[12]),(points[44])))

                getcolor4gui(abstractcube,22)
                pygame.draw.polygon(window,cubie_color4gui,((points[45]),(points[44]),(points[46]),(points[47])))

                getcolor4gui(abstractcube,23)
                pygame.draw.polygon(window,cubie_color4gui,((points[44]),(points[12]),(points[15]),(points[46])))

                getcolor4gui(abstractcube,25)
                pygame.draw.polygon(window,cubie_color4gui,((points[47]),(points[46]),(points[16]),(points[28])))

                getcolor4gui(abstractcube,26)
                pygame.draw.polygon(window,cubie_color4gui,((points[46]),(points[15]),(points[2]),(points[16])))

                # static green

                getcolor4gui(abstractcube,36)
                pygame.draw.polygon(window,cubie_color4gui,((points[1]),(points[11]),(points[49]),(points[12])))

                getcolor4gui(abstractcube,37)
                pygame.draw.polygon(window,cubie_color4gui,((points[11]),(points[8]),(points[48]),(points[49])))

                getcolor4gui(abstractcube,38)
                pygame.draw.polygon(window,cubie_color4gui,((points[8]),(points[0]),(points[9]),(points[48])))

                getcolor4gui(abstractcube,39)
                pygame.draw.polygon(window,cubie_color4gui,((points[12]),(points[49]),(points[51]),(points[15])))

                getcolor4gui(abstractcube,40)
                pygame.draw.polygon(window,cubie_color4gui,((points[49]),(points[48]),(points[50]),(points[51])))

                getcolor4gui(abstractcube,41)
                pygame.draw.polygon(window,cubie_color4gui,((points[48]),(points[9]),(points[18]),(points[50])))

                getcolor4gui(abstractcube,42)
                pygame.draw.polygon(window,cubie_color4gui,((points[15]),(points[51]),(points[14]),(points[2])))

                getcolor4gui(abstractcube,43)
                pygame.draw.polygon(window,cubie_color4gui,((points[51]),(points[50]),(points[17]),(points[14])))

                getcolor4gui(abstractcube,44)
                pygame.draw.polygon(window,cubie_color4gui,((points[50]),(points[18]),(points[3]),(points[17])))

                #gray layer
                #pygame.draw.polygon(window,(69,69,69),((points[22]),(points[25]),(points[28]),(points[31])))

                # perimiter and lines
                
                connect_points(0, 22, points)
                connect_points(22, 25, points)
                connect_points(25, 1, points)
                connect_points(1, 0, points)

                connect_points(1, 2, points)
                connect_points(0, 3, points)

                connect_points(13, 10, points)
                connect_points(22, 25, points)
                connect_points(8, 34, points)
                connect_points(11, 35, points)

                connect_points(13, 16, points)
                connect_points(25, 28, points)
                connect_points(12, 45, points)
                connect_points(15, 47, points)

                connect_points(8, 17, points)
                connect_points(11, 14, points)
                connect_points(12, 9, points)
                connect_points(15, 18, points)

            elif colorkey == 'WGR':
                
                if direction == 'clockwise':
                    
                    #cubies right of the turning face
                    
                    getcolor4gui(abstractcube,18)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[3]),(face_pts[7]),(face_pts[21]),(face_pts[19])))

                    getcolor4gui(abstractcube,21)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[21]),(face_pts[7]),(face_pts[11]),(face_pts[23])))

                    getcolor4gui(abstractcube,24)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[23]),(face_pts[11]),(face_pts[15]),(face_pts[27])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies top of the turning face
                    
                    getcolor4gui(abstractcube,6)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[17]),(face_pts[1]),(face_pts[0])))

                    getcolor4gui(abstractcube,7)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[17]),(face_pts[18]),(face_pts[2]),(face_pts[1])))

                    getcolor4gui(abstractcube,8)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[18]),(face_pts[19]),(face_pts[3]),(face_pts[2])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[17][0], face_pts[17][1]) , (face_pts[1][0], face_pts[1][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[18][0], face_pts[18][1]) , (face_pts[2][0], face_pts[2][1]))


                    #cubies under the turning face (they are "turning" therfore this is before the color changes)
                
                    getcolor4gui(abstractcube,45)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[24]),(face_pts[25]),(face_pts[13]),(face_pts[12])))

                    getcolor4gui(abstractcube,46)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[25]),(face_pts[26]),(face_pts[14]),(face_pts[13])))

                    getcolor4gui(abstractcube,47)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[26]),(face_pts[27]),(face_pts[15]),(face_pts[14])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies left of the turning face
                    
                    getcolor4gui(abstractcube,29)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[0]),(face_pts[4]),(face_pts[20])))

                    getcolor4gui(abstractcube,32)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[20]),(face_pts[4]),(face_pts[8]),(face_pts[22])))

                    getcolor4gui(abstractcube,35)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[22]),(face_pts[8]),(face_pts[12]),(face_pts[24])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[20][0], face_pts[20][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[22][0], face_pts[22][1]) , (face_pts[8][0], face_pts[8][1]))

                
                elif direction == 'anticlockwise':

                    #cubies under the turning face (they are "turning" therfore this is before the color changes)
                
                    getcolor4gui(abstractcube,45)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[24]),(face_pts[25]),(face_pts[13]),(face_pts[12])))

                    getcolor4gui(abstractcube,46)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[25]),(face_pts[26]),(face_pts[14]),(face_pts[13])))

                    getcolor4gui(abstractcube,47)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[26]),(face_pts[27]),(face_pts[15]),(face_pts[14])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies left of the turning face
                    
                    getcolor4gui(abstractcube,29)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[0]),(face_pts[4]),(face_pts[20])))

                    getcolor4gui(abstractcube,32)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[20]),(face_pts[4]),(face_pts[8]),(face_pts[22])))

                    getcolor4gui(abstractcube,35)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[22]),(face_pts[8]),(face_pts[12]),(face_pts[24])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[20][0], face_pts[20][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[22][0], face_pts[22][1]) , (face_pts[8][0], face_pts[8][1]))

                    #cubies right of the turning face
                    
                    getcolor4gui(abstractcube,18)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[3]),(face_pts[7]),(face_pts[21]),(face_pts[19])))

                    getcolor4gui(abstractcube,21)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[21]),(face_pts[7]),(face_pts[11]),(face_pts[23])))

                    getcolor4gui(abstractcube,24)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[23]),(face_pts[11]),(face_pts[15]),(face_pts[27])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[23][0], face_pts[23][1]) , (face_pts[11][0], face_pts[11][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[21][0], face_pts[21][1]) , (face_pts[7][0], face_pts[7][1]))


                    #cubies top of the turning face
                    
                    getcolor4gui(abstractcube,6)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[17]),(face_pts[1]),(face_pts[0])))

                    getcolor4gui(abstractcube,7)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[17]),(face_pts[18]),(face_pts[2]),(face_pts[1])))

                    getcolor4gui(abstractcube,8)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[18]),(face_pts[19]),(face_pts[3]),(face_pts[2])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[17][0], face_pts[17][1]) , (face_pts[1][0], face_pts[1][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[18][0], face_pts[18][1]) , (face_pts[2][0], face_pts[2][1]))
    


                pygame.draw.polygon(window,(69,69,69),((face_pts[16]),(face_pts[19]),(face_pts[27]),(face_pts[24])))
                
                #static white cubies

                getcolor4gui(abstractcube,0)
                pygame.draw.polygon(window,cubie_color4gui,((points[0]),(points[8]),(points[32]),(points[10])))

                getcolor4gui(abstractcube,1)
                pygame.draw.polygon(window,cubie_color4gui,((points[8]),(points[11]),(points[33]),(points[32])))
                    
                getcolor4gui(abstractcube,2)
                pygame.draw.polygon(window,cubie_color4gui,((points[11]),(points[1]),(points[13]),(points[33])))

                getcolor4gui(abstractcube,3)
                pygame.draw.polygon(window,cubie_color4gui,((points[10]),(points[32]),(points[34]),(points[22])))

                getcolor4gui(abstractcube,4)
                pygame.draw.polygon(window,cubie_color4gui,((points[32]),(points[33]),(points[35]),(points[34])))

                getcolor4gui(abstractcube,5)
                pygame.draw.polygon(window,cubie_color4gui,((points[33]),(points[13]),(points[25]),(points[35])))

                #static orange cubies
                
                getcolor4gui(abstractcube,27)
                pygame.draw.polygon(window,cubie_color4gui,((points[0]),(points[10]),(points[40]),(points[9])))

                getcolor4gui(abstractcube,28)
                pygame.draw.polygon(window,cubie_color4gui,((points[10]),(points[22]),(points[41]),(points[40])))

                getcolor4gui(abstractcube,30)
                pygame.draw.polygon(window,cubie_color4gui,((points[9]),(points[40]),(points[42]),(points[18])))

                getcolor4gui(abstractcube,31)
                pygame.draw.polygon(window,cubie_color4gui,((points[40]),(points[41]),(points[43]),(points[42])))

                getcolor4gui(abstractcube,33)
                pygame.draw.polygon(window,cubie_color4gui,((points[18]),(points[42]),(points[19]),(points[3])))

                getcolor4gui(abstractcube,34)
                pygame.draw.polygon(window,cubie_color4gui,((points[42]),(points[43]),(points[31]),(points[19])))

                # static green

                getcolor4gui(abstractcube,36)
                pygame.draw.polygon(window,cubie_color4gui,((points[1]),(points[11]),(points[49]),(points[12])))

                getcolor4gui(abstractcube,37)
                pygame.draw.polygon(window,cubie_color4gui,((points[11]),(points[8]),(points[48]),(points[49])))

                getcolor4gui(abstractcube,38)
                pygame.draw.polygon(window,cubie_color4gui,((points[8]),(points[0]),(points[9]),(points[48])))

                getcolor4gui(abstractcube,39)
                pygame.draw.polygon(window,cubie_color4gui,((points[12]),(points[49]),(points[51]),(points[15])))

                getcolor4gui(abstractcube,40)
                pygame.draw.polygon(window,cubie_color4gui,((points[49]),(points[48]),(points[50]),(points[51])))

                getcolor4gui(abstractcube,41)
                pygame.draw.polygon(window,cubie_color4gui,((points[48]),(points[9]),(points[18]),(points[50])))

                getcolor4gui(abstractcube,42)
                pygame.draw.polygon(window,cubie_color4gui,((points[15]),(points[51]),(points[14]),(points[2])))

                getcolor4gui(abstractcube,43)
                pygame.draw.polygon(window,cubie_color4gui,((points[51]),(points[50]),(points[17]),(points[14])))

                getcolor4gui(abstractcube,44)
                pygame.draw.polygon(window,cubie_color4gui,((points[50]),(points[18]),(points[3]),(points[17])))

                #gray layer
                #pygame.draw.polygon(window,(69,69,69),((points[22]),(points[25]),(points[28]),(points[31])))

                # perimiter and lines
                
                connect_points(0, 22, points)
                connect_points(22, 25, points)
                connect_points(25, 1, points)
                connect_points(1, 0, points)

                connect_points(1, 2, points)
                connect_points(0, 3, points)

                connect_points(13, 10, points)
                connect_points(22, 25, points)
                connect_points(8, 34, points)
                connect_points(11, 35, points)

                connect_points(10, 19, points)
                connect_points(22, 31, points)
                connect_points(9, 41, points)
                connect_points(18, 43, points)

                connect_points(8, 17, points)
                connect_points(11, 14, points)
                connect_points(12, 9, points)
                connect_points(15, 18, points)

            elif colorkey == 'YBR':

                #static red cubies
                
                getcolor4gui(abstractcube,27)
                pygame.draw.polygon(window,cubie_color4gui,((points[0]),(points[10]),(points[40]),(points[9])))

                getcolor4gui(abstractcube,28)
                pygame.draw.polygon(window,cubie_color4gui,((points[10]),(points[22]),(points[41]),(points[40])))

                getcolor4gui(abstractcube,30)
                pygame.draw.polygon(window,cubie_color4gui,((points[9]),(points[40]),(points[42]),(points[18])))

                getcolor4gui(abstractcube,31)
                pygame.draw.polygon(window,cubie_color4gui,((points[40]),(points[41]),(points[43]),(points[42])))

                getcolor4gui(abstractcube,34)
                pygame.draw.polygon(window,cubie_color4gui,((points[42]),(points[43]),(points[31]),(points[19])))

                getcolor4gui(abstractcube,33)
                pygame.draw.polygon(window,cubie_color4gui,((points[18]),(points[42]),(points[19]),(points[3])))

                #static yellow cubies
                
                getcolor4gui(abstractcube,48)
                pygame.draw.polygon(window,cubie_color4gui,((points[31]),(points[54]),(points[52]),(points[19])))

                getcolor4gui(abstractcube,49)
                pygame.draw.polygon(window,cubie_color4gui,((points[54]),(points[55]),(points[53]),(points[52])))

                getcolor4gui(abstractcube,50)
                pygame.draw.polygon(window,cubie_color4gui,((points[55]),(points[28]),(points[16]),(points[53])))

                getcolor4gui(abstractcube,51)
                pygame.draw.polygon(window,cubie_color4gui,((points[19]),(points[52]),(points[17]),(points[3])))

                getcolor4gui(abstractcube,52)
                pygame.draw.polygon(window,cubie_color4gui,((points[52]),(points[53]),(points[14]),(points[17])))

                getcolor4gui(abstractcube,53)
                pygame.draw.polygon(window,cubie_color4gui,((points[53]),(points[16]),(points[2]),(points[14])))

                connect_points(0, 3, points)
                connect_points(0, 22, points)
                connect_points(22, 31, points)
                connect_points(31, 3, points)

                connect_points(2, 3, points)
                connect_points(2, 28, points)
                connect_points(28, 31, points)
                connect_points(10, 19, points)
                connect_points(18, 30, points)

                connect_points(9, 41, points)
                connect_points(18, 43, points)

                connect_points(16, 19, points)
                connect_points(31, 28, points)

                connect_points(17, 54, points)
                connect_points(14, 55, points)


                # grey layer (seperates static and dynamic stuff)
                
                pygame.draw.polygon(window,(69,69,69),((points[22]),(points[25]),(points[28]),(points[31])))

                if direction == 'clockwise':

                    #cubies top of the turning face
                    
                    getcolor4gui(abstractcube,6)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[17]),(face_pts[1]),(face_pts[0])))

                    getcolor4gui(abstractcube,7)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[17]),(face_pts[18]),(face_pts[2]),(face_pts[1])))

                    getcolor4gui(abstractcube,8)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[18]),(face_pts[19]),(face_pts[3]),(face_pts[2])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[17][0], face_pts[17][1]) , (face_pts[1][0], face_pts[1][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[18][0], face_pts[18][1]) , (face_pts[2][0], face_pts[2][1]))

                    #cubies left of the turning face
                    
                    getcolor4gui(abstractcube,29)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[0]),(face_pts[4]),(face_pts[20])))

                    getcolor4gui(abstractcube,32)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[20]),(face_pts[4]),(face_pts[8]),(face_pts[22])))

                    getcolor4gui(abstractcube,35)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[22]),(face_pts[8]),(face_pts[12]),(face_pts[24])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[20][0], face_pts[20][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[22][0], face_pts[22][1]) , (face_pts[8][0], face_pts[8][1]))

                    #cubies right of the turning face
                    
                    getcolor4gui(abstractcube,18)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[3]),(face_pts[7]),(face_pts[21]),(face_pts[19])))

                    getcolor4gui(abstractcube,21)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[21]),(face_pts[7]),(face_pts[11]),(face_pts[23])))

                    getcolor4gui(abstractcube,24)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[23]),(face_pts[11]),(face_pts[15]),(face_pts[27])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))
                    
                    #cubies under the turning face (they are "turning" therfore this is before the color changes)
                
                    getcolor4gui(abstractcube,45)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[24]),(face_pts[25]),(face_pts[13]),(face_pts[12])))

                    getcolor4gui(abstractcube,46)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[25]),(face_pts[26]),(face_pts[14]),(face_pts[13])))

                    getcolor4gui(abstractcube,47)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[26]),(face_pts[27]),(face_pts[15]),(face_pts[14])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[21][0], face_pts[21][1]) , (face_pts[7][0], face_pts[7][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[23][0], face_pts[23][1]) , (face_pts[11][0], face_pts[11][1]))


                
                elif direction == 'anticlockwise':
    
                    #cubies right of the turning face
                    
                    getcolor4gui(abstractcube,18)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[3]),(face_pts[7]),(face_pts[21]),(face_pts[19])))

                    getcolor4gui(abstractcube,21)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[21]),(face_pts[7]),(face_pts[11]),(face_pts[23])))

                    getcolor4gui(abstractcube,24)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[23]),(face_pts[11]),(face_pts[15]),(face_pts[27])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies under the turning face (they are "turning" therfore this is before the color changes)
                
                    getcolor4gui(abstractcube,45)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[24]),(face_pts[25]),(face_pts[13]),(face_pts[12])))

                    getcolor4gui(abstractcube,46)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[25]),(face_pts[26]),(face_pts[14]),(face_pts[13])))

                    getcolor4gui(abstractcube,47)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[26]),(face_pts[27]),(face_pts[15]),(face_pts[14])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #cubies top of the turning face
                    
                    getcolor4gui(abstractcube,6)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[17]),(face_pts[1]),(face_pts[0])))

                    getcolor4gui(abstractcube,7)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[17]),(face_pts[18]),(face_pts[2]),(face_pts[1])))

                    getcolor4gui(abstractcube,8)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[18]),(face_pts[19]),(face_pts[3]),(face_pts[2])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[17][0], face_pts[17][1]) , (face_pts[1][0], face_pts[1][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[18][0], face_pts[18][1]) , (face_pts[2][0], face_pts[2][1]))


                    

                    #cubies left of the turning face
                    
                    getcolor4gui(abstractcube,29)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[0]),(face_pts[4]),(face_pts[20])))

                    getcolor4gui(abstractcube,32)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[20]),(face_pts[4]),(face_pts[8]),(face_pts[22])))

                    getcolor4gui(abstractcube,35)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[22]),(face_pts[8]),(face_pts[12]),(face_pts[24])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[20][0], face_pts[20][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[22][0], face_pts[22][1]) , (face_pts[8][0], face_pts[8][1]))


                # cubies of the turning face

                getcolor4gui(abstractcube,9)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[0]),(face_pts[1]),(face_pts[5]),(face_pts[4])))

                getcolor4gui(abstractcube,10)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[1]),(face_pts[2]),(face_pts[6]),(face_pts[5])))

                getcolor4gui(abstractcube,11)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[2]),(face_pts[3]),(face_pts[7]),(face_pts[6])))

                getcolor4gui(abstractcube,12)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[4]),(face_pts[5]),(face_pts[9]),(face_pts[8])))

                getcolor4gui(abstractcube,13)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[5]),(face_pts[6]),(face_pts[10]),(face_pts[9])))

                getcolor4gui(abstractcube,14)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[6]),(face_pts[7]),(face_pts[11]),(face_pts[10])))

                getcolor4gui(abstractcube,15)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[8]),(face_pts[9]),(face_pts[13]),(face_pts[12])))

                getcolor4gui(abstractcube,16)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[9]),(face_pts[10]),(face_pts[14]),(face_pts[13])))

                getcolor4gui(abstractcube,17)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[10]),(face_pts[11]),(face_pts[15]),(face_pts[14])))


                pygame.draw.line(window, (0, 0, 0), (face_pts[1][0], face_pts[1][1]) , (face_pts[13][0], face_pts[13][1])) 
                pygame.draw.line(window, (0, 0, 0), (face_pts[2][0], face_pts[2][1]) , (face_pts[14][0], face_pts[14][1]))
                pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[7][0], face_pts[7][1]))
                pygame.draw.line(window, (0, 0, 0), (face_pts[8][0], face_pts[8][1]) , (face_pts[11][0], face_pts[11][1]))

            elif colorkey == 'YOB':

                #static orange cubies
                
                getcolor4gui(abstractcube,19)
                pygame.draw.polygon(window,cubie_color4gui,((points[25]),(points[13]),(points[44]),(points[45])))

                getcolor4gui(abstractcube,20)
                pygame.draw.polygon(window,cubie_color4gui,((points[13]),(points[1]),(points[12]),(points[44])))

                getcolor4gui(abstractcube,22)
                pygame.draw.polygon(window,cubie_color4gui,((points[45]),(points[44]),(points[46]),(points[47])))

                getcolor4gui(abstractcube,23)
                pygame.draw.polygon(window,cubie_color4gui,((points[44]),(points[12]),(points[15]),(points[46])))

                getcolor4gui(abstractcube,25)
                pygame.draw.polygon(window,cubie_color4gui,((points[47]),(points[28]),(points[16]),(points[46])))

                getcolor4gui(abstractcube,26)
                pygame.draw.polygon(window,cubie_color4gui,((points[46]),(points[15]),(points[2]),(points[16])))

                #static yellow cubies
                
                getcolor4gui(abstractcube,48)
                pygame.draw.polygon(window,cubie_color4gui,((points[31]),(points[54]),(points[52]),(points[19])))

                getcolor4gui(abstractcube,49)
                pygame.draw.polygon(window,cubie_color4gui,((points[54]),(points[55]),(points[53]),(points[52])))

                getcolor4gui(abstractcube,50)
                pygame.draw.polygon(window,cubie_color4gui,((points[55]),(points[28]),(points[16]),(points[53])))

                getcolor4gui(abstractcube,51)
                pygame.draw.polygon(window,cubie_color4gui,((points[19]),(points[52]),(points[17]),(points[3])))

                getcolor4gui(abstractcube,52)
                pygame.draw.polygon(window,cubie_color4gui,((points[52]),(points[53]),(points[14]),(points[17])))

                getcolor4gui(abstractcube,53)
                pygame.draw.polygon(window,cubie_color4gui,((points[53]),(points[16]),(points[2]),(points[14])))

                #perimeter and lines
                connect_points(2, 28, points)
                connect_points(28, 31, points)
                connect_points(31, 3, points)
                connect_points(3, 2, points)

                connect_points(1, 2, points)
                connect_points(28, 25, points)
                connect_points(25, 1, points)
                
                connect_points(13, 16, points)
                connect_points(25, 28, points)
                connect_points(12, 45, points)
                connect_points(15, 47, points)

                connect_points(16, 19, points)
                connect_points(31, 28, points)
                connect_points(17, 54, points)
                connect_points(14, 55, points)

                pygame.draw.polygon(window,(69,69,69),((points[22]),(points[25]),(points[28]),(points[31])))

                if direction == 'clockwise':

                    #cubies left of the turning face
                    
                    getcolor4gui(abstractcube,29)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[0]),(face_pts[4]),(face_pts[20])))

                    getcolor4gui(abstractcube,32)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[20]),(face_pts[4]),(face_pts[8]),(face_pts[22])))

                    getcolor4gui(abstractcube,35)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[22]),(face_pts[8]),(face_pts[12]),(face_pts[24])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[20][0], face_pts[20][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[22][0], face_pts[22][1]) , (face_pts[8][0], face_pts[8][1]))

                    #cubies under the turning face (they are "turning" therfore this is before the color changes)
                
                    getcolor4gui(abstractcube,45)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[24]),(face_pts[25]),(face_pts[13]),(face_pts[12])))

                    getcolor4gui(abstractcube,46)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[25]),(face_pts[26]),(face_pts[14]),(face_pts[13])))

                    getcolor4gui(abstractcube,47)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[26]),(face_pts[27]),(face_pts[15]),(face_pts[14])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[21][0], face_pts[21][1]) , (face_pts[7][0], face_pts[7][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[23][0], face_pts[23][1]) , (face_pts[11][0], face_pts[11][1]))

                    
                    #cubies top of the turning face
                    
                    getcolor4gui(abstractcube,6)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[17]),(face_pts[1]),(face_pts[0])))

                    getcolor4gui(abstractcube,7)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[17]),(face_pts[18]),(face_pts[2]),(face_pts[1])))

                    getcolor4gui(abstractcube,8)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[18]),(face_pts[19]),(face_pts[3]),(face_pts[2])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[17][0], face_pts[17][1]) , (face_pts[1][0], face_pts[1][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[18][0], face_pts[18][1]) , (face_pts[2][0], face_pts[2][1]))

                    #cubies right of the turning face
                    
                    getcolor4gui(abstractcube,18)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[3]),(face_pts[7]),(face_pts[21]),(face_pts[19])))

                    getcolor4gui(abstractcube,21)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[21]),(face_pts[7]),(face_pts[11]),(face_pts[23])))

                    getcolor4gui(abstractcube,24)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[23]),(face_pts[11]),(face_pts[15]),(face_pts[27])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))


                
                elif direction == 'anticlockwise':
    
                    #cubies top of the turning face
                    
                    getcolor4gui(abstractcube,6)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[17]),(face_pts[1]),(face_pts[0])))

                    getcolor4gui(abstractcube,7)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[17]),(face_pts[18]),(face_pts[2]),(face_pts[1])))

                    getcolor4gui(abstractcube,8)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[18]),(face_pts[19]),(face_pts[3]),(face_pts[2])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[17][0], face_pts[17][1]) , (face_pts[1][0], face_pts[1][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[18][0], face_pts[18][1]) , (face_pts[2][0], face_pts[2][1]))

                    #cubies right of the turning face
                    
                    getcolor4gui(abstractcube,18)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[3]),(face_pts[7]),(face_pts[21]),(face_pts[19])))

                    getcolor4gui(abstractcube,21)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[21]),(face_pts[7]),(face_pts[11]),(face_pts[23])))

                    getcolor4gui(abstractcube,24)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[23]),(face_pts[11]),(face_pts[15]),(face_pts[27])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[21][0], face_pts[21][1]) , (face_pts[7][0], face_pts[7][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[23][0], face_pts[23][1]) , (face_pts[11][0], face_pts[11][1]))

                    #cubies left of the turning face
                    
                    getcolor4gui(abstractcube,29)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[0]),(face_pts[4]),(face_pts[20])))

                    getcolor4gui(abstractcube,32)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[20]),(face_pts[4]),(face_pts[8]),(face_pts[22])))

                    getcolor4gui(abstractcube,35)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[22]),(face_pts[8]),(face_pts[12]),(face_pts[24])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[20][0], face_pts[20][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[22][0], face_pts[22][1]) , (face_pts[8][0], face_pts[8][1]))

                    #cubies under the turning face (they are "turning" therfore this is before the color changes)
                
                    getcolor4gui(abstractcube,45)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[24]),(face_pts[25]),(face_pts[13]),(face_pts[12])))

                    getcolor4gui(abstractcube,46)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[25]),(face_pts[26]),(face_pts[14]),(face_pts[13])))

                    getcolor4gui(abstractcube,47)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[26]),(face_pts[27]),(face_pts[15]),(face_pts[14])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    
                # cubies of the turning face

                getcolor4gui(abstractcube,9)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[0]),(face_pts[1]),(face_pts[5]),(face_pts[4])))

                getcolor4gui(abstractcube,10)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[1]),(face_pts[2]),(face_pts[6]),(face_pts[5])))

                getcolor4gui(abstractcube,11)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[2]),(face_pts[3]),(face_pts[7]),(face_pts[6])))

                getcolor4gui(abstractcube,12)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[4]),(face_pts[5]),(face_pts[9]),(face_pts[8])))

                getcolor4gui(abstractcube,13)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[5]),(face_pts[6]),(face_pts[10]),(face_pts[9])))

                getcolor4gui(abstractcube,14)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[6]),(face_pts[7]),(face_pts[11]),(face_pts[10])))

                getcolor4gui(abstractcube,15)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[8]),(face_pts[9]),(face_pts[13]),(face_pts[12])))

                getcolor4gui(abstractcube,16)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[9]),(face_pts[10]),(face_pts[14]),(face_pts[13])))

                getcolor4gui(abstractcube,17)
                pygame.draw.polygon(window,cubie_color4gui,((face_pts[10]),(face_pts[11]),(face_pts[15]),(face_pts[14])))

                pygame.draw.line(window, (0, 0, 0), (face_pts[1][0], face_pts[1][1]) , (face_pts[13][0], face_pts[13][1])) 
                pygame.draw.line(window, (0, 0, 0), (face_pts[2][0], face_pts[2][1]) , (face_pts[14][0], face_pts[14][1]))
                pygame.draw.line(window, (0, 0, 0), (face_pts[4][0], face_pts[4][1]) , (face_pts[7][0], face_pts[7][1]))
                pygame.draw.line(window, (0, 0, 0), (face_pts[8][0], face_pts[8][1]) , (face_pts[11][0], face_pts[11][1]))

                pygame.draw.line(window, (0, 0, 0), (face_pts[23][0], face_pts[23][1]) , (face_pts[11][0], face_pts[11][1]))
                pygame.draw.line(window, (0, 0, 0), (face_pts[7][0], face_pts[7][1]) , (face_pts[21][0], face_pts[21][1]))

            elif colorkey == 'YOG':
                if direction == 'clockwise':

                    #left cubies
                    
                    getcolor4gui(abstractcube,29)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[0]),(face_pts[4]),(face_pts[20])))

                    getcolor4gui(abstractcube,32)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[20]),(face_pts[4]),(face_pts[8]),(face_pts[22])))

                    getcolor4gui(abstractcube,35)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[22]),(face_pts[8]),(face_pts[12]),(face_pts[24])))

                    #top cubies
                    getcolor4gui(abstractcube,6)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[17]),(face_pts[1]),(face_pts[0])))

                    getcolor4gui(abstractcube,7)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[17]),(face_pts[18]),(face_pts[2]),(face_pts[1])))

                    getcolor4gui(abstractcube,8)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[18]),(face_pts[19]),(face_pts[3]),(face_pts[2])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[17][0], face_pts[17][1]) , (face_pts[1][0], face_pts[1][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[18][0], face_pts[18][1]) , (face_pts[2][0], face_pts[2][1]))


                    #bottom cubies
                    getcolor4gui(abstractcube,45)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[15]),(face_pts[14]),(face_pts[26]),(face_pts[27])))

                    getcolor4gui(abstractcube,46)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[14]),(face_pts[13]),(face_pts[25]),(face_pts[26])))

                    getcolor4gui(abstractcube,47)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[13]),(face_pts[12]),(face_pts[24]),(face_pts[25])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    
                    #right cubies
                    getcolor4gui(abstractcube,18)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[3]),(face_pts[19]),(face_pts[21]),(face_pts[7])))

                    getcolor4gui(abstractcube,21)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[7]),(face_pts[21]),(face_pts[23]),(face_pts[11])))

                    getcolor4gui(abstractcube,24)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[11]),(face_pts[23]),(face_pts[27]),(face_pts[15])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[21][0], face_pts[21][1]) , (face_pts[7][0], face_pts[7][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[23][0], face_pts[23][1]) , (face_pts[11][0], face_pts[11][1]))
                
                elif direction == 'anticlockwise':

                    #top cubies
                    getcolor4gui(abstractcube,6)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[17]),(face_pts[1]),(face_pts[0])))

                    getcolor4gui(abstractcube,7)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[17]),(face_pts[18]),(face_pts[2]),(face_pts[1])))

                    getcolor4gui(abstractcube,8)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[18]),(face_pts[19]),(face_pts[3]),(face_pts[2])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[17][0], face_pts[17][1]) , (face_pts[1][0], face_pts[1][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[18][0], face_pts[18][1]) , (face_pts[2][0], face_pts[2][1]))

                    #bottom cubies
                    getcolor4gui(abstractcube,45)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[15]),(face_pts[14]),(face_pts[26]),(face_pts[27])))

                    getcolor4gui(abstractcube,46)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[14]),(face_pts[13]),(face_pts[25]),(face_pts[26])))

                    getcolor4gui(abstractcube,47)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[13]),(face_pts[12]),(face_pts[24]),(face_pts[25])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[25][0], face_pts[25][1]) , (face_pts[13][0], face_pts[13][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[26][0], face_pts[26][1]) , (face_pts[14][0], face_pts[14][1]))

                    #right cubies
                    getcolor4gui(abstractcube,18)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[3]),(face_pts[19]),(face_pts[21]),(face_pts[7])))

                    getcolor4gui(abstractcube,21)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[7]),(face_pts[21]),(face_pts[23]),(face_pts[11])))

                    getcolor4gui(abstractcube,24)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[11]),(face_pts[23]),(face_pts[27]),(face_pts[15])))

                    pygame.draw.line(window, (0, 0, 0), (face_pts[21][0], face_pts[21][1]) , (face_pts[7][0], face_pts[7][1]))
                    pygame.draw.line(window, (0, 0, 0), (face_pts[23][0], face_pts[23][1]) , (face_pts[11][0], face_pts[11][1]))

                    #left cubies
                    
                    getcolor4gui(abstractcube,29)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[16]),(face_pts[0]),(face_pts[4]),(face_pts[20])))

                    getcolor4gui(abstractcube,32)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[20]),(face_pts[4]),(face_pts[8]),(face_pts[22])))

                    getcolor4gui(abstractcube,35)
                    pygame.draw.polygon(window,cubie_color4gui,((face_pts[22]),(face_pts[8]),(face_pts[12]),(face_pts[24])))



                pygame.draw.polygon(window,(69,69,69),((face_pts[16]),(face_pts[19]),(face_pts[27]),(face_pts[24])))
            

                #static orange cubies
                
                getcolor4gui(abstractcube,19)
                pygame.draw.polygon(window,cubie_color4gui,((points[25]),(points[13]),(points[44]),(points[45])))

                getcolor4gui(abstractcube,20)
                pygame.draw.polygon(window,cubie_color4gui,((points[13]),(points[1]),(points[12]),(points[44])))

                getcolor4gui(abstractcube,22)
                pygame.draw.polygon(window,cubie_color4gui,((points[45]),(points[44]),(points[46]),(points[47])))

                getcolor4gui(abstractcube,23)
                pygame.draw.polygon(window,cubie_color4gui,((points[44]),(points[12]),(points[15]),(points[46])))

                getcolor4gui(abstractcube,25)
                pygame.draw.polygon(window,cubie_color4gui,((points[47]),(points[46]),(points[16]),(points[28])))

                getcolor4gui(abstractcube,26)
                pygame.draw.polygon(window,cubie_color4gui,((points[46]),(points[15]),(points[2]),(points[16])))

                # static green

                getcolor4gui(abstractcube,36)
                pygame.draw.polygon(window,cubie_color4gui,((points[1]),(points[11]),(points[49]),(points[12])))

                getcolor4gui(abstractcube,37)
                pygame.draw.polygon(window,cubie_color4gui,((points[11]),(points[8]),(points[48]),(points[49])))

                getcolor4gui(abstractcube,38)
                pygame.draw.polygon(window,cubie_color4gui,((points[8]),(points[0]),(points[9]),(points[48])))

                getcolor4gui(abstractcube,39)
                pygame.draw.polygon(window,cubie_color4gui,((points[12]),(points[49]),(points[51]),(points[15])))

                getcolor4gui(abstractcube,40)
                pygame.draw.polygon(window,cubie_color4gui,((points[49]),(points[48]),(points[50]),(points[51])))

                getcolor4gui(abstractcube,41)
                pygame.draw.polygon(window,cubie_color4gui,((points[48]),(points[9]),(points[18]),(points[50])))

                getcolor4gui(abstractcube,42)
                pygame.draw.polygon(window,cubie_color4gui,((points[15]),(points[51]),(points[14]),(points[2])))

                getcolor4gui(abstractcube,43)
                pygame.draw.polygon(window,cubie_color4gui,((points[51]),(points[50]),(points[17]),(points[14])))

                getcolor4gui(abstractcube,44)
                pygame.draw.polygon(window,cubie_color4gui,((points[50]),(points[18]),(points[3]),(points[17])))

                #static yellow cubies
                
                getcolor4gui(abstractcube,48)
                pygame.draw.polygon(window,cubie_color4gui,((points[31]),(points[54]),(points[52]),(points[19])))

                getcolor4gui(abstractcube,49)
                pygame.draw.polygon(window,cubie_color4gui,((points[54]),(points[55]),(points[53]),(points[52])))

                getcolor4gui(abstractcube,50)
                pygame.draw.polygon(window,cubie_color4gui,((points[55]),(points[28]),(points[16]),(points[53])))

                getcolor4gui(abstractcube,51)
                pygame.draw.polygon(window,cubie_color4gui,((points[19]),(points[52]),(points[17]),(points[3])))

                getcolor4gui(abstractcube,52)
                pygame.draw.polygon(window,cubie_color4gui,((points[52]),(points[53]),(points[14]),(points[17])))

                getcolor4gui(abstractcube,53)
                pygame.draw.polygon(window,cubie_color4gui,((points[53]),(points[16]),(points[2]),(points[14])))

                #perimeter and lines

                connect_points(1, 0, points)
                connect_points(0, 3, points)
                connect_points(3, 2, points)
                connect_points(2, 1, points)

                connect_points(1, 25, points)
                connect_points(25, 28, points)
                connect_points(28, 2, points)

                connect_points(3, 31, points)
                connect_points(31, 28, points)
                
                connect_points(8, 17, points)
                connect_points(11, 14, points)
                connect_points(12, 9, points)
                connect_points(15, 18, points)

                connect_points(12, 45, points)
                connect_points(15, 47, points)
                connect_points(13, 16, points)
                connect_points(25, 28, points)

                connect_points(16, 19, points)
                connect_points(31, 28, points)
                connect_points(17, 54, points)
                connect_points(14, 55, points)

        
        #elif drawing_key == 'draw r':
 
        #elif drawing_key == 'draw b':
            
        #elif drawing_key == 'draw l':
        
        #elif drawing_key == 'draw u':

        #elif drawing_key == 'draw d':
        
    
        pygame.display.update()
