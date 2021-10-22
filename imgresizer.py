from PIL import Image
image=Image.open("demo_image.jpg")
while True:
    print("Menu Driven program")
    print("1.To get details about the image")
    print("2.To resize the image")
    print("3.To crop the image")
    print("4.To rotate the image")
    print("5.To flip the image")
    print("6.Exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        print("Format of the image:",image.format)                              # The file format of the source file.
        print("Pixel format of the image:",image.mode)                          # The pixel format used by the image. Typical values are "1", "L", "RGB", or "CMYK."
        print("Size of the image:", image.size)                                 # Image size, in pixels. The size is given as a 2-tuple (width, height).
        image.show()
    elif choice==2:
        image = Image.open('demo_image.jpg')                                    
        width=int(input("enter the width of the resized image:"))
        height=int(input("enter the height of thr resized image:"))
        new_image = image.resize((width, height))
        #new_image.save('resized_image.jpg')
        print("Size of original image:",image.size)
        print("Size of resized image:",new_image.size)
        new_image.show()
    elif choice==3:
        image = Image.open('demo_image.jpg')                                    
        ul=int(input("enter the value of upper left:"))
        ur=int(input("enter the value of upper right:"))
        ll=int(input("enter the value of lower left:"))
        lr=int(input("enter the value of lower right:"))
        box = (ul,ur,ll,lr)
        cropped_image = image.crop(box)
        #cropped_image.save('cropped_image.jpg')
        cropped_image.show()
    elif choice==4:
        image = Image.open('demo_image.jpg')
        rot=int(input("Enter the degree of rotation:"))
        image_rot = image.rotate(rot)
        #image_rot.save('image_rot.jpg')
        image_rot.show()
    elif choice==5:
        image = Image.open('demo_image.jpg')
        image_flip = image.transpose(Image.FLIP_LEFT_RIGHT) 
        #image_flip.save('image_flip.jpg')
        image_flip.show()
    elif choice==6:
        break
    else:
        print("Wrong Choice")

                                                





