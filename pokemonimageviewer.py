from tkinter import *
from tkinter import ttk
from library import download_image_from_url
from library import set_desktop_background_image
from pokeapi import get_pokemon_list, get_pokemon_image_url
import sys
import os
import ctypes


def main():
    
    script_dir = sys.path[0]

    # Create directory for images to be stored
    image_dir = os.path.join(script_dir, 'images')
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)
    

    # Create window
    root = Tk()
    root.title('Pokemon Image Viewer')

    # Add icons to window and taskbar
    app_id = 'pokemon.image-viewer'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    root.iconbitmap(os.path.join(script_dir, 'ultraball.ico'))
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.minsize(500, 600)


    # Create the frame
    frm = ttk.Frame(root)
    frm.grid(sticky=(N,S,E,W))
    frm.rowconfigure(0,weight=10)
    frm.rowconfigure(1,weight=0)
    frm.rowconfigure(2,weight=0)
    frm.columnconfigure(0,weight=1)

    
    # Create default image
    img_poke = PhotoImage(file = os.path.join(script_dir, 'pokeball.png'))
    lbl_img = ttk.Label(frm, image=img_poke)
    lbl_img.grid(row=0, column=0, padx=10, pady=10)

    # Create combo box
    pokemon_list = get_pokemon_list()
    pokemon_list.sort()
    pokemon_list=[p.capitalize() for p in pokemon_list]
    cbo_pokemon = ttk.Combobox(frm, values=pokemon_list, state='readonly')
    cbo_pokemon.set('Select a Pokemon')
    cbo_pokemon.grid(row=1, column=0, padx=10, pady=10)

    def handle_poke_select(event):
        """
        Adds image of selected pokemon into created image folder
        :param event: place holder to make the function run
        :returns: .png file added to images folder
        """
        pokemon_name = cbo_pokemon.get()
        image_url = get_pokemon_image_url(pokemon_name)
        image_path = os.path.join(image_dir, pokemon_name + '.png')
        download_image_from_url(image_url, image_path)
        img_poke['file'] = image_path
        btn_set_desktop.state(['!disabled'])
        
    # Changes default image to selected image
    cbo_pokemon.bind('<<ComboBoxSelected>>', handle_poke_select)


    def handle_btn_set_desktop():
        """
        Event handler function for button click event 
        :returns: changes background to selected image
        """
        pokemon_name = cbo_pokemon.get()
        image_path = os.path.join(image_dir, pokemon_name + '.png')
        set_desktop_background_image(image_path)

    # Create button
    btn_set_desktop = ttk.Button(frm, text='Set as Desktop Image', command= handle_btn_set_desktop)
    btn_set_desktop.state(['disabled'])
    btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)
    


    root.mainloop()

main()