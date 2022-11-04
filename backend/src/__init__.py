"""Flask app factory"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow
import connexion


# from src.uni.routes.study_disciplines_routes import (
#    StudyDisciplineIdApi,
#    StudyDisciplineNameApi,
#    StudyDisciplinesApi,
# )
from src.uni.data_loader import fill_tables
from database import Database


# from flask_oidc import OpenIDConnect
# from okta.client import Client as UsersClient


# Globally accessible libraries
# db = SQLAlchemy()
db = Database()
migrate = Migrate()
ma = Marshmallow()


def create_app(config_class="config.DevConfig"):
    "initiate core application"
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_class)
    print(app.config["DEBUG"])

    CORS(app)
    api = Api(app)

    """initialize plugins"""
    # from src.uni.models.uni_model import Uni
    # from src.uni.models.voivodeship_model import Voivodeship

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    with app.app_context():
        # include routes
        # from . import routes
        # from src.uni.resources.uni_routes import Vo
        from src.uni.resources.voivodeship_routes import (
            VoivodeshipIdApi,
            # VoivodeshipNameApi,
            VoivodeshipsApi,
        )

        from src.uni.routes.study_disciplines_routes import (
            StudyDisciplineIdApi,
            StudyDisciplineNameApi,
            StudyDisciplinesApi,
        )
        from src.uni.routes.studies_routes import (
            StudyIdApi,
            StudyNameApi,
            StudiesApi,
            StudyLevelsApi,
        )

        from src.uni.routes.uni_routes import (
            UniIdApi,
            UniNameApi,
            UnisApi,
            CitiesApi,
        )

        api.add_resource(VoivodeshipIdApi, "/voivodeships/<id>")
        # api.add_resource(VoivodeshipNameApi,'/voivodeships/<name>')
        api.add_resource(VoivodeshipsApi, "/voivodeships")

        api.add_resource(
            StudyDisciplineIdApi, "/study_disciplines/<study_discipline_id>"
        )
        api.add_resource(
            StudyDisciplineNameApi, "/study_disciplines/name/<study_disciline_name>"
        )
        api.add_resource(StudyDisciplinesApi, "/study_disciplines")

        api.add_resource(StudyIdApi, "/studies/<study_id>")
        api.add_resource(StudyNameApi, "/studies/name/<study_name>")
        api.add_resource(StudiesApi, "/studies")
        api.add_resource(StudyLevelsApi, "/studies/levels")

        api.add_resource(UniIdApi, "/unis/<uni_id>")
        api.add_resource(UniNameApi, "/unis/name/<uni_name>")
        api.add_resource(UnisApi, "/unis")
        api.add_resource(CitiesApi, "/unis/cities")

        # from src.uni.models.uni_model import Uni
        # from src.uni.models.voivodeship_model import Voivodeship

        # if Uni is None:
        #    print("None?????????????????/")

        # db.create_all()
        print("db=====================================================")
        print(db.engine.url.database)

        # fill_tables(db.engine.url.database)

    return app


# @app.before_first_request
# @with_appcontext
# def create_tables():
#    db.create_all()

"""

app.config["OIDC_CLIENT_SECRETS"] = "client_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["SECRET_KEY"] = "super secret"
oidc = OpenIDConnect(app)
# app.config["SECRET_KEY"] = "{{ LONG_RANDOM_STRINGS }}"
# okta_client = UsersClient("{{ OKTA_ORG_URL }}", "{{ OKTA_AUTH_TOKEN }}")
okta_client = UsersClient(
    {
        "orgUrl": "https://dev-73352242.okta.com/",
        "token": "00wypJxwIxxILACoZp3bnbxPFHh34UN1khVKFdN55e",
    }
)
# okta_client = UsersClient(
#    os.environ.get("OKTA_ORG_URL"), os.environ.get("OKTA_AUTH_TOKEN")
# )
# okta_client = UsersClient(app.config["OKTA_ORG_URL"], app.config["OKTA_AUTH_TOKEN"])

# app.config["DEBUG"] = DEBUG


@app.before_request
def inject_user_into_each_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None
    print(g.user)


# @app.route("/greet")
# @oidc.require_login
def greet():
    time = datetime.now().hour
    if time >= 0 and time < 12:
        return "Good Morning!"
    if time >= 12 and time < 16:
        return "Good Afternoon!"

    return "Good Evening!"


@app.route("/login")
@oidc.require_login
def login():
    return redirect(url_for(".greet"))


@app.route("/logout")
def logout():
    oidc.logout()
    return redirect(url_for(".index"))


# api.add_resource(UniList, '/unis')


@app.route("/")
def index():
    "function for initial testing"
    return "Hello from Wroclaw Portal"


@app.route("/unis/f", methods=["GET", "POST"])
def unis_list():
    "get univercity list"
    # uniSearchWord=request.args.get("query")
    if request.method == "GET":
        # read
        # unis=unis_collection.find({})
        # return jsonify([uni for uni in unis ])
        uniss = [
            {
                "id": 1,
                "title": "Uni 1",
                "logo": "https://avatars.mds.yandex.net/i?id=3879b1e342099fb44cbf3565b1e6f384-5313761-images-thumbs&n=13",
                "site": "https://pwr.edu.pl/",
            },
            {
                "id": 2,
                "title": "Uni 2",
                "logo": "https://cdn11.bigcommerce.com/s-7va6f0fjxr/images/stencil/1280x1280/products/60361/76600/Hello-Kitty-With-Gun-Decal__92727.1506656896.jpg?c=2&imbypass=on",
                "site": "https://www.igig.up.wroc.pl/en/",
            },
        ]

        return jsonify(uniss)

    if request.method == "POST":
        # save
        return {}


@app.route("/search/unis", methods=["GET", "POST"])
def unis_search_list():
    "get univercity list"
    # uniSearchWord=request.args.get("query")
    if request.method == "GET":
        # read
        # unis=unis_collection.find({})
        # return jsonify([uni for uni in unis ])
        uniss = [
            {
                "id": 1,
                "title": "Uni 1",
                "logo": "https://avatars.mds.yandex.net/i?id=3879b1e342099fb44cbf3565b1e6f384-5313761-images-thumbs&n=13",
                "site": "https://pwr.edu.pl/",
            },
            {
                "id": 2,
                "title": "Uni 2",
                "logo": "https://cdn11.bigcommerce.com/s-7va6f0fjxr/images/stencil/1280x1280/products/60361/76600/Hello-Kitty-With-Gun-Decal__92727.1506656896.jpg?c=2&imbypass=on",
                "site": "https://www.igig.up.wroc.pl/en/",
            },
        ]
        # return jsonify([uni for uni in unis])
        query_param = request.args.get("q")
        print(type(query_param))
        if query_param is None:
            filtered_unis = uniss
        else:
            filtered_unis = list(filter(lambda x: x["id"] == int(query_param), uniss))
        # filtered_unis = [uni for uni in unis if uni["id"] == int(query_param)]

        # return jsonify(unis)
        return jsonify(filtered_unis)
    if request.method == "POST":
        # save
        return "It is POST"

"""
