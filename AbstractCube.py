

class rubiks:

    def __init__(self, create_cube):
        self.create_cube = create_cube

    def turn(self, side):
        clockwise_turn(cube.create_cube, side)

def clockwise_turn(cube_data, face):

    if face == 'u':
        
        subzero = cube.create_cube[0]
        sub1 = cube.create_cube[1]
        sub5 = cube.create_cube[5]
        sub2 = cube.create_cube[2]

        cube.create_cube[0]= cube.create_cube[6]
        cube.create_cube[1]= cube.create_cube[3]
        cube.create_cube[2]= subzero

        cube.create_cube[3]= cube.create_cube[7]
        cube.create_cube[5]= sub1
        cube.create_cube[6]= cube.create_cube[8]
        cube.create_cube[7]= sub5
        cube.create_cube[8]= sub2

        sub9 = cube.create_cube[9]
        sub10 = cube.create_cube[10]
        sub11 = cube.create_cube[11]

        cube.create_cube[9]= cube.create_cube[18]
        cube.create_cube[10]= cube.create_cube[19]
        cube.create_cube[11]= cube.create_cube[20]

        cube.create_cube[18]= cube.create_cube[36]
        cube.create_cube[19]= cube.create_cube[37]
        cube.create_cube[20]= cube.create_cube[38]

        cube.create_cube[36]= cube.create_cube[27]
        cube.create_cube[37]= cube.create_cube[28]
        cube.create_cube[38]= cube.create_cube[29]

        cube.create_cube[27]= sub9
        cube.create_cube[28]= sub10
        cube.create_cube[29]= sub11
        
        #print(cube.create_cube)

    if face == 'f':

        sub9 = cube.create_cube[9]
        sub10 = cube.create_cube[10]
        sub14 = cube.create_cube[14]
        sub11 = cube.create_cube[11]

        cube.create_cube[9]= cube.create_cube[15]
        cube.create_cube[10]= cube.create_cube[12]
        cube.create_cube[11]= sub9

        cube.create_cube[12]= cube.create_cube[16]
        cube.create_cube[14]= sub10
        cube.create_cube[15]= cube.create_cube[17]
        cube.create_cube[16]= sub14
        cube.create_cube[17]= sub11

        sub6 = cube.create_cube[6]
        sub7 = cube.create_cube[7]
        sub8 = cube.create_cube[8]

        cube.create_cube[6]= cube.create_cube[35]
        cube.create_cube[7]= cube.create_cube[32]
        cube.create_cube[8]= cube.create_cube[29]

        cube.create_cube[29]= cube.create_cube[45]
        cube.create_cube[32]= cube.create_cube[46]
        cube.create_cube[35]= cube.create_cube[47]

        cube.create_cube[45]= cube.create_cube[24]
        cube.create_cube[46]= cube.create_cube[21]
        cube.create_cube[47]= cube.create_cube[18]
        
        cube.create_cube[18]= sub6
        cube.create_cube[21]= sub7
        cube.create_cube[24]= sub8
        
        #print(cube.create_cube)

    if face == 'r':

        sub18 = cube.create_cube[18]
        sub19 = cube.create_cube[19]
        sub23 = cube.create_cube[23]
        sub20 = cube.create_cube[20]

        cube.create_cube[18]= cube.create_cube[24]
        cube.create_cube[19]= cube.create_cube[21]
        cube.create_cube[20]= sub18

        cube.create_cube[21]= cube.create_cube[25]
        cube.create_cube[23]= sub19
        cube.create_cube[24]= cube.create_cube[26]
        cube.create_cube[25]= sub23
        cube.create_cube[26]= sub20

        sub2 = cube.create_cube[2]
        sub5 = cube.create_cube[5]
        sub8 = cube.create_cube[8]

        cube.create_cube[2]= cube.create_cube[11]
        cube.create_cube[5]= cube.create_cube[14]
        cube.create_cube[8]= cube.create_cube[17]

        cube.create_cube[11]= cube.create_cube[47]
        cube.create_cube[14]= cube.create_cube[50]
        cube.create_cube[17]= cube.create_cube[53]

        cube.create_cube[47]= cube.create_cube[42]
        cube.create_cube[50]= cube.create_cube[39]
        cube.create_cube[53]= cube.create_cube[36]

        cube.create_cube[36]= sub8
        cube.create_cube[39]= sub5
        cube.create_cube[42]= sub2
        
        #print(cube.create_cube)

    if face == 'l':

        sub27 = cube.create_cube[27]
        sub28 = cube.create_cube[28]
        sub32 = cube.create_cube[32]
        sub29 = cube.create_cube[29]

        cube.create_cube[27]= cube.create_cube[33]
        cube.create_cube[28]= cube.create_cube[30]
        cube.create_cube[29]= sub27

        cube.create_cube[30]= cube.create_cube[34]
        cube.create_cube[32]= sub28
        cube.create_cube[33]= cube.create_cube[35]
        cube.create_cube[34]= sub32
        cube.create_cube[35]= sub29

        subzero = cube.create_cube[0]
        sub3 = cube.create_cube[3]
        sub6 = cube.create_cube[6]

        cube.create_cube[0]= cube.create_cube[44]
        cube.create_cube[3]= cube.create_cube[41]
        cube.create_cube[6]= cube.create_cube[38]

        cube.create_cube[38]= cube.create_cube[51]
        cube.create_cube[41]= cube.create_cube[48]
        cube.create_cube[44]= cube.create_cube[45]

        cube.create_cube[45]= cube.create_cube[9]
        cube.create_cube[48]= cube.create_cube[12]
        cube.create_cube[51]= cube.create_cube[15]

        cube.create_cube[9]= subzero
        cube.create_cube[12]= sub3
        cube.create_cube[15]= sub6
        
        #print(cube.create_cube)

    if face == 'b':

        sub36 = cube.create_cube[36]
        sub37 = cube.create_cube[37]
        sub41 = cube.create_cube[41]
        sub38 = cube.create_cube[38]

        cube.create_cube[36]= cube.create_cube[42]
        cube.create_cube[37]= cube.create_cube[39]
        cube.create_cube[38]= sub36

        cube.create_cube[39]= cube.create_cube[43]
        cube.create_cube[41]= sub37
        cube.create_cube[42]= cube.create_cube[44]
        cube.create_cube[43]= sub41
        cube.create_cube[44]= sub38

        subzero = cube.create_cube[0]
        sub2 = cube.create_cube[2]
        sub1 = cube.create_cube[1]

        cube.create_cube[0]= cube.create_cube[20]
        cube.create_cube[1]= cube.create_cube[23]
        cube.create_cube[2]= cube.create_cube[26]

        cube.create_cube[20]= cube.create_cube[53]
        cube.create_cube[23]= cube.create_cube[52]
        cube.create_cube[26]= cube.create_cube[51]

        cube.create_cube[51]= cube.create_cube[27]
        cube.create_cube[52]= cube.create_cube[30]
        cube.create_cube[53]= cube.create_cube[33]

        cube.create_cube[27]= sub2
        cube.create_cube[30]= sub1
        cube.create_cube[33]= subzero
        
        #print(cube.create_cube)

    if face == 'd':

        sub45 = cube.create_cube[45]
        sub46 = cube.create_cube[46]
        sub50 = cube.create_cube[50]
        sub47 = cube.create_cube[47]

        cube.create_cube[45]= cube.create_cube[51]
        cube.create_cube[46]= cube.create_cube[48]
        cube.create_cube[47]= sub45

        cube.create_cube[48]= cube.create_cube[52]
        cube.create_cube[50]= sub46
        cube.create_cube[51]= cube.create_cube[53]
        cube.create_cube[52]= sub50
        cube.create_cube[53]= sub47

        sub15 = cube.create_cube[15]
        sub16 = cube.create_cube[16]
        sub17 = cube.create_cube[17]

        cube.create_cube[15]= cube.create_cube[33]
        cube.create_cube[16]= cube.create_cube[34]
        cube.create_cube[17]= cube.create_cube[35]

        cube.create_cube[33]= cube.create_cube[42]
        cube.create_cube[34]= cube.create_cube[43]
        cube.create_cube[35]= cube.create_cube[44]

        cube.create_cube[42]= cube.create_cube[24]
        cube.create_cube[43]= cube.create_cube[25]
        cube.create_cube[44]= cube.create_cube[26]

        cube.create_cube[24]= sub15
        cube.create_cube[25]= sub16
        cube.create_cube[26]= sub17
        
        #print(cube.create_cube)

        #if cube.create_cube == list(range(0,54)):
            #print('true')
        #else:
            #print('false')
    

A = list(range(0,54))

cube = rubiks(A)




