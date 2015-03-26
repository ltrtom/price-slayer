import re
h = """
<!DOCTYPE html>
<html lang="fr">
    <head>
        <title>Welcome!</title>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!--[if lt IE 9]>
            <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
        <link rel="icon" type="image/x-icon" href="/bo/31ae08103366/favicon.ico" />
                <link rel="stylesheet" type="text/css" href="/bo/31ae08103366/css/bootstrap_iscustom.css">
        <link rel="stylesheet" type="text/css" href="/bo/31ae08103366/css/bootstrap-glyphicons.css">
        <link rel="stylesheet" type="text/css" href="/bo/31ae08103366/css/backshop.css">
        <link rel="stylesheet" type="text/css" href="/bo/31ae08103366/css/fontello.css">
        <link rel="stylesheet" type="text/css" href="/bo/31ae08103366/css/style.css">
                        <script src="/bo/31ae08103366/js/jquery-2.0.3.js"></script>
        <script src="/bo/31ae08103366/js/animation-nav.js"></script>
        <script src="/bo/31ae08103366/bootstrap/js/bootstrap.js"></script>
            </head>
    <body>
        <div id="mainwrap">
            <header>
                <h2 style="cursor: pointer;" onclick="window.location.href='/bo/31ae08103366/';">Backshop</h2>
                <h3>
                                            <a href="/bo/31ae08103366/login" class="btn btn-bs">Login</a>
                                    </h3>
            </header>
                        <section>
            <div class="panel panel-default panel-center">
    <div class="panel-heading">
        <h3 class="panel-title text-center">


                Connexion
                                    </h3>
    </div>
    <div class="panel-body">
        <form action="/bo/31ae08103366/login_check" method="post">
        <form>
        <ul class="form">
                <li>
                    <input type="hidden" name="_csrf_token" value="6af350357344b4df3ef42e0668fc92ef29f15e6e" />
                    <input class="form-control"  type="text" id="username" value="thomas.letelvvvvlier_t@y-nov.com" name="_username" placeholder="email" required="required">
                </li>
                <li>
                    <input type="password" class="form-control"  id="password" name="_password" placeholder="Mot de passe" required="required">
                </li>
                <li>
                    <label>Se souvenir de moi</label>
                    <input type="checkbox" id="remember_me" name="_remember_me" class="pull-right" value="on">
                </li>
                <li>
                    <input type="submit" id="_submit" name="_submit" class="btn btn-bs btn-block" value="Se connecter"/>
                </li>
                <li class="other-links">
                    <a href="/bo/31ae08103366/register/"><h5>Créer un compte</h5></a>
                    <a href="/bo/31ae08103366/resetting/request"><h5>Mot de passe oublié</h5></a>
                </li>
                                           </ul>
        </form>
    </div>
</div>
            </section>
        </div>
    </body>
</html>"""

print(re.sub(r'(<!--[^--]*-->)', '', h))








