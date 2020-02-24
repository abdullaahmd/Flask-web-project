from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


#@app.route('/<username>/<int:post_id>')
#def hello_world(username=None, post_id=None):


@app.route('/')
def my_home():
    #print(url_for('static', filename='python.ico'))
    return render_template('index.html')

@app.route('/<page_name>')
def pages(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', newline='', mode='a') as database:
        file = database.write(f"{data['name']}, {data['email']}, {data['text']}, {data['message']}")

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        csv_write = csv.writer(database, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        #csv_write.writerow([data['name'], data['email'], data['text'], data['message']])
        csv_write.writerow(data.values())

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #request.form.to_dic
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Couldnt write the database'
    return 'something went wrong'