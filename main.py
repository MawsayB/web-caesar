from flask import Flask, request  
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <!--create your form here-->

        <form action="" method="post">
            <label>Rotate by:</label>
            <input type="text" name="rot" value="0" />
            <textarea name="text" >{0}</textarea>
            <input type="submit" />
        </form>

    </body>
</html>

"""

@app.route("/")
def index():
    return form.format("") 

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = request.form['rot']
    rot = int(rot)
    text = str(text)

    encrypt = rotate_string(text, rot)
    rendered = "<h1>" + encrypt + "</h1>"
    
    return form.format(encrypt) 

app.run()