''' Web Routes '''
from masonite.routes import Get, Post
from dashboard.routes import routes as DashboardRoutes

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),
    DashboardRoutes()
]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show'),
    Get().route('/logout', 'LoginController@logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show'),
    Post().route('/register', 'RegisterController@store'),
    Get().route('/home', 'HomeController@show'),
]
