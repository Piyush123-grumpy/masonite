from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from app.models.Todo import Todo

class PagesController(Controller):

    def __init__(self,view:View,request:Request):
        self.view=view
        self.request=request

    def nigga(self):
        return self.view.render("firstpage",{
            "username":self.request.param("username"),
            "todos":Todo.all()
        })
    def show(self):
        return Todo.all()
