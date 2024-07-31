from flask import Flask, redirect, render_template,request, url_for, jsonify
import authentication
import db_initializer
import dictionaries

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/registration', methods=['POST'])
def reg():
    if request.method == 'POST':
        data = request.json
        if authentication.registration(data):
            return jsonify({'status': 'success', 'data': data}), 200
        
@app.route('/authorization', methods=['POST'])
def log_in():
    if request.method == 'POST':
        data = request.json
        print(data['Value'])
        if authentication.authorization(data):
            return jsonify({'status': 'success', 'data': data}), 200

@app.route('/userPage')
def user_page():
    user = authentication.uservv.username
    dictionary = dictionaries.load_data_toDay()
    
    
    if dictionary != False:
        return render_template('userPage.html',user=user, dictionary=dictionary)
    else:
        return render_template('userPage.html',user=user)

@app.route('/sendData', methods=['POST'])
def sendData():
    if request.method == 'POST':
        data = request.json
        if db_initializer.sendData(data):
            return jsonify({'status': 'success', 'data': data}), 200
        
@app.route('/dictionaries')
def activDictonaries():
    dictionary=dictionaries.getting_all_dictionaries()
    print('РАБОТАЕТ!!!!!!!')
    print(dictionary)
    return render_template('dictionaries.html',dictionary=dictionary)

if __name__ == "__main__":
    app.run(debug=True)