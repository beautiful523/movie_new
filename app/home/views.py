from . import home

@home.route("/")
def index():
    return "这是前台"