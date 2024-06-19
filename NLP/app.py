from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Paste the provided code here

# Define route to render the form
@app.route('/')
def home():
    return render_template('index.html')

# Define route to handle form submission
@app.route('/analyze', methods=['POST'])
def analyze():
    # Get text data from form
    text = request.form['text']

    # Paste the provided code here to process the text and generate plots

    # Save plot to a bytes object
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Return rendered template with plot
    return render_template('result.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
