
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
            var filepath = $('#image_upload').val();
            var filename = filepath.substring(filepath.lastIndexOf('\\') + 1);
            $('.photoField_ERRORS').remove();
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