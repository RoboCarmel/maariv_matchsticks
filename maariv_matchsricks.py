"""
first introducing the program, we would make 2 images, one is a matchstick riddle and the second is the solution,
then we would post it on the instagram account "matchsticks_puzzles" as a carrousel post (2 images together)
##### the logic part###
we would take each one of the numbers and numerators and turn it to an array of
0 and 1 based om each line in the number. *in the first place there would be the number
itself

            1
        ---------
        |       |
     4  |       |  6
        |   2   |
        ---------
        |       |
     5  |       |  7
        |   3   |
        ---------

so the number 4 would represent as [0,1,0,1,0,1,1]

             
        |       |
     4  |       |  6
        |   2   |
        ---------
                |
                |  7
                |
        

the next stage would be to create an equation and then decide whether to remove/add/move
 a number of matchhes to get a correct new equation

 for the add and remove we take a correct equation and just add/remove matches to get diffrenet numbers
"""

import numpy as np
import random
from PIL import Image, ImageDraw, ImageFont 
import glob
import matplotlib.pyplot as plt
import matplotlib
import os
import shutil
import image
import time
from matplotlib import font_manager
import matplotlib.patheffects as pe

font_dir = ['C:/Users/Roee/python/fonts']
for font in font_manager.findSystemFonts(font_dir):
    font_manager.fontManager.addfont(font)
    print(font)
font_manager.findfont("Gan CLM")

difficulty_indicator=[2]
difficulty_list=["easy","hard","impossible"]

""" logic phase - main function called 'generate_puzzle'"""


def changeMatchsticks(fd,sd,rd,symbol,numbers,num_of_matchsticks):
    #this function responsible for making a "move puzzle" as it is take a right equation then itiratiing
    #through all numbers and numerators available and check whether the sum of total matchstick is
    #equal (as we only need to move matchsticks around)
    main_equation=list(fd)
    main_equation.append(symbol)
    main_equation.extend(list(sd))
    main_equation.extend(list(rd))
    #we are combining the numbers and numerator to get one long array of 0 and 1 which is now a lot easier to use
    rl1 = list(range(0,(len(numbers)-1)))
    rl2 = list(range(0,(len(numbers)-1)))
    rl3 = list(range(0,(len(numbers)-1)))
    random.shuffle(rl1)
    random.shuffle(rl2)
    random.shuffle(rl3)
    #itirating through all numbers randomly until we get a "good shuffle" (next func)
    for i in rl1:
        new_fd=list(numbers[i])
        for k in rl2:
            new_sd=list(numbers[k])
            for j in rl3:
                new_rd=list(numbers[j])
                for s in range (0,1):
                    new_equation=list(new_fd)
                    new_equation.append(s)
                    new_equation.extend(list(new_sd))
                    new_equation.extend(list(new_rd))
                    if (good_shuffle(main_equation,new_equation,num_of_matchsticks,num_of_matchsticks)): # we want
                        #an absence of num_of_matchsticks matches and num_of_matchsticks new matchsticks
                        if (s==0):
                            res=numbers.index(new_fd)-numbers.index(new_sd)
                        else:
                            res=numbers.index(new_fd)+numbers.index(new_sd)
                        if (res!=numbers.index(new_rd)):
                            return True,new_fd,new_sd,new_rd,s
    return False,fd,sd,rd,symbol
        
    
            
        
#############################################################################################

def addMatchsticks(fd,sd,rd,symbol,numbers,num_of_matchsticks):
    #this function responsible for making an "add puzzle" as it is take a right equation then itiratiing
    #through all numbers and numerators available and check whether the sum of total absence of matchstick is
    #equal to num_of_matchsticks, so that the riddle will be to find and add them
    main_equation=list(fd)
    main_equation.append(symbol)
    main_equation.extend(list(sd))
    main_equation.extend(list(rd))
    #we are combining the numbers and numerator to get one long array of 0 and 1 which is now a lot easier to use
    rl1 = list(range(0,(len(numbers)-1)))
    rl2 = list(range(0,(len(numbers)-1)))
    rl3 = list(range(0,(len(numbers)-1)))
    random.shuffle(rl1)
    random.shuffle(rl2)
    random.shuffle(rl3)
    #itirating through all numbers randomly until we get a "good shuffle" (next func)
    for i in rl1:
        new_fd=list(numbers[i])
        for k in rl2:
            new_sd=list(numbers[k])
            for j in rl3:
                new_rd=list(numbers[j])
                for s in range (0,1):
                    new_equation=list(new_fd)
                    new_equation.append(s)
                    new_equation.extend(list(new_sd))
                    new_equation.extend(list(new_rd))
                    if (good_shuffle(main_equation,new_equation,num_of_matchsticks,0)): # we want an absence of
                        #num_of_matchsticks matches and 0 new matchsticks
                        if (s==0):
                            res=numbers.index(new_fd)-numbers.index(new_sd)
                        else:
                            res=numbers.index(new_fd)+numbers.index(new_sd)
                        if (res!=numbers.index(new_rd)):
                            return True,new_fd,new_sd,new_rd,s
    return False,fd,sd,rd,symbol
                    

#############################################################################################

def removeMatchsticks(fd,sd,rd,symbol,numbers,num_of_matchsticks):
    #this function responsible for making an "remove puzzle" as it is take a right equation then itiratiing
    #through all numbers and numerators available and check whether the sum of total new matchstick is
    #equal to num_of_matchsticks, so that the riddle will be to find and remove them
    main_equation=list(fd)
    main_equation.append(symbol)
    main_equation.extend(list(sd))
    main_equation.extend(list(rd))
    #we are combining the numbers and numerator to get one long array of 0 and 1 which is now a lot easier to use
    # i removed the number 8 because the model over use it
    rl1 = list(range(0,(len(numbers)-1)))
    rl2 = list(range(0,(len(numbers)-1)))
    rl3 = list(range(0,(len(numbers)-1)))
    rl1.remove(8)
    rl2.remove(8)
    rl3.remove(8)
    random.shuffle(rl1)
    random.shuffle(rl2)
    random.shuffle(rl3)
    #itirating through all numbers randomly until we get a "good shuffle" (next func)
    for i in rl1:
        new_fd=list(numbers[i])
        for k in rl2:
            new_sd=list(numbers[k])
            for j in rl3:
                new_rd=list(numbers[j])
                for s in range (0,1):
                    new_equation=list(new_fd)
                    new_equation.append(s)
                    new_equation.extend(list(new_sd))
                    new_equation.extend(list(new_rd))
                    if (good_shuffle(main_equation,new_equation,0,num_of_matchsticks)): # we want an absence of
                        #0 matches and num_of_matchsticks new matchsticks
                        if (s==0):
                            res=numbers.index(new_fd)-numbers.index(new_sd)
                        else:
                            res=numbers.index(new_fd)+numbers.index(new_sd)
                        if (res!=numbers.index(new_rd)):
                            return True,new_fd,new_sd,new_rd,s
    return False,fd,sd,rd,symbol
                    


#############################################################################################


def good_shuffle(main_equation,new_equation,count_of_one, count_of_minus_one):
    #checks whether the count of new matchsticks in the riddle equation (represented as the digit -1)
    #and the count of the absence of matchsticks in the riddle equation (represented as the digit 1)is equal
    #to the needed values:
    #lets say we want the riddle to be an "add" riddle so we check if there are enough matchsticks which were in
    #the solution equation but are not in the riddle one(count.1=num_of_matchsticks), and that there are
    #no new matchsticks in the riddle equatuon (count.-1=0)
    array1 = np.array(main_equation)
    array2 = np.array(new_equation)
    # the sustructed list would be an array with the numbers -1,0,1. -1 represent a match which was in the
    #second array nut not in the first, 0 is a place that left unchanged and 1 is a match which was in the
    #first array nut not in the second
    subtracted_array = np.subtract(array1, array2)
    subtracted = list(subtracted_array)
    if (subtracted.count(-1)==count_of_minus_one and subtracted.count(1)==count_of_one):
        return True
    return False

    

        


#############################################################################################


def checkDigit(digit,numbers):
    #checks wether an array of 0 and 1 is equal to one of the numbers represnted as 0 and 1
    for i in range (len(numbers)):
        if (digit==numbers[i]):
            return True
    return False
        




#############################################################################################

### main logic function!! ####
    
def generate_puzzle(post_name,story_name, difficulty):
    num0=[1,0,1,1,1,1,1]
    num1=[0,0,0,0,0,1,1]
    num2=[1,1,1,0,1,1,0]
    num3=[1,1,1,0,0,1,1]
    num4=[0,1,0,1,0,1,1]
    num5=[1,1,1,1,0,0,1]
    num6=[1,1,1,1,1,0,1]
    num7=[1,0,0,0,0,1,1]
    num8=[1,1,1,1,1,1,1]
    num9=[1,1,1,1,0,1,1]
    num11=[0,0,0,1,1,1,1] # a special presentation to enhance difficulty :) 11 -> 4
    numnull=[0,0,0,0,0,0,0]
    action=["ופיסוה","ודירוה","וזיזה"]
    numbers9=[num0,num1,num2,num3,num4,num5,num6,num7,num8,num9]
    #initializing the numbers lists
    numbers19=[]
    numbers99=[]
    numbers199=[]
    numbers999=[]
    for i in range (0,10):
        numbers19.append(numnull+numbers9[i])
        numbers99.append(numnull+numbers9[i])
        numbers199.append(numnull+numnull+numbers9[i])
        numbers999.append(numnull+numnull+numbers9[i])
        
    for i in range (10,100):
        if (i==11):
            numbers19.append(numnull+num11)
            numbers99.append(numnull+num11)
            numbers199.append(numnull+numnull+num11)
            numbers999.append(numnull+numnull+num11)
        else:
            if (i<20):
                numbers19.append(num1+numbers9[i%10])
            numbers99.append(numbers9[i//10]+numbers9[i%10])
            numbers199.append(numnull+numbers9[i//10]+numbers9[i%10])
            numbers999.append(numnull+numbers9[i//10]+numbers9[i%10])
            
    for i in range (100,1000):
        if (i//10 ==11):
            numbers999.append(numnull+num11+numbers9[i%10])
            numbers199.append(numnull+num11+numbers9[i%10])
        elif (i%100==11):
            numbers999.append(numnull+numbers9[i//100]+num11)
        else:
            if (i<200):
                numbers199.append(numbers9[i//100]+numbers9[(i%100)//10]+numbers9[i%10])
            numbers999.append(numbers9[i//100]+numbers9[(i%100)//10]+numbers9[i%10])
    # the 'numbers9' list contains a 7 digit 0,1 lists as shown in the begining for each number 0-9
    # the 'numbers19' list contains a 14 digit 0,1 lists as shown in the begining for each number 0-19
    # the 'numbers99' list contains a 14 digit 0,1 lists as shown in the begining for each number 0-99
    # the 'numbers199' list contains a 21 digit 0,1 lists as shown in the begining for each number 0-199
    # the 'numbers999' list contains a 21 digit 0,1 lists as shown in the begining for each number 0-999

    big_numbers=[numbers9,numbers9,numbers9]
    numbers=list(big_numbers[difficulty])
    #'numbers' is the list we work with based on difficulty
    image_datas = []
    for filename in glob.glob('C:/Users/Roee/python/matches/*.jpg'): 
        im=Image.open(filename)
        image_datas.append(im)

    good_equation=False
    found_solution=False
    #looping until we find a good riddle which isnt already correct
    while (not good_equation or not found_solution):
        symbol=random.randint(0,1)
        result_symbol=symbol
        action_number=random.randint(0,2)
        #randomizing minus/plus and add/remove/move  by order!
        good_equation=False
        first_digit=random.randint(1,(len(numbers)-1))
        second_digit=random.randint(1,(len(numbers)-1))
        if (symbol==0):
            #minus problem
            
            result_digit=first_digit-second_digit
            if (result_digit>0):
                good_equation=True
            if (good_equation):
                #creating temp lists of numbers
                fd=list(numbers[first_digit])  
                sd=list(numbers[second_digit])
                rd=list(numbers[result_digit])
                
                if (action_number==0):
                    # we need to add matchsticks
                    num_of_matchsticks=random.randint(1,3)
                    found_solution,fd,sd,rd,symbol = addMatchsticks(fd,sd,rd,symbol,numbers,num_of_matchsticks)
                    
                elif (action_number==1):
                    # we need to remove matchsticks
                    num_of_matchsticks=random.randint(1,3)
                    found_solution,fd,sd,rd,symbol = removeMatchsticks(fd,sd,rd,symbol,numbers,num_of_matchsticks)
                    
                elif (action_number==2):
                    # we need to change matchsticks
                    num_of_matchsticks=random.randint(1,2)
                    found_solution,fd,sd,rd,symbol = changeMatchsticks(fd,sd,rd,symbol,numbers,num_of_matchsticks)
                    
                # i dont want a correct equation
                if (numbers.index(fd)-numbers.index(sd)==numbers.index(rd)):  
                    found_solution=False
        else:
            #plus problem
            
            result_digit=first_digit+second_digit
            if (result_digit<len(numbers)):
                good_equation=True
            if (good_equation):
                #creating temp lists of numbers
                fd=list(numbers[first_digit])   
                sd=list(numbers[second_digit])
                rd=list(numbers[result_digit])
                
                if (action_number==0):
                    # we need to add matchsticks
                    num_of_matchsticks=random.randint(1,3)
                    found_solution,fd,sd,rd,symbol = addMatchsticks(fd,sd,rd,symbol,numbers,num_of_matchsticks)
                    
                elif (action_number==1):
                    # we need to remove matchsticks
                    num_of_matchsticks=random.randint(1,3)
                    found_solution,fd,sd,rd,symbol = removeMatchsticks(fd,sd,rd,symbol,numbers,num_of_matchsticks)
                    
                elif (action_number==2):
                    # we need to move matchsticks
                    num_of_matchsticks=random.randint(1,2)
                    found_solution,fd,sd,rd,symbol = changeMatchsticks(fd,sd,rd,symbol,numbers,num_of_matchsticks)
                    
                # i dont want a correct equation
                if (numbers.index(fd)+numbers.index(sd)==numbers.index(rd) ):
                    found_solution=False

##########################################################################################################################
##########################################################################################################################

            """ designing part!!!!"""

    #here we start designing the post making it a subplot for each number and giving it a random title
    print(str(fd)+ " + " + str(sd) + " = "+ str (rd))
    instructions= "{plural}רורפג {num} {actionword}".format(actionword=action[action_number],num= num_of_matchsticks if
                                              num_of_matchsticks >1 else "",plural= "םי" if
                                              num_of_matchsticks >1 else " דחא " )
    plt.rcParams["figure.figsize"] = [12, 8]
    f = plt.figure()
    font_title = {'family':'Dorian CLM','color':'red'}
    title="\n\n תימויה םירורפגה תדיח"
    st = f.suptitle( title,
              fontdict = font_title,
              fontsize=60,
              path_effects=[pe.withStroke(linewidth=4, foreground="black")])
        #
    # we divide our equation to simple numbers to represnt them as digits
    equation=[]
    for i in range (0,(len(fd)//7)):
        fd_temp=fd[(i*7):(i*7+7)]
        if (fd_temp[0] != 0 or fd_temp[-1] != 0 ): #checkimg whether this digit is null
            equation.append(fd_temp)
        
    equation.append([(11+symbol)])

    
    for i in range (0,(len(sd)//7)):
        sd_temp=sd[(i*7):(i*7+7)]
        if (sd_temp[0] != 0 or sd_temp[-1] != 0 ):
            equation.append(sd_temp)

    equation.append([10])

    for i in range (0,(len(rd)//7)):
        rd_temp=rd[(i*7):(i*7+7)]
        if (rd_temp[0] != 0 or rd_temp[-1] != 0 ):
            equation.append(rd_temp)
    if (len(equation)<6):
        ind=2
        equation_len=len(equation)+2
    else:
        ind=1
        equation_len=len(equation)
    for i in equation:    
        f.add_subplot(1,equation_len, ind)
        if (len(i)>3):
            if (i==num11):
                plt.imshow(image_datas[-1])
                plt.axis('off')
            else:
                plt.imshow(image_datas[numbers9.index(i)])
                plt.axis('off')
        else:
            plt.imshow(image_datas[i[0]])
            plt.axis('off')
        ind+=1
    plt.figtext(0.5, 0.18, instructions,
                ha="center",
                fontdict = font_title,
                fontsize=60,
                path_effects=[pe.withStroke(linewidth=4, foreground="black")])
               
    
    image_demo='my_post1.JPEG'
    plt.savefig(image_demo)
    background(image_demo, post_name, (difficulty+1))
    
    print("solution")
    print(str(numbers[first_digit])+ " + " + str(numbers[second_digit]) + " = "+ str (numbers[result_digit]))
    fd=list(numbers[first_digit])   
    sd=list(numbers[second_digit])
    rd=list(numbers[result_digit])

    f = plt.figure()
    title="\n\n הדיחה ןורתיפ"
    st = f.suptitle( title,
              fontdict = font_title,
              fontsize=60,
              path_effects=[pe.withStroke(linewidth=4, foreground="black")])
    # we divide our equation to simple numbers to represnt them as digits
    equation=[]
    for i in range (0,(len(fd)//7)):
        fd_temp=fd[(i*7):(i*7+7)]
        if (fd_temp[0] != 0 or fd_temp[-1] != 0 ): #checkimg whether this digit is null
            equation.append(fd_temp)
        
    equation.append([(11+result_symbol)])

    
    for i in range (0,(len(sd)//7)):
        sd_temp=sd[(i*7):(i*7+7)]
        if (sd_temp[0] != 0 or sd_temp[-1] != 0 ):
            equation.append(sd_temp)

    equation.append([10])

    for i in range (0,(len(rd)//7)):
        rd_temp=rd[(i*7):(i*7+7)]
        if (rd_temp[0] != 0 or rd_temp[-1] != 0 ):
            equation.append(rd_temp)
    if (len(equation)<6):
        ind=2
        equation_len=len(equation)+2
    else:
        ind=1
        equation_len=len(equation)
    for i in equation:    
        f.add_subplot(1,equation_len, ind)
        if (len(i)>3):
            if (i==num11):
                plt.imshow(image_datas[-1])
                plt.axis('off')
            else:
                plt.imshow(image_datas[numbers9.index(i)])
                plt.axis('off')
        else:
            plt.imshow(image_datas[i[0]])
            plt.axis('off')
        ind+=1
    plt.figtext(0.5, 0.18, "?םתחלצה",
                ha="center",
                fontdict = font_title,
                fontsize=60,
                path_effects=[pe.withStroke(linewidth=4, foreground="black")])
                #, ha="center", fontsize=30, fontdict = font_sub, bbox={"facecolor":"teal", "alpha":0.5, "pad":5})
    
    image_demo='my_solution1.JPEG'
    plt.savefig(image_demo)
    background(image_demo, story_name, (difficulty+1))
    

##########################################################################################################################


""" giving background for the posts"""

def background(OLD_PATH, NEW_PATH,difficulty):
    background = Image.open('background_maariv2.jpg')
    background_resized = background.resize((1200, 800))
    background_resized=background_resized.convert("RGB")
    background_data=background_resized.getdata()
    img = Image.open(OLD_PATH)
    img = img.convert("RGB")
     
    d = img.getdata()
    i=0
    new_image = []
    for item in d:
       
        # change all white (also shades of whites)
        # pixels to yellow
        if (item[2] in list(range(200, 256))):
            new_image.append((background_data[i][0], background_data[i][1], background_data[i][2]))
        else:
            new_image.append(item)
        i+=1
             
    # update image data
    img.putdata(new_image)
    img.save(NEW_PATH)
    
##########################################################################################################################
def upload_to_instagram():

    #imporant note is that every post name includes its timestamp in order to differ from one another
    timestamp = int(time.time())
    difficulty=difficulty_indicator[-1]%3
    
    post_path = "C:/Users/Roee/python/posts/my_post{}.JPEG".format(timestamp)
    story_path= "C:/Users/Roee/python/posts/story{}.JPEG".format(timestamp)
    generate_puzzle(post_path,story_path,difficulty)
    difficulty_indicator.append((difficulty_indicator[-1]+1))




##########################################################################################################################

"""         main!!!!    """
for i in range (0,3):
    upload_to_instagram()
