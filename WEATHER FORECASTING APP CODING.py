from tkinter import * # board  
from tkinter import ttk#for combo list
import requests # moldula

def data_get():
 city=city_name.get()
 data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=78b430a7800aab4cd2b39fe3d62e5cb9").json()# from api weather app" city name is variable no is api key
 w_Label1.config(text=data["weather"][0]["main"])
 wb_Label1.config(text=data["weather"][0]["description"])
 temp_Label1.config(text=str(int(data["main"]["temp"]-273.15)))
 pre_Label1.config(text=(data["main"]["pressure"]))

wind = Tk()
wind.title("weather")
wind.config(bg ="light blue")
wind.geometry("600x600")# board mesurment

name_Label= Label(wind,text="weather cast",
                  font=("Time New Roman",40,"bold"))# heading
name_Label.place(x=25,y=50,height=50,width=450)# for heading


city_name=StringVar()
List_name=["Ahmadpur East","Ahmed Nager Chatha","Ali Khan Abad","Alipur","Arifwala","Attock","Bhera","Bhalwal","Bahawalnagar","Bahawalpur","Bhakkar","Burewala","Chenab Nagar","Chillianwala","Choa Saidanshah","Chakwal","Chak Jhumra","Chichawatni","Chiniot","Chishtian","Chunian","Dajkot","Daska","Davispur","Darya Khan","Dera Ghazi Khan","Dhaular","Dina","Dinga","Dhudial Chakwal","Dipalpur","Faisalabad","Fateh Jang","Ghakhar Mandi","Gojra","Gujranwala","Gujrat","Gujar Khan","Harappa","Hafizabad","Haroonabad","Hasilpur","Haveli Lakha","Jalalpur Jattan","Jampur","Jaranwala","Jhang","Jhelum","Kallar Syedan","Kalabagh","Karor Lal Esan","Kasur","Kamalia","Kāmoke","Khanewal","Khanpur","Khanqah Sharif","Kharian","Khushab","Kot Adu","Jauharabad","Lahore","Islamabad","Lalamusa","Layyah","Lawa Chakwal","Liaquat Pur","Lodhran","Malakwal","Mamoori","Mailsi","Mandi Bahauddin","Mian Channu","Mianwali","Miani","Multan","Murree","Muridke","Mianwali Bangla","Muzaffargarh","Narowal","Nankana Sahib","Okara","Renala Khurd","Pakpattan","Pattoki","Pindi Bhattian","Pind Dadan Khan","Pir Mahal","Qaimpur","Qila Didar Singh","Raiwind","Rajanpur","Rahim Yar Khan","Rawalpindi","Sadiqabad","Sagri","Sahiwal","Sambrial","Samundri","Sangla Hill","Sarai Alamgir","Sargodha","Shakargarh","Sheikhupura","Shujaabad","Sialkot","Sohawa","Soianwala","Siranwali","Tandlianwala","Talagang","Taxila","Toba Tek Singh","Vehari","Wah Cantonment","Wazirabad", "Yazman", "Zafarwal", ]
com=ttk.Combobox(wind,text="weather cast",values=List_name,
                  font=("Time New Roman",20),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

w_Label=Label(wind,text="Weather Climate",
                  font=("Time New Roman",20))
w_Label.place(x=25,y=260,height=50,width=210)
w_Label1=Label(wind,text="",
                  font=("Time New Roman",20,))
w_Label1.place(x=250,y=260,height=50,width=210)

wb_Label=Label(wind,text="Weather Description",
                  font=("Time New Roman",17,))
wb_Label.place(x=25,y=330,height=50,width=210)
wb_Label1=Label(wind,text="",
                  font=("Time New Roman",20,))
wb_Label1.place(x=250,y=330,height=50,width=210)

temp_Label=Label(wind,text="Temperature",
                  font=("Time New Roman",20,))
temp_Label.place(x=25,y=400,height=50,width=210)
temp_Label1=Label(wind,text="",
                  font=("Time New Roman",20,))
temp_Label1.place(x=250,y=400,height=50,width=210)

pre_Label=Label(wind,text="Pressure",
                  font=("Time New Roman",20,))
pre_Label.place(x=25,y=470,height=50,width=210)
pre_Label1=Label(wind,text="",
                  font=("Time New Roman",20,))
pre_Label1.place(x=250,y=470,height=50,width=210)

done_button=Button(wind,text="Done",
                  font=("Time New Roman",20,"bold"),command = data_get)#command=data_get)# FOR BUTTON
done_button.place(y=190,height=50,width=100,x=200)

wind.mainloop()
