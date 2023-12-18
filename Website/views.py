from flask import Blueprint, render_template
import requests
# Strapi Product
headers =  {"Authorization":"Bearer c53babe2fe89486a252266ce30471ffd9d1caa60a3b18b11f2330c1c4676ce20eb9131cfeececdd503bd61003c70a2f04ba6fca0e273975a0bd244852de0b054198500f0993166a809afeac63d8a8e81e35ad3a3502e8365930cdc6b2409d934c4b8cbd16f21d2a2fb34075f7c793bb5789e4ea2a35a9e5afde047973b1c134b"}
api_url = "http://localhost:1337/api/products?populate=*"
response = requests.get(api_url, headers=headers)
data = response.json()

# Strapi Display
api_url1 = "http://localhost:1337/api/product-displays?populate=*"
response1 = requests.get(api_url1, headers=headers)
data2 = response1.json()

api_url_apex = "http://localhost:1337/api/apex-legends?populate=*"
responseapex = requests.get(api_url_apex, headers=headers)
dataapex = responseapex.json()
print(responseapex)



views = Blueprint ('views', __name__)


@views.route('/')
def home():
        return render_template("home.html", products=data, displays=data2)

@views.route('/login')
def login():
      return render_template("Login.html", boolean=True)

@views.route('/logout')
def logout():
        return "<p>Logout</p>"


@views.route('/checkout')
def checkout():
       return render_template("checkout.html")


@views.route('/kategori')
def kategori():
       return render_template("kategori.html")

# @views.route('/home')
# def home():
#        return render_template ("home.html")


