from patient import Patient
import db
import logic

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
