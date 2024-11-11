from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', error='')

@app.route('/result', methods=['POST'])
def result():
    username = request.form.get('username').strip()
    if not username:
        return render_template('index.html', error="Username cannot be empty")

    try:
        response = requests.get(f'https://github.com/{username}')

        soup = BeautifulSoup(response.text, 'html.parser')

        name = soup.find('span', class_='p-name')
        bio = soup.find('div', class_='p-note')
        img_url = soup.find('img', class_='avatar')
        repos = soup.find('span', class_='Counter')
        followers = soup.find('span', class_='text-bold color-fg-default')

        name = name.text.strip()
        bio = bio.get('data-bio-text') or "Not Specified"
        img_url = img_url.get('src') 
        repos = repos.text.strip() or "0"
        followers = followers.text.strip() or "0"
        return render_template('result.html', name=name, bio=bio, img_url=img_url, repos=repos, followers=followers)

    except requests.exceptions.RequestException:
        error = "Please check your network."
        return render_template('index.html', error=error)
    except AttributeError:
        error = "The username may be incorrect."
        return render_template('index.html', error=error)
    except Exception as e:
        error = f"Unexpected error: {str(e)}"
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
