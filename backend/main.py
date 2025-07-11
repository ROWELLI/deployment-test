from flask import Flask, jsonify, request
from flask_cors import CORS
import dash
from dash import html, dcc
import plotly.express as px
import os
from dotenv import load_dotenv
load_dotenv()

server = Flask(__name__)
CORS(server)  # 모든 origin 허용

# Dash 연결
dash_app = dash.Dash(__name__, server=server, routes_pathname_prefix='/dash/')

# 샘플 그래프
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

dash_app.layout = html.Div([
    html.H2("Dash 그래프 예시"),
    dcc.Graph(figure=fig)
])

# 사용자 입력 저장용 변수
user_input = {}

# 🔥 반드시 GET, POST 모두 허용해야 함!
@server.route("/api/config", methods=["GET", "POST"])
def config_handler():
    global user_input
    if request.method == "GET":
        return jsonify({
            "windowSize": "1600x900",
            "outputLocation": "./output",
            "processes": {
                "COMPOSITING": {
                    "time": 480, "throughput": 2, "reject": 0, "delay": 1, "ratio": 1
                }
            },
            "userInput": user_input
        })
    elif request.method == "POST":
        data = request.get_json()
        user_input = data
        print("[사용자 입력]:", data)
        return jsonify({"message": "성공적으로 저장됨", "data": data}), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    server.run(host="0.0.0.0", port=port)
