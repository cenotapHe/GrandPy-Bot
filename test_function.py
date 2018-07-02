from function import uprint, sequence_query, delete_useless_word, recuperate_name_wiki_page, recuperate_number_wiki_page, recuperate_resume_wiki_page, delete_balise_html, sequence_wiki_final


def test_sequence_query():
	result = sequence_query("Tu connais Openclassrooms ?")
	assert result == ["Tu", "connais", "Openclassrooms"]


def test_delete_useless_word():
	result = delete_useless_word(["Tu", "connais", "Openclassrooms"])
	assert result == "Openclassrooms"


def test_recuperate_number_wiki_page():
	result = recuperate_number_wiki_page("Openclassrooms")
	assert result == 4338589


def test_recuperate_name_wiki_page():
	result = recuperate_name_wiki_page("Openclassrooms")
	assert result == "OpenClassrooms"


"""
def test_recuperate_resume_wiki_page():
	result = recuperate_resume_wiki_page("OpenClassrooms", 4338589)
	assert result == "<p><b>OpenClassrooms</b> est une école en ligne. Chaque visiteur peut à la fois être un lecteur ou un rédacteur. Les cours peuvent être réalisés aussi bien par des membres, par l'équipe du site, ou éventuellement par des professeurs d'universités ou de grandes écoles partenaires. Initialement orientée autour de la programmation informatique, la plate-forme couvre depuis 2013 des thématiques plus larges tels que le marketing, l'entrepreneuriat et les sciences.</p>"

"""


def test_delete_balise_html():
	result = delete_balise_html("<h1>Bonjour.</h1>")
	assert result == "Bonjour."


def test_2_delete_balise_html():
	result = delete_balise_html("Bonjour.[Wikipedia]")
	assert result == "Bonjour."


def test_3_delete_balise_html():
	result = delete_balise_html("Bonjour.&#160;")
	assert result == "Bonjour. "


def test_sequence_wiki_final():
	result = sequence_wiki_final("Bonjour.\nTu vas bien ?\nOui, merci.")
	assert result == ["Bonjour.", "Tu vas bien ?"]