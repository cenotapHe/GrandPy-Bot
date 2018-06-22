var variable = "";

// Création d'une requête HTTP

var req = new XMLHttpRequest();

// Requête HTTP GET synchrone vers le fichier langages.txt publié localement

req.open("POST", "http://localhost:5000");

var boutonElt = document.getElementById("formulaire");


// Gestion de l'événement indiquant la fin de la requête

boutonElt.addEventListener("click", function () {

	if (req.status >= 200 && req.status < 400) {

		// Récupération de la question tapé par l'utilisateur
		var queriesElt = document.getElementById("msg");
		//console.log(queriesElt.value);

		variable = queriesElt.value;

	    // Affiche la réponse reçue pour la requête
	    console.log(req.responseText);

	    alert("clic !");

	} else {

		// Affichage des informations sur l'échec du traitement de la requête

        console.error(req.status + " " + req.statusText);

        alert("clic autre !");

	}

	req.addEventListener("error", function () {

	    // La requête n'a pas réussi à atteindre le serveur

	    console.error("Erreur réseau");

	});

	console.log(variable);
	// Envoi de la requête
	req.send(variable);


});

