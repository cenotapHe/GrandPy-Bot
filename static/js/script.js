function ajaxGet(url, data, callback) {

    var req = new XMLHttpRequest();

    req.open("POST", url);

    req.addEventListener("load", function () {

        if (req.status >= 200 && req.status < 400) {

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

    document.getElementById("map").innerHTML = "<iframe width=\"100%\" height=\"100%\" frameborder=\"0\" style=\"border:0\" src=\"https://www.google.com/maps/embed/v1/place?key=AIzaSyBtKZJuJonuqxYsm_f6BTcvP3UTQpzZ8gU&q=" + responseList[1] + "Paris+France\" allowfullscreen></iframe>"

    document.getElementById("image").innerHTML = "</br><img src=\"/static/images/grandpy_" + responseList[0] + ".png\" width=\"120px\" height=\"120px\" />"


    document.getElementById("afficher").innerHTML = "</br>" + responseList[2]; 

}



var boutonElt = document.getElementById("formulaire");

boutonElt.addEventListener("click", function (e) {

	// Récupération de la question tapé par l'utilisateur
	var queriesElt = document.getElementById("msg");
	var dataSend = (queriesElt.value);

	ajaxGet("http://localhost:5000/results/?query=" + dataSend, dataSend, afficher);

    e.preventDefault();

});