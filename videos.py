from tkinter import *
from backendVideos import VideoDatabase
from tkinter import messagebox

database = VideoDatabase("dbname='Library' user='postgres' password='postgres1' host='localhost' port='5432'")

class VideoGUI(object):
    """ This class creates the GUI and defines calls the button behavior """

    def __init__(self, window, parent):
        self.window = window
        self.parent = parent
        self.window.wm_title("Video Section")

        # Create text labels:
        self.title_label = Label(window, text="Title")
        self.title_label.grid(row=1, column=12)

        self.producer_label = Label(window, text="Producer")
        self.producer_label.grid(row=1, column=16)

        self.year_label = Label(window, text="Year")
        self.year_label.grid(row=2, column=12)

        self.director_label = Label(window, text="Director")
        self.director_label.grid(row=2, column=16)

        # Create the entry boxes
        self.title_value = StringVar()
        self.title_box = Entry(window, textvariable=self.title_value)
        self.title_box.grid(row=1, column=13, columnspan=2)

        self.producer_value = StringVar()
        self.producer_box = Entry(window, textvariable=self.producer_value)
        self.producer_box.grid(row=1, column=17, columnspan=2)

        self.year_value = StringVar()
        self.year_box = Entry(window, textvariable=self.year_value)
        self.year_box.grid(row=2, column=13, columnspan=2)

        self.director_value = StringVar()
        self.director_box = Entry(window, textvariable=self.director_value)
        self.director_box.grid(row=2, column=17, columnspan=2)

        # Create the textbox to view the "library":
        self.view_box = Listbox(window, height=20, width=70)
        self.view_box.grid(row=1, column=0, rowspan=10, columnspan=10)

        # Create the scroll bars:
        self.scroll_bar = Scrollbar(window)
        self.scroll_bar.grid(row=1, column=10, rowspan=10)
        self.hscroll_bar = Scrollbar(window, orient=HORIZONTAL)
        self.hscroll_bar.grid(row=11, column=0, columnspan=10)

        # Define a bind function to the scroll bar:
        self.view_box.configure(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.configure(command=self.view_box.yview)
        self.hscroll_bar.configure(command=self.view_box.xview)

        # Define a bind function to the view box:
        self.view_box.bind('<<ListboxSelect>>', self.get_selected_row)

        # Create the buttons:
        self.view_button = Button(window, \
                                text="View All", \
                                width=12, \
                                command=self.view)
        self.view_button.grid(row=5, column=15)

        self.search_button = Button(window, \
                                    text="Search Entry", \
                                    width=12, \
                                    command=self.search)
        self.search_button.grid(row=6, column=15)

        self.add_button = Button(window, \
                                    text="Add Entry", \
                                    width=12, \
                                    command=self.insert)
        self.add_button.grid(row=7, column=15)

        self.update_button = Button(window, \
                                    text="Update Selected", \
                                    width=12,\
                                    command=self.update)
        self.update_button.grid(row=8, column=15)

        self.delete_button = Button(window, \
                                    text="Delete Selected", \
                                    width=12, \
                                    command=self.delete)
        self.delete_button.grid(row=9, column=15)

        self.close_button = Button(window, \
                                    text="Close", \
                                    width=12, \
                                    command=self.close_click)
        self.close_button.grid(row=10, column=15)

        # create space areas:
        self.spacing1 = Label(window, text="")
        self.spacing1.grid(row=11, column=14)

        self.spacing2 = Label(window, text="")
        self.spacing2.grid(row=8, column=11)

        self.spacing3 = Label(window, text="")
        self.spacing3.grid(row=8, column=12)

        self.spacing4 = Label(window, text="")
        self.spacing4.grid(row=0, column=0)
        
    # Define all the functions:
    def get_selected_row(self, event):
        index = self.view_box.curselection()
        self.selected_tuple = self.view_box.get(index)
        self.title_box.delete(0,END)
        self.title_box.insert(END, self.selected_tuple[1])
        self.producer_box.delete(0,END)
        self.producer_box.insert(END, self.selected_tuple[2])
        self.year_box.delete(0,END)
        self.year_box.insert(END, self.selected_tuple[3])
        self.director_box.delete(0,END)
        self.director_box.insert(END, self.selected_tuple[4])

    def view(self):
        self.view_box.delete(0,END)
        for row in database.view():
            self.view_box.insert(END,row)

    def insert(self):
        database.insert(self.title_box.get(), \
                        self.producer_box.get(), \
                        self.year_box.get(), \
                        self.director_box.get())
        self.view_box.delete(0,END)
        self.view_box.insert(END,(self.title_value.get(), \
                                self.producer_value.get(), \
                                self.year_value.get(), \
                                self.director_value.get()))
        messagebox.showinfo("Saved Successfully", "The book was saved successfully")

    def delete(self):
        answer = messagebox.askokcancel("Warning","You are about to delete the chosen book. \
                                Press 'OK' if you want to delete it or Cancel to end.")
        if answer:
            self.view_box.delete(0,END)
            database.delete(self.selected_tuple[0])
            self.view_box.insert(END,(self.title_value.get(), \
                                        self.producer_value.get(), \
                                        self.year_value.get(), \
                                        self.director_value.get()))
            messagebox.showinfo("Delete Successful", "The book was deleted successfully")
        else:
            pass

    def update(self):
        self.view_box.delete(0,END)
        database.update(self.selected_tuple[0], \
                        self.title_value.get(), \
                        self.producer_value.get(), \
                        self.year_value.get(), \
                        self.director_value.get())
        self.view_box.insert(END,(self.title_value.get(), \
                                    self.producer_value.get(), \
                                    self.year_value.get(), \
                                    self.director_value.get()))
        messagebox.showinfo("Update Successfully", "The book was updated successfully")

    def search(self):
        self.view_box.delete(0,END)
        for row in database.search(str(self.title_value.get()), \
                                    str(self.producer_value.get()), \
                                    str(self.year_value.get()), \
                                    str(self.director_value.get())):
            self.view_box.insert(END,row)
        rows = self.view_box.get(0,END)
        if len(rows) == 0:
            messagebox.showerror("Error", "No matches to your search")

    def close_click(self):
        self.window.destroy()
        self.parent.deiconify()