<!DOCTYPE html>
<html>
<head>
    <title>{{title}}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="/css/ini.css">
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
        crossorigin="anonymous">
    
    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp"
        crossorigin="anonymous">
        
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
        crossorigin="anonymous"></script>
    <script src="/js/ini.js"></script>
</head>
<body>
    <div class="navbar-wrapper">
        <div class="container-fluid">  
            <nav class="navbar sticky-top">
                <div class="container-fluid">
                    <div class="navbar-header">
                        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false"
                            aria-controls="navbar">
                            <span class="sr-only">Toggle navigation</span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                        <a class="navbar-brand" href="#">Seguimiento Proyectos</a>
                    </div>
                    <div id="navbar" class="navbar-collapse collapse">    
                        <ul class="nav navbar-nav">
                            <li class="active">
                                <a href="/">Inicio</a>
                            </li>
                            <li>
                                <a href="/projects">Proyectos</a>
                            </li>
                        </ul>
                        <ul class="nav navbar-nav pull-right">
                            <li class="dropdown">
                                <a class="dropdown-toggle active" data-toggle="dropdown" 
                                href="#" role="button" aria-haspopup="true" 
                                aria-expanded="false">
                                    Configuración
                                    <span class="caret"></span>
                                </a>
                                <ul class="dropdown-menu">
                                    <li><a class="dropdown-item" href="/config/parameterization">Parametrizar</a></li>
                                    <li><a class="dropdown-item" href="/config/security">Usuarios</a></li>
                                    <div class="dropdown-divider"></div>
                                    <li><a class="dropdown-item" href="/lol">Personalizar</a></li>
                                </ul>
                            </li>
                            <li>
                                <a href="/logout">Salir</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    </div>
    <div class="container-fluid">
        {{!base}}
    </div>
</body>
</html>