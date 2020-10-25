from flask import Flask, render_template, request, redirect
from random import randint

app = Flask(__name__)

'''
Note: this sample code does NOT store the dogs data to a database.
Instead, we store the dogs data in memory in the below "dogs" Python object.
Consequently, the dogs data is reset every time the application is restarted.
If you would like, you can replace this dogs data structure with your own database connection logic.
'''

items = [
    {
        "id": 1,
        "name": "Blender",
        "condition": "Like New",
        "description": ,
        "photo_name": "blender.jpg",
        "available": True
    },
    {
        "id": 2,
        "name": "Pixie",
        "breed": "Pug",
        "age": 7,
        "photo_name": "dog_2.jpg",
        "available_for_adoption": True
    },
    {
        "id": 3,
        "name": "Ellie",
        "breed": "Golden Retriever",
        "age": 3,
        "photo_name": "dog_3.jpg",
        "available_for_adoption": True
    }
]


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/listings', methods=['GET'])
def listings():
    return render_template('listings.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


# @app.route('/create-dog', methods=['GET', 'POST'])
# def create_dog():
#     dog_name = request.form['dog_name']
#     dog_breed = request.form['dog_breed']
#     dog_age = request.form['dog_age']
#     dog_is_available_for_adoption = True

#     new_dog = {
#         "id": len(dogs),
#         "name": dog_name,
#         "breed": dog_breed,
#         "age": dog_age,
#         "photo_name": "placeholder_dog.png",
#         "available_for_adoption": dog_is_available_for_adoption
#     }

#     dogs.append(new_dog)

#     return redirect(all_dogs)


if __name__ == "__main__":
    app.run(debug=True)
