jQuery(document).ready(function($) {
    showForm = function() {

        var $formDIV = $('#inscrivezVousContent_DIV');  
        var $triangleDIV = $('#triangle_DIV'); 

        if ($formDIV.is(':visible')) {
            // Slide away
            $formDIV.animate({bottom: -($formDIV.outerHeight() + 2)}, function() {
                    $formDIV.hide();
                    //$triangleDIV.transition({ rotate: '0deg' }, 500, 'ease');
                    $triangleDIV.removeClass('triangle_DIV_rotated').addClass('triangle_DIV_begin');
                });
        }
        else {
            // Slide in
            $formDIV.show().animate({top: 0});

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
