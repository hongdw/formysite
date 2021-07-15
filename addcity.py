#  addcity
import os
import django
import pandas as pd
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Country, City
url = "https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html"
raw_data = pd.read_html(url)
time.sleep(3)

data = raw_data[0]
cities = list()
for i in range(len(data)):
	temp = tuple(data['cities'].iloc[i])
	cities.append(temp)
print(cities)
for city in cities:
	    country = Country.objects.get(country_id=city[2])
	    temp = City(name=city[1], country=country, population=city[3])
	    temp.save()		
cities = City.objects.all()
print(cities)
print("Done!")


# for country in countries:
# 	temp = Country(name=country[1], country_id=country[0])
# 	temp.save()
# 	print(country)

# countries = Country.objects.all()
# print(countries)
# print("Done!")

#--------------------自行小測試--------
#c = [
#{"name":"阿米果", "id":1000},
#{"name":"狗", "id":1001}
#]
#
#for country in c:
#	temp = Country(name=country['name'], country_id=country['id'])
###	temp.save()
#
#countries = Country.objects.all()
#print(countries)
#print("Done!")