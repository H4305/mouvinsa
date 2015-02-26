/**
 * Created by vcaen on 25/02/2015.
 */

slidshow = function() {
    $(".slideshow ul").animate({marginLeft: -590}, 700, function () {
        $(this).css({marginLeft: 0}).find("li:last").after($(this).find("li:first"));
        slidshow();
    });
}
