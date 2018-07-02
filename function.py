# coding: utf-8

import json
import os
import sys


def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    """ Just print fonction, without probleme of encodation from sql file."""
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        def f(obj): return str(obj).encode(
            enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)


def sequence_query(query):

    query = query + " "
    query_word = ""
    query_list = []
    pass_list = [" ", ".", ",", ";", "'", "-", "?", "\n", "\r"]

    for i in enumerate(query):
        if i[1] not in pass_list:
            query_word = query_word + i[1]
        else:
            if query_word != "":
                query_list.append(query_word)
                query_word = ""

    return query_list


def delete_useless_word(query_list):
    json_data = open('stopwords-fr.json', encoding='utf-8')
    data = json.load(json_data)
    query_list_2 = []
    query_search = ""
    for i in enumerate(query_list):
        if query_list[i[0]].lower() not in data:
            query_list_2.append(query_list[i[0]])
    while len(query_list_2) > 2:
        del query_list_2[len(query_list_2) - 1]
    for i in enumerate(query_list_2):
        if query_search == "":
            query_search = str(query_list_2[i[0]])
        else:
            query_search = query_search + "+" + str(query_list_2[i[0]])

    while query_search[0] == "+":
        query_search = query_search[1:]
    json_data.close()

    return query_search


def recuperate_number_wiki_page(search):
    os.system("curl -X GET \"https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&format=json\" --output fichier.json".format(search))
    json_data = open('fichier.json')
    data = json.load(json_data)
    variable = data["query"]["search"][0]["pageid"]
    json_data.close()
    os.remove('fichier.json')
    print("NUMBER OK")
    return variable


def recuperate_name_wiki_page(search):
    os.system("curl -X GET \"https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&format=json\" --output fichier2.json".format(search))
    json_data = open('fichier2.json')
    data = json.load(json_data)
    variable = data["query"]["search"][0]["title"]
    json_data.close()
    os.remove('fichier2.json')
    name_wiki_page = ""
    for i in enumerate(variable):
        if i[1] == " ":
            name_wiki_page = name_wiki_page + "_"
        else:
            name_wiki_page = name_wiki_page + i[1]
    print("NAME OK")
    return name_wiki_page


def recuperate_resume_wiki_page(name_wiki_page, number_wiki_page):
    os.system("curl -X GET \"https://fr.wikipedia.org/w/api.php?action=query&titles={}&prop=extracts&exsentences=4&format=json\" --output fichier4.json".format(name_wiki_page))
    json_data = open('fichier4.json')
    data = json.load(json_data)
    variable = data["query"]["pages"][str(number_wiki_page)]["extract"]
    json_data.close()
    os.remove('fichier4.json')
    return variable


def delete_balise_html(text_wiki_page):
    write = True
    text_wiki_second = ""
    text_wiki_third = ""
    text_wiki_forth = ""
    text_wiki_fifth = ""
    text_wiki_final = ""

    for i in enumerate(text_wiki_page):
        if i[1] == '<':
            write = False
        elif i[1] == '>':
            write = True
        else:
            write = write
        if write == True:
            text_wiki_second = text_wiki_second + i[1]

    for i in enumerate(text_wiki_second):
        if i[1] == '[':
            write = False
        elif i[1] == ']':
            write = True
        else:
            write = write
        if write == True:
            text_wiki_third = text_wiki_third + i[1]

    for i in enumerate(text_wiki_third):
        if i[1] == ']' or i[1] == '>':
            text_wiki_forth = text_wiki_forth
        else:
            text_wiki_forth = text_wiki_forth + i[1]

    for i in enumerate(text_wiki_forth):
        #        if i[1] == "↑":
        #            break
        if i[1] == "\n" and text_wiki_final[len(text_wiki_final) - 1] == "\n":
            text_wiki_final = text_wiki_final
        else:
            text_wiki_final = text_wiki_final + i[1]

#    for i in enumerate(text_wiki_fifth):
#        if i[1] == "\n" and text_wiki_final[len(text_wiki_final) - 1] != ".":
#           text_wiki_final = text_wiki_final + " :\n"
#        else:
#            text_wiki_final = text_wiki_final + i[1]

    while text_wiki_final.find("&#160;") != -1:
        print(text_wiki_final.find("&#160;"))
        text_wiki_final = text_wiki_final[:text_wiki_final.find(
            "&#160;")] + " " + text_wiki_final[(text_wiki_final.find("&#160;") + 6):]

    print("ERASE HTML OK")
    return text_wiki_final


def sequence_wiki_final(text_wiki_final):
    sequence = ""
    list_sequence = []

    for i in enumerate(text_wiki_final):
        if i[1] != "\n":
            sequence = sequence + i[1]
        else:
            list_sequence.append(sequence)
            sequence = ""

    return list_sequence


#variable = "Est-ce que tu peux me donner l'adresse de la cathédrale notre dame openclassrooms tour eiffel s'il te plait ?"

#resultat = sequence_query(variable)

# print(resultat)

#resultat_2 = delete_useless_word(resultat)

# print(resultat_2)

#resultat_3 = recuperate_number_wiki_page(resultat_2)

# print(resultat_3)

#resultat_3_2 = recuperate_name_wiki_page(resultat_2)

# print(resultat_3_2)

#resultat_4 = recuperate_resume_wiki_page(resultat_3_2, resultat_3)

# uprint(resultat_4)

#resultat_5 = delete_balise_html(resultat_4)

# uprint(resultat_5)

#resultat_6 = sequence_wiki_final(resultat_5)

# uprint(resultat_6)

# https://fr.wikipedia.org/w/api.php?action=query&titles=Cit%C3%A9_Paradis&prop=revisions&rvprop=content&format=json&formatversion=2
