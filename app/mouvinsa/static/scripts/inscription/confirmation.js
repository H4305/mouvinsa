
$(document).ready(function(){
    var href = $('#tab_title_confirmation li.active a').attr('href');
    $(href).addClass('active');
    $('#tab_title_confirmation li.active a').tab('show');
    $('#tab_title_confirmation a').click(function (e) {
            e.preventDefault();
            $(this).tab('show');
    });
    $('.next_button').on('click',function(){
        if ($(this).text() != 'Terminer') {
            $('#tab_title_confirmation li.active').next('li').children().first().tab('show');
        }
        else {
            alert('Vous pouvez vous connecter avec votre login.');
            window.location = "/login";
        }
    });
    $('.prev_button').on('click',function(){
          $('#tab_title_confirmation li.active').prev('li').children().first().tab('show');
    });
    $('#btn_choisir, #divPhotoPreview img').on('click',function(){
        $("#image_upload").trigger('click');
    });
    $('#image_upload').on('change',function() {
            previewPhoto(this);
            var filepath = $(this)[0].files[0].name;
            var filename = filepath.substring(filepath.lastIndexOf('\\') + 1);
            $('.photoField_ERRORS').empty();
            $('#imgFileName').html(filename);
    });
    setTimeout(function(){
        $('.photoField_MESSAGE, .confirmationField_MESSAGE').fadeOut(5000)
    },1000);

});

function submitForm(id){
    document.getElementById(id).submit();
}

function previewPhoto(input){
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#divPhotoPreview img').attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function submitImageForm(id){
    if ($('#image_upload')[0].files && $('#image_upload')[0].files[0]){
        var image_file = $('#image_upload')[0].files[0],
        image_size = image_file.size,
        image_name = image_file.name,
        image_ext = image_name.substring(image_name.lastIndexOf('.') + 1),
        list_allowed_ext = ["jpg","jpeg","png"];
        if(image_size > 1 * 1024 * 1024) {
            $('.photoField_ERRORS').html('<li>La taille de l\'image doit être inférieure à 1 Mo.</li>');
        }
        else if ($.inArray(image_ext,list_allowed_ext)== -1) {
            $('.photoField_ERRORS').html('<li>La photo doit être en format: jpg, jpeg, png.</li>');
        }
        else {
            submitForm(id);
        }
    }
    else{
        $('.photoField_ERRORS').html('<li>Veuillez choisir votre photo.</li>');
    }
}