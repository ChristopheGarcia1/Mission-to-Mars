# importing our tools

from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# Within the def index(): function the following is accomplished:

# mars = mongo.db.mars.find_one() uses PyMongo to find the 
# "mars" collection in our database, which we will 
# create when we convert our Jupyter scraping code to Python Script. 
# We will also assign that path to themars variable for use later.

# return render_template("index.html" 
# tells Flask to return an HTML template using an index.html file. We'll create this file after we build the Flask routes.

# , mars=mars) tells Python to use the "mars" collection in MongoDB.

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

# The first line, @app.route(“/scrape”) defines the route that Flask 
# will be using. This route, “/scrape”, will run the function that we create just beneath it.

# The next lines allow us to access the database, scrape new data 
# using our scraping.py script, update the database, and return 
# a message when successful. Let's break it down.

# First, we define it with def scrape():.

# Then, we assign a new variable that points to our Mongo database: 
# mars = mongo.db.mars.

# Next, we created a new variable to hold the newly scraped data:
#  mars_data = scraping.scrape_all(). 
# In this line, we're referencing the scrape_all function in the scraping.py file exported from Jupyter Notebook.

# Now that we've gathered new data, we need to update the database using .update(). Let's take a look at the syntax we'll use, as shown below:


if __name__ == "__main__":
   app.run()