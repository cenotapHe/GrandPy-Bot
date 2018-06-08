#-*- coding: utf-8 -*-

from flask import Flask, render_template, abort, request, flash, get_flashed_messages

from datetime import datetime

from flask import send_file

from function import uprint, sequence_query, delete_useless_word, recuperate_name_wiki_page, recuperate_number_wiki_page, recuperate_resume_wiki_page, delete_balise_html, sequence_wiki_final

import json

import random


app = Flask(__name__)

app.secret_key = "blablabla"


@app.route('/')
def home():
    return render_template('pages/home.html')


@app.route('/', methods=['GET', 'POST'])
def contact():

    json_data = open('sentence.json', encoding='utf-8')
    data = json.load(json_data)

    if request.method == 'POST':

        try:
            variable_before = sequence_query(str(request.form['msg']))

            variable = delete_useless_word(variable_before)

            search = variable + ","

            number = recuperate_number_wiki_page(variable)

            name = recuperate_name_wiki_page(variable)

            article = recuperate_resume_wiki_page(name, number)

            article = delete_balise_html(article)

            article = sequence_wiki_final(article)

            if article == []:

                flash(data["sentence_error"][random.randint(
                    0, (len(data["sentence_error"])) - 1)])

                return render_template('pages/home.html', search=search)

            else:

                polite = False
                for i in enumerate(variable_before):
                    if variable_before[i[0]].lower in data["courtesy"]:
                        polite = True

                if polite:
                    flash(data["sentence_salutation"][random.randint(
                        0, (len(data["sentence_salutation"])) - 1)])

                else:
                    flash(data["courtesy_answer"][random.randint(
                        0, (len(data["courtesy_answer"])) - 1)])

                flash(data["sentence_search_ok"][random.randint(
                    0, (len(data["sentence_search_ok"])) - 1)])

                for sequence in article:
                    flash(sequence)

                flash((data["sentence_continu"][random.randint(
                    0, (len(data["sentence_continu"])) - 1)]))

                return render_template('pages/home.html', search=search, grandpy='Happy')

        except IndexError:

            flash(data["sentence_error"][random.randint(
                0, (len(data["sentence_error"])) - 1)])

            return render_template('pages/home.html', search='Paris', grandpy='Error')

        except FileNotFoundError:

            flash(data["sentence_error_acid"][random.randint(
                0, (len(data["sentence_error_acid"])) - 1)])

            return render_template('pages/home.html', search='Paris', grandpy='Acid')

        except KeyError:

            flash(data["sentence_error"][random.randint(
                0, (len(data["sentence_error"])) - 1)])

            return render_template('pages/home.html', search='Paris', grandpy='Error')

    json_data.close()


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
    app.run(debug=True, port=3000)
