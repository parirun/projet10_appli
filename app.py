from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/reco', methods=['GET'])
def reco():
    user_id = request.args.get('user_id', 15)
    top_k = request.args.get('top_k', 10)
    
    azure_url = f"https://mvpreco.azurewebsites.net/api/reco?user_id={user_id}&top_k={top_k}"
    try:
        response = requests.get(azure_url)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Erreur lors de l'appel à l'API Azure"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
