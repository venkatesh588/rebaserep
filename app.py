from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for students webhook verification test
data_store = {
    'students': []
}

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data:
        return jsonify({'error': 'Name and age are required.'}), 400
    student = {
        'id': len(data_store['students']) + 1,
        'name': data['name'],
        'age': data['age']
    }
    data_store['students'].append(student)
    return jsonify(student), 201

@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(data_store['students'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
