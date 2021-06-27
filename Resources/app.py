# Import Flask dependency
from flask import Flask
# Create a new Flask instance
app = Flask(__name__) #__name__ is a magic method variable-used to determine if your code is being run from the command line or if it has been imported into another piece of code
# Define the starting point (also known as the root)
@app.route('/') #The / denotes that we want to put our data at the root of our routes (highest level of hierarchy)
def hello_world():
    return 'Hello world'