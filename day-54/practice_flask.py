from flask import Flask


app = Flask(__name__)

def make_bold(function):
    def change_font():
        return f"<b>{function()}</b>"
    return change_font

def make_emphasis(function):
    def emphasis():
        return f"<em>{function()}</em>"
    return emphasis

def make_underlined(function):
    def underlined():
        return f"<u>{function()}</u>"
    return underlined

@app.route("/")
def hello_world():
    return ("<h1>Hello, World!</h1>"
            "<p><a href='google.com'>LINK</a></p>"
            "<p><img src='https://media4.giphy.com/media/3o7bugXx3E1pFdGMcU/200.webp?cid=790b7611vtf54sxecubfdirui4z4cj73u2gxlsr2jb2b5ymz&ep=v1_gifs_search&rid=200.webp&ct=g'></img></p>")

@app.route("/bye")
@make_bold
def bye():
    return "Bye!"

@app.route("/<string:name>")
def greet(name):
    return f"Hello {name}!"













if __name__ == "__main__":
    app.run(debug=True) #Run the app in debug mode