from function import sequence_query, delete_useless_word, recuperate_name_wiki_page, recuperate_number_wiki_page, recuperate_resume_wiki_page, delete_balise_html, sequence_wiki_final


def test_sequence_query():
    """ Test the sequence of a query."""
    result = sequence_query("Tu connais Openclassrooms ?")
    assert result == ["Tu", "connais", "Openclassrooms"]


def test_delete_useless_word():
    """ Test the elimination of useless word."""
    result = delete_useless_word(["Tu", "connais", "Openclassrooms"])
    assert result == "Openclassrooms"


def test_recuperate_number_wiki_page():
    """ Test the recuperation of the number of a wikipage."""
    result = recuperate_number_wiki_page("Openclassrooms")
    assert result == 4338589


def test_recuperate_name_wiki_page():
    """ Test the recuperation of the name of a wikipage."""
    result = recuperate_name_wiki_page("Openclassrooms")
    assert result == "OpenClassrooms"


def test_delete_balise_html():
    """ Test the deletion of the html balise."""
    result = delete_balise_html("<h1>Bonjour.</h1>")
    assert result == "Bonjour."


def test_2_delete_balise_html():
    """ Test the deletion of comment on wiki article."""
    result = delete_balise_html("Bonjour.[Wikipedia]")
    assert result == "Bonjour."


def test_3_delete_balise_html():
    """ Test the deletion of the special character useless."""
    result = delete_balise_html("Bonjour.&#160;")
    assert result == "Bonjour. "


def test_sequence_wiki_final():
    """ Test the final page setting."""
    result = sequence_wiki_final("Bonjour.\nTu vas bien ?\nOui, merci.")
    assert result == ["Bonjour.", "Tu vas bien ?"]
