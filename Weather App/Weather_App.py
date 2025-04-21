from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city= city_name.get()
    #Here you need to input your API KEY of (open weather api) to start using app
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid={API KEY}").json()
    info11.config(text =data["weather"][0]["main"])
    info22.config(text =data["weather"][0]["description"])
    info33.config(text = str(int(data["main"]["temp"]-273.15)))
    info44.config(text = data["main"]["pressure"])

win = Tk()
win.title("Weather App")
win.config(bg="yellow")
win.geometry("500x500")

name_label  =Label(win,text='Weather App Python',font=('Times New Roman',30,'bold'))
name_label.place(x=25,y=50,height=50,width=450)

# Pakistan Cities only for dropdown
list_name = [
    "Ahmadpur East",
    "Ahmed Nager Chatha",
    "Ali Khan Abad",
    "Alipur",
    "Arifwala",
    "Attock",
    "Bhera",
    "Bhalwal",
    "Bahawalnagar",
    "Bahawalpur",
    "Bhakkar",
    "Burewala",
    "Chenab Nagar",
    "Chillianwala",
    "Choa Saidanshah",
    "Chakwal",
    "Chak Jhumra",
    "Chichawatni",
    "Chiniot",
    "Chishtian",
    "Chunian",
    "Dajkot",
    "Daska",
    "Davispur",
    "Darya Khan",
    "Dera Ghazi Khan",
    "Dhaular",
    "Dina",
    "Dinga",
    "Dhudial Chakwal",
    "Dipalpur",
    "Faisalabad",
    "Fateh Jang",
    "Ghakhar Mandi",
    "Gojra",
    "Gujranwala",
    "Gujrat",
    "Gujar Khan",
    "Harappa",
    "Hafizabad",
    "Haroonabad",
    "Hasilpur",
    "Haveli Lakha",
    "Islamabad",
    "Jalalpur Jattan",
    "Jampur",
    "Jaranwala",
    "Jhang",
    "Jhelum",
    "Jauharabad",
    "Kallar Syedan",
    "Kalabagh",
    "Karor Lal Esan",
    "Karachi",
    "Kasur",
    "Kamalia",
    "Kāmoke",
    "Khanewal",
    "Khanpur",
    "Khanqah Sharif",
    "Kharian",
    "Khushab",
    "Kot Adu",
    "Lahore",
    "Lalamusa",
    "Layyah",
    "Lawa Chakwal",
    "Liaquat Pur",
    "Lodhran",
    "Malakwal",
    "Mamoori",
    "Mailsi",
    "Mandi Bahauddin",
    "Mian Channu",
    "Mianwali",
    "Miani",
    "Multan",
    "Murree",
    "Muridke",
    "Mianwali Bangla",
    "Muzaffargarh",
    "Narowal",
    "Nankana Sahib",
    "Okara",
    "Pakpattan",
    "Pattoki",
    "Pindi Bhattian",
    "Pind Dadan Khan",
    "Pir Mahal",
    "Qaimpur",
    "Qila Didar Singh",
    "Raiwind",
    "Rajanpur",
    "Rahim Yar Khan",
    "Rawalpindi",
    "Renala Khurd",
    "Sadiqabad",
    "Sagri",
    "Sahiwal",
    "Sambrial",
    "Samundri",
    "Sangla Hill",
    "Sarai Alamgir",
    "Sargodha",
    "Shakargarh",
    "Sheikhupura",
    "Shujaabad",
    "Sialkot",
    "Sohawa",
    "Soianwala",
    "Siranwali",
    "Tandlianwala",
    "Talagang",
    "Taxila",
    "Toba Tek Singh",
    "Vehari",
    "Wah Cantonment",
    "Wazirabad",
    "Yazman",
    "Zafarwal"
  ]

city_name = StringVar()
com = ttk.Combobox(win,text='Weather App Python',values=list_name,font=('Times New Roman',20,'bold'),textvariable =city_name)
com.place(x=25,y=120,height=50,width=450)

info1  =Label(win,text='Weather Climate',font=('Times New Roman',15,'bold'))
info1.place(x=25,y=260,height=40,width=200)
info11  =Label(win,text='',font=('Times New Roman',15,'bold'))
info11.place(x=235,y=260,height=40,width=200)

info2  =Label(win,text='Description',font=('Times New Roman',15,'bold'))
info2.place(x=25,y=310  ,height=40,width=200)
info22  =Label(win,text='',font=('Times New Roman',15,'bold'))
info22.place(x=235,y=310,height=40,width=200)

info3  =Label(win,text='Temperature',font=('Times New Roman',15,'bold'))
info3.place(x=25,y=360  ,height=40,width=200)
info33  =Label(win,text='',font=('Times New Roman',15,'bold'))
info33.place(x=235,y=360,height=40,width=200)

info4  =Label(win,text='Pressure',font=('Times New Roman',15,'bold'))
info4.place(x=25,y=410  ,height=40,width=200)
info44  =Label(win,text='',font=('Times New Roman',15,'bold'))
info44.place(x=235,y=410,height=40,width=200)

done_button  =Button(win,text='Done',font=('Times New Roman',20,'bold'),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)
win.mainloop()
