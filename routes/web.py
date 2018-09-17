''' Web Routes '''
from masonite.routes import Get, Post
from dashboard.routes import routes as DashboardRoutes

ROUTES = [
    Get().route('/', 'HomeController@show').name('welcome'),
    
    DashboardRoutes(),

    Get().route('/blog', 'PostsController@show_all'),
    Get().route('/blog/post/@id', 'PostsController@show_one'),

    Get().route('/dashboard/blog', 'BlogEditorController@show'),
    Get().route('/dashboard/post/create', 'BlogEditorController@show_create'),
    Post().route('/dashboard/post/create', 'BlogEditorController@create')


]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show'),
    Get().route('/logout', 'LoginController@logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show'),
    Post().route('/register', 'RegisterController@store'),
    Get().route('/home', 'HomeController@show'),
]
