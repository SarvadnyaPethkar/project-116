# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Jhonson" # write your name
    age = "8" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    name = "Mark"
    age = 28

    return render_template('father.html', name=name, age=age)

# define the route to mother webpage
@app.route("/mother")
def mother():
    name = "Liv"
    age = 26

    return render_template('mother.html', name=name, age=age)

# define the route to friends webpage
@app.route("/friend")
def friend():
    name = "Smith"
    age = 8

    return render_template('friend.html', name=name, age=age)

# add other routes, if you want
#defining the route to sister's webpage
@app.route("/sister")
def sister():
    name = "Sarah"
    age = 13

    return render_template('sister.html', name=name, age=age)

#defining the route to pet's webpage
@app.route("/pet")
def pet():
    name = "Sami"
    
    return render_template("pet.html", name=name)

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
