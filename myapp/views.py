from django.shortcuts import render, HttpResponse

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is...'},
    {'id':2, 'title':'view', 'body':'View is...'},
    {'id':3, 'title':'model', 'body':'Model is...'}
]
# Create your views here.
# 클라이언로 정보를 전송하기 위한 함수를 만든다.
# 우리가 처리한 결과를 클라이언트로 보내줄 때 return을 사용한다.(여기에서는 HttpResponse라는 객체이용)
def HTMLTemplate(articleTag): 
    global topics
    for topic in topics:
        ol = f'<li><a></a href="/read/{topics["id"]}">{topics["title"]}</li>'
        
    return f'''        
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
    </body>    
    </html>
    '''

def index(request):
    article = '''<h2>Welcome</h2>
        Hello, Django'''
    
    return HttpResponse(HTMLTemplate(article)) #article이라는 매개변수는 HTMLTemplate함수에서 articleTag라는 매개변수로 들어가 사용된다.
                        

def create(request):
    return HttpResponse('This is Login page')

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))
