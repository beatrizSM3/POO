
from customtkinter import *
from tkintermapview import TkinterMapView
from tkinter import Listbox,END
from database import DataBase
import geocoder


class Map:
    set_appearance_mode("Dark")
    def __init__(self):
        self.db=DataBase()
        
        self.local = geocoder.ip('me')

        self.window=CTk()
        self.window.geometry("880x520+250+80")
        self.window.title("GEOLOCALIZATION")
        self.font_sans=("Calibri",15)
        self.frame()
        self.change_frame_page1()
        self.label()
        self.map_background()
        self.entry()
        self.buttons_frame1()
        #self.scrollbar()
        self.window.mainloop()


    def get_button(self,btn):
        if btn=="find":
            address_find=entry_address.get()
            if address_find:
                self.map_find()
                
                marker_1 = map_find.set_address(self.local.city, marker=True)  
                marker_2=map_find.set_address(address_find, marker=True)     
                #print(marker_1.position, marker_2.position)  
            
                marker_1.set_text(self.local.city)   #self.local.city
                marker_2.set_text(address_find)   #adress_find
                path = map_find.set_path([marker_1.position, marker_2.position])
         
                map_find.pack(fill='both',expand=True)
                self.buttons_frame2()
                btn_back.place(x=810,y=20)
                self.change_frame_page2()
                

        elif btn=="delete":
            value=list_box.curselection()
            address=list_box.get(value)
            self.db.delete(address)
            list_box.delete(value)
          

        elif btn=="go":
            value=list_box.curselection()
            place=list_box.get(value)
            if place:
                map_widget.set_address(place)
        
        elif btn=="back":
            self.change_frame_page1()
       
            map_find.destroy()
           
            
            
        elif btn=="save":
               
            self.list_box()
            
            address_save=entry_save.get() 
            if address_save:
                self.db.adicionar(address_save)
            lista=self.db.select()
            
            if lista:
                for address in lista:
                    list_box.insert(END,address)     
               
            else:
                print(address_save)
                list_box.insert(END,address_save)
        

    def frame(self):
        global frame_page1,frame_page2
        frame_page1=CTkFrame(master=self.window,width=900,height=520,corner_radius=0)    
        frame_page2=CTkFrame(master=self.window,width=900,height=520)

    def scrollbar(self):
        global scrollbar
        scrollbar=Scrollbar(frame_page1,orient="vertical",bg="#0F0F0F",troughcolor="blue")
        

    def list_box(self):
        global list_box
        list_box=Listbox(label_saved,relief=None,bg="#1B1A1B",selectbackground="#0F0F0F",bd=0,font=self.font_sans,highlightthickness = 0,height=430,fg="#F0F0F1")
        print(list_box)

        list_box.place(x=30,y=40)   

    #CHANGES BETWEEN PAGES (FRAMES)
    def change_frame_page2(self):
        frame_page2.pack(fill='both',expand=True)
        frame_page1.pack_forget()

    def change_frame_page1(self):
        frame_page1.pack(fill='both',expand=True)
        frame_page2.pack_forget()

    def map_background(self):
        global map_widget
        map_widget = TkinterMapView(label_map, width=500, height=300,corner_radius=10)
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga")
        map_widget.set_address(self.local.city)
        map_widget.place(relx=0.5, rely=0.5, anchor="center")


    def map_find(self):
        global map_find

        map_find=TkinterMapView(frame_page2, width=900,height=550)
        map_find.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga")

      
    def label(self):
        global label_map,label_saved
        ##CECECF

        label_map=CTkLabel(master=frame_page1,text=None,fg_color="#1B1A1B", width=550, height=350,corner_radius=20)
            
        label_map.place(x=300,y=40)

        label_saved=CTkLabel(master=frame_page1,text="Favorite Places",fg_color="#1B1A1B", width=250, height=450,corner_radius=20,text_font=self.font_sans,anchor="w")
          
        label_saved.place(x=30,y=40)


    def entry(self):
        global entry_save,entry_address
        entry_address=CTkEntry(master=frame_page1,placeholder_text="Find Address",fg_color="#FEFFFE", border_color="#FEFFFE",corner_radius=10, width=150, height=30,text_color="#262A33")
        entry_save=CTkEntry(master=frame_page1,placeholder_text="Save Address",corner_radius=10,fg_color="#FEFFFE", border_color="#FEFFFE", width=150, height=30, text_color="#262A33")

        entry_address.place(x=400, y=420)
        entry_save.place(x=600, y=420)

    def buttons_frame1(self):
        global btn_find,btn_save

        #creating buttons at frame 1
        btn_find=CTkButton(master=frame_page1,text="Find Place",width=150,height=30,corner_radius=10,fg_color="#010001",text_color='#F0F1F0',hover_color="#1A1C1D",command=lambda which="find": self.get_button(which))
        btn_save=CTkButton(master=frame_page1,text="Save Place",width=150,height=30,corner_radius=10,fg_color="#010001",text_color='#F0F1F0',hover_color="#1A1C1D",command= lambda which="save": self.get_button(which))
        btn_delete=CTkButton(master=frame_page1,text="X", width=20, corner_radius=0,text_color="red",fg_color="#1B1A1B",hover_color=None,command=lambda which="delete": self.get_button(which))
        btn_go=CTkButton(master=frame_page1,text="FIND",width=20,corner_radius=0,text_color="green",fg_color="#1B1A1B",hover_color=None,command=lambda which="go": self.get_button(which))
       
        #placing buttons with place()
        btn_delete.place(x=240,y=50)
        btn_go.place(x=240,y=450)
        btn_find.place(x=400,y=460)
        btn_save.place(x=600,y=460)


    def buttons_frame2(self):
        global btn_back
        btn_back=CTkButton(master=frame_page2,text="Back",width=50,height=30,corner_radius=10,fg_color="#010001",text_color='#F0F1F0',hover_color="#1A1C1D", command=lambda which="back":self.get_button(which))


map=Map()

    




