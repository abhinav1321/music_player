import tkinter

root= tkinter.Tk()
root.geometry('300x300')
image=tkinter.PhotoImage(file='img1.jpg')

def change(imglbl):
    new = tkinter.PhotoImage(file='default.png')
    imglbl.configure(image=new)
    imglbl.photo_ref=new

imglbl=tkinter.Label(root,image=image)
print(type(imglbl))
button=tkinter.Button(root,text='boitton',command= lambda : change(imglbl)).pack()
imglbl.pack()
root.mainloop()

