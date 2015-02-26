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
    var nombreDePasFaits = $( 'nbPas').val();

    var clock = $('.your-clock').FlipClock(nombreDePasFaits, {
        // ... your options here
        countdown: true,
        clockFace: 'Counter'
    });

});