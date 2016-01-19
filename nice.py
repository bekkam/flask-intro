from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<html><a href='/hello'>Hello!</a> This is the home page.</html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          Compliment:
            <select name="complimenttype">
              <option value="awesome">awesome</option>
              <option value="terrific">terrific</option>
              <option value="fantastic">fantastic</option>
            </select>
          <input type="submit">
        </form>
        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
          Insult:
            <select name="insulttype">
              <option value="awful">awful</option>
              <option value="horrible">horrible</option>
              <option value="boring">boring</option>
              <option value="disgrace">disgrace to humanity</option>
            </select>
            <input type="radio" name="cohort" value="X">X
            <input type="radio" name="cohort" value="elevensies">elevensies            
            <input type="radio" name="cohort" value="twelfthbright">twelfthbright
            <input type="radio" name="cohort" value="thirteeneers">thirteeneers
          <input type="submit">
        </form>                 
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("complimenttype")
    cohort_name = request.args.get("cohort")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s, from Cohort %s, I think you're %s!
      </body>
    </html>
    """ % (player, cohort_name, compliment)

@app.route('/diss')
def insult_person():
    """Get user by name."""

    player = request.args.get("person")
    insult = request.args.get("insulttype")
    cohort_name = request.args.get("cohort")    

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi %s, from Cohort %s, I think you're %s!
      </body>
    </html>
    """ % (player, cohort_name, insult)    


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
