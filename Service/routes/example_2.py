from flask import Flask, request
from flask_restplus import Resource, Api, fields

"""
https://flask-restplus.readthedocs.io/en/stable/index.html

与原生 Flask 不同，Flask rest plus 引入了一个 Api, 并通过这个 Api 来配置应用接口，提供额外服务。
"""


"""
1) 初始化 Flask
"""
flask = Flask(__name__)

"""
2）获得 flask-restplus API 接口
"""
api = Api(flask)


"""
3) 基于 api 接口定义 url 并绑定服务。

  * URL 可以带参数。
  * 服务必须是基于 Resource 的类。类中的成员函数名称表明访问的方法。
  * 集成的 Swagger 装饰器可以生成 API 文档。允许修饰在 class 或方法层。(https://flask-restplus.readthedocs.io/en/stable/swagger.html)
"""
@api.route('/hello/<string:name>')
@api.doc(params={'name': 'User name'})
class HelloWorld(Resource):
    """
      函数名代表访问方法，可以接受来自 URL 的参数，URL 参数支持路径(/value1/value2/...)参数和请求参数(?key1=value1&key2=value2...)：
        $ curl -X GET http://localhost:5000/hello/xxx?key=value
    """
    @api.doc(responses={403: 'Not Authorized'})
    def get(self, name):
        print(request.headers['content-type'])
        print(request.args['key'])
        """
         与原生 Flask 中实现 JSONResponse 不同，RESTPlus 提供了一个 marshal_with 装饰器来实现对输入和输出数据类型的转换，
         本例不打算演示，具体参考 example_3 和：https://flask-restplus.readthedocs.io/en/stable/marshalling.html
        """
        return {'hello': '{0}'.format(name)}  # 返回 JSON

    """
      参数也可以放在表单中提交（content-type: application/x-www-form-urlencoded），可以用request.form 获取: 
        $ curl -X POST http://localhost:5000/hello/xxx -d "param=Some one"
    """
    def post(self, name):  # 但是 url 参数不能省，哪怕不用
        param = request.form['param']  # 获得表单数据
        return {'hello': '{0}'.format(param)}


    """
      也可以放在 body 中提交（content-type: application/json），通过 request.data 得到：
        $ curl -X PUT http://localhost:5000/hello/xxx -b "{ "param": "value" }"
    """
    def put(self, name):  # 但是 url 参数不能省，哪怕不用
        param = request.data.decode("utf-8")  # 获得表单数据
        return {'hello': '{0}'.format(param)}
"""
4) 启动 flask
"""
if __name__ == '__main__':
    flask.run(debug=True)
