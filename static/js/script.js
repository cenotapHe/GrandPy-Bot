function ajaxGet(url, data, callback) {

    var req = new XMLHttpRequest();

    req.open("POST", url);

    req.addEventListener("load", function () {

        if (req.status >= 200 && req.status < 400) {

            // Appelle la fonction callback en lui passant la réponse de la requête

            callback(req.responseText);

        } else {

            console.error(req.status + " " + req.statusText + " " + url);

        }

    });

    req.addEventListener("error", function () {

        console.error("Erreur réseau avec l'URL " + url);


    });

    req.send(data);

}


function afficher(reponse) {

    var delimitate = "###";

    var responseList = reponse.split(delimitate);

    console.log(responseList);

    document.getElementById("map").innerHTML = "</br><iframe width=\"600\" height=\"450\" frameborder=\"0\" style=\"border:0\" src=\"https://www.google.com/maps/embed/v1/place?key=AIzaSyBtKZJuJonuqxYsm_f6BTcvP3UTQpzZ8gU&q=" + responseList[1] + "Paris+France\" allowfullscreen></iframe>"

    document.getElementById("image").innerHTML = "</br><img src=\"/static/images/grandpy_" + responseList[0] + ".png\" width=\"10%\" height=\"10%\" />"

	document.getElementById("afficher").innerHTML = responseList[2];

}



//req.open("POST", "http://localhost:5000");

var boutonElt = document.getElementById("formulaire");


// Gestion de l'événement indiquant la fin de la requête

boutonElt.addEventListener("click", function (e) {

	// Récupération de la question tapé par l'utilisateur
	var queriesElt = document.getElementById("msg");
	var dataSend = (queriesElt.value);

	ajaxGet("http://localhost:5000/results/?query=" + dataSend, dataSend, afficher);

    e.preventDefault();

});