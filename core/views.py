from django.http import HttpResponse

def test(request):
    return HttpResponse('Hello World from Django!!')
def test2(request):
    return HttpResponse('Outra páginaa')