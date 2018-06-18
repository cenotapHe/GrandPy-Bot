

var req = new XMLHttpRequest();

req.open("GET", "http://localhost:3000");

req.addEventListener("load", function () {

    if (req.status >= 200 && req.status < 400) { // Le serveur a réussi à traiter la requête

        var variableTest = String(req.responseText);

   		document.getElementsByTagName("body").innerHTML += variableTest;

    } else {

        // Affichage des informations sur l'échec du traitement de la requête

        console.error(req.status + " " + req.statusText);

    }

});

req.addEventListener("error", function () {

    // La requête n'a pas réussi à atteindre le serveur

    console.error("Erreur réseau");

});

req.send(null);



/*

// Exécute un appel AJAX GET

function ajaxGet(url) {

    var req = new XMLHttpRequest();

    req.open("GET", url);

    req.addEventListener("load", function () {

        if (req.status >= 200 && req.status < 400) {

            var variableTest = String(req.responseText);

            variableTest += "<p>Bonjour</p>";

   			document.getElementsByTagName("body").innerHTML = "<p>Bonjour</p>";

        } else {

            console.error(req.status + " " + req.statusText + " " + url);

        }

    });

    req.addEventListener("error", function () {

        console.error("Erreur réseau avec l'URL " + url);

    });

    req.send(null);

}

ajaxGet("http://localhost:3000");

*/