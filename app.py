import flask from Flask,render_template
app = Flask(__name__)
def index():
    return render_template('index.html',data[
        {
            description:'todo1'
        },
        {
            description:'todo2'
        },
        {
            description:'todo3'
        },
        {
            description:'todo4'
        }
    ])
