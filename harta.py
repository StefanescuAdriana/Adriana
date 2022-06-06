import pandas as pd
import folium
from geopy import Nominatim
import tkinter as tk
from tkinter import *
import webbrowser
import os
base=os.path.dirname(os.path.abspath(__file__))
df=pd.read_excel('data.xlsx')
loc = Nominatim(user_agent="myGeocoder")
# am creeat harta
m = folium.Map(location=[45.9432, 24.9668],type='OpenStreetMap', zoom_start=7)


# nume titlu si stil
name = " Calitatea aerului "
title = '<h2 align="center" style="background-color:#0080ff" style="font-size:20px"><b>{}</h2>'.format(name)
m.get_root().html.add_child(folium.Element(title))

mylist = df['Indicator'].tolist()
for i in range(len(mylist)):
    print("\n")
    print(mylist[i])



data = pd.DataFrame({
   'lon':[26.119589,23.581032,21.624355,24.969343,26.890523,21.951330,24.462865,26.633738,25.597141,27.874585,26.879803,21.898792,27.356590,23.668878,28.551263,26.011607,25.453440,23.758293,27.818343,25.882763,23.302778,25.574939,22.910256,27.082692, 27.209827,26.226931,23.662678,22.870217,24.701261,26.419871,24.323755,26.093871,22.834839,23.089780,24.114899,26.162729, 25.374389,21.270276,28.800632,27.728812,24.273787,27.202092],
   'lat':[44.409354,46.019415,46.225520,44.815766,46.510462,47.020893,47.121704,47.822863,45.626468,45.226549,45.116731,45.265581,44.210641,46.771364,44.186990,45.886259,44.858205,44.247246,45.753323,44.057073,45.006535,46.432248,45.735482,44.591251,47.236678,44.329409,47.566533,44.604936,46.637914,46.892426,44.165956,45.059379,47.665908,47.174072,45.768105,47.562907,43.948314,45.715091,45.01185,46.589941,45.076783,45.818082 ],
   'name':['Municipiul Bucuresti','Judetul Alba','judetul Arad','Judetul Arges','Bacau','Bihor','Bistrita','Botosani','Brasov','Braila','Buzau','Caras','Calarasi','Cluj','Constanta','Covasna','Dambovita','Dolj','Galati','Giurgiu','Gorj','Harghita','Hunedoara','Ialomita','Iasi','Ilfov','Maramures','Mehedinti','Mures','Neamt','Olt','Prahova','Satu Mare','Salaj','Sibiu','Suceava','Teleorman','Timis','Tulcea','Vaslui','Valcea','Vrancea'],
   'value':[10, 12, 40, 70, 23, 43, 100, 43, 45, 43,89,64,234,68,90,86,44,33,45,56,78,45,6,7,87,5,4,3,5,67,8,65,4,234,5,43,456,78,45,65,76,34],
   'indicator':mylist,
}, dtype=str)


data
for i in range(0,len(data)):
   folium.Marker(
    location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
    popup=[data.iloc[i]['name'], data.iloc[i]['indicator']],
    html='<div style="font-size: 13pt"><b></b><br><br>''</div>',

    ).add_to(m)





m.save('index.html')


url = 'index.html'
window = tk.Tk()
window.title("Interfata grafica")
window.geometry("250x100")
window.configure(bg='blue')
frame = Frame(window)
frame.pack()

def OpenUrl(url):
   webbrowser.open_new(url)
button = tk.Button(window, text="Deschide harta ", command=lambda aurl=url:OpenUrl(aurl), bg="red")
button2 = tk.Button(window, text="Inchide fereastra", bg="red", command=window.destroy)
button.pack(pady=5)
button2.pack(pady=5)
window.mainloop()