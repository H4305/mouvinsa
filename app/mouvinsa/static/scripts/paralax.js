/**
 * Created by vcaen on 01/03/2015.
 */
(function() {

    var header = $('header');

    $(window).scroll(function () {
        s = $(document).scrollTop();
       
        $(header).css("-webkit-transform", "translateY(" + (s * 0.4) + "px)");
        $(header).css("transform", "translateY(" + (s * 0.4) + "px)");
    });
})();