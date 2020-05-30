# from werkzeug.serving import run_simple
# from werkzeug.wrappers import Request, Response
#
# @Request.application
# def app(request):
#     print(request.method)
#     return Response('ok')
#
# run_simple("127.0.0.1", 9527, app)

class Oldboy(object):
    def __call__(self, *args, **kwargs):
        print("666")
    # pass

ob = Oldboy()

ob()