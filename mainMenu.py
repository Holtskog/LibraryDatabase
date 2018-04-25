'''
    File name: mainMenu.py
    Author: Øyvind Holtskog
    Date created: 3/20/2018
    Date last modified: 4/25/2018
    Python Version: 3.6.4
'''

from tkinter import *
from videos import VideoGUI
from music import MusicGUI
from books import BookGUI

main_window = Tk()
main_window.title("Library Menu")

def books():
    main_window.withdraw()
    window = Toplevel()
    books_gui = BookGUI(window, main_window)
    #window.mainloop()

def videos():
    main_window.withdraw()
    window = Toplevel()
    video_gui = VideoGUI(window, main_window)
    #window.mainloop()

def music():
    main_window.withdraw()
    window = Toplevel()
    music_gui = MusicGUI(window, main_window)
    #window.mainloop()

header = Label(main_window, text="Øyvind's Library")
header.configure(width=50, font=("Helvetica", 18, "bold"))
header.grid(row=1,column=0, columnspan=3)

sub_header = Label(main_window, text="Choose the library of your choosing")
sub_header.configure(width=50, font=("Helvetica", 14, "bold"))
sub_header.grid(row=3, column=0, columnspan=3, rowspan=3)

video_button = Button(main_window, text="Movies", width=15, font=("Helvetica", 8, "bold"), command=videos)
video_button.grid(row=8, column=1)

music_button = Button(main_window, text="Music", width=15, font=("Helvetica", 8, "bold"), command=music)
music_button.grid(row=10, column=1)

book_button = Button(main_window, text="Books", width=15, font=("Helvetica", 8, "bold"), command=books)
book_button.grid(row=12, column=1)

close_button = Button(main_window, text="Close", width=15, font=("Helvetica", 8, "bold"), command=main_window.destroy)
close_button.grid(row=16, column=1)

spacing1 = Label(main_window, text=" ")
spacing1.grid(row=7,column=1)

spacing2 = Label(main_window, text=" ")
spacing2.grid(row=9,column=1)

spacing3 = Label(main_window, text=" ")
spacing3.grid(row=11,column=1)

spacing4 = Label(main_window, text=" ")
spacing4.grid(row=13,column=1)

spacing5 = Label(main_window, text=" ")
spacing5.grid(row=15,column=1)

spacing6 = Label(main_window, text=" ")
spacing6.grid(row=17, column=1, rowspan=3)



main_window.mainloop()

"""

add all the GUI classes here ...

instead of window = Tk() write e.g. music_window = Toplevel()

"""