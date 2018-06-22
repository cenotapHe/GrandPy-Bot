
function ajaxGet(url, callback) {
	
	var req = new XMLHttpRequest();
	req.open("POST", url);
	req.addEventListener("load", function() {
		// if no errors occur
		if (req.status >= 200 && req.status < 400) {
			global_response = JSON.stringify(req.responseText)
			global_response = JSON.parse(global_response)
			response = global_response.response
			callback(response, global_response);
		} else {
			console.error(req.status + " " + req.statusText + " " + url);
		}
	});
	req.addEventListener("error", function() {
		console.error("Network error in URL: " + url);
	});
	req.send(null);
}




function display(response, global_response) {

	document.getElementById("testtest").innerHTML = global_response;

	
}

/*
var url = "/";

function clic() {

	ajaxGet(url, display);

	console.log("test");

	e.preventDefault();

}

var boutonElt = document.getElementById("formulaire");

boutonElt.addEventListener("click", clic);

*/

var url = encodeURI("/");

var form = document.querySelector("form");

form.addEventListener("submit", function (e) {

	ajaxGet(url, display);

    console.log(document);

	e.preventDefault();

});