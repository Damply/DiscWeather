from darksky import forecast
from datetime import date, timedelta
from geopy.geocoders import Nominatim
import datetime
from dhooks import Webhook, Embed


hook = Webhook('DISCORD WEBHOOK HERE')


d = datetime.datetime.today()
key = 'DARK SKY API KEY HERE'
geolocator = Nominatim(user_agent="testshit")
#zip = input("Enter your zip: ")
zipper = geolocator.geocode(PUT YOUR ZIPCODE HERE)

actzip = zipper.latitude, zipper.longitude

year = d.strftime("%Y")
month = d.strftime("%B")
day = d.strftime("%d")



today = date.today()
with forecast(key, *actzip) as theplace:
	tempy = theplace.temperature
	summ = theplace.hourly.summary
	wtype = str(theplace.currently.icon)
	#print(wtype)
	#print('Date:',month, day, year, end='\n')
	#print('Temperature:',tempy)
	#print(theplace.daily.icon)
	#print("Summary: ", theplace.daily.summary)
	
embed = Embed(
	description='',
	color=0x1e0f3,
	timestamp='now'  # sets the timestamp to current time
	)



if wtype == "clear-day":
	embed.set_thumbnail('https://i.imgur.com/qmNGoE1.png')
elif wtype == "clear-night":
	embed.set_thumbnail('https://i.imgur.com/AOG5kYe.png')
elif wtype == "rain":
	embed.set_thumbnail('https://i.imgur.com/EQT2KjP.png')
elif wtype == "sleet":
	embed.set_thumbnail('https://i.imgur.com/u03j5pJ.png')
elif wtype == "windy":
	embed.set_thumbnail('https://i.imgur.com/KRgDuno.png')
elif wtype == "fog":
	embed.set_thumbnail('https://i.imgur.com/tHvFSVT.png')
elif wtype == "cloudy":
	embed.set_thumbnail('https://i.imgur.com/eBYkmzZ.png')
elif wtype == "partly-cloudy-day":
	embed.set_thumbnail('https://i.imgur.com/yjej8ok.png')
elif wtype == "partly-cloudy-night":
	embed.set_thumbnail('https://i.imgur.com/KJPgzdI.png')
elif wtype == "hail":
	embed.set_thumbnail('https://i.imgur.com/Nit0CQA.png')
elif wtype == "thunderstorm":
	embed.set_thumbnail('https://i.imgur.com/wKyjqbY.png')
elif wtype == "tornado":
	embed.set_thumbnail('https://i.imgur.com/bIUq5Iw.png')
	


image1 = 'https://i.imgur.com/vcGBgwx.png'	

embed.set_author(name='Daily Weather', icon_url=image1)
embed.add_field(name='Date', value=month+' / '+day+' / '+year)
embed.add_field(name='Temperature', value=str(tempy))
#embed.add_field(name='Weather Type', value=str(wtype))
embed.set_footer(text=summ)
hook.send(embed=embed)


	
	
