from flask import Blueprint, request, jsonify
from .models import Job, Application
from . import db

main = Blueprint('main', __name__)

@main.route('/jobs', methods=['POST'])
def create_job():
    data = request.get_json()
    new_job = Job(
        title=data['title'],
        company=data['company'],
        location=data['location'],
        description=data['description']
    )
    db.session.add(new_job)
    db.session.commit()
    return jsonify({"message": "Job created successfully!"})

@main.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([{ 'id': j.id, 'title': j.title, 'company': j.company, 'location': j.location, 'description': j.description } for j in jobs])

@main.route('/jobs/search', methods=['GET'])
def search_jobs():
    keyword = request.args.get('q', '')
    jobs = Job.query.filter(Job.title.contains(keyword)).all()
    return jsonify([{ 'id': j.id, 'title': j.title, 'company': j.company, 'location': j.location, 'description': j.description } for j in jobs])

@main.route('/apply', methods=['POST'])
def apply_job():
    data = request.get_json()
    job = Job.query.get(data['job_id'])
    if not job:
        return jsonify({"error": "Job not found"}), 404

    application = Application(
        job_id=data['job_id'],
        applicant_name=data['applicant_name'],
        email=data['email']
    )
    db.session.add(application)
    db.session.commit()
    return jsonify({"message": "Application submitted successfully!"})

@main.route('/applications', methods=['GET'])
def get_applications():
    apps = Application.query.all()
    return jsonify([{ 'id': a.id, 'job_id': a.job_id, 'name': a.applicant_name, 'email': a.email } for a in apps])

@main.route('/applications/<int:id>', methods=['DELETE'])
def delete_application(id):
    app = Application.query.get(id)
    if not app:
        return jsonify({"error": "Application not found"}), 404

    db.session.delete(app)
    db.session.commit()
    return jsonify({"message": "Application deleted"})
