( function() {

    "use strict";

    var action_load = null;

    $( document ).ready( init );

    function init() {
        $( "body" ).checkEvents();
    }

    function setSendEvent( element ) {
        var buttons = $( element ).find( "[data-btn]" );
        var forms = $( element ).find( "[data-form]" );
        buttons.click( send );
        forms.submit( submit );
    }

    function send() {
        var self = $( this );
        var link = self.data("link");
        var method = self.data( "method" );
        var reload = self.data("reload" );
        var id = self.data( "id" );

        var formMethod = method || "POST";

        var form = $("<form method='" + formMethod + "'></form>" );
            form.attr( "action", link );
            form.data( "reload", reload );

        if( !!id ) {
            var id_input = $( "<input type='hidden' value='" + id + "' id='id' name='id' />" );
            form.append( id_input );
        }

        form.on( 'submit', submit );
        
        $( "body" ).append( form );
        
        form.submit();
    }

    function submit( e ) {
        var form = $( this );
        var content = $( "div#action" );
        var ajax = false;

        if ( content.length > 0 ) {
            e.preventDefault();
            e.stopPropagation();
            ajax = true;
        }

        if( ajax ) {
            sendAjax( form );
        } else {
            form.submit();
        }
    }

    function sendAjax( form ) {
        var data = form.serialize();
        var url = form.attr( "action" );
        var method = form.attr("method");
        
        action_load = form.data( "reload" );

        var ajax = $.ajax( {
            url: url,
            data: data,
            type: method
        } );

        ajax.done( ajaxCallback );
        ajax.fail( errorCallback );
    }

    function ajaxCallback( response, status, request ) {
        if ( !!request.responseJSON ) {
            if( response.error > 0 ) {
                alert( response.text );
            } else {
                if( !!action_load ) {
                    $( "div#main" ).load( action_load, "", divLoaded );
                    $( "div#action" ).empty();
                }
            }
        } else {
            var content = $( "div#action" );
            content.html( response );
            content.checkEvents();
        }
    }
    
    function divLoaded() {
        $( "div#main" ).checkEvents();
    }

    function errorCallback( err, xht, msj ) {
        console.error( err, xht, msj );
    }

    $.fn.extend( {
        checkEvents: function() {
            return this.each( function() {
                setSendEvent( this );
            } );
        }
    } );

} () );