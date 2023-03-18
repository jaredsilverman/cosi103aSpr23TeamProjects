'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>GPT Demo</h1>
        <a href="{url_for('about')}">About</a><br>
        <a href="{url_for('team')}">Meet the team</a><br>
        <a href="{url_for('keyword_info')}">Get info about a Python keyword</a><br>
        <a href="{url_for('book_info')}">Get info about where to buy a book</a><br>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a><br>
    '''


@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/about')
def about():
    ''' Explains what our program does '''
    return f'''
    <h1>About</h1>
    <p>Welcome to our project that provides prompts to ChatGPT!<p>
    <p>In the Meet the Team page you can see bios for each participant
    <p>You can get information about codes in "Get info about a Python keyword".<p>
    <p>You can also get info about where to buy a book<p>
    <p>Finally, you can also ask general questions in the "Ask questions to GPT" page<p>

    '''

@app.route('/team')
def team():
    ''' Gives a short bio of each team member and what their role was '''
    return f'''
    <h1>Meet the team</h1>
    <p>Gabriel Abreu is a sophmore from Rio de Janeiro, Brazil studying Applied Mathematics
    He created  the page that gives you information on where to buy a book, and added text to different sections on the index page</p>
    <p>Jared Silverman is a sophomore from Somerset, MA studying Applied Mathematics.
    He created the page that gives info about Python keywords and formatted the index page.</p>
    '''

@app.route('/keyword_info', methods=['GET','POST'])
def keyword_info():
    ''' Handles a get request by sending a form prompting for a Python keyword
    and a post request by returning the GPT response explaining the keyword
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_info(prompt)
        return f'''
        <h1>Python keyword info</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is what this keyword does:
        <div style="border:thin solid black">{answer}</div>
        <a href={url_for('index')}>make another query</a>
        '''
    else:
        return '''
        <h1>Python keyword info</h1>
        Enter a Python keyword below:
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
@app.route('/book_info', methods=['GET','POST'])
def book_info():
    ''' Handles a get request by sending a form prompting for a book name
    and a post request by returning the GPT response explaining where to buy the given book
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_book(prompt)
        return f'''
        <h1>Book link</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is what this keyword does:
        <div style="border:thin solid black">{answer}</div>
        <a href={url_for('index')}>make another query</a>
        '''
    else:
        return '''
        <h1>Book link</h1>
        Enter a Book name below:
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)