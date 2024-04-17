from customtkinter import *
import requests
import os
from PIL import Image
from api import fetchData
from api import fetchSimilar
from io import BytesIO

def runApp():
    app = CTk()
    app.geometry("500x700")

    
    
    
    def displayData(movie_name, description, poster_image, movie_id):
        base_url = "https://image.tmdb.org/t/p/w500"  # Replace with the actual base URL
        full_url = base_url + poster_image

        # Download the image
        response = requests.get(full_url)
        img_data = response.content

        recommended_label = CTkLabel(app, text="Recommended Films:", font=("Nexa Heavy", 12))
        recommended_label.place(x=30, y=470) 

        # Open the image
        img = Image.open(BytesIO(img_data))

        poster = CTkImage(img, size=(250, 364))

        posterLabel = CTkLabel(app, image=poster, text="")
        posterLabel.place(x=30, y=105)

        synopsisframe = CTkFrame(app, width=175, height=360)
        synopsisframe.pack_propagate(0)  # Prevent frame from changing size

        synopsislabel = CTkLabel(master=synopsisframe, text=f"{movie_name}\n\n{description}", font=("Nexa Heavy", 12), wraplength=160, anchor="w", justify="left")
        synopsislabel.pack()
        synopsisframe.place(x=300, y=105)
        
        # Recommendations
        recommended = fetchSimilar(movie_id)
        print(recommended)

        # Add poster images
        def button1_handler():
            movie_name, description, poster_image, movie_id = fetchData(recommended[0][0])
            displayData(movie_name, description, poster_image, movie_id)
            pass

        def button2_handler():
            movie_name, description, poster_image, movie_id = fetchData(recommended[1][0])
            displayData(movie_name, description, poster_image, movie_id)
            pass

        def button3_handler():
            movie_name, description, poster_image, movie_id = fetchData(recommended[2][0])
            displayData(movie_name, description, poster_image, movie_id)
            pass

        def button4_handler():
            movie_name, description, poster_image, movie_id = fetchData(recommended[3][0])
            displayData(movie_name, description, poster_image, movie_id)
            pass
        
        # Displays the recommended movie's posters
        poster1 = CTkImage(Image.open(BytesIO(requests.get("https://image.tmdb.org/t/p/w500" + recommended[0][1]).content)), size=(99, 165))
        poster1_label = CTkLabel(app, image=poster1, text="")
        poster1_label.place(x=30, y=500)
        poster1_button = CTkButton(app, text="See More", font=("Nexa Heavy", 10), command=button1_handler, width=99, height=20)
        poster1_button.place(x=30, y=673)

        poster2 = CTkImage(Image.open(BytesIO(requests.get("https://image.tmdb.org/t/p/w500" + recommended[1][1]).content)), size=(99, 165))
        poster2_label = CTkLabel(app, image=poster2, text="")
        poster2_label.place(x=144, y=500)
        poster2_button = CTkButton(app, text="See More", font=("Nexa Heavy", 10), command=button2_handler, width=99, height=20)
        poster2_button.place(x=144, y=673)

        poster3 = CTkImage(Image.open(BytesIO(requests.get("https://image.tmdb.org/t/p/w500" + recommended[2][1]).content)), size=(99, 165))
        poster3_label = CTkLabel(app, image=poster3, text="")
        poster3_label.place(x=258, y=500)
        poster3_button = CTkButton(app, text="See More", font=("Nexa Heavy", 10), command=button3_handler, width=99, height=20)
        poster3_button.place(x=258, y=673)

        poster4 = CTkImage(Image.open(BytesIO(requests.get("https://image.tmdb.org/t/p/w500" + recommended[3][1]).content)), size=(99, 165))
        poster4_label = CTkLabel(app, image=poster4, text="")
        poster4_label.place(x=372, y=500)
        poster4_button = CTkButton(app, text="See More", font=("Nexa Heavy", 10), command=button4_handler, width=99, height=20)
        poster4_button.place(x=372, y=673)
        return 0


    def click_handler():
        print(entry.get())
        movie_name, description, poster_image, movie_id = fetchData(entry.get())
        displayData(movie_name, description, poster_image, movie_id)
    
    #logo = CTkImage(Image.open("kinorecs.png"), size=(200, 200))
    #logo.place(x=150, y=0)
        
    label = CTkLabel(app, text="Enter the name of the movie", font=("Nexa Heavy", 20))
    label.place(x=30, y=30)

    entry = CTkEntry(app, placeholder_text="Enter movie name here...", width=300, font=("Nexa Heavy", 15))
    btn = CTkButton(app, text="Search", command=click_handler, font=("Nexa Heavy", 15))

    entry.place(x=30, y=65)
    btn.place(x=340, y=65)

    app.mainloop()




