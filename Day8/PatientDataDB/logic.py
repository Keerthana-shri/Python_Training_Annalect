from patient import Patient
import db
import logic
# from db import insert_patient, update_patient, select_patient_by_id, select_patient_by_phone, close_connection
# from logic import add_patient, modify_patient, find_patient_by_id, find_patient_by_phone, close_db_connection

# def add_patient(first_name, last_name, dob, phone_number, email):
#     insert_patient(first_name, last_name, dob, phone_number, email)

# def modify_patient(patient_id, first_name=None, last_name=None, dob=None, phone_number=None, email=None):
#     update_patient(patient_id, first_name, last_name, dob, phone_number, email)

# def find_patient_by_id(patient_id):
#     select_patient_by_id(patient_id)

# def find_patient_by_phone(phone_number):
#     select_patient_by_phone(phone_number)

# def close_db_connection():
#     close_connection()


# patient1 = Patient('a', 'b', '1985-06-15', '123-456-7890', 'a@poc.com')
# add_patient(patient1.first_name, patient1.last_name, patient1.dob, patient1.phone_number, patient1.email)

# modify_patient(1, phone_number='111-222-3333', email='freak@poc.com')
# find_patient_by_id(1)
# find_patient_by_phone('987-654-3210')

# close_db_connection()

# Insert some test data
db.insert_patient('a', 'b', '1985-06-15', '123-456-7890', 'a@poc.com')
db.insert_patient('c', 'd', '1992-02-20', '987-654-3210', 'de@poc.com')
db.insert_patient('e', 'f', '1975-08-25', '555-444-3333', 're@poc.com')

# Try to insert a patient with a duplicate email (will violate primary key constraint)
db.insert_patient('abc', 'def', '1990-10-10', '123-123-1234', 'abcdef@poc.com')

# Update patient with ID 1 (John Doe)
db.update_patient(1, phone_number='111-222-3333', email='freak@poc.com')

# Try to update a non-existent patient
db.update_patient(999, phone_number='000-000-0000')

# Select patient by primary key (patient_id)
db.select_patient_by_id(1)  
db.select_patient_by_id(999)  # Should show "patient not found"

# Select patients by non-primary key (phone number)
db.select_patient_by_phone('987-654-3210')  # Should find
db.select_patient_by_phone('000-000-0000')  # Should show "no patient found"
