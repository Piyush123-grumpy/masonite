from masonite.routes import Route

ROUTES = [Route.get("/", "WelcomeController@show"),
Route.get("/nigga", "PagesController@nigga"),
Route.get("/firstpage/@username", "PagesController@nigga"),
Route.get("/all", "PagesController@show")
]


