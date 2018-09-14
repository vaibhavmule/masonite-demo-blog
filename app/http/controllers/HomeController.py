''' Welcome The User To Masonite '''

class HomeController:
    ''' Controller For Welcoming The User '''

    def show(self, Application):
        ''' Show Welcome Template '''
        return view('index', {'app': Application})
