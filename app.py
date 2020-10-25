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


@app.route('/dogs', methods=['GET'])
@app.route('/dogs/<dog_id>', methods=['GET'])
def all_dogs(dog_id=None):
    if dog_id:  # show single dog
        single_dog = [dogs[int(dog_id)]] if len(dogs)-1 >= int(dog_id) else []
        return render_template('dogs.html', dogs=single_dog)
    else:  # show all dogs
        return render_template('dogs.html', dogs=dogs)





@app.route('/create-listing', methods=['GET', 'POST'])
def create_dog():
    item_name = request.form['dog_name']
    item_condition = request.form['dog_breed']
    item_description = request.form['dog_age']
    item_is_available_for_adoption = True

    new_listing = {
        "id": len(items),
        "item": item_name,
        "condition": item_condition,
        "description": item_description,
        "photo_name": "placeholder_icon.png",
        "available": item_is_available
    }

    item.append(new_item)

    return redirect(all_listings)


if __name__ == "__main__":
    app.run(debug=True)
