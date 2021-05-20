from tkinter import *
window=Tk()
# add widgets here
lbl=Label(window, text="The Mental Health Quiz", fg='Black', font=("Serif", 21))
lbl.place(x=110, y=50)
btn=Button(window, text="Press To Continue", fg='Blue') 
btn.place(x=210, y=280)
window.title('The Mental Health Quiz 2021')
window.geometry("600x500+10+20")
# Button for closing
exit_button = Button(root, text="Exit", command=root.destroy) 

window.mainloop()
