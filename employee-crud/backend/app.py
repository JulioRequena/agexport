from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db = SQLAlchemy(app)

# Definición del modelo de datos
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    gender = db.Column(db.String(10))
    marital_status = db.Column(db.String(20))
    birth_date = db.Column(db.String(10))
    salary = db.Column(db.Float)

# Endpoint para obtener la lista de empleados
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([{
        "id": e.id,
        "name": e.name,
        "last_name": e.last_name,
        "salary": e.salary
    } for e in employees])

# Endpoint para obtener detalles de un empleado por ID
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify({
        "id": employee.id,
        "name": employee.name,
        "last_name": employee.last_name,
        "gender": employee.gender,
        "marital_status": employee.marital_status,
        "birth_date": employee.birth_date,
        "salary": employee.salary
    })

# Endpoint para agregar un nuevo empleado
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    new_employee = Employee(**data)
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({"message": "Employee created successfully!"}), 201

# Endpoint para actualizar la información de un empleado por ID
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    data = request.json
    for key, value in data.items():
        setattr(employee, key, value)
    db.session.commit()
    return jsonify({"message": "Employee updated successfully!"})

# Endpoint para eliminar un empleado por ID
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": "Employee deleted successfully!"})

# Inicialización y ejecución de la aplicación
if __name__ == '__main__':
    db.create_all()  # Crear las tablas si no existen
    app.run(debug=True)
