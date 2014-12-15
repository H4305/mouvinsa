from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    name = request.args.get('name', '')
    return render_template('index.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
