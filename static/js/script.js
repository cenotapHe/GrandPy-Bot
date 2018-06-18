/*
var req = new XMLHttpRequest();
// La requête est asynchrone lorsque le 3ème paramètre vaut true ou est absent
req.open("GET", "http://localhost:3000");
// Gestion de l'événement indiquant la fin de la requête
req.addEventListener("load", function () {
    // Affiche la réponse reçue pour la requête
    var variableTest = String(req.responseText);

    console.log(variableTest);

    document.getElementById("afficher").innerHTML += variableTest;

});
req.send(null);

*/
// Exécute un appel AJAX GET

var count = 0;

function ajaxGet(url) {

    var req = new XMLHttpRequest();

    req.open("GET", url);

    req.addEventListener("load", function () {

        if (req.status >= 200 && req.status < 400) {

            var variableTest = String(req.responseText);

    		document.getElementById("afficher").innerHTML += variableTest;


        } else {

            console.error(req.status + " " + req.statusText + " " + url);

        }

    });

    req.addEventListener("error", function () {

        console.error("Erreur réseau avec l'URL " + url);

    });

    req.send(null);

}

/*

ajaxGet("http://localhost:3000");

function clic() {

	ajaxGet("http://localhost:3000");

	console.log("test");

}

var boutonElt = document.getElementById("formulaire");

boutonElt.addEventListener("click", clic);

*/

var form = document.querySelector("form");

form.addEventListener("submit", function (e) {

	ajaxGet("http://localhost:3000");

	//e.preventDefault();

});

