''' Web Routes '''
from masonite.routes import Get, Post, Put, Delete
from dashboard.routes import routes as DashboardRoutes

ROUTES = [
    Get().route('/', 'HomeController@show').name('welcome'),

    DashboardRoutes(),

    Get().route('/blog', 'PostsController@show_all'),
    Get().route('/blog/post/@id', 'PostsController@show_one'),


    Get().route('/blog/category/@id', 'PostsController@show_category'),
    Get().route('/blog/author/@id', 'PostsController@show_author'),

    Get().route('/dashboard/blog', 'BlogEditorController@show_all'),

    Get().route('/dashboard/post/create', 'BlogEditorController@show_create'),
    Post().route('/dashboard/post/create', 'BlogEditorController@create'),

    Get().route('/dashboard/post/@id/update', 'BlogEditorController@show_update'),
    Post().route('/dashboard/post/@id/update', 'BlogEditorController@update'),

    Get().route('/dashboard/post/@id/delete', 'BlogEditorController@show_delete'),
    Post().route('/dashboard/post/@id/delete', 'BlogEditorController@delete'),

    Get().route('/dashboard/post/@id/activate', 'BlogEditorController@activate'),
    Get().route('/dashboard/post/@id/deactivate', 'BlogEditorController@deactivate'),

    Get().route('/dashboard/post/preview/@id', 'BlogEditorController@preview'),
    
    Get().route('/dashboard/profile', 'ProfileController@show'),
    Post().route('/dashboard/profile', 'ProfileController@store')


]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show'),
    Get().route('/logout', 'LoginController@logout'),
    Post().route('/login', 'LoginController@store'),
    # Get().route('/register', 'RegisterController@show'),
    # Post().route('/register', 'RegisterController@store'),
    Get().route('/home', 'HomeController@show'),
]
