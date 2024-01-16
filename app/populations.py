import read_csv

def get_country_by_name(country):
  countries = read_csv.read_csv("./app/data.csv")
  my_country = [dict for dict in countries if dict["Country/Territory"] == country.title()]
  return my_country

def get_population_by_country(country):
  my_country = get_country_by_name(country)[0]
  #my_country2 = my_country[0]
  my_population = {
    "2022": my_country["2022 Population"],
    "2020": my_country["2020 Population"],
    "2015": my_country["2015 Population"],
    "2010": my_country["2010 Population"],
    "2000": my_country["2000 Population"],
    "1990": my_country["1990 Population"],
    "1980": my_country["1980 Population"],
    "1970": my_country["1970 Population"]
  }
  return my_population

if __name__ == "__main__":
  # print(get_country_by_name("mexico"))
  print(get_population_by_country("mexico"))
