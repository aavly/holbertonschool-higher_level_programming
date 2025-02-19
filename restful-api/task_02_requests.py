#!/usr/bin/python3
"""
2. Consuming and processing data
    from an API using Python.
"""
import csv
import requests


# connecting to API and storing response in object
API_URL = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    response = requests.get(API_URL)
    print("Status code:", response.status_code)

    # if connection successful (200)
    if response.status_code == 200:
        # then store fetched data into json object
        fetched_data = response.json()

        # printing only the field 'title'
        for post in fetched_data:
            print(post['title'])


def fetch_and_save_posts():
    response = requests.get(API_URL)

    if response.status_code == 200:
        fetched_data = response.json()
        
        # structure data into a list of dictionaries
        title_list = []
        for item in fetched_data:
            titles = {
                    'id': item['id'],
                    'title': item['title'],
                    'body': item['body']
            }
            title_list.append(titles)
        print(title_list)

    # write into CSV file called posts.csv
    field_names = ['id', 'title', 'body']
    with open('posts.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(title_list)
