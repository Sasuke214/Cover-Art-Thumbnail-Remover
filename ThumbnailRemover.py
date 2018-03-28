import eyed3
from tkinter import *
import tkinter
import tkinter.messagebox
import glob
import warnings
import os


class AlbumArtRemover:
    def __init__(self):
        eyed3.log.setLevel("ERROR")
        self.drawWindow()
    def one(self):
        #get a single file
        file=tkinter.filedialog.askopenfilename(title='select a file',filetypes=(('mp3 files','*.mp3'),('all files','*.*')))

        #if file is not selected, show error
        if(file==''):
            tkinter.messagebox.showerror('Error','Please select a audio file')
            return
        try:
            #load the audio file
            audiofile=eyed3.load(file)
            #remove the thumbnail art
            audiofile.tag.images.remove(u'')
            #save the file
            audiofile.tag.save()
        except:
            tkinter.messagebox.showerror('Error','Please select a audio file')
            
    def multiple(self):

        #take the directory where all songs are stored
        allfiles=tkinter.filedialog.askdirectory()
        if allfiles!='':
            os.chdir(allfiles)

            #get all files with mp3 and wav format
            songList=glob.glob('*.wav')
            songList.extend(glob.glob('*.mp3'))
            totalSongs=len(songList)
            for i in range(0,totalSongs):
                try:
                    #load the audio file
                    audiofile=eyed3.load(totalSongs[i])
                    #remove the thumbnail art
                    audiofile.tag.images.remove(u'')
                    #save the file
                    audiofile.tag.save()
                except:
                    continue
        else:
            tkinter.messagebox.showerror('Error','Please select a folder')
    
    def drawWindow(self):
        self.window=Tk()
        self.window.geometry("55x60")
        self.window.title('Album Art Cover Remover')
        self.window.resizable(False,False)

        self.frame0=Frame(self.window)
        self.frame0.grid(row=1)

        self.single=Button(self.frame0,text="One",command=self.one)
        self.single.grid()

        self.multiple=Button(self.frame0,text="All",command=self.multiple)
        self.multiple.grid()

        self.window.mainloop()
        

ac=AlbumArtRemover()
