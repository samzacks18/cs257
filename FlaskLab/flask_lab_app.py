from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html', title="Silly Dataset", headings = data[0])

if __name__ == '__main__':
     app.run()

data = []

def load_data():
     #slightly weird syntax for reading from a file, but apparently the proper Pythonic way:
     with open('dataset.csv', newline='') as f:
         reader = csv.reader(f)
         for row in reader:
             data.append(row)
@app.route('/<row>/<column>', strict_slashes=False)
def get_cell(row, column):
     return data[int(row)][int(column)]