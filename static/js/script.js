// appel AJAX POST
function ajaxGet(url, data, callback) {

    var req = new XMLHttpRequest();

    req.open("POST", url);

    req.addEventListener("load", function () {

        // with no error status
        if (req.status >= 200 && req.status < 400) {

            callback(req.responseText);

        } else {

            console.error(req.status + " " + req.statusText + " " + url);

        }

    });

    // display error if the HTTP status is not good
    req.addEventListener("error", function () {

        console.error("Erreur réseau avec l'URL " + url);


    });

    req.send(data);

}


// this function take the return from flask, interprete it, and display it on HTML
function display(reponse) {

    var delimitate = "###";

    var responseList = reponse.split(delimitate);

    console.log(responseList);

    document.getElementById("map").innerHTML = "<iframe width=\"100%\" height=\"100%\" frameborder=\"0\" style=\"border:0\" src=\"https://www.google.com/maps/embed/v1/place?key=AIzaSyBtKZJuJonuqxYsm_f6BTcvP3UTQpzZ8gU&q=" + responseList[1] + ",Paris+France\" allowfullscreen></iframe>"

    document.getElementById("image").innerHTML = "</br><img src=\"/static/images/grandpy_" + responseList[0] + ".png\" width=\"120px\" height=\"120px\" />"

    document.getElementById("display").innerHTML = "</br>" + responseList[2];

}


// make a button variable for launch AJAX
var boutonElt = document.getElementById("form");

boutonElt.addEventListener("click", function (e) {

	var queriesElt = document.getElementById("msg");
	var dataSend = (queriesElt.value);

   	ajaxGet("https://my-grandpy-bot.herokuapp.com/results/?query=" + dataSend, dataSend, display);

    e.preventDefault();

});