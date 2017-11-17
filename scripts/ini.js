( function() {

    $( document ).ready( init );

    function init() {
        setSendEvent()
    }

    function setSendEvent() {
        var buttons = $( "[data-btn]" );
        buttons.click( send );
    }

    function send() {
        var self = $( this );
        var link = self.data("link");
        var id = self.data( "id" );

        var form = $( "<form method='POST'></form>" );
            form.attr( "action", link );

        if( !!id ) {
            var id_input = $( "<input type='hidden' value='" + id + "' id='id' name='id' />" );
            form.append( id_input );
        }
        
        $( "body" ).append( form );
        
        form.submit();
    }

} () );