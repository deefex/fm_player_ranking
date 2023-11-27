from flask import Flask, render_template, request
from roles_data import ROLES_DATA
from parse_and_calculate import parse_and_calculate

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    result_table = None

    if request.method == 'POST':
        # Handle file upload logic here
        file = request.files['file']
        selected_roles = request.form.getlist('playerRoles')

        # Call your parse_and_calculate function
        result_table = parse_and_calculate(file, selected_roles)

    return render_template('upload.html', roles_data=ROLES_DATA, result_table=result_table)


if __name__ == '__main__':
    app.run(port=8000, debug=False)
