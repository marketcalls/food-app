from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    recipes = [
        {"name": "Spaghetti Carbonara", "image": "images/Spaghetti Carbonara.jpg"},
        {"name": "Chicken Alfredo", "image": "images/Chicken Alfredo.jpg"},
        {"name": "Beef Tacos", "image": "images/Beef Tacos.jpg"},
        {"name": "Vegetable Stir Fry", "image": "images/Vegetable Stir Fry.jpg"}
    ]
    return render_template('index.html', recipes=recipes)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/recipe/<name>')
def recipe(name):
    return render_template('recipe.html', recipe_name=name)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
