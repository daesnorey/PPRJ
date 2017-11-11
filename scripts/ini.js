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

        var form = $( "<form method='POST'></form>" );
            form.attr( "action", link );
        
        $( "body" ).append( form );
        
        form.submit();
    }

} () );