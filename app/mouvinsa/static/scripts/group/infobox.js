/**
 * Created by vcaen on 25/02/2015.
 */

function slidshow() {
    $(".slideshow ul").delay(3000).animate({marginLeft: -590}, 900, 'swing', function () {
        $(this).css({marginLeft: 0}).find("li:last").after($(this).find("li:first"));
        slidshow();
    });
};

slidshow();




