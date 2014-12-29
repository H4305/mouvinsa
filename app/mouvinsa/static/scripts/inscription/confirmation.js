
$(document).ready(function(){
    $('#tab_title_confirmation a:first').tab('show');
    $('#tab_title_confirmation a').click(function (e) {
            e.preventDefault();
            $(this).tab('show');
    });
    $('.next_button').on('click',function(){
       if ($(this).text()=='Terminer'){
           window.location.href = "/";
       }
       else {
          $('#tab_title_confirmation li.active').next('li').children().first().tab('show');
       }
    });
});