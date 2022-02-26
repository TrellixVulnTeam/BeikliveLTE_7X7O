# -*- coding: utf-8 -*-  
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
import os.path
# 定义变量
define("port", default=6350, help="默认端口6350")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def make_app():
    settings = {
        'debug' : True,         # 修改源文件后程序自动重启
        # "img_path": os.path.join(os.path.dirname(__file__), "imgSource"),        # 图片路由
        # "thumb_path": os.path.join(os.path.dirname(__file__), "thumbnail"),     #略缩图路由
        "static_path": os.path.join(os.path.dirname(__file__), "templates"),        # 静态文件目录， 储存html的CSS和js
        "template_path" : os.path.join(os.path.dirname(__file__), "templates"),        # 储存html模板
    }
    return tornado.web.Application([
        (r"/", MainHandler),
        # (r"/redirect",RedirectRequestHandler),
        # (r"/ImgUpload", ImgUploadHandler),
        # (r"/ImgRequest",ImgRequestHandler),
        # (r"/img/(.*)$", tornado.web.StaticFileHandler, dict(path=settings['img_path'])),
        # (r"/thumb/(.*)$", tornado.web.StaticFileHandler, dict(path=settings['thumb_path'])),
    ],
    **settings
    )

if __name__ == "__main__":
    try:
        app = make_app()
        app.listen(options.port)
        print("localhost:" + str(options.port))
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("\nSee You !!!")