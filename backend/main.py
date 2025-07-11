from flask import Flask, jsonify
from flask_cors import CORS
import dash
from dash import html, dcc
import plotly.express as px
import os
from dotenv import load_dotenv
load_dotenv() # 같은 폴더에 위치한 env 불러옴

# Flask 서버 생성
server = Flask(__name__)
CORS(server)

# Dash 앱 생성 (Flask에 붙이기)
dash_app = dash.Dash(__name__, server=server, routes_pathname_prefix='/dash/')

# 예시 그래프 데이터
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

# Dash 레이아웃
dash_app.layout = html.Div([
    html.H2("Dash 그래프 예시"),
    dcc.Graph(figure=fig)
])

# config API
@server.route("/api/config")
def get_config():
    return jsonify({
        "windowSize": "1600x900",
        "outputLocation": "./output",
        "processes": {"COMPOSITING": {"time": 480, "throughput": 2, "reject": 0, "delay": 1, "ratio": 1}}
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000)) 
    server.run(host="0.0.0.0", port=port)
