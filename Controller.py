# all the top level code

# web.py


import web
from Models import RegisterModel


urls = (
    '/', 'Home',
    '/register', 'Register',
    '/postregistration', 'PostRegistration'
)

render = web.template.render("Views/Templates", base="MainLayout")

app = web.application(urls, globals())


# Classes/Routes
# Each class will be controlling a route

class Home:
    def GET(self):
        return render.Home()

class Register:
    def GET(self):
        return render.Register()

class PostRegistration:
    def POST(self):
        data = web.input()
        print(data.username)

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username


if __name__=="__main__":
    app.run()