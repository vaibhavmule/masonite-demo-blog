''' Web Routes '''
from masonite.routes import Get, Post
from dashboard.routes import routes as DashboardRoutes

ROUTES = [
    Get().route('/', 'HomeController@show').name('welcome'),
    DashboardRoutes(),

    Get().route('/posts', 'AllPostsController@show'),
    Get().route('/post/@id:string', 'ShowPostController@show'),

    Get().route('/create', 'NewPostController@show'),
    Post().route('/create', 'NewPostController@store'),

]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show'),
    Get().route('/logout', 'LoginController@logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show'),
    Post().route('/register', 'RegisterController@store'),
    Get().route('/home', 'HomeController@show'),
]
