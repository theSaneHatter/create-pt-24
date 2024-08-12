
import pandas as pd
import os
import random
import sys

if __name__ == '__main__':
  excel_path = '/home/runner/Flasktests/country_data.xlsx'
else:
  excel_path = ''




#takes a file path and returns True if it exists. Otherwise, it prints error message and raises FileNotFoundError
def check_existance(a_path):

  path_exists = os.path.exists(excel_path)
  if path_exists == False:
    print(f'\033[31mERROR: {excel_path} does not exist\033[0m')
    raise FileNotFoundError(
        f'\033[31mERROR: {excel_path} does not exist\033[0m')
  elif path_exists == True:
    return True
  else:
    print(f'\033[31mERROR: an unknown error has occured\033[0m')
    raise RuntimeError(f'\033[31mERROR: an unknown error has occured\033[0m')
    return False

#takes a pandas xls file object, returns a tuple, containing: (random_country, random_country_index)
def get_random_country(sheet):
  index = random.randint(0, len(sheet['Country'].tolist()) - 1)
  rand_country = sheet['Country'].tolist()[index]
  return (rand_country, index)


#takes a country and panda xls object and returns a the object as a
class Country:

  def __init__(self, index, name, population, GDP, Area, POP_Density,
               GDP_per_capata, First_Letter, Hemesphere):

    self.index = index
    self.name = name
    self.population = population
    self.Area = Area
    self.POP_Density = POP_Density
    self.GDP = GDP
    self.First_Letter = First_Letter
    self.Hemesphere = Hemesphere
    self.GDP_per_capata = GDP_per_capata


#takes panda xls object and returns a list of country objects
#it ittorates through all the indexes in the xls file and create a country object for each ittoration.
#it returns a list of lists of country objects, each in this order: [index, name, population, area, pop_density, gdp, first_letter]
def orgonize_countries(country_xls):
  country_object_list = []
  if not country_xls.empty:
    headers = country_xls.columns.ravel()

    for n, i in enumerate(range(len(country_xls))):
      index = n
      name = country_xls.iloc[index, 1]
      population = country_xls.iloc[index, 2]
      gdp = country_xls.iloc[index, 3]
      area = country_xls.iloc[index, 4]
      density = country_xls.iloc[index, 5]
      gdp_per_capata = country_xls.iloc[index, 6]
      first_letter = country_xls.iloc[index, 7]
      hemesphere = country_xls.iloc[index, 8]

      country_object = Country(index, name, population, gdp, area, density,
                               gdp_per_capata, first_letter, hemesphere)

      country_object_list.append(country_object)

      #make global countriy variables
      #globals()[name] = country_object

  else:
    print(f'\033[31mERROR:{country_xls} is empty\033[0m')
    raise ValueError(f'\033[31mERROR:{country_xls} is empty\033[0m')

  return country_object_list


#takes a variable and returns its name in a string format
def get_variable_name(value):
  namespace = locals()
  for name, obj in namespace.items():
    if obj is value:
      return str(name)
  raise ValueError('Variable name not found for giben value')


#takes a list of countries, as produced by orgonize_countries(), and makes the indevigual country objects global
def make_country_objects_global(a_list):
  for object in a_list:

    attrabutes = ''
    for index, attrabute in enumerate(object):
      if index == 0:
        attrabutes += str(f'"{attrabute}"')
      else:
        attrabutes += str(f',"{attrabute}"')

    exec(f'{get_variable_name(object)} = Country({attrabutes})')
    exec(f'global {get_variable_name(object)}')


#takes a country (e.g. 'Kosovo') and the list created by orgonize_countries() and returns a list of that countries attrabutes
def get_attrabutes(a_country, a_country_list):
  name = a_country
  attrabutes = []
  country_column_name = 'Country'

  for country in a_country_list:
    if name == country.name:
      target_data = vars(country)
      return target_data

  print(f'\033[31mERROR: {name} is not a valid country\033[0m')
  return f'\033[31mERROR: {name} is not a valid country\033[0m'
#

#takes 2 countries and a xls panda object and returns the country with the greater population
#example: population_comparason("Italy", "Zambia", panda_object)
def population_comparason(country_1, country_2, panda_object):

  country_1_data = get_attrabutes(country_1, panda_object)
  country_2_data = get_attrabutes(country_2, panda_object)

  country_1_pop = country_1_data['population']
  country_2_pop = country_2_data['population']

  try:
    country_1_pop = int(country_1_pop)
  except ValueError:
    return print(
        f'\033[31mERROR: Cannot convert {country_1_pop} to an integer\033[0m')

  try:
    country_2_pop = int(country_2_pop)
  except ValueError:
    return print(
        f'\033[31mERROR: Cannot convert {country_2_pop} to an integer\033[0m')

  if country_1_pop > country_2_pop:
    greater_country = country_1
  elif country_1_pop < country_2_pop:
    greater_country = country_2
  elif country_1_pop == country_2_pop:
    greater_country = False
  else:
    return print(
        f'\033[31mERROR: Cannot compare {country_1_pop} and {country_2_pop}\033[0m'
    )

  return greater_country



#takes 2 countries and a xls panda object and returns the country with the greater area
#example: population_comparason("Italy", "Zambia", panda_object)
def size_comparason(country_1, country_2, panda_object):

  country_1_data = get_attrabutes(country_1, panda_object)
  country_2_data = get_attrabutes(country_2, panda_object)

  country_1_pop = country_1_data['Area']
  country_2_pop = country_2_data['Area']

  try:
    country_1_pop = int(country_1_pop)
  except ValueError:
    return print(
        f'\033[31mERROR: Cannot convert {country_1_pop} to an integer\033[0m')

  try:
    country_2_pop = int(country_2_pop)
  except ValueError:
    return print(
        f'\033[31mERROR: Cannot convert {country_2_pop} to an integer\033[0m')

  if country_1_pop > country_2_pop:
    greater_country = country_1
  elif country_1_pop < country_2_pop:
    greater_country = country_2
  elif country_1_pop == country_2_pop:
    greater_country = False
  else:
    return print(
        f'\033[31mERROR: Cannot compare {country_1_pop} and {country_2_pop}\033[0m'
    )

  return greater_country



#takes a list of countries (as created by orgonize_countries()), a list of already given hints, the target country 
def GDP_hint(country_list, hints, target_country, a_guess):
  hint = ''
  used = True
  tries = 0

  while used:
    if int(target_country['GDP']) < int(a_guess['GDP']):
      hint = f'The GDP of country you should guess is less than that of {a_guess["name"]}'
    elif int(target_country['GDP']) > int(a_guess['GDP']):
      hint = f'The GDP of the country you should guess is greater than that of {a_guess["name"]}'
    elif int(target_country['GDP']) == int(a_guess['GDP']):
      hint = f'The GDP of country you should guess is that of {a_guess["name"]}'
    else:
      print(f'\033[31mERROR:UNEXPECTED ERROR OCCURED\033[0m')
      hint = 'An error occured in provideing this hint.'

    if hint not in hints:
      used = False
    else:
      tries += 1
    if tries > len(country_list):
      used = False
      hint = 'I have no more hints for you regarding GDP :('

  return hint
#

#takes 2 countries and a xls panda object and returns the country with the greater GDP 
#per capata
#example: population_comparason("Italy", "Zambia", panda_object)
def GDP_per_capata_comparason(country_1, country_2, panda_object):

  country_1_data = get_attrabutes(country_1, panda_object)
  country_2_data = get_attrabutes(country_2, panda_object)

  country_1_pop = country_1_data['GDP_per_capata']
  country_2_pop = country_2_data['GDP_per_capata']

  try:
    country_1_pop = int(country_1_pop)
  except ValueError:
    return print(
        f'\033[31mERROR: Cannot convert {country_1_pop} to an integer\033[0m')

  try:
    country_2_pop = int(country_2_pop)
  except ValueError:
    return print(
        f'\033[31mERROR: Cannot convert {country_2_pop} to an integer\033[0m')

  if country_1_pop > country_2_pop:
    greater_country = country_1
  elif country_1_pop < country_2_pop:
    greater_country = country_2
  elif country_1_pop == country_2_pop:
    greater_country = False
  else:
    return print(
        f'\033[31mERROR: Cannot compare {country_1_pop} and {country_2_pop}\033[0m'
    )

  return greater_country

#takes 2 countries and a xls panda object and returns the country with the greater density
#example: population_comparason("Italy", "Zambia", panda_object)
def density_comparason(country_1, country_2, panda_object):

  country_1_data = get_attrabutes(country_1, panda_object)
  country_2_data = get_attrabutes(country_2, panda_object)

  country_1_pop = country_1_data['POP_Density']
  country_2_pop = country_2_data['POP_Density']

  try:
    country_1_pop = int(country_1_pop)
  except ValueError:
    return print(
        f'\033[31mERROR: Cannot convert {country_1_pop} to an integer\033[0m')

  try:
    country_2_pop = int(country_2_pop)
  except ValueError:
    return print(
        f'\033[31mERROR: Cannot convert {country_2_pop} to an integer\033[0m')

  if country_1_pop > country_2_pop:
    greater_country = country_1
  elif country_1_pop < country_2_pop:
    greater_country = country_2
  elif country_1_pop == country_2_pop:
    greater_country = False
  else:
    return print(
        f'\033[31mERROR: Cannot compare {country_1_pop} and {country_2_pop}\033[0m'
    )

  return greater_country


#takes 2 countries and a xls panda object and returns the country with the greater index
#example: population_comparason("Italy", "Zambia", panda_object)
def index_comparason(country_1, country_2, panda_object):

  country_1_data = get_attrabutes(country_1, panda_object)
  country_2_data = get_attrabutes(country_2, panda_object)

  country_1_pop = country_1_data['index']
  country_2_pop = country_2_data['index']

  try:
    country_1_pop = int(country_1_pop)
  except ValueError:
    return print(
        f'\033[31mERROR: Cannot convert {country_1_pop} to an integer\033[0m')

  try:
    country_2_pop = int(country_2_pop)
  except ValueError:
    return print(
        f'\033[31mERROR: Cannot convert {country_2_pop} to an integer\033[0m')

  if country_1_pop > country_2_pop:
    greater_country = country_1
  elif country_1_pop < country_2_pop:
    greater_country = country_2
  elif country_1_pop == country_2_pop:
    greater_country = False
  else:
    return print(
        f'\033[31mERROR: Cannot compare {country_1_pop} and {country_2_pop}\033[0m'
    )

  return greater_country


#takes a list of countries (as created by orgonize_countries()), a list of already given hints, the target country 
def name_hint(country_list, hints, target_country, a_guess):
  hint = ''
  used = True
  tries = 0
  while used:
    choices = random.randint(0,1)
    potentual_hint = random.choice(country_list)
    potentual_hint = get_attrabutes(potentual_hint.name, country_list)

    while potentual_hint == target_country:
      potentual_hint = random.choice(country_list)
      potentual_hint = get_attrabutes(potentual_hint.name, country_list)

    if choices == 0:
      if potentual_hint['First_Letter'] == target_country['First_Letter']:
        hint = f'The first letter of the {potentual_hint["name"]} is the same as that of ' + target_country['name']
      else:
        hint = f'The first letter of {potentual_hint["name"]} is not the same as that of {potentual_hint["name"]}'

    elif choices == 1:

      if potentual_hint['index'] < target_country['index']:
        hint = f'The first letter of {potentual_hint["name"]} comes after the first letter of {potentual_hint["name"]} in the alphabet'
      else:
        hint = f'The first letter of {target_country["name"]} comes before the first letter of {potentual_hint["name"]} in the alphabet'

    else:
      print(f'chosen option (choices) = <{choices}>')
      print(f'chosen country (potentual_hint) = <\n{potentual_hint}\n>')
      print(f'\033[31mERROR:UNEXPECTED ERROR OCCURED\033[0m ')

    if hint not in hints:
      used = False
    tries += 1
    if tries > len(country_list):
      used = False
      hint = 'I have no more hints for you regarding names :('

  return hint  


#takes a list of countries (as created by orgonize_countries()), a list of already given hints, the target country 
def population_hint(country_list, hints, target_country, a_guess):
  hint = ''
  used = True
  tries = 0

  while used:
    if target_country['population'] < a_guess['population']:
      hint = f'The population of the country you should guess is less than that of ' +a_guess["name"]
    elif target_country['population'] > a_guess['population']:
      hint = f'The population of country you should guess is greater than that of ' +a_guess["name"]
    elif target_country['population'] == a_guess['population']:
      hint = f'The population of country you should guess is that of {a_guess["name"]}'
    else:
      

      print(f'\033[31mERROR:UNEXPECTED ERROR OCCURED\033[0m')
      hint = 'An error occured in provideing this hint.'



    if hint not in hints:
      used = False
    else:
      tries += 1
    if tries > len(country_list):
      used = False
      hint = 'I have no more hints for you regarding population :('

  return hint
#

#takes a list of countries (as created by orgonize_countries()), a list of already given hints, the target country 
def area_hint(country_list, hints, target_country, a_guess):
  hint = ''
  used = True
  tries = 0

  while used:
    if target_country['Area'] < a_guess['Area']:
      hint = f'The Area of country you should guess is less than that of {a_guess["name"]}'
    elif target_country['Area'] > a_guess['Area']:
      hint = f'The Area of country you should guess is greater than that of {a_guess["name"]}'
    elif target_country['Area'] == a_guess['Area']:
      hint = f'The Area of the country you should guess is that of {a_guess["name"]}'
    else:
      print(f'\033[31mERROR:UNEXPECTED ERROR OCCURED\033[0m')
      hint = 'An error occured in provideing this hint.'



    if hint not in hints:
      used = False
    else:
      tries += 1
    if tries > len(country_list):
      used = False
      hint = 'I have no more hints for you regarding Area :('

  return hint


#takes a list of countries (as created by orgonize_countries()), a list of already given hints, the target country 
def GDP_hint(country_list, hints, target_country, a_guess):
  hint = ''
  used = True
  tries = 0

  while used:
    if int(target_country['GDP']) < int(a_guess['GDP']):
      hint = f'The GDP of country you shoud guess is less than that of {a_guess["name"]}'
    elif int(target_country['GDP']) > int(a_guess['GDP']):
      hint = f'The GDP of the country you shoud guess is greater than that of {a_guess["name"]}'
    elif int(target_country['GDP']) == int(a_guess['GDP']):
      hint = f'The GDP of country you shoud guess is that of {a_guess["name"]}'
    else:
      print(f'\033[31mERROR:UNEXPECTED ERROR OCCURED\033[0m')
      hint = 'An error occured in provideing this hint.'

    if hint not in hints:
      used = False
    else:
      tries += 1
    if tries > len(country_list):
      used = False
      hint = 'I have no more hints for you regarding GDP :('

  return hint
#

  
#takes a list of countries (as created by orgonize_countries()), a list of already given hints, the target country 
def GDP_per_capata_hint(country_list, hints, target_country, a_guess):
  hint = ''
  used = True
  tries = 0


  while used:
    if target_country['GDP_per_capata'] < a_guess['GDP_per_capata']:
      hint = f'The GDP per capata of country (the country you sould guess) is less than that of {a_guess["name"]}'
    elif target_country['GDP_per_capata'] > a_guess['GDP_per_capata']:
      hint = f'The GDP per capata of country (the country you sould guess) is greater than that of {a_guess["name"]}'
    elif target_country['GDP_per_capata'] == a_guess['GDP_per_capata']:
      hint = f'The GDP per capata of target country (the country you sould guess) is that of {a_guess["name"]}'
    else:
      print(f'chosen option (choices) = <{choices}>')
      print(f'chosen country (potentual_hint) = <\n{potentual_hint}\n>')
      print(f'\033[31mERROR:UNEXPECTED ERROR OCCURED\033[0m')
      hint = 'An error occured in provideing this hint.'



    if hint not in hints:
      used = False
    else:
      tries += 1
    if tries > len(country_list):
      used = False
      hint = 'I have no more hints for you regarding GDP_per_capata :('

  return hint
#

#takes a list of countries (as created by orgonize_countries()), a list of already given hints, the target country 
def hemesphere_hint(country_list, hints, target_country, a_guess):
  hint = ''
  used = True
  tries = 0

  while used:
    if target_country['Hemesphere'] == a_guess['Hemesphere']:
      hint = f'The Hemesphere of the country you should guess is that of {a_guess["name"]}'
    elif target_country['Hemesphere'] != a_guess['Hemesphere']:
      hint = f'The Hemesphere of country you should guess not that of {a_guess["name"]}'
    else:
      print(f'chosen country (potentual_hint) = <\n{potentual_hint}\n>')
      print(f'\033[31mERROR:UNEXPECTED ERROR OCCURED\033[0m')
      hint = 'An error occured in provideing this hint.'



    if hint not in hints:
      used = False
    else:
      tries += 1
    if tries > len(country_list):
      used = False
      hint = 'I have no more hints for you regarding Hemesphere :('

  return hint
#
#takes a list of countries (as created by orgonize_countries()), a list of already given hints, the target country 
def pop_density_hint(country_list, hints, target_country, a_guess):
  hint = ''
  used = True
  tries = 0

  while used:
    if target_country['POP_Density'] < a_guess['POP_Density']:
      hint = f'The POP_Density of country you shoud guess is less than that of {a_guess["name"]}'
    elif target_country['POP_Density'] > a_guess['POP_Density']:
      hint = f'The POP_Density of country you shoud guess is greater than that of {a_guess["name"]}'
    elif target_country['POP_Density'] == a_guess['POP_Density']:
      hint = f'The POP_Density of country you shoud guess is that of {a_guess["name"]}'
    else:
      print(f'chosen country (potentual_hint) = <\n{potentual_hint}\n>')
      print(f'\033[31mERROR:UNEXPECTED ERROR OCCURED\033[0m')
      hint = 'An error occured in provideing this hint.'



    if hint not in hints:
      used = False
    else:
      tries += 1
    if tries > len(country_list):
      used = False
      hint = 'I have no more hints for you regarding POP_Density :('

  return hint


#takes a orgonize_countries() object, a list of hints, a target country, a guess, and returns
#a uneque hint
def provide_hint(country_list, hints, target_country, a_guess):
  hint = ''
  

  hint_methiod = random.choice([name_hint, population_hint, area_hint, GDP_hint, GDP_per_capata_hint, hemesphere_hint])
  hint = hint_methiod(country_list, hints, target_country, a_guess)
  return hint

#

def varaify_country(pandas_xls_object, country_name):

  name_column_list = pandas_xls_object['Country'].tolist()
  if country_name in name_column_list:
    print(f'\033[32mThe country <{country_name}> has been found in the pandas xls object, and varaify_country() has valadated it as a country\033[0m')
    return True
  else:
    print(f'\033[33mCountry submitted by used is not a country\033[0m')

    return False
    
    

if __name__ == '__main__':
    check_existance(excel_path)

    df = pd.read_excel(excel_path)

    countries = orgonize_countries(df)


    print(get_attrabutes('Zambia', countries))

    print('name is:', get_attrabutes('Zambia', countries)["name"])

    print('larger pop:', population_comparason('United States of America', 'Russia',countries))


    print('larger area:', size_comparason('United States of America', 'Russia',countries))

    print('larger GDP:', GDP_comparason('United States of America', 'Russia',countries))

    print('larger GDP per capata:', GDP_per_capata_comparason('United States of America', 'Russia',countries))

    print('larger density:', density_comparason('United States of America', 'Russia',countries))

    print('larger index:', index_comparason('United States of America', 'Russia',countries))

    print('\n\n\n\n---\n\n\n\n---')

    hints_used = []
    for i in range(1):
        selected_country = random.choice(countries)
        selected_country = get_attrabutes(selected_country.name, countries)
        #print(f'Selected Country: {selected_country}')

      
        target_country = get_attrabutes('Zambia', countries)
        
        print(f'\n selected_country["name"] = {selected_country["name"]} \n')
        print(f'\n selected_country["First_Letter"] = {selected_country["First_Letter"]} \n')
        print(f'\n target_country["name"] = {target_country["name"]} \n')
        print(f'\n target_country["First_Letter"] = {target_country["First_Letter"]} \n')


        #country_list, hints, target_country, a_guess

        hint = provide_hint(countries, hints_used, selected_country, target_country)
        print('\nhint:', hint, '\n')
        hints_used.append(hint)
        
        print('valid country test:', varaify_country(df, 'Zambia'))
        print('valid country test:', varaify_country(df, 'Zamsbia'))

      

else:
  print(f'\033[32m{sys.argv[0]} HAS BEEN IMPORTED! \033[0m')

