#IMPORTS:
from flask import Flask, render_template, redirect, flash, request, session
import jinja2
from melons import get_all_melons, find_melon_by_id
from forms import LoginForm
import customers


app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined
app.sercret_key = 'chickensoup'



#ROUTES:

@app.route('/')
def home():
    return redirect('/all_melons')

# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user into site."""
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = customers.get_by_username(username)

        if not user or user['password'] != password:
            flash("Invalid username or password, please try again")
            return redirect('/login')
        else:
            session["username"] = user['username']
            flash("You were succsesfully logged in!")
            return redirect("/melons")

    return render_template("login.html", form=form)

# LOGOUT
@app.route("/logout")
def logout():
    """"Log user out"""

    del session["username"]
    flash("Logged out.")
    return redirect("/login")




# shows all melons 
@app.route('/all_melons') 
def melons():
    melon_list = get_all_melons()
    return render_template("all_melons.html", melon_list=melon_list)

# shows info about a specfic melon
@app.route('/melon/<melon_id>')
def melon_details(melon_id):
    melon = find_melon_by_id(melon_id)
    return render_template("melon_details.html", melon=melon)

# adds a specfic melon to cart
@app.route('/add_to_cart/<melon_id>')
def add_to_cart(melon_id):
    # if 'username' not in session:
    #     return redirect('/login')
    # else:
        if 'cart' not in session:
            session["cart"] = {}
        cart = session["cart"]

        cart[melon_id] = cart.get(melon_id, 0) + 1
        session.modified = True
        flash(f'{melon_id} added to the cart!')
        print(cart)

        return redirect("/cart")
        
# displays melon/s in the users cart
@app.route('/cart')
def cart():
    # if 'username' not in session:
    #     return redirect('/login')
    # else:
    order_total = 0
    cart_melons = []

    cart = session.get("cart", {})

    for melon_id, qauntity in cart.items():
        melon = melons.get_by_id(melon_id)

        total_cost = qauntity * melon.price
        order_total += total_cost

        melon.quantity = qauntity
        melon.total_cost = total_cost

        cart_melons.append(melon)

    return render_template("cart.html", cart_melons=cart_melons, order_total=order_total)

# empty cart
@app.route("/empty-cart")
def empty_cart():
    session["cart"] = {}

    return redirect("/cart")

@app.errorhandler(404)
def error404(err):
    return render_template("404.html")

# SERVER SETUP:
if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")