#-*- coding: utf-8 -*-

from flask import Flask, render_template, abort, request, flash, get_flashed_messages, send_file

from datetime import datetime

from flask_cors import CORS

from function import uprint, sequence_query, delete_useless_word, recuperate_name_wiki_page, recuperate_number_wiki_page, recuperate_resume_wiki_page, delete_balise_html, sequence_wiki_final

import json

import random


app = Flask(__name__)

CORS(app)

app.secret_key = "blablabla"

"""
@app.route('/')
def home():
    return render_template('pages/home.html', grandpy='accueil')
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('pages/home.html', grandpy='accueil')

@app.route('/results/', methods=['POST'])
def results():

    grandpyText = ""

    json_data = open('sentence.json', encoding='utf-8')
    data = json.load(json_data)

    polite = False

    if request.method == 'POST':
        query = request.args.get('query')
        print(query)

        try:
            variable_before = sequence_query(query)

            variable = delete_useless_word(variable_before)

            search = variable + ","

            number = recuperate_number_wiki_page(variable)

            name = recuperate_name_wiki_page(variable)

            article = recuperate_resume_wiki_page(name, number)

            article = delete_balise_html(article)

            article = sequence_wiki_final(article)

            if article == []:

                grandpy = 'no_idea'

                grandpyText += (search.capitalize() + " quoi ?") + "\n"

                grandpyText += (data["sentence_No_Idea"][random.randint(
                    0, (len(data["sentence_No_Idea"])) - 1)]) + "\n"

                search = search

            	#return render_template('pages/home.html', search=search, grandpy='no_idea')

            else:

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

                i = 0
                for sequence in article:
                    if i > 2:
                        break
                    if len(sequence) < 50:
                        pass
                    else:
                      	grandpyText += sequence + "\n"
                      	i += 1

                grandpyText += ((data["sentence_continu"][random.randint(
                    0, (len(data["sentence_continu"])) - 1)])) + "\n"

                humeur = ['Happy', 'accueil']
                random_humeur = humeur[random.randint(0, 1)]

                grandpy=random_humeur

                search = search

                #return render_template('pages/home.html', search=search, grandpy=random_humeur)

        except IndexError:

            grandpyText += (data["sentence_error"][random.randint(
                0, (len(data["sentence_error"])) - 1)]) + "\n"

            grandpy='Error'

            search='Paris'

            #return render_template('pages/home.html', search='Paris', grandpy='Error')

        except FileNotFoundError:

            grandpyText += (data["sentence_error_acid"][random.randint(
                0, (len(data["sentence_error_acid"])) - 1)]) + "\n"

            search = 'Paris'

            #return render_template('pages/home.html', search='Paris', grandpy='Acid')

            grandpy='Acid'

        except KeyError:

            grandpyText += (data["sentence_error"][random.randint(
                0, (len(data["sentence_error"])) - 1)]) + "\n"

            grandpy='Error'

            search='Paris'

            #return render_template('pages/home.html', search='Paris', grandpy='Error')

    json_data.close()

    # Make or Open the SQL file
    """
    fichier = open("search_papy.json", "a", encoding='utf-8')

    fichier.write("[\"text\": " + grandpyText + ", \"mood\": " + grandpy + ", \"search\": " + search + "]")
    fichier.close()
    """

    dictionary = grandpy + "###" + search + "###" + grandpyText

    return(dictionary)


#@app.route('/', methods=['POST'])
# def reponse_grandpy():
#	return "Maintenant il faut que je récupère ces données... *facepalm*"


@app.context_processor
def inject_now():
    return {'now': datetime.now()}


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
