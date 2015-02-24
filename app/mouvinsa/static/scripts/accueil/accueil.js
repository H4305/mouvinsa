/**
 * Created by marcomontalto on 24/02/15.
 */

jQuery(document).ready(function($) {
    $('#menu-deroulant').on('click', function () {

        var $menuContainer = $('#menu-container');

        if ($menuContainer.is(':visible')) {
            $menuContainer.hide();

        }
        else {
            $menuContainer.show();
        }

        event.stopPropagation();
    });
});

$(document).click(function(event) {
    if(!$(event.target).closest('#menu-container').length && !$(event.target).closest('#menu-deroulant').length) {
        if($('#menu-container').is(":visible")) {
            $('#menu-container').hide()
        }
    }
})

$(document).ready(function() {

    //en moyenne 8000 pas / jour * 100 personnes = 800 000 pas/jour = aprox 10 pas par seconde
    //= une incremenatation tous les 100 ms
    var nombreDePasFaits;
    /*
        Solution 1 on récupere le nombres réel de pas faits
        TODO - à recuperer de la base de données
    */

    /*  // Solution 2 - on calcule le temps passé depuis le début du projet et
            //  on fait une estimation de nombre de pas faits

        var end = Date.parse("26 Jan 2015 8:00:00 +0100");
        var now = Date.now();
        nombreDePasFaits = (now-end) * 10;
    */

    //Solution 3 on pars de 100 000 000
    nombreDePasFaits = 100000000;

    var clock = $('.your-clock').FlipClock(nombreDePasFaits, {
        // ... your options here
        countdown: true,
        clockFace: 'Counter'
    });
    setTimeout(function() {
        setInterval(function() {

            clock.increment();
            //nombreDePasFaits ++;
            //clock.setValue(nombreDePasFaits);
        }, 100);
    });

    var lesEquipes = [{
        id: 3,
        nom:  "grp1",
        pas: 2000
    }, {
        id: 5,
        nom:  "group34343",
        pas: 4000
    }, {
        id: 7,
        nom:  "rteggg",
        pas: 400
    }, {
        id: 11,
        nom:  "gergebet",
        pas: 1000
    }, {
        id: 15,
        nom: "brbrbn",
        pas: 500000
    }, {
        id: 18,
        nom:  "Boi",
        pas: 5000
    }
    ];

    var table = $("#teamsTable");
    var nombreEquipes = lesEquipes.length;


    var tableHtml = "<tr>";
    var photoURL;
    var numberSteps;
    var teamName;

    for ( var i = 0; i < nombreEquipes; i++ ) {

        numberSteps = lesEquipes[i].pas;
        teamName = lesEquipes[i].nom;
        tableHtml += "<td><table class='teamTable'><td class = 'team'><div class='imgIdGroup'>" + lesEquipes[i].id + "</td><td><ul class='listDescriptionTeam'><li class='teamName'>" +
                    teamName +  "</li>" + "<li class='steps'>" + numberSteps + " pas</li>" + "</ul></td></table></td>";

        if(i%3 == 2) {
            tableHtml += "</tr><tr>";
        }
    }

    tableHtml += "</tr>";
    table.html(tableHtml);


});