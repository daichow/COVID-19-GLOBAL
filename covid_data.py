import requests
from pprint import pprint
import json
from  datetime import  datetime
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from matplotlib import dates as mpl_dates
import pandas as pd
import re
import os
import time
import pycountry

class CovidData():

	def do_fuzzy_search(self, country):
		try:

			self.country_name = country
			result = pycountry.countries.search_fuzzy(country)
		except Exception:
			return np.nan
		else:
			self.country_id = result[0].alpha_3

	def download_country_flag(self, country):
	    country = country.replace(" ", "-")
	    r = requests.get("https://www.countryflags.com/en/{}-flag-image.html".format(country))
	    content = BeautifulSoup(r.content, 'html.parser')
	    img_tag = "https:{}".format(content.findAll("img")[2].attrs['src'])
	    # print(img_tag)
	    
	    pic = requests.get(img_tag, stream=True, headers={'User-agent': 'Mozilla/5.0'})

	    if pic.status_code == 200:
	        with open(os.path.join(os.getcwd(),"{}.png".format(country)), 'wb') as f:
	            f.write(pic.content)

	def updateJSONData(self):
		self.loadJSONData()
		# print(len(list(self.data.keys())))
		previous_name = pycountry.countries.get(alpha_3=list(self.data.keys())[0]).name.lower()

		date_mod = str(datetime.strptime(time.ctime(os.path.getmtime("data.json")), "%a %b %d %H:%M:%S %Y"))[0:10]
		date_now = str(datetime.now())[0:10]

		if date_now != date_mod or self.country_name != previous_name:
			# self.country_id = country_id

			r = requests.get("https://covid.ourworldindata.org/data/owid-covid-data.json").json().get(self.country_id)
			r2 = requests.get("https://covid.ourworldindata.org/data/owid-covid-data.json").json().get("OWID_WRL")

			dictionary = {
			self.country_id : r,
			"WRLD":r2
			}

			with open("data.json", "w") as my_file:
			    my_file.write(json.dumps(dictionary, indent = 4))
		else:
			pass

		for file in os.listdir(os.getcwd()):
			if not file.endswith('.png'):
				self.download_country_flag(self.country_name)
			elif self.country_name != previous_name:
				os.remove(file)
			else:
				self.download_country_flag(self.country_name)

	def loadJSONData(self):
		with open('data.json', 'r') as json_file:
		    self.data = json.load(json_file)

	def getValueList (self, key, _type):
		list = []
		for each_data_entry in self.data.get(self.country_id):
			if _type == "_str":
				list.append(str(each_data_entry.get(key)))
			else:
				list.append(int(each_data_entry.get(key)))
		return list

	def populate_variables(self):
		# country information
		self.continent = self.data.get(self.country_id)[0].get("continent")
		self.location = self.data.get(self.country_id)[0].get("location")

		self.date = self.getValueList("date", "_str")

		# COVID INFO
		self.total_cases = self.getValueList("total_cases", "_int")
		self.new_cases = self.getValueList("new_cases", "_int")
		self.total_deaths = self.getValueList("total_deaths", "_int")
		self.new_deaths = self.getValueList("new_deaths", "_int")

		# COUNTRY DEMOGRAPHICS
		self.population = self.data.get(self.country_id)[-1].get("population")	
		self.population_density = self.data.get(self.country_id)[0].get("population_density")
		self.aged_65_older = self.data.get(self.country_id)[-1].get("aged_65_older")
		self.gdp_per_capita = self.data.get(self.country_id)[-1].get("gdp_per_capita")

		# COUNTRY HEALTH BACKGROUND
		self.cvd_death_rate = self.data.get(self.country_id)[-1].get("cvd_death_rate")
		self.diabetes_prevalence = self.data.get(self.country_id)[-1].get("diabetes_prevalence")
		self.hospital_beds_per_thousand = self.data.get(self.country_id)[-1].get("hospital_beds_per_thousand")
		# self.handwashing_facilities = self.data.get(self.country_id)[-1].get("handwashing_facilities")
		# if self.handwashing_facilities == None:
		# 	self.handwashing_facilities = "data not available"

	def populate_world_variables(self):
		self.total_world_cases = self.data.get("WRLD")[-1].get("total_cases")
		self.new_world_cases = self.data.get("WRLD")[-1].get("new_cases")
		self.total_world_deaths = self.data.get("WRLD")[-1].get("total_deaths")
		self.new_world_deaths = self.data.get("WRLD")[-1].get("new_deaths")


	def plotTimeSeries(self, _list, yaxislabel, country, islog):
		plt.style.use('dark_background')
		# ax = plt.gca()
		df = pd.DataFrame(list(zip(self.date,  _list)), 
		               columns =['Date', 'Value'])

		df['Date'] = pd.to_datetime(df['Date'])
		# df.sort_values('Date', inplace=True)

		fig, axes = plt.subplots(nrows=1, ncols=1)
		# print(axes)
		plt.gcf().autofmt_xdate()

		plt.title("{} Analysis By Date in {}".format(yaxislabel, country))
		plt.xlabel("Date")
		plt.ylabel(yaxislabel)

		if islog:
			axes.set_yscale('log')
			log = "(Log Scaled Graph)"
		else:
			log = "(Linear Graph)"

		fig = plt.gcf()

		fig.canvas.set_window_title("{} Analysis By Date in {} {}".format(yaxislabel, country, log))



		plt.tight_layout()

		plt.plot_date(df['Date'], df['Value'], linestyle='solid', marker=".", markersize=5)
		# df["Value"].plot()
		# df.plot(x='Date', y='Value',grid = True, ax=axes, logy = True, legend = False)
		plt.show()

# if __name__ == "__main__":
# 	covid = CovidData()
# 	covid.do_fuzzy_search("china")
# 	covid.updateJSONData()
# 	covid.loadJSONData()
# 	covid.populate_variables()
# 	# covid.populate_world_variables()
# 	# pprint(len(covid.total_cases))
# 	covid.plotTimeSeries(covid.total_cases, "Total Cases", covid.location, True)
	# print(covid.total_world_cases)