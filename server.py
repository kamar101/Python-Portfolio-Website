from flask import Flask, render_template, request, redirect
from flask import send_file, send_from_directory
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def other_pages(page_name):
    return render_template(page_name)


def write_to_database(data):
    with open ('database.txt', mode ='a') as database:
        name = data['name']
        email = data['email']
        message = data['message']
        file = database.write (f"\n{name}, {email}, {message}")

def write_to_csv(data):
    with open ('database.csv',newline='\n', mode ='a') as database_csv:
        name = data['name']
        email = data['email']
        message = data['message']
        databsewriter = csv.writer(database_csv, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        databsewriter.writerow([name,email,message])

@app.route('/recieved_form', methods=['POST', 'GET'])
def recieved_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:"faild to save to database"
    else:
        return 'Something went wrong'

# @app.route('/Resume') 
# def sendResume():
#     return send_file('./templates/samuelKamar_Resume.docx',
#                 mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
#                 attachment_filename='samuelKamar_Resume.docx',
#                 as_attachment=True)

@app.route("/templates/samuelKamar_Resume.docx")
def download_file(name):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], name, as_attachment=True
    )
