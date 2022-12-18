from flask import Flask
import utils


app = Flask(__name__)

@app.route('/Bear')
def bear():
    return 'Bear Paddington'


app.run()




