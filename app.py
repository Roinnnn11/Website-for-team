from sanic import Sanic
from sanic.response import json, html

# 初始化 Sanic
app = Sanic(__name__)
app.static('/static', './static')

@app.route("/", methods=["GET"])
async def index(request):
    return html(open("./templates/index.html",encoding='utf-8').read())

@app.route("/heatmap", methods=["GET"])
async def new_page(request):
    return html(open("./templates/child_page.html", encoding='utf-8').read())

@app.route("/api/heatmap-data", methods=["GET"])
async def get_heatmap_data(request):
    # 假设这些数据从数据库或其他地方获取
    data = [
        {"lat": 37.7749, "lng": -122.4194, "value": 10},  # 示例: 每个点的数据
        {"lat": 37.7750, "lng": -122.4195, "value": 15},
        {"lat": 37.7751, "lng": -122.4196, "value": 20},
        {"lat": 37.7752, "lng": -122.4197, "value": 25},
        {"lat": 37.7753, "lng": -122.4198, "value": 30},
        # 可以添加更多数据点
    ]
    return json(data)  # 将数据以 JSON 格式返回给前端

if __name__ == '__main__':
    app.run()