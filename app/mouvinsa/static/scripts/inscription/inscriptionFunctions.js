jQuery(document).ready(function($) {
    $('#inscrivezVousHeader_DIV').on('click', function () {

        var $formDIV = $('#inscrivezVousContent_DIV');  
        var $triangleDIV = $('#triangleForm_DIV');

        if ($formDIV.is(':visible')) {
            $formDIV.hide();
            $triangleDIV.removeClass('triangle_DIV_rotated').addClass('triangle_DIV_begin');

        }
        else {
            $formDIV.show();

            $triangleDIV.removeClass('triangle_DIV_begin').addClass('triangle_DIV_rotated');
            
            //$triangleDIV.transition({ rotate: '90deg' }, 500, 'ease');
            
        }
    });
});

jQuery(document).ready(function($) {
    $('#descriptionProjetHeader_DIV').on('click', function () {

        var $descriptionDIV = $('#descriptionProjectDIV');
        var $triangleDIV = $('#triangle_DIV');

        if ($descriptionDIV.is(':visible')) {

            $descriptionDIV.hide();
            //$triangleDIV.transition({ rotate: '0deg' }, 500, 'ease');
            $triangleDIV.removeClass('triangle_DIV_rotated').addClass('triangle_DIV_begin');
        }
        else {

            $descriptionDIV.show();

            $triangleDIV.removeClass('triangle_DIV_begin').addClass('triangle_DIV_rotated');

            //$triangleDIV.transition({ rotate: '90deg' }, 500, 'ease');

        }
    });
});

jQuery(document).ready(function($) {

    $('#menuButton').on('click', function () {

        var $navigationMenu = $('#onclick-menu-content');

        if($navigationMenu.is(':visible')) {
            console.log('visible');
        }else{
            console.log('notVisible');
        }
    });
});

jQuery(document).ready(function($) {
    $('#categorieDIV').on('change', function () {

        console.log('categorieChanged');

        var $selectedCategorie = $('#categorie').val();

        if($selectedCategorie === 'Enseignant-Chercheur') {

            console.log('ens-cherch');

            $('#cycleDIV').hide();
            $('#anneeDIV').hide();
            $('#filiereDIV').hide();

            $('#positionDIV').show();
            $('#affiliationDIV').show();
            $('#departementDIV').show();


        }else if($selectedCategorie === 'Personnel IATOS') {

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
    });
});

jQuery(document).ready(function($) {
    $('#cycleDIV').on('change', function () {

        console.log('cycleChanged');

        var $selectedCycle = $('#cycle').val();

        if($selectedCycle === 'Premier') {

            console.log('Premier');

            $('#departementDIV').hide();
            $('#anneeDIV option[value="Troisieme"]').remove();
            $('#anneeDIV option[value="Quatrieme"]').remove();
            $('#anneeDIV option[value="Cinquieme"]').remove();

            $('#filiereDIV').show();

            addFirstSecondYear();

        }else if($selectedCycle === 'Second') {

            console.log('Second');

            $('#filiereDIV').hide();
            $('#anneeDIV option[value="Premiere"]').remove();
            $('#anneeDIV option[value="Deuxieme"]').remove();

            $('#departementDIV').show();

            addThirdFourthFifthYear();

        }else if($selectedCycle === '') {

            console.log('NONE');

            $('#filiereDIV').show();
            $('#departementDIV').show();

            addYears();
        }
    });

});

function addFirstSecondYear() {
    var itemExists = false;
    var txt = 'Premiere';

    $("#annee option").each(function() {
        if ($(this).text() == $.trim(txt)) {
            itemExists = true;
            console.log('No need to add Years');
        }
    });

    if (!itemExists) {
        $('#annee').append($('<option>', {
            value : 'Premiere',
            text : 'Premiere'
        }));

        $('#annee').append($('<option>', {
            value : "Deuxieme",
            text : "Deuxieme"
        }));
    }
}

function addThirdFourthFifthYear() {

    var itemExists = false;
    var txt = 'Troisieme';

    $("#annee option").each(function() {
        if ($(this).text() == $.trim(txt)) {
            itemExists = true;
            console.log('No need to add Years');
        }
    });

    if (!itemExists) {
        $('#annee').append($('<option>', {
            value : 'Troisieme',
            text : 'Troisieme'
        }));

        $('#annee').append($('<option>', {
            value : "Quatrieme",
            text : "Quatrieme"
        }));

        $('#annee').append($('<option>', {
            value : "Cinquieme",
            text : "Cinquieme"
        }));
    }
}

function addYears() {

    $('#anneeDIV option[value="Troisieme"]').remove();
    $('#anneeDIV option[value="Quatrieme"]').remove();
    $('#anneeDIV option[value="Cinquieme"]').remove();
    addFirstSecondYear();
    addThirdFourthFifthYear();
}

$(document).ready(function () {
    $('#anneeDIV').on('change', function () {

        console.log('annee Changed');

        var $selectedYear = $('#annee').val();

        if($selectedYear === 'Premiere' || $selectedYear === 'Deuxieme') {

            console.log('1 cycle');

            $('#cycleDIV option[value="Second"]').remove();

            $('#departementDIV').hide();

            $('#filiereDIV').show();

            addPremierCycle();

        }else if ($selectedYear === ''){

            console.log('No year selected');

            $('#departementDIV').show();

            $('#filiereDIV').show();

            addCycles();

        }else{

            console.log('2 cycle');

            $('#cycleDIV option[value="Premier"]').remove();

            addDeuxiemeCycle();

            $('#departementDIV').show();

            $('#filiereDIV').hide();

        }
    });
});

function addPremierCycle() {

    var itemExists = false;
    var txt = 'Premier';

    $("#cycle option").each(function() {
        if ($(this).text() == $.trim(txt)) {
            itemExists = true;
            console.log('No need to add Cycle');
        }
    });

    if (!itemExists) {
        $('#cycle').append($('<option>', {
            value : 'Premier',
            text : 'Premier'
        }));
    }
}

function addDeuxiemeCycle() {

    var itemExists = false;
    var txt = 'Second';

    $("#cycle option").each(function() {
        if ($(this).text() == $.trim(txt)) {
            itemExists = true;
            console.log('No need to add Cycle');
        }
    });

    if (!itemExists) {
        $('#cycle').append($('<option>', {
            value : 'Second',
            text : 'Second'
        }));
    }
}

function addCycles() {

    $('#cycleDIV option[value="Second"]').remove();

    addPremierCycle();
    addDeuxiemeCycle();
}

$(document).ready(function () {
    $('#filiereDIV').on('change', function () {

        console.log('filiere Changed');

        var $selectedFiliere = $('#filiere').val();

        if($selectedFiliere === '') {

            console.log('No Filiere Selected');

            $('#departementDIV').show();

            addDeuxiemeCycle();
            addThirdFourthFifthYear();

        }else{

            console.log('Filiere Selected');

            $('#cycleDIV option[value="Second"]').remove();

            $('#anneeDIV option[value="Troisieme"]').remove();
            $('#anneeDIV option[value="Quatrieme"]').remove();
            $('#anneeDIV option[value="Cinquieme"]').remove();

            $('#departementDIV').hide();

        }
    });
});

$(document).ready(function () {
    $('#departementDIV').on('change', function () {

        console.log('Departement Changed');

        var $selectedDepartement = $('#departement').val();

        if($selectedDepartement === '') {

            console.log('No Filiere Selected');

            if ($('#categorie').val() === 'Etudiant'){

                $('#filiereDIV').show();

                addCycles();
                addYears();
            }

        }else{

            console.log('Filiere Selected');

            $('#cycleDIV option[value="Premier"]').remove();

            $('#anneeDIV option[value="Premiere"]').remove();
            $('#anneeDIV option[value="Deuxieme"]').remove();

            $('#filiereDIV').hide();

        }
    });
});