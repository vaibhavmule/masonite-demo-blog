''' Dashboard Authentication Middleware '''

class DashboardAuthenticationMiddleware:
    ''' Middleware To Check If The User Is Logged In. If not, redirect to dashboard login page '''

    def __init__(self, Request):
        ''' Inject Any Dependencies From The Service Container '''
        self.request = Request

    def before(self):
        ''' Run This Middleware Before The Route Executes '''
        if not self.request.user():
            self.request.redirect_to('dashboard/login')

    def after(self):
        ''' Run This Middleware After The Route Executes '''
        pass
