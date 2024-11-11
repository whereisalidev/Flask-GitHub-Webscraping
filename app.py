from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

# app = Flask(__name__)

# app.route('/')
# def index():
#     return render_template('index.html')

# app.route('/result')
# def result():
# username = request.form['username']
github_html = requests.get(f'https://github.com/whereisalidev').text
soup = BeautifulSoup(github_html, 'html.parser')
name = soup.find('span', class_='p-name').text.strip()
bio = soup.find('div', class_='p-note').get('data-bio-text')
img_url = soup.find_all('img', class_='avatar')[0].get('src')
repos = soup.find('span', class_='Counter').text

print(name)
print(bio)
print(img_url)
print(repos)
# return render_template('result.html', )


