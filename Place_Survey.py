import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



#*In this version of the code I have improved the aesthetics of my program by adding a border to the frame and adding background colors to make it look it better.


#*This is the list that is going to be used in the first dropdown box
city_prt = [
    "Select Area",
    "Central Auckland",
    "North Auckland",
    "South Auckland",
    "East Auckland",
    "West Auckland"
]

#*This is the list that will be used for the second dropdown box if the user picks North Auckland
nrth_city_prt = [
    "Select Suburb",
    "Albany",
    "Beach Haven",
    "Northcote",
    "Castor Bay",
    "Glenfield",
    "Takapuna"
]

#*This is the list that will be used for the second dropdown box if the user picks South Auckland
sth_city_prt = [
    "Select Suburb",
    "Botany Downs",
    "East Tamaki",
    "Flat Bush",
    "Ormiston",
]

#*This is the list that will be used for the second dropdown box if the user picks West Auckland
wst_city_prt = [
    "Select Suburb",
    "Henderson",
    "Massey",
    "New Lynn",
    "Swanson"
]

#*This is the list that will be used for the second dropdown box if the user picks East Auckland
est_city_prt = [
    "Select Suburb",
    "Mission Bay",
    "Point Chevalier",
    "Penrose"
]

#*This is the list that will be used for the second dropdown box if the user picks Central Auckland
cent_city_prt = [
    "Select Suburb",
    "Epsom",
    "Mount Albert",
    "Mount Roskill/Hillsbrough",
    'St Lukes',
]

#*This function will make it so that user will get different results for the second drop box, in terms of what they choose from the first
def pick_suburb(e):
    if dp_1.get() == "Central Auckland":
        dp_2.config(value = cent_city_prt)
        dp_2.current(0)

    if dp_1.get() == "North Auckland":
        dp_2.config(value = nrth_city_prt)
        dp_2.current(0)
    
    if dp_1.get() == "South Auckland":
        dp_2.config(value = sth_city_prt)
        dp_2.current(0)

    if dp_1.get() == "West Auckland":
        dp_2.config(value = wst_city_prt)
        dp_2.current(0)

    if dp_1.get() == "East Auckland":
        dp_2.config(value = est_city_prt)
        dp_2.current(0)

    if dp_1.get() == "Select Area":
            dp_2.config(value = ["Select Suburb"])
            dp_2.current(0)

def show_place():#*this is the function that will determine how the messagebox will show up in terms of what is picked from the second drop box or if nothing is selected from the first drop box 
    if dp_1.get() == "Select Area":
        messagebox.showinfo(title = "ERROR!", message = "Pick a Area")

    if dp_2.get() == "Select Suburb":
        messagebox.showinfo(title = "ERROR!", message = "Pick A Suburb")

    if dp_2.get() == "Albany":
        messagebox.showinfo(title = "Locations To Study", message = "Columbus Coffee:"+"\n"+"Address: 219 Don Mckinnon Drive Westfield, Albany, Auckland 0632"+"\n"+"Phone: 09 441 6475"+"\n"+"\n"+"Scholars Cafe:"+"\n"+"Address: Massey University Gate 1, next to Recreation Centre, Albany Expressway, Albany, Auckland 0632"+"\n"+"Phone: 09 415 6485"+"\n"+"\n"+"The Coffee Club Albany:"+"\n"+"Address: Shop S265B, Shop S265B/219 Don McKinnon Drive, Albany, Auckland 0632"+"\n"+"Phone: 09 443 2763")

    if dp_2.get() == "Beach Haven":
        messagebox.showinfo(title = "Locations To Study", message = "The Haven:"+"\n"+"Address: 366 Rangatira Road, Beach Haven, Auckland 0626"+"\n"+"Phone: 0274 474 471"+"\n"+"\n"+"Fika with Me:"+"\n"+"Address: 5 Birkenhead Avenue, Birkenhead, Auckland 0626"+"\n"+"Phone: 09 418 5508"+"\n"+"\n"+"Fabric Cafe Bistro:"+"\n"+"Address: 8 Boundary Road, Hobsonville, Auckland 0618"+"\n"+"Phone: 09 416 8013")

    if dp_2.get() == "Northcote":
        messagebox.showinfo(title = "Locations To Study", message = "The Glasshouse Cafe:"+"\n"+"Address: 7/3 Akoranga Drive, Northcote, Auckland 0627"+"\n"+"Phone: 09 419 5652")

    if dp_2.get() == "Castor Bay":
        messagebox.showinfo(title = "Locations To Study", message = "Fact-Tree:"+"\n"+"Address: 1/24 Tonkin Drive, Sunnynook, Auckland 0630"+"\n"+"Phone: 09 410 7617"+"\n"+"\n"+"The Great Cafe:"+"\n"+"Address: Shop8/120 Sunnynook Road, Sunnynook, Auckland 0620"+"\n"+"Phone: 09 410 4270"+"\n"+"\n"+"VIBE Coffee Roasters:"+"\n"+"Address: 1/15 Porana Road, Wairau Valley, Auckland 0627"+"\n"+"Phone: 0800 652 701")

    if dp_2.get() == "Glenfield":
        messagebox.showinfo(title = "Locations To Study", message = "Little Things Coffee Shop & Micro-Roastery:"+"\n"+"Address: Glenfield Mall Shop 502C, Level 5/385 Glenfield Road, Glenfield, Auckland 0629"+"\n"+"Phone: 09 600 3210"+"\n"+"\n"+"The Coffee Club Glenfield:"+"\n"+"Address: Shop S201, Glenfield Road &, Downing Street, Glenfield, Auckland 0629"+"\n"+"Phone: 09 441 9062"+"\n"+"\n"+"Muffin Break:"+"\n"+"Address: Glenfield Road and, Downing Street, Glenfield, Auckland 0629"+"\n"+"Phone: 09 281 5042")

    if dp_2.get() == "Takapuna":
        messagebox.showinfo(title = "Locations To Study", message = "Starbucks Takapuna:"+"\n"+"Address: 50 Hurstmere Road, Takapuna, Auckland 0622"+"\n"+"Phone: 09 489 6770"+"\n"+"\n"+"The Library Cafe:"+"\n"+"Address: 7 The Strand, Takapuna, Beach 0622"+"\n"+"Phone: 09 489 2557"+"\n"+"\n"+"Jam Organic Cafe:"+"\n"+"Address: 33-45 Hurstmere Road, Takapuna, Auckland 0622"+"\n"+"Phone: 09 486 1600")

    if dp_2.get() == "Botany Downs":
        messagebox.showinfo(title = "Locations To Study", message = "Coffee and Tea Lovers - Botany:"+"\n"+"Address: 12e Amera Place Huntington Park, East Tāmaki, Auckland 2013"+"\n"+"Phone: 09 250 1510"+"\n"+"\n"+"The Cafe Botany Downs:"+"\n"+"Address: 501 Ti Rakau Drive, Golflands, Auckland 2013"+"\n"+"Phone: 09 274 7184")

    if dp_2.get() == "East Tamaki":
        messagebox.showinfo(title = "Locations To Study", message = "Esquires Cafe - East Tamaki:"+"\n"+"Address: 19 Cryers Road, East Tāmaki, Auckland 2013"+"\n"+"Phone: 09 274 0471"+"\n"+"\n"+"Hello Stranger:"+"\n"+"Address: 27a Smales Road, East Tāmaki, Auckland 2013"+"\n"+"Phone: 09 271 0302")        

    if dp_2.get() == "Flat Bush":
        messagebox.showinfo(title = "Locations To Study", message = "Texture Cafe:"+"\n"+"Address: 1 Arranmore Drive, Flat Bush, Auckland 2016"+"\n"+"Phone: 09 265 4364"+"\n"+"\n"+"Ormiston Cafe:"+"\n"+"Address: Shop#5/1 Bellingham Road, Flat Bush, Auckland 2019"+"\n"+"Phone: 09 215 5000")

    if dp_2.get() == "Ormiston":
        messagebox.showinfo(title = "Locations To Study", message = "Ormiston Cafe:"+"\n"+"Address: Shop#5/1 Bellingham Road, Flat Bush, Auckland 2019"+"\n"+"Phone: 09 215 5000"+"\n"+"\n"+"Journal Cafe:"+"\n"+"Address: 240 Ormiston Road, Flat Bush, Auckland 2019"+"Phone: 09 212 3638")

    if dp_2.get() == "Henderson":
        messagebox.showinfo(title = "Locations To Study", message = "Kreem Bake Cook:"+"\n"+"Address: 189-193 Universal Drive, Henderson, Auckland 0610"+"\n"+"Phone: 09 835 9221")

    if dp_2.get() == "Massey":
        messagebox.showinfo(title = "Locations To Study", message = "Scholars Cafe:"+"\n"+"Address: Massey University Gate 1, next to Recreation Centre, Albany Expressway, Albany, Auckland 0632"+"\n"+"Phone: 09 415 6485"+"\n"+"\n"+"")

    if dp_2.get() == "New Lynn":
        messagebox.showinfo(title = "Locations To Study", message = "Mt Atkinson coffee shop:"+"\n"+"Address: 44b Portage Road, New Lynn, Auckland 0600"+"\n"+"Phone: 09 827 6608"+"\n"+"\n"+"The Coffee Club LynnMall:"+"\n"+"Address: 3058 Great North Road, New Lynn, Auckland 0600"+"\n"+"Phone: 09 826 3155")

    if dp_2.get() == "Swanson":
        messagebox.showinfo(title = "Locations To Study", message = "Swanson Station Cafe:"+"\n"+"Address: 760 Swanson Road, Swanson, Auckland 0612"+"\n"+"Phone: 09 833 9999"+"\n"+"\n"+"Cafe Korero:"+"\n"+"Address: 474 Swanson Road, Ranui, Auckland 0612"+"\n"+"Phone: 09 833 6280")

    if dp_2.get() == "Mission Bay":
        messagebox.showinfo(title = "Locations To Study", message = "The Coffee Club Mission Bay:"+"\n"+"Address: 49/51 Tamaki Drive, Mission Bay, Auckland 1071"+"\n"+"Phone: 09 578 0299"+"\n"+"\n"+"Kiwiyo Mission Bay:"+"\n"+"Address: 95 Tamaki Drive, Mission Bay, Auckland 1071"+"\n"+"Phone: 09 521 6996")

    if dp_2.get() == "Point Chevalier":
        messagebox.showinfo(title = "Locations To Study", message = "The Pt Chev Beach Cafe"+"\n"+"Address: 506 Point Chevalier Road, Point Chevalier, Auckland 1022"+"\n"+"Phone: 09 815 6636")

    if dp_2.get() == "Penrose":
        messagebox.showinfo(title = "Locations To Study", message = "Espresso @ Work:"+"\n"+"Address: 8 Hugo Johnston Drive, Penrose, Auckland 1061"+"\n"+"Phone: 09 579 9955"+"\n"+"\n"+"central + kitchen:"+"\n"+"Address: Building 8/666 Great South Road, Ellerslie, Auckland 1051"+"\n"+"Phone: 09 579 9023")

    if dp_2.get() == "Epsom":
        messagebox.showinfo(title = "Locations To Study", message = "Cornwall Park Cafe:"+"\n"+"Address: Cornwall Park Pohutakawa Drive, Epsom, Auckland 1051"+"\n"+"Phone: 09 630 2888"+"\n"+"\n"+"NOTE Coffee & Eats:"+"\n"+"Address: 75 Great South Road, Epsom, Auckland 1051"+"\n"+"Phone: 09 524 4119")

    if dp_2.get() == "Mount Albert":
        messagebox.showinfo(title = "Locations To Study", message = "The Lodge Cafe:"+"\n"+"Address: 201 Carrington Road, Mount Albert, Auckland 1025"+"\n"+"Phone: 09 849 7464")

    if dp_2.get() == "Mount Roskill/Hillsbrough":
        messagebox.showinfo(title = "Locations To Study", message = "Deluxe Coffee and Kitchen:"+"\n"+"Address: 69 Carr Road, Mount Roskill, Auckland 1041"+"\n"+"Phone: 022 312 1839"+"\n"+"\n"+"Kreem Cafe Mount Roskill:"+"\n"+"Address: 4 Carr Road, Three Kings, Auckland 1042"+"\n"+"Phone: 09 624 1414")

    if dp_2.get() == "St Lukes":
        messagebox.showinfo(title = "Locations To Study", message = "The Coffee Club St Lukes:"+"\n"+"Address: Shop 450/80 Saint Lukes Road, Mount Albert, Auckland 1025"+"\n"+"Phone: 09 815 7000"+"\n"+"\n"+"Geeks on Sainsbury:"+"\n"+"Address: 1/55 Sainsbury Road, Mount Albert, Auckland 1025"+"\n"+"Phone: 09 845 4797")


window = tk.Tk()#*The code to generate a window
window.state("zoomed")#*This code makes the GUI page full-screen 
window.title("Place Survey")#*This code sets the windows title
window.configure(bg = "#E3F6F5")

inner_frame = tk.Frame(window, width = 1000, height = 550, bg = "#FFFFFE", highlightbackground = "#272343", highlightthickness = 2)
inner_frame.place(relx = 0.5, rely = 0.57, anchor = CENTER)

#*This is the code for the header
label = tk.Label(window, text = "PLACE SURVEY", font = ("Arial", 60, "bold"))
label.pack(padx = 20, pady = 20)
label.configure(bg = "#E3F6F5", fg = "#272343")

#*This is the text to ask the first question
text_1 = tk.Label(window, text = "What Part Of Auckland Do You Live In", font = ("Arial", 30))
text_1.pack(padx = 20, pady = 20)
text_1.configure(bg = "#FFFFFE", fg = "#272343")

#*This is the first drop box to ask users what part of auckland they live in
dp_1 = ttk.Combobox(window, values = city_prt, state = "readonly", font = ("Arial", 20))
dp_1.config(background = "#272343")
dp_1.current(0)
dp_1.pack(pady = 40)
dp_1.bind("<<ComboboxSelected>>", pick_suburb)

#*This is the text on top of the second drop down box to display the question on top of it
text_2 = tk.Label(window, text = "Which Suburb In Auckland Do You Live In Or Near", font = ("Arial", 30))
text_2.pack(padx = 20, pady = 20)
text_2.configure(bg = "#FFFFFE", fg = "#272343")

#*This is the second drop box to ask users what suburb in auckland they live in
dp_2 =ttk.Combobox(window, values = ["Select Suburb"], state = "readonly", font = ("Arial", 20))
dp_2.current(0)
dp_2.pack(pady = 40)

#*This is the button that will give a messagebox when pushed, showing results in terms of what is chosen by the users in the above drop down boxes
btn = tk.Button(window, text = "Get Locations To Study", font = ("Arial", 35), command = show_place)
btn.pack(padx = 20, pady = 20)



window.mainloop()