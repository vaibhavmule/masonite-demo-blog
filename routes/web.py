''' Web Routes '''
from masonite.routes import Get, Post
from masonite.routes import RouteGroup
from dashboard.routes import routes as DashboardRoutes

ROUTES = [
    Get().route('/', 'HomeController@show').name('welcome'),

    # Blog
    RouteGroup([
        Get().route('/blog', 'PostsController@show_all'),
        Get().route('/blog/post/@id', 'PostsController@show_one'),
        Get().route('/blog/category/@id', 'PostsController@show_category'),
        Get().route('/blog/author/@id', 'PostsController@show_author'),
    ]),

    # Dashboard
    DashboardRoutes(),

    RouteGroup([
        Get().route('/blog', 'BlogEditorController@show_all'),
        Get().route('/profile', 'ProfileController@show'),
        Post().route('/profile', 'ProfileController@store'),

        # Blog Editor
        RouteGroup([
            Get().route('/create', 'BlogEditorController@show_create'),
            Post().route('/create', 'BlogEditorController@create'),

            Get().route('/@id/update', 'BlogEditorController@show_update'),
            Post().route('/@id/update', 'BlogEditorController@update'),

            Get().route('/@id/delete', 'BlogEditorController@show_delete'),
            Post().route('/@id/delete', 'BlogEditorController@delete'),

            Get().route('/@id/activate', 'BlogEditorController@activate'),
            Get().route('/@id/deactivate', 'BlogEditorController@deactivate'),

            Get().route('/preview/@id', 'BlogEditorController@preview')
        ], prefix="/post")

    ], prefix='/dashboard', middleware=('auth',))

]
