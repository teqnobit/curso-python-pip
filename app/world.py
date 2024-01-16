import read_csv
import charts

dataset = read_csv.read_csv("./app/data.csv")

def get_country_percentage(dataset):
  paises = []
  porcentaje = []
  for i in dataset:
    paises.append(i["Country/Territory"])
    porcentaje.append(i["World Population Percentage"])
  return paises, porcentaje

labels, values = get_country_percentage(dataset)
charts.generate_pie_chart(labels, values)