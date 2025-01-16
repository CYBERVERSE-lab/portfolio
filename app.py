import json
from flask import Flask, jsonify, Response
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# PostgreSQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/portfolio_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


class DeveloperAbout(db.Model):
    __tablename__ = 'developer_about'  # Table name in the database

    developer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    designation = db.Column(db.String(50), nullable=False)
    gmail_id = db.Column(db.String(50), nullable=False)
    linkedin_id = db.Column(db.String(50), nullable=False)
    github_id = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.BigInteger, nullable=False)
    date_added = db.Column(db.Date, default=db.func.current_date())

    def __repr__(self):
        return f"<DeveloperAbout {self.name}>"
    

@app.route('/aboutme', methods=['GET'])
def get_developers():
    developer = DeveloperAbout.query.filter_by(developer_id=1).first()
    result = {
                "Name": developer.name,
                "Designation": developer.designation,
                "Gmail ID": developer.gmail_id,
                "Linkedin ID": developer.linkedin_id,
                "Github ID": developer.github_id,
                "Phone Number": developer.phone_number
            }
    return Response(json.dumps(result, indent=2), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
