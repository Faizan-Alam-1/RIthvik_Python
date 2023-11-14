from tkinter import *

win = Tk()

win.title("MY app")

win.geometry("550x550")
win.resizable(False, False)

main_frame = LabelFrame(win ,  padx=200,  pady =400)  
main_frame.grid(row = 0 , column= 0) 



count_label = Label(main_frame , text="counter:0")
count_label.grid(row = 0 ,  column = 0)



count = 0
def counter_increment():
   global count
   count = count+1
   count_label.config(text=f"counter: {count}")

def counter_decrement():
    global count

    if count > 0:
        count = count-1
        count_label.config(text=f"counter: {count}")
     
def rest_button():
    global count
    count = 0
    count_label.config(text=f"counter: {count}")

      


count_Button_add = Button(main_frame  , text="Add : +" , command = counter_increment)
count_Button_add.grid(row = 1 , column = 0)


count_Button_sub = Button(main_frame  , text="sub : -" , command = counter_decrement)
count_Button_sub.grid(row = 1  ,  column =1)

count_Button_rest = Button(main_frame  , text="Rest : " , command =  rest_button)
count_Button_rest.grid(row = 1  ,  column =2)



# pack() , gird()







win.mainloop()
