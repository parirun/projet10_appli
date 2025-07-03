from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    reco = None
    error = None
    user_id = 15
    top_k = 5

    if request.method == 'POST':
        user_id = request.form.get('user_id', 15)
        top_k = request.form.get('top_k', 5)
        try:
            url = f"https://mvpreco.azurewebsites.net/api/reco?user_id={user_id}&top_k={top_k}"
            response = requests.get(url)
            response.raise_for_status()
            reco = response.json()
        except Exception as e:
            error = f"Erreur lors de l'appel API : {str(e)}"

    return render_template('index.html', reco=reco, user_id=user_id, top_k=top_k, error=error)


from flask import jsonify

@app.route('/api/reco')
def api_reco():
    user_id = request.args.get('user_id', 15)
    top_k = request.args.get('top_k', 5)
    try:
        url = f"https://mvpreco.azurewebsites.net/api/reco?user_id={user_id}&top_k={top_k}"
        response = requests.get(url)
        response.raise_for_status()
        return jsonify(response.json())  # renvoie JSON au frontend
    except Exception as e:
        return jsonify({'error': str(e)}), 500
