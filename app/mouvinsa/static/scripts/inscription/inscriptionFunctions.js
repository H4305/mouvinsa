jQuery(document).ready(function($) {
    showForm = function() {

        var $formDIV = $('#inscrivezVousContent_DIV');  
        var $triangleDIV = $('#triangleForm_DIV');

        if ($formDIV.is(':visible')) {
            // Slide away
            $formDIV.animate({bottom: -($formDIV.outerHeight() + 2)}, 'slow', function() {
                    $formDIV.hide();
                    //$triangleDIV.transition({ rotate: '0deg' }, 500, 'ease');
                    $triangleDIV.removeClass('triangle_DIV_rotated').addClass('triangle_DIV_begin');
                });
        }
        else {
            // Slide in
            $formDIV.show().animate({top: 0}, 'slow');

            $triangleDIV.removeClass('triangle_DIV_begin').addClass('triangle_DIV_rotated');
            
            //$triangleDIV.transition({ rotate: '90deg' }, 500, 'ease');
            
        }
    }
});

jQuery(document).ready(function($) {
    showDescription = function() {

        var $descriptionDIV = $('#descriptionProjectDIV');
        var $triangleDIV = $('#triangle_DIV');

        if ($descriptionDIV.is(':visible')) {
            // Slide away
            $descriptionDIV.animate({bottom: -($descriptionDIV.outerHeight() + 2)}, function() {
                    $descriptionDIV.hide();
                    //$triangleDIV.transition({ rotate: '0deg' }, 500, 'ease');
                    $triangleDIV.removeClass('triangle_DIV_rotated').addClass('triangle_DIV_begin');
                });
        }
        else {
            // Slide in
            $descriptionDIV.show().animate({top: 0});

            $triangleDIV.removeClass('triangle_DIV_begin').addClass('triangle_DIV_rotated');

            //$triangleDIV.transition({ rotate: '90deg' }, 500, 'ease');

        }
    }
});

jQuery(document).ready(function($) {
    clickMenu = function() {

        var $navigationMenu = $('#onclick-menu-content');

        if($navigationMenu.is(':visible')) {
            console.log('visible');
        }else{
            console.log('notVisible');
        }
    }
});

jQuery(document).ready(function($) {
    categorieChanged = function() {

        console.log('categorieChanged');

        var $selectedCategorie = $('#categorie').val();

        if($selectedCategorie === 'Enseignant-Chercheur') {

            console.log('ens-cherch');

            $('#cycleDIV').hide();
            $('#anneeDIV').hide();
            $('#filiereDIV').hide();

            $('#positionDIV').show();
            $('#affiliationDIV').show();


        }else if($selectedCategorie === 'Personnel BIATOS') {

            console.log('pers biatos');

            $('#cycleDIV').hide();
            $('#anneeDIV').hide();
            $('#filiereDIV').hide();
            $('#departementDIV').hide();

            $('#positionDIV').show();
            $('#affiliationDIV').show();

        }else if($selectedCategorie === 'Etudiant') {

            console.log('etu');

            $('#positionDIV').hide();
            $('#affiliationDIV').hide();

            $('#cycleDIV').show();
            $('#anneeDIV').show();
            $('#filiereDIV').show();
            $('#departementDIV').show();
        }
    }

});