from tkinter import *
# from PIL import Image, ImageTK
win  = Tk()
win.geometry("600x600")
win.title("Drink water notification")
win.resizable(False , False)

main_frame = LabelFrame(win , padx= 100 ,  pady= 8 , borderwidth=3 )
main_frame.grid(row= 0 ,  column=0, padx=60 ,  pady=60)



# here Lable 

lable_display = Label(main_frame ,text= "Drinking water notification" , font= ("Comic Sans MS" , 14 , "bold" ),  bg= "#C4C4C4" )
lable_display.grid(row=1 , column=0, padx=60 ,  pady=40)


# image 

# Display_image =  ImageTK.PhotoImage(Image.open("image/drink.jpg"))
# Image_label = Label(main_frame , image=Display_image)
# Image_label.grid(row=1 ,  column=0)


# input box 

time_interver = Entry(main_frame,  width=40)
time_interver.insert(0, "Enter the time :")
time_interver.grid(row=2, column=0 , padx=30)


def nofication_function():
    print("Hello world funtion is working")



# button 

btn = Button(main_frame ,text="Set" ,   pady=16 ,  padx=40, borderwidth=3 , relief=SOLID , command=nofication_function)
btn.grid(row =3 , column = 0 )




win.mainloop()