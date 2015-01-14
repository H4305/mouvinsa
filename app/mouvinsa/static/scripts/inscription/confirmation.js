
$(document).ready(function(){
    var href = $('#tab_title_confirmation li.active a').attr('href');
    $(href).addClass('active');
    $('#tab_title_confirmation li.active a').tab('show');
    $('#tab_title_confirmation a').click(function (e) {
            e.preventDefault();
            $(this).tab('show');
    });
    $('.next_button').on('click',function(){
    if ($('#tab_title_confirmation li.active') != $('#tab_title_confirmation li').last()){
          $('#tab_title_confirmation li.active').next('li').children().first().tab('show');
    }
  });
});

function submitForm(id){
    document.getElementById(id).submit();
}