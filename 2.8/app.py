from sanic import Sanic
from sanic.response import json, html

# 初始化 Sanic
app = Sanic(__name__)
app.static('/static', './static')

@app.route("/", methods=["GET"])
async def index(request):
    return html(open("./templates/index.html",encoding='utf-8').read())


if __name__ == '__main__':
    app.run()