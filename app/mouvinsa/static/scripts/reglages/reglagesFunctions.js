

jQuery(document).ready(function($) {
    $('#birthdate_button').on('click', function () {

        var $birthdateEditButton = $('#birthdate_button');
        var $birthdateInput = $('#birthdate');
        var $birthdateSpan = $('#date_span');

        $birthdateEditButton.hide();
        $birthdateSpan.hide();
        $birthdateInput.show();
    });
});

jQuery(document).ready(function($) {
    $('#sex_button').on('click', function () {

        var $sexEditButton = $('#sex_button');
        var $sexInput = $('#sex');
        var $sexSpan = $('#sex_span');

        $sexEditButton.hide();
        $sexInput.show();
        $sexSpan.hide();
    });
});

jQuery(document).ready(function($) {
    $('#weight_button').on('click', function () {

        var $weightEditButton = $('#weight_button');
        var $weightInput = $('#weight');
        var $weightSpan = $('#weight_span');

        $weightEditButton.hide();
        $weightInput.show();
        $weightSpan.hide();
    });
});

jQuery(document).ready(function($) {
    $('#height_button').on('click', function () {

        var $heightEditButton = $('#height_button');
        var $heightInput = $('#height');
        var $heightSpan = $('#height_span');

        $heightEditButton.hide();
        $heightInput.show();
        $heightSpan.hide();
    });
});






