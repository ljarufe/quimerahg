/*

* ------------------------------------------------------------------------------
* jqPopin: Popin para jQuery
*
* Popin fixed colocado al medio de la pantalla sobre todos los elementos, coloca
* un div con opacidad sobre los demás elementos
* ------------------------------------------------------------------------------
* Autor: Luis Jarufe
* Versión: 0.1
*
* Las opciones son:
* trigger: Elemento del DOM que activa el popin
* close: Elemento del DOM que cierra el popin
*
* Ejemplo:
* 1. Es necesario añadir la hoja de estilo jquery.jqpopin.css
*
* 2. Para utilizarlo sobre un elemento del DOM
* $("#id_popin").jqPopin({trigger: $("#id_trigger"), close: $("#id_close")});
*
* 3. Se puede acceder a las funciones para mostrar y ocultar el popin
* $("#id_popin").jqpopin_show();
* $("#id_popin").jqpopin_close();
*
* */

(function($) {
    $.fn.jqPopin = function(user_options) {
        // Opciones del usuario
        var options = $.extend({
            trigger: false,
            close: false
        }, user_options);

        // Propiedades del popin
        var popin = this;
        popin.addClass("jqpopin_frame");

        // div para apagar las luces, se coloca una sola vez si hay mas de un
        // popin en la misma página
        if($(".jqpopin_lights_out").length < 1) {
            popin.parents("div:first").prepend("<div class='jqpopin_lights_out'></div>");
        }
        var lights_out = $(".jqpopin_lights_out");

        // Posición en la pantalla
        var left = ($(window).width() - popin.width())/2;
        popin.css("left", left.toString() + "px");
        var top = ($(window).height() - popin.height())/3;
        popin.css("top", top.toString() + "px");
        options.close.css("cursor", "pointer");

        // TODO: animar segun una opcion animate
        var jqpopin_show = function() {
            lights_out.show();
            popin.show();
        };

        var jqpopin_close = function() {
            popin.hide();
            lights_out.hide();
        };

        if(options.trigger) {
            options.trigger.click(function() {
                jqpopin_show();
            });
        }

        if(options.close) {
            options.close.click(function() {
                jqpopin_close();
            });
        }

        lights_out.click(function() {
            jqpopin_close();
        });

        $("html").keydown(function(event){
            if(event.keyCode == '27') {
                jqpopin_close();
            }
        });
    }
})(jQuery);