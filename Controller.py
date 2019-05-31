# all the top level code

# web.py


import web
from Models import RegisterModel, LoginModel

web.config.debug = False

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/postregistration', 'PostRegistration',
    '/check-login', 'CheckLogin'
)

#the "app" line should be above the "render" line. Coz we will be writing code between "app" and "render".
app = web.application(urls, globals())

# A session is a way to store information (in variables) to be used across multiple pages.
# Unlike a cookie, the information is not stored on the users computer.
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer = {"user" : None})

#We need to initialize the Initializer which then will initialize the session.
session_data = session._initializer






# Passing globals in the render method means, we don't need to pass the session_data to each of the below routes(like
# Home, Register, Login, etc. The session variable will always going to exist for any of these routes in the HTML
# templates.
render = web.template.render("Views/Templates", base="MainLayout", globals={"session":session_data,
                                                                            "current_user": session_data["user"]})

# Classes/Routes
# Each class will be controlling a route

class Home:
    def GET(self):
        return render.Home() # this will open the MainLayout.html with Home.html content

class Register:
    def GET(self):
        return render.Register() # this will open the MainLayout.html with Register.html content

class Login:
    def GET(self):
        return render.Login() # this will open the MainLayout.html with Login.html content

class PostRegistration:
    def POST(self):
        data = web.input()
        print(data.items())

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username


class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()

        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect
            return isCorrect

        return "error"

class Logout:
    def GET(self):
        session["user"] = None
        session_data["user"] = None
        session.kill()
        return "success"




if __name__=="__main__":
    app.run()