from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

app.route('/')
def index():
    return render_template()



github_html = requests.get(f'https://github.com/{username}').text

soup = BeautifulSoup(github_html, 'html.parser')

avatar_block = soup.find_all('img', class_='avatar')[0].get('src')

print(avatar_block)

repos = soup.find('span', class_='Counter').text
print(repos)