from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Massa atom sederhana (bisa diperluas)
atomic_mass = {
    'H': 1.008,
    'He': 4.0026,
    'Li': 6.94,
    'Be': 9.0122,
    'B': 10.81,
    'C': 12.011,
    'N': 14.007,
    'O': 15.999,
    'F': 18.998,
    'Na': 22.990,
    'Mg': 24.305,
    'Al': 26.982,
    'Si': 28.085,
    'P': 30.974,
    'S': 32.06,
    'Cl': 35.45,
    'K': 39.098,
    'Ca': 40.078
}

def calculate_molar_mass(formula):
    pattern = r'([A-Z][a-z]?)(\d*)'
    matches = re.findall(pattern, formula)
    total_mass = 0

    for (element, count) in matches:
        count = int(count) if count else 1
        if element not in atomic_mass:
            raise ValueError(f"Unrecognized element: {element}")
        total_mass += atomic_mass[element] * count
    return round(total_mass, 3)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    formula = data.get('formula', '').strip()

    try:
        result = calculate_molar_mass(formula)
        return jsonify({'success': True, 'mass': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
