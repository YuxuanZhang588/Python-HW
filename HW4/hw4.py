'''
Author: Thatcher Craig  David Zhang
'''

import image

def gradient_blend():
    rick_red = image.get_channel('rick.jpg', 'red')
    rick_green = image.get_channel('rick.jpg', 'green')
    rick_blue = image.get_channel('rick.jpg', 'blue')
    
    ilsa_red = image.get_channel('ilsa.jpg', 'red')
    ilsa_green = image.get_channel('ilsa.jpg', 'green')
    ilsa_blue = image.get_channel('ilsa.jpg', 'blue')
    
    height = len(ilsa_red)
    width = len(ilsa_red[0])
    

    
    for row in range(height):
        Br = row/height
        for col in range(width):
            Bc = col/width
            B = max(Br, Bc)
            rick_red[row][col] = int(B*rick_red[row][col]+(1-B)*ilsa_red[row][col])
            rick_green[row][col] = int(B*rick_green[row][col]+(1-B)*ilsa_green[row][col])
            rick_blue[row][col] = int(B*rick_blue[row][col]+(1-B)*ilsa_blue[row][col])
    
    image.write_jpg(rick_red, rick_green, rick_blue, 'blended.jpg')
    
    image.show('blended.jpg')
            
def mirror():
    
    name = input("Enter the name of an image file: ")
    
    name_red = image.get_channel(name, 'red')
    name_green = image.get_channel(name, 'green')
    name_blue = image.get_channel(name, 'blue')
    
    height = len(name_red)
    width = len(name_red[0])
    
    for row in range(height):
        for col in range(width):
            name_red[row][-col-1] = name_red[row][col]
            name_green[row][-col-1] = name_green[row][col]
            name_blue[row][-col-1] = name_blue[row][col]
    
    image.write_jpg(name_red, name_green, name_blue, 'mirrored.jpg')
    
    image.show('mirrored.jpg')
    
def pencil_sketch():
    name = input("Enter the name of an image file: ")
    
    name_red = image.get_channel(name, 'red')
    name_green = image.get_channel(name, 'green')
    name_blue = image.get_channel(name, 'blue')
    
    height = len(name_red)
    width = len(name_red[0])
    
    for row in range(height-1):
        for col in range(width-1):
            if abs(int((name_red[row][col]+name_green[row]
                        [col]+name_blue[row][col])/3)-
                   int((name_red[row+1][col]+name_green[row+1]
                    [col]+name_blue[row+1][col])/3)) > 8 and abs(int((
                    name_red[row][col]+name_green[row][col]+name_blue[row][col])/3)-
                   int((name_red[row][col+1]+name_green[row][col+1]
                        +name_blue[row][col+1])/3)) > 8:
                name_red[row][col] = 0
                name_green[row][col] = 0
                name_blue[row][col] = 0
            
            else:
                name_red[row][col] = 255
                name_green[row][col] = 255
                name_blue[row][col] = 255
    
    image.write_jpg(name_red, name_green, name_blue, 'sketched.jpg')
    
    image.show('sketched.jpg')
                
def sliding_tilt():
    name = input("Enter the name of an image file: ")
    
    name_red = image.get_channel(name, 'red')
    name_green = image.get_channel(name, 'green')
    name_blue = image.get_channel(name, 'blue')
    
    height = len(name_red)
    width = len(name_red[0])
    
    for row in range(height):
        for col in range(int(width*2/3),width):
            name_red[row][col] = name_red[row][col-int(width*2/3)]
            name_green[row][col] = name_green[row][col-int(width*2/3)]
            name_blue[row][col] = name_blue[row][col-int(width*2/3)]

    image.write_jpg(name_red, name_green, name_blue, 'step1.jpg')
    
    #image.show('step1.jpg')
    
    name_red = image.get_channel(name, 'red')
    name_green = image.get_channel(name, 'green')
    name_blue = image.get_channel(name, 'blue')
    
    step1_red = image.get_channel('step1.jpg', 'red')
    step1_green = image.get_channel('step1.jpg', 'green')
    step1_blue = image.get_channel('step1.jpg', 'blue')
    
    for row in range(height):
        for col in range(int(width/3)):
            step1_red[row][col] = name_red[row][int(width*2/3)+col]
            step1_green[row][col] = name_green[row][int(width*2/3)+col]
            step1_blue[row][col] = name_blue[row][int(width*2/3)+col]
    
    image.write_jpg(step1_red, step1_green, step1_blue, 'step2.jpg')
    image.show('step2.jpg')
    
    step2_red = image.get_channel('step2.jpg', 'red')
    step2_green = image.get_channel('step2.jpg', 'green')
    step2_blue = image.get_channel('step2.jpg', 'blue')
    
    for row in range(int(height*2/3),height):
        for col in range(width):
            step2_red[row][col] = step2_red[row-int(height*2/3)][col]
            step2_green[row][col] = step2_green[row-int(height*2/3)][col]
            step2_blue[row][col] = step2_blue[row-int(height*2/3)][col]
    
    image.write_jpg(step2_red, step2_green, step2_blue, 'step3.jpg')
    #image.show('step3.jpg')
        
    step2_red = image.get_channel('step2.jpg', 'red')
    step2_green = image.get_channel('step2.jpg', 'green')
    step2_blue = image.get_channel('step2.jpg', 'blue')
    
    step3_red = image.get_channel('step3.jpg', 'red')
    step3_green = image.get_channel('step3.jpg', 'green')
    step3_blue = image.get_channel('step3.jpg', 'blue')
    
    for row in range(int(height/3)):
        for col in range(width):
            step3_red[row][col] = step2_red[row+int(height*2/3)][col]
            step3_green[row][col] = step2_green[row+int(height*2/3)][col]
            step3_blue[row][col] = step2_blue[row+int(height*2/3)][col]
            
    image.write_jpg(step3_red, step3_green, step3_blue, 'tilted.jpg')
    image.show('tilted.jpg')
         
              

def main():
    gradient_blend()
    mirror()
    pencil_sketch()
    sliding_tilt()

if __name__ == "__main__":
    main()
    