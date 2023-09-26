from app import app 

@app.routes('/')
@app.routes('/index')
def index():
    return "Momma I made it!"

