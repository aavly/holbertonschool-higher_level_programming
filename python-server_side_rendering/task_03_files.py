#!/usr/bin/python3
"""Creating a Basic html Template in Flask"""

from flask import Flask, render_template, request
import os
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # Reading data from item.json file
    try:
        with open ("items.json", "r") as file:
            data = json.load(file)
        items = data.get('items', [])
        return render_template('items.html', items=items)
    except FileNotFoundError:
        return "File not found", 404
    except json.JSONDecodeError:
        return "Error decoding JSON", 500

# Reading data from JSON file
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Reading data from CSV file
def read_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products
    
@app.route('/products')
def products():
    # using request.args.get to get query arguements and assign to variables 
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # determining what file type is entered as an argument, then setting products accordingly
    if source == 'json':
        file_path = 'products.json'
    elif source == 'csv':
        file_path = 'products.csv'
    else:
        return render_template('product_display.html', error="Invalid file format. Only JSON and CSV accepted")
    
    #checking if file exists
    if not os.path.exists(file_path):
        return render_template('product_display.html', error="File not found")
    
    try:
        if source == 'json':
            products = read_json(file_path)
        else:
            products = read_csv(file_path)
    except Exception:
        return render_template('product_display.html', error="Error reading file")

    if product_id:
        try:
            product_id = int(product_id)
            # BELOW - if p for a product in products has its id matched with the product_id requested in the parameter...
            # then set it to the variable products (which is to be used later on when returning the rendered template)
            found_products = [p for p in products if p['id'] == product_id]
            if not found_products:
                return render_template('product_display.html', error="Product not found")
            return render_template('product_display.html', products=found_products)
        except ValueError:
            return render_template('product_display.html',error="Error: Product ID must be an integer")
        
    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)