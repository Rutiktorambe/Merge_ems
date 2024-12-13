from flask import jsonify, request
from flask_login import login_required, current_user

@app.route('/get_trainings/<string:training>', methods=['GET'])
@login_required
def get_trainings(training):
    """
    Fetches training data for the current user based on training type (internal or external).
    """
    # Query the database based on the training type and current user
    if training.lower() == "internal":
        trainings = TrainingRegistration.query.join(Training, TrainingRegistration.TID == Training.TID) \
            .filter(Training.Mode == "internal", TrainingRegistration.Status == "Approved", TrainingRegistration.EmpID == current_user.EmpID).all()
    elif training.lower() == "external":
        trainings = TrainingRegistration.query.join(Training, TrainingRegistration.TID == Training.TID) \
            .filter(Training.Mode == "external", TrainingRegistration.Status == "Approved", TrainingRegistration.EmpID == current_user.EmpID).all()
    else:
        trainings = []

    # Prepare data for the response
    if trainings:
        trainings_data = [
            {"TID": training.TID, "TName": Training.query.filter_by(TID=training.TID).first().TName} 
            for training in trainings
        ]
    else:
        trainings_data = []

    # Return the data as JSON
    return jsonify(trainings_data)


