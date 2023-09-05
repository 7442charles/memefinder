from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/searchmeme', methods=['POST'])
def search_meme():
    try:
        data = request.get_json()  # Assuming JSON data is sent in the request body
        if data is None:
            return "No data received", 400
        else:
            received_text = data.get('text', '')

            # Specify the full path to the Python executable
            python_executable = '/usr/bin/python3'  # Replace with the actual path

            # Pass the received text as a command-line argument to another Python script
            result = subprocess.run([python_executable, 'processing.py', received_text], capture_output=True, text=True)
            if result.returncode == 0:
                processed_output = result.stdout.strip()
                return jsonify({"message": processed_output})
            else:
                return jsonify({"error": "An error occurred while processing the data."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
