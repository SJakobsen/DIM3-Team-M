from django.http import HttpResponse

def index(request):
    return HttpResponse("MAIN PAGE   <a href='/gofish/login/'>login</a>   <a href='/gofish/register/'>register</a>   <a href='/gofish/game/'>game</a>")
    
def login(request):
    return HttpResponse("LOGIN PAGE   <a href='/gofish/'>index</a>   <a href='/gofish/register/'>register</a>   <a href='/gofish/game/'>game</a>")
    
def register(request):
    return HttpResponse("REGISTER PAGE   <a href='/gofish'>index</a>   <a href='/gofish/login/'>login</a>   <a href='/gofish/game/'>game</a>")
    
def game(request):
    return HttpResponse("GAME PAGE   <a href='/gofish/'>index</a>   <a href='/gofish/login/'>login</a>   <a href='/gofish/register/'>register</a>")