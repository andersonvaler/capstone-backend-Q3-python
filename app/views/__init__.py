from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint


def init_app(app: Flask):
    from .signup_views import bp as bp_signup
    from .endereco_view import bp as bp_endereco
    from .login_views import bp as bp_login
    from .carrinho_views import bp as bp_carrinho
    from .produtos_views import bp as bp_product
    from .home_view import bp as bp_home
    from .vendas_views import bp as bp_vendas
    from .compras_views import bp as bp_compras
    from .categorias_views import bp as bp_categorias
    from .perfil_views import bp as bp_perfil

    app.register_blueprint(bp_product)
    app.register_blueprint(bp_signup)
    app.register_blueprint(bp_login)
    app.register_blueprint(bp_endereco)
    app.register_blueprint(bp_carrinho)
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_vendas)
    app.register_blueprint(bp_compras)
    app.register_blueprint(bp_categorias)
    app.register_blueprint(bp_perfil)

    SWAGGER_URL = '/swagger'
    API_URL = '../static/swagger.yaml'
    swaggeruri_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
        API_URL,
        config={
            'app_name': "KLCHAT"
        }
    )
    app.register_blueprint(swaggeruri_blueprint, url_prefix=SWAGGER_URL)