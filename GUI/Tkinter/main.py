from tkinter import *
win = Tk()

# To change title 
win.title("Shailesh")

# To change trancepancy 
win.attributes("-alpha",1) # -alpha value lies between 0 to 1

# To change background color
#win.config(bg="red")

# Another method to change background color
win['bg'] = "yellow"

# To set the dimension of win
#win.geometry("300x500")

# To fix it in centre
height = 300
width = 500

# For system width and height
sys_width = win.winfo_screenwidth()
sys_height = win.winfo_screenheight()

# For window in centre
c_x = int(sys_width/2 - width/2)
c_y = int(sys_height/2 - height/2)

# To set geometry
win.geometry(f"{width}x{height}+{c_x}+{c_y}")

win.mainloop()