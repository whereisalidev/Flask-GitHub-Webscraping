from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

app.route('/')
def index():
    return render_template('index.html')

app.route('/result')
def result():
    username = request.form['username']
    github_html = requests.get(f'https://github.com/{username}').text
    soup = BeautifulSoup(github_html, 'html.parser')
    name = soup.find('span', class_='p-name').text.strip()
    bio = soup.find('div', class_='p-note').get('data-bio-text') or 'Not Specified'
    img_url = soup.find_all('img', class_='avatar')[0].get('src')
    repos = soup.find('span', class_='Counter').text
    followers = soup.find('span', class_='text-bold color-fg-default').text
    # print(name)
    # print(bio)
    # print(img_url)
    # print(repos)
    # print(followers)
    return render_template('result.html', name=name, bio=bio, img_url=img_url, repos=repos, followers=followers)

if __name__ == '__main__':
    app.run()