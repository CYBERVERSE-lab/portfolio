import json

from flask import Response
from config import app
from models import DeveloperAbout, Skills
    

@app.route('/projects', methods=['GET'])
def get_projects():
    """"""

@app.route('/skills', methods=['GET'])
def get_skills():
    skills = Skills.query.all()
    result = []
    for skill in skills:
        result.append({
            "Skill Name": skill.skill_name,
            "Description": skill.description,
            "Competency": skill.competency,
            "Years of Experience": skill.years_of_experience
        })
    return Response(json.dumps(result, indent=2), mimetype='application/json')

@app.route('/experience', methods=['GET'])
def get_experience():
    """"""

@app.route('/education', methods=['GET'])
def get_education():
    """"""

@app.route('/certifications', methods=['GET'])
def get_certifications():
    """"""


@app.route('/aboutme', methods=['GET'])
def get_developers():
    developer = DeveloperAbout.query.filter_by(developer_id=1).first()
    result = {
                "Name": developer.name,
                "Designation": developer.designation
            }
    return Response(json.dumps(result, indent=2), mimetype='application/json')


@app.route('/contacts', methods=['GET'])
def get_contacts():
    developer = DeveloperAbout.query.filter_by(developer_id=1).first()
    result = {
                "Gmail ID": developer.gmail_id,
                "Linkedin ID": developer.linkedin_id,
                "Github ID": developer.github_id,
                "Phone Number": developer.phone_number
            }
    return Response(json.dumps(result, indent=2), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
