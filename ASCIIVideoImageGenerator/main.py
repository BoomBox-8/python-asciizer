'''
• A program that converts images to an ASCII Art styled image! 
• Works on ALMOST all resolutions, 1280x720p images reccomended!
• Effect works best on images with a lot of 'variance' in contrast, ie, a picture consisting of
  smoothly blended colors or more or less the same few colors in its color pallete won't work well enough
• Test images are included in the folder for use, try them out!
No programmers were harmed in the making of this!
'''


import time, sys, numpy as np
from moviepy.editor import * 
from PIL import Image, ImageOps


empty = Image.open('empty.png').convert(mode = 'L')  #Gotta convert these to greyscale 
hashed = Image.open('#.png').convert(mode = 'L')     #This is because .getcolors for RGB images returns a tuple consisting of individual values of R,G,&B Channels
comma = Image.open(',.png').convert(mode = 'L')      #mode = 'L' gives you just the 'intensity' from 0-256
at = Image.open('@.png').convert(mode = 'L')         #Much easier to deal with!
O = Image.open('O.png').convert(mode = 'L')         
period = Image.open('period.png').convert(mode = 'L')

asciiDict = {0: empty, 25: period, 70: comma, 128: hashed, 208: O, 255: at} #Dict of all the above images, ez access
#We find the average color intensity of each 8x8 block of the image and paste in one of the above pics
#This is based on the avg color in the 8x8 block

def imageGrabber(avg): 
    '''Finds the most appropriate 8x8 image to paste over the block in which we found the average intensity'''
    
    keyList = [i for i in asciiDict]
    matching = min(keyList, key = lambda x: abs(x-avg)) #Gives us the closest matching key. Principle further explained in .README
    return asciiDict[matching] #Returns suitable ascii image


def colorAvg(colorArray,sumVal=0,size=0):
    '''Finds the average intensity based on colorArray, a list of intensity values (.getcolors())'''
    
    for i,j in colorArray:
        sumVal+= i*j #.getColors() returns a list consisting of EVERY intensity of pixels in the 8x8 block, along with their frequency
        size+=i #[(x,y)] where x is the number of times that specific intensity appears, and y is the value of the intensity from 0-256
    return sumVal//size #Mean/Avg formula : Sum of Obv/Number Of Obv


def moveSquare(image,lurd,imageCopy): 
    '''Supplies the 8x8 block to colorAvg to find the avg intensity of, and moves the square across the image'''
    
    cropped = image.crop(lurd) 
    avg = colorAvg(cropped.getcolors())
    matched = imageGrabber(avg)
    imageCopy.paste(matched,lurd) #Pastes in the matched 8x8 image into copy
    #Try to find out its dimensions


def quitLoop(): 
    '''A function that either quits the program or updates a flag to keep the program going'''

    choice = int(input('''Choose your option:
1) Quit
2) Rerun The Program\n''')) #Enter the number of the choice you want as input here!

    if choice == 1: sys.exit('Till we meet again')

    else: return True #The flag here is simple. Return True to keep it going. No need to return False in the other case, sys.exit() takes care of it


def ascii(pic, pure = True):
    '''Returns either an ASCII image or ASCII Image converted into an array depending on the pure arg'''

    if pic.size != (1280, 720): pic = pic.resize((1280, 720), Image.NEAREST) 

    picCopy = pic.copy()  #Some of the methods I use modify the image objects in place, hence make a copy
    l, u, r, d = 0, 0, 8, 8  #Explanation about this in .README hopefully
    
    while r <= 1280 and d <= 720:  #When both these conditions are satisifed, moveSquare() has reached the end of the image, the bottom-right corner
        lurd = (l, u, r, d)
        moveSquare(pic, lurd, picCopy)

        if r == 1280:  #If moveSquare reaches the end of a row of pixels in the images, send moveSquare to next row
            l, u, r, d = 0, u+8, 8, d+8

        else:
            l, r = l+8, r+8  #If it hasn't, just send moveSqaure() to the adjcent 8x8 square of pixels to scan

    if pure == True:
        return ImageOps.invert(picCopy)

    return np.asarray(ImageOps.invert(picCopy)) #Return this if its not a pure image file; if its an array


def asciiFilterImg(pic):
    '''Just to make ASCII images from a regular image'''

    return ascii(pic, pure = True)

      #All done hopefully


def asciiFilterVid(array):
    '''Turns Video Into ASCII, output has low af fps tho'''

    pic = Image.fromarray(array).convert(mode= 'L')
    return ascii(pic, pure = False)


def vidAscii():
    '''Name your file and run fl_image on it and shoot out a gif'''

    with VideoFileClip(f"{input('Name: ')}.{input('Extension: ')}") as vid:
        newVid = vid.fl_image(asciiFilterVid)
        newVid.write_gif(f'{input("Name your GIF File: ")}.gif', True)


def imgAscii():
    '''Name your file and shoot out a picture'''

    with Image.open(f"{input('Name: ')}.{input('Extension: ')}") as img:
        newImg = asciiFilterImg(img.convert(mode = 'L'))
        newImg.show()


repeatFlag = True #The flag that either runs or stops the program

while repeatFlag == True:
    choice = int(input("""Enter your choice:
    1) ASCII A Video
    2) ASCII An Image
    """))

    if choice == 1: vidAscii()
    else: imgAscii()
    
    repeatFlag = quitLoop()

