from flask import Flask, request, render_template, jsonify
import guesser_lib as gl
import pandas as pd
import os
import random
import sys
  
#prelimanary management for guesser_lib
gl.excel_path = './country_data.xlsx'
excel_path = './country_data.xlsx'
gl.df = pd.read_excel(excel_path)
df = gl.df
gl.countries = gl.orgonize_countries(gl.df)
countries =  gl.countries
print('path exists:',gl.check_existance(excel_path))
print(f'Random  Country: {gl.get_random_country(gl.df)}')

random_country = None

hints_used = []

#takes list of countries (as created by orgonize_countries()), a list of already given hints, the target country (as genorated by start() as a list), and a guess (eg "Russa"). 
def manage_guess(a_country_list, a_hints_used, a_target_country, a_guess):
  global df
  if a_target_country == None:
    print(f'\033[33mThe user has entered <{a_guess}> w/o pressing start \033[0m')
    return 'Press start to begin.'
    
  elif a_guess == '':
    print(f'\033[33mThe user has entered empty string: <{a_guess}> \033[0m')
    return 'Enter country into country field'
    

  #print('valid country test:', varaify_country(countries, 'Zamsbia'))
  if gl.varaify_country(df, a_guess) == False:
    print(f'\033[33mThe user has entered invalid country: <{a_guess}> \033[0m')
    return 'The country you have entered is not a valid country. Please enter a valid country.'
  else:
    print(f'\033[33mThe user has entered valid country: <{a_guess}> \033[0m')
    
    
  if a_target_country['name'] == a_guess:
    print(f'\033[33mThe user has guessed the country with guess:<{a_guess}> \033[0m')
    return f'CONGRATS! You have guessed the country correctly! Correct answer: {a_target_country["name"]}, Your answer: {a_guess}'
    
  else:
    print(f'\033[33mThe user has not guessed the country with guess:<{a_guess}> \033[0m')
    a_output_message = f'{a_guess} is not the correct country.' 
    print(f'\033[34mAttempting to genorate hint\033[0m')
    #hint = provide_hint(countries, hints_used, selected_country, target_country)
    a_hint = gl.provide_hint(a_country_list, a_hints_used, a_target_country, gl.get_attrabutes(a_guess, a_country_list))
    a_hints_used.append(a_hint)
    print(f'\033[33mThe user has been provided with the hint: <{a_hint}>')
    return a_output_message + '--- Hint:' + a_hint
    


def guess(a_guess, correct_guess):
  global hints_used
  if a_guess == None:
    print(f'\033[33mThe User has not selected a country, yet is trying to guess <{a_guess["name"]}>\033[0m')
    return 'Please select a country first'

  if a_guess == correct_guess:
    print(f'\033[33mThe User has guessed the correct country, witch is {a_guess["name"]}\033[0m')
    victory_message = f'CONGRADULATIONS! YOU HAVE GUESSED THE COUNTRY CORRECTALLY! THE CORRECT ANSWER WAS {correct_guess["name"]}, AND YOUR GUESS WAS {a_guess["name"]}'
    a_POST = {'hint': 'false', 'message': victory_message}
    return victory_message
  if a_guess != correct_guess:
    print(f'\033[33mThe User has guessed the wrong country, <{a_guess["name"]}>\033[0m')
    new_hint = gl.provide_hint(gl.countries, hints_used, correct_guess, a_guess)
    hints_used.append(new_hint)
    a_message = f'Incorrect. {a_guess["name"]} is not the correct country'
    a_POST = {'hint': new_hint, 'message': a_message}
    return a_POST

app = Flask(__name__, static_url_path='/static') 

format_path = '/home/runner/Flasktests/templates/format.html'

@app.route('/')
@app.route('/index/name')
def index(name=None):

    return render_template('format.html', name=name)

@app.route('/get_output')
def get_output():
    output = my_function()
    return output


#a_country_list, a_hints_used, a_target_country, a_guess
@app.route('/guess_country', methods=['POST'])
def guess_country():
  global hints_used, random_country, countries, df
  value = request.form['value']
  

  
  return manage_guess(countries, hints_used, random_country, value)
  
  
          
  

@app.route('/start', methods=['POST'])
def start():
  global random_country, hints_used
  value = request.form['value']
  if value == 'start':
    random_country = random.choice(gl.countries)
    random_country = gl.get_attrabutes(random_country.name, gl.countries)
    hints_used = []
    print(f'\033[33mThe User has started the game. The random country is <{random_country["name"]}>\033[0m')
  return 'The Game Has Started!'
  


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)