from customtkinter import *
import requests
import os
from PIL import Image
from api import fetchData

from io import BytesIO

def runApp():
    app = CTk()
    app.geometry("500x700")

    poster1 = CTkLabel(app, text="Interstellar", font=("Nexa Heavy", 12))
    if poster1.winfo_width() > 75:
        poster1.place(x=30, y=530)
    else:
        poster1.place(x=30, y=500)

    poster2 = CTkLabel(app, text="Dune Part 2", font=("Nexa Heavy", 12))
    if poster2.winfo_width() > 75:
        poster2.place(x=145, y=530)
    else:
        poster2.place(x=145, y=500)

    poster3 = CTkLabel(app, text="2001", font=("Nexa Heavy", 12))
    if poster3.winfo_width() > 75:
        poster3.place(x=275, y=530)
    else:
        poster3.place(x=275, y=500)

    poster4 = CTkLabel(app, text="Blade Runner", font=("Nexa Heavy", 12))
    if poster4.winfo_width() > 75:
        poster4.place(x=395, y=530)
    else:
        poster4.place(x=395, y=500)

    # Add poster images
    def button1_handler():
        movie_name, description, poster_image = fetchData("interstellar")
        displayData(movie_name, description, poster_image)
        pass

    def button2_handler():
        movie_name, description, poster_image = fetchData("dune part 2")
        displayData(movie_name, description, poster_image)
        pass

    def button3_handler():
        movie_name, description, poster_image = fetchData("2001: a space odyssey")
        displayData(movie_name, description, poster_image)
        pass

    def button4_handler():
        movie_name, description, poster_image = fetchData("Blade runner")
        displayData(movie_name, description, poster_image)
        pass
    
    
    recommended_label = CTkLabel(app, text="Recommended Films:", font=("Nexa Heavy", 12))
    recommended_label.place(x=30, y=480)
    
    
    poster1_img = Image.open(os.path.join(os.path.dirname(__file__), "posters", "interstellar.jpg"))
    poster1 = CTkImage(poster1_img, size=(75, 109))
    poster1_label = CTkLabel(app, image=poster1, text="")
    poster1_label.place(x=30, y=530)
    poster1_button = CTkButton(app, text="See More", font=("Nexa Heavy", 10), command=button1_handler, width=75)
    poster1_button.place(x=30, y=650)

    poster2_img = Image.open(os.path.join(os.path.dirname(__file__), "posters", "dunepart2.jpg"))
    poster2 = CTkImage(poster2_img, size=(75, 109))
    poster2_label = CTkLabel(app, image=poster2, text="")
    poster2_label.place(x=145, y=530)
    poster2_button = CTkButton(app, text="See More", font=("Nexa Heavy", 10), command=button2_handler, width=75)
    poster2_button.place(x=145, y=650)

    poster3_img = Image.open(os.path.join(os.path.dirname(__file__), "posters", "spaceodyssey.jpg"))
    poster3 = CTkImage(poster3_img, size=(75, 109))
    poster3_label = CTkLabel(app, image=poster3, text="")
    poster3_label.place(x=275, y=530)
    poster3_button = CTkButton(app, text="See More", font=("Nexa Heavy", 10), command=button3_handler, width=75)
    poster3_button.place(x=275, y=650)

    poster4_img = Image.open(os.path.join(os.path.dirname(__file__), "posters", "bladerunner.jpg"))
    poster4 = CTkImage(poster4_img, size=(75, 109))
    poster4_label = CTkLabel(app, image=poster4, text="")
    poster4_label.place(x=395, y=530)
    poster4_button = CTkButton(app, text="See More", font=("Nexa Heavy", 10), command=button4_handler, width=75)
    poster4_button.place(x=395, y=650)
    
    
    def displayData(movie_name, description, poster_image):
        base_url = "https://image.tmdb.org/t/p/w500"  # Replace with the actual base URL
        full_url = base_url + poster_image

        # Download the image
        response = requests.get(full_url)
        img_data = response.content

        # Open the image
        img = Image.open(BytesIO(img_data))


        #"C:/Users/santi/OneDrive/Documents/1-Classes Documents/VS Code/MovieRecApp/posterTest.jpg"
        #img = Image.open(imgPath)
        poster = CTkImage(img, size=(250, 364))

        posterLabel = CTkLabel(app, image=poster, text="")
        posterLabel.place(x=30, y=120)

        synopsisframe = CTkFrame(app, width=175, height=360)
        synopsisframe.pack_propagate(0)  # Prevent frame from changing size

        synopsislabel = CTkLabel(master=synopsisframe, text=description, font=("Nexa Heavy", 13), wraplength=160, anchor="w", justify="left")
        synopsislabel.pack()
        synopsisframe.place(x=300, y=120)
        return 0


    def click_handler():
        print(entry.get())
        movie_name, description, poster_image = fetchData(entry.get())
        displayData(movie_name, description, poster_image)
        
    label = CTkLabel(app, text="Enter the name of the movie", font=("Nexa Heavy", 20))
    label.place(x=30, y=45)

    entry = CTkEntry(app, placeholder_text="Enter movie name here...", width=300, font=("Nexa Heavy", 15))
    btn = CTkButton(app, text="Search", command=click_handler, font=("Nexa Heavy", 15))

    entry.place(x=30, y=80)
    btn.place(x=340, y=80)

    app.mainloop()




