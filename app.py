#-*- coding: utf-8 -*-

# import module for usign Flask and AJAX
from flask import Flask, render_template, abort, request, flash, get_flashed_messages, send_file
from flask_cors import CORS

# import function from function.py
from function import sequence_query, delete_useless_word, recuperate_name_wiki_page, recuperate_number_wiki_page, recuperate_resume_wiki_page, delete_balise_html, sequence_wiki_final

# import different module for the functionnement of the website
from datetime import datetime
import json
import random


# Launch Flask
app = Flask(__name__)
CORS(app)

app.secret_key = "secret.key.for.running.apps"


# Use this route for load the home page without user's request
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('pages/home.html', grandpy='accueil')


# With a querie in the text area, the appeal AJAX use the POST method
@app.route('/results/', methods=['POST'])
def results():

    # Create the variable for the awnser of GrandPy
    grandpyText = ""
    polite = False

    # Load the JSON file with all the sentence of GrandPy
    json_data = open('sentence.json', encoding='utf-8')
    data = json.load(json_data)

    # Treatement of the querie send with the POST request
    if request.method == 'POST':
        query = request.args.get('query')

        try:

            # Use all the function on function.py for tranformate the querie, use API, and display the awnser
            variable_before = sequence_query(query)
            variable = delete_useless_word(variable_before)
            search = variable + ","
            number = recuperate_number_wiki_page(variable)
            name = recuperate_name_wiki_page(variable)
            article = recuperate_resume_wiki_page(name, number)
            article = delete_balise_html(article)
            article = sequence_wiki_final(article)


            # If GrandPy doesn't found the location
            if article == []:

                grandpy = 'no_idea'
                grandpyText += (search.capitalize() + " quoi ?") + "\n"
                grandpyText += (data["sentence_No_Idea"][random.randint(
                    0, (len(data["sentence_No_Idea"])) - 1)]) + "\n"
                search = search

            else:

                # GrandPy modification this answer in function of the courtesy of user
                i = 0
                while i < len(variable_before):

                    if variable_before[i].lower() not in data["courtesy"]:
                        pass
                    else:
                        polite = True
                    i += 1

                if polite == False:
                    grandpyText += (data["courtesy_answer"][random.randint(
                        0, (len(data["courtesy_answer"])) - 1)]) + "\n"

                else:
                    grandpyText += (data["sentence_salutation"][random.randint(
                        0, (len(data["sentence_salutation"])) - 1)]) + "\n"

                grandpyText += (data["sentence_search_ok"][random.randint(
                    0, (len(data["sentence_search_ok"])) - 1)]) + "\n"

                # GrandPy select the begining of the wiki article
                i = 0
                for sequence in article:
                    if i > 2:
                        break
                    if len(sequence) < 50:
                        pass
                    else:
                        grandpyText += sequence + "\n"
                        i += 1

                # GrandPy set this mood random with the good answer
                grandpyText += ((data["sentence_continu"][random.randint(
                    0, (len(data["sentence_continu"])) - 1)])) + "\n"
                humeur = ['Happy', 'accueil', 'accueil_main', 'Happy_2']
                random_humeur = humeur[random.randint(0, 3)]
                grandpy = random_humeur
                search = search

        # GrandPy change his mood with the error
        except IndexError:

            grandpyText += (data["sentence_error"][random.randint(
                0, (len(data["sentence_error"])) - 1)]) + "\n"
            grandpy = 'Error'
            search = 'Paris'

        # GrandPy change his mood with the error
        except FileNotFoundError:

            grandpyText += (data["sentence_error_acid"][random.randint(
                0, (len(data["sentence_error_acid"])) - 1)]) + "\n"
            search = 'Paris'
            grandpy = 'Acid'

        # GrandPy change his mood with the error
        except KeyError:

            grandpyText += (data["sentence_error"][random.randint(
                0, (len(data["sentence_error"])) - 1)]) + "\n"
            grandpy = 'Error'
            search = 'Paris'

    # close the file with the sentence of GrandPY
    json_data.close()

    # sequence the different variable for the javascript file
    dictionary = grandpy + "###" + search + "###" + grandpyText
    return(dictionary)


# Select the year in course, for the footer of website
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

# Gestion of 404 error
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

# Running the website with Flask
if __name__ == '__main__':
    app.run(debug=True)
