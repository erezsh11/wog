from flask import Flask

app = Flask(__name__)


@app.route('/')
def score_server():
    try:

        with open('scores.txt', 'r') as file:
            score = file.read().strip()

        # Construct HTML response with the score
        html_response = """
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{}</div></h1>
        </body>
        </html>
        """.format(score)

    except Exception as e:
        # Handle any errors that occur during file reading
        error_message = str(e)
        html_response = """
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score" style="color:red">{}</div></h1>
        </body>
        </html>
        """.format(error_message)

    return html_response


if __name__ == '__main__':
    app.run(debug=True)
