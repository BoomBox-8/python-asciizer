## **Program**

This is a simple Python program capable of converting images (preferably 1280x720 images due to the algorithms used) to an ASCII-Art style image (emphasis on the last point, the output is merely an image, not text one can copy

## Usage

To use the program, run main.py and type in the numbers corresponding to your choice or file names/extensions when prompted
Videos converted to ASCII-style GIFs will have the GIFs saved in the program folder. Save supports don't exist for images at this time, the image will only be displayed

## Working Principles

The idea of the program is relatively straightforward. The image is scanned in block-sized chunks, where the average intensity (here, intensity refers to how white or black the pixels are, image is converted to a single-channel greyscale image beforehand, for this purpose) in the entire block is found

A block with a very low average pixel intensity would be very dark in the original image, since dark pixels have low intensity values while light pixels will have high intensity values. Of course, if a 8x8 block has 1 bright pixel and 7 very dark pixels, the average will still be calculated to be low. I believe this is a shortcoming of the mean formula. Weighted means could be used, but I neither know what to weight, nor the time to implement it at the moment

Moving back to the main point, based on the average pixel value found, we paste in a 8x8 picture of an ASCII character at that very spot. The background of these pictures are white, where white is to be logically considered as 'blank'. Therefore, an ASCII character made up of many pixels like an '@' would appear 'brighter' and 'larger' than a '.'. Note all ASCII character images are the same size of 8x8 pixels, it is merely that a larger, brighter character like an '@' would take up more space of these 8x8 pixels than a '.'. Do note that the main attribute with which letters are picked, is with the number of pixels the characters in these very tiny images are made up of!

Hence, if the average color intensity of the scanned 8x8 block from the original image is very high, paste in an 8x8 ASCII character image  that is made up of 'many pixels' or is 'large' relative to the 8x8 block it sits in

An 8x8 block consisting of pure black would have an average intensity of 0, hence paste in an 8x8 'blank-space' character image (because such a character image is logically made of NO ASCII characters = NO Pixels = Suitable for this scenario)

The box moves sideways across the image, that is, from left to right. Once it reaches the end of the screen, the box moves to the left of screen to the below rows to start the process again. Left to Right, and Up to Down is how these boxes move.

Once the box has moved across the full image and pasted in the suitable ASCII character pictures, the image is ready! Do note that as of now for some odd reasons, the images generated are not capable of being saved properly, so its best these are screenshotted and saved. That being said, feel free to add more ASCII character images, and decide the intensity values at which they should be picked accordingly. This can provide a nice smooth 'gradient' in generated images if you do it right. Very time intensive to find the optimal characters and values to use though

## FAQ And Other Miscellaneous Info
**Q1. Why do the ASCII Character images appear to be clipped at the bottom?**
This is a major shortcoming of the program with which I made these 8x8 images, i.e., MS Paint. GIMP didn't quite cut it right, hence it was not used. The issue is that Paint refuses to let you move the text box you make up and down. Does not help the image is already very small, and that Paint can only zoom in so far. For similar reasons, centering the text was also tough

**Q2. How is the 'resolution' of the ASCII characters decided here?**
Note that larger the block with which you scan, and larger the ASCII character images, the less 'accurate' they will be, since you are attempting to represent a huge area of pixel data where pixel values might differ a lot, with a single ASCII character. Hence, smaller the block, the more 'highres' it looks

8x8 was derived experimentally. I used an online image to ASCII converter just to observe the average size of the pixels making up each ASCII characters. Do note that such  online converters provide the ability to change the 'resolution'. I decided to observe the 'middleground' 'resolution' at which the image could still be identified and look like ASCII art, and still look detailed enough. 8 also happens to be an LCM of 1280 and 720 so you won't encounter issues when moving a non-LCM sized box across the images (because of what would happen when one encounters an edge). That being said, I did encounter my algorithm working with non 1280x720 images, not sure of any edge cases that'd throw up an error. Better be on the safe side!

**Q3. Uh oh! My image I want to turn into an ASCII-Art style image is not 1280x720! What do I do?**
Luckily the program will scale your image to 1280x720, though keep in mind aspect ratios can be changed for non-16:9 images. On top of that, low-res images scaled up to 1280x720 will not be as detailed as a true native 1280x720 image. This is exacerbated for very low-res images. Small deviations below 1280x720 are okay, the ASCII character don't express super fine detail anyway, so it is fine

**Q4. What is a LURD?**
Pillow uses a 4-tuple ( like (x,y,w,z), a 4-element tuple ) to define the 'size' and boundaries of methods that make use of bounding boxes. X is called Left, or the co-ordinate of the upper-left corner on the x-axis. On the extreme left, this value would be zero, since the origin is considered to start from the upper-left corner of the image. Y is called Upper, or the co-ordinate of the upper-left corner on the y-axis. Simiarly, w and z are right and down, or the x-axis and y-axis co-ordinates of the bottom-right corner. In an 1280x720 image, the very bottom-right corner would have w,z values of 1280,720. I simply call these values LURD for short (Left,Upper,Right,Down)

**Important**
Keep in mind, due to the working mechanism described above, an image with very little variance in shades or colors can not be represented in the ASCII-Art style accurately. Similarly, images with a lot of fine detail can also not be expected to be drawn perfectly since we are essentially representing boxes larger than a single pixel with a single character. Contures, curves, shapes, shadows and some gradients can be easily represented however. This is merely a consequence of how ASCII art works. When micro-detail is represented by the arrangement of pixels on the original image, ASCII characters can not produce the same amount of detail

Also do try out the program on the car image provided! Works like a charm!

Also note that Notepad isn't the best to view this file, formatting is killed off and makes it an unreadable mess


 
