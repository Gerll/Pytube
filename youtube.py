from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as Messagebox

print(os.getcwd())

def accion():
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()

def popup():
    Messagebox.showinfo("Sobre mi, enlace a mi perfil de Linkedin:")

root = Tk()
root.config(bd=15)
root.title("Script descargar videos")

#Image
#imagen = PhotoImage(file="imageName.format")
#foto = Label(root, image=imagen, bd=0)
#foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Para más información", menu=helpmenu)
helpmenu.add_command(label="Información del autor", command=popup)
menubar.add_command(label="Salir", command=root.destroy)

instrucciones = Label(root, text="Programa creado en Python para descargar videos de YouTube")
instrucciones.grid(row=0, column=1)

videos=Entry(root)
videos.grid(row=1, column=1)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1)

root.mainloop()