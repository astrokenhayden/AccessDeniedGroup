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
        "description": "Great for making smoothies!",
        "photo_name": "blender.jpg"
    },
    {
        "id": 2,
        "name": "Crockpot",
        "condition": "Used",
        "description": "Only works half of the time",
        "photo_name": "crockpot.jpg"
    },
    {
        "id": 3,
        "name": "Microwave",
        "condition": "Never Used",
        "description": "Still in the box, great for college",
        "photo_name": "microwave.jpg"
    }
]

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/loginpage', methods=['GET'])
def login():
    if 'button':
        return render_template('login.html')


@app.route('/listings', methods=['GET'])
@app.route('/listings/<list_id>', methods=['GET'])
def all_listings(item_id=None):
    if item_id:  # show single listing
        single_item = [items[int(item_id)]] if len(items)-1 >= int(item_id) else []
        return render_template('listings.html', items=single_item)
    else:  # show all listings
        return render_template('listings.html', items=items)


# @app.route('/listings', methods=['GET'])
# def listings():
#     return render_template('listings.html')


@app.route('/create-listing', methods=['GET', 'POST'])
def create_listing():
    item_name = request.form['item_name']
    condition = request.form['condition']
    description = request.form['description']

    new_item = {
        "id": len(items),
        "name": item_name,
        "condtion": condition,
        "description": description,
        "photo_name": "placeholder_icon.png"
    }

    items.append(new_item)

    return redirect(all_listings)


if __name__ == "__main__":
    app.run(debug=True)
