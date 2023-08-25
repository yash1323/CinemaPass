#!/usr/bin/env python
# coding: utf-8

# In[6]:


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk
from pathlib import Path
import json
from datetime import date
import copy

def bill(nw7,session_info,name,ticket,show,phone,dir_movie_info):
    
    
    #this blocks deletes all seats with empty strings in it 
    temp_session_info = session_info.copy()
    for key1 in temp_session_info["seat"]:
        for key2 in list(temp_session_info["seat"][key1]["matrix"]):
            if temp_session_info["seat"][key1]["matrix"][key2] == "":
                del session_info["seat"][key1]["matrix"][key2]    
    #this line creates ticket to be made to printed out 
    ticket.update(session_info)

    dir_ticket = Path(dir_movie_info).parent.parent.parent / 'Tickets'
    
    
    #this updates the show dictionary and makes it ready to be written off in the 1000.json or whatever
    for seat_type, seat_data in ticket['seat'].items():
        if seat_type in show['seat']:
            show['seat'][seat_type]['matrix'].update(seat_data['matrix'])
    
    #dir_movie_info is 1000.json file dir in string
    with open(dir_movie_info, 'w+') as f:
        json.dump(show, f)
        
    # Get the file path
    dir_ticket = dir_ticket / (phone+'.json')
    
    # Check if the file already exists and if it does append numbers at the end
    if dir_ticket.exists():
        i = 1
        while (new_file_path := Path(f"Tickets/{phone}-{i}.json")).exists():
            i += 1
        dir_ticket = new_file_path
        
    print(dir_ticket)
    print("final ticket before printing it to phone_number.json")
    print(ticket)
    # Create the ticket.json file
    with dir_ticket.open("w") as f:
        json.dump(ticket, f)
    
def seat(nw6,film,screen,time,name,phone,dir_movie_info):    
    #clear screen
    nw6.title(time)
    for widget in nw6.winfo_children():
        widget.destroy()
        
    print(film)
    print(screen)
    print(time)
    
    with open(film["screen"][screen]['shows'][time] ,'r+')as f:
        show = json.load(f)
        
    if(film["name"]==show["film"]):
        f = Frame(nw6,bg="black")
        
        session_info=dict()
        session_info['seat']={}
        session_info['seat']= copy.deepcopy(show['seat'])        
        
        ticket={}
        ticket.update({"name":name,'phone':phone,'screen':screen,'film':film['name']})
      
        for i in show['seat'].keys():
            for j in show['seat'][i]['matrix'].keys():
                session_info['seat'][i]['matrix'][j]=''
                
        

        for i in show["seat"].keys():
            Label(f,text=i+"="+str(show["seat"][i]["price"])+"\n", font=('Helvetica',20)).pack(pady=100)
            for j in show["seat"][i]["matrix"].keys():
                seat_state = DISABLED if show['seat'][i]['matrix'][j] else NORMAL

                def button_command(button=None):
                    button.configure(state=DISABLED)

                button = Button(f, text=j, bg='gold', state=seat_state, width='5', height='5')
                button.configure(command=lambda button=button,seat_type=i,seat_no=j:(session_info['seat'][seat_type]['matrix'].update({seat_no: name}), button_command(button=button)))
                button.pack(side=LEFT, padx=10)
        Button(nw6, text="submit", command=lambda session_info=session_info, show=show, ticket=ticket: bill(nw6, session_info, name, ticket, show,phone,dir_movie_info)).pack(side=BOTTOM, pady=(0,70))
        f.pack()
    else:
        print("movie name in movie-info.json and movie name in screens/....json does not match")
        
def show(nw4,film,name,phone):
#     film = str(film)
    #clear screen
    for widget in nw4.winfo_children():
        widget.destroy()
        
    nw4.title(film)
    today = date.today()
    with open(film / "Movie-info.json" ,'r+')as f:
        film = json.load(f)
        
    
    for i in film['screen']:
        Label(nw4,text= "Screen : " + i , font=('Helvetica',20)).pack(pady=100)
        for j in film['screen'][i]['shows']:
            ttk.Button(nw4, text=j, command=lambda i=i,j=j: seat(nw4,film,i,j,name,phone,film['screen'][i]['shows'][j])).pack(pady=20)
        
def NextScreen(nw1,path,name,phone):
    
    
    for widget in nw1.winfo_children():
        widget.destroy()
        
    films = path / 'Films'

    # Get the names of directories in the specified directory
    dirs = [x for x in films.iterdir() if x.is_dir()]
        
    Label(nw1,text="Click on image to book tickets !!", font=('Helvetica',20)).pack(pady=20)
    canvas = Canvas(nw1, width = 1000, height = 800).pack(expand=YES)
    
    print([x for x in films.iterdir() if x.is_dir()])
    
    padding = 20
    for i in [x for x in films.iterdir() if x.is_dir()]:
        photo = ImageTk.PhotoImage(Image.open(i / 'Poster.jpeg').resize((500,750)))
        poster = ttk.Button(canvas,text=i,image= photo)
        poster.image=photo
        poster.place(x = padding , y = 70)
        padding+=photo.width()
        poster.bind("<Button-1>", lambda event,i=i: show(nw1,i,name,phone))

def validate_phone(nw2,path,phone_number,uname):
    if phone_number.get().isdigit() and len(phone_number.get()) == 10:
        if uname.get() != '':
            name = uname.get()
            phone = phone_number.get()
            NextScreen(nw2,path,name,phone)
        else:        
            messagebox.showinfo("Alert", "Not Valid Name", icon="warning")
    else:
        messagebox.showinfo("Alert", "Not Valid Phone Number", icon="warning")
    
def home(nw3):
    # Get the current working directory
    path = Path(".")
    
    nw3.title("CinemaPass : Your one stop for faster tickets")
    nw3.geometry("700x700")
    nw3.state('zoomed')
    nw3.iconbitmap(path / 'icon-low.ico')

    image = Image.open(path / 'icon-high.png')
    resized_image= image
    photo = ImageTk.PhotoImage(resized_image)
    i1 = Label(nw3,image=photo)
    i1.image = photo
    i1.pack(side=LEFT, padx=(200,0))
    
    credentials = Canvas(nw3)
    
    Label(credentials,text="Enter your name", font=('Helvetica',20)).pack(pady=20)
    uname= Entry(credentials,width=20)
    uname.pack()
    Label(credentials,text="Enter your phone number", font=('Helvetica',20)).pack(pady=20)
    phone_number = Entry(credentials, width=20)
    phone_number.pack()
    Button(credentials, text="Submit", command=lambda:validate_phone(nw3,path,phone_number,uname)).pack(pady=23)
    credentials.pack(side=RIGHT,padx=(0,300))
    
window = Tk()

home(window)
window.mainloop()

