$(document).ready(function(){

    /**
     * Show the input field for each row
     */
    (function(){
        $('table.setting tr').each(function(index, elem) {
            $(elem).on('click','.toggle-display', function(){
                console.log("click");
                $(elem).find('.span-visible').hide();
                $(elem).find('input, select').show();
                $(elem).find('button.annuler, button.valider').show();
            });
        });
    })();

    /**
     * Cancel the modification
     */
     (function(){
        $('table.setting tr').each(function(index, elem) {
            $(elem).on('click','button.annuler', function(){
                console.log("annuler");
                $(elem).find('.span-visible').show();
                $(elem).find('input, select').hide();
                $(elem).find('button.annuler, button.valider').hide();
                text = $(elem).find('.span-visible').text();
                $(elem).find('input, select').first().val($.trim(text));
            });
        });
    })();

    /**
     * Validate the modification
     */
    (function(){
        $('table.setting tr').each(function(index, elem) {
            $(elem).on('click','button.valider', function(){
                console.log("valider");
                $(elem).find('.span-visible').show();
                $(elem).find('input, select').hide();
                $(elem).find('button.annuler, button.valider').hide();
                text = $(elem).find('input, select').first().val();
                $(elem).find('.span-visible').text($.trim(text));
                $(elem).find('.span-visible').css("font-weight","Bold");
            });
        });
    })();
});
