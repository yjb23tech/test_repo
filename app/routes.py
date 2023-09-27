from app import app 

#The basic routing below tells my server how to respond to client side requests into the server
@app.route('/')
@app.route('/index')
def index():
    return "Paradise Lost!"

