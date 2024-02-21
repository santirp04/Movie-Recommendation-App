from customtkinter import *
import requests
from PIL import Image
from api import fetchData

from io import BytesIO

def runApp():
    app = CTk()
    app.geometry("500x500")


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




