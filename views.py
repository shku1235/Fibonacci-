from django.shortcuts import render
from fibpro import fiblogic
from forms import fibform

# Create your views here.

def index(request):
    return render(request, 'fib/search.html',)


def fibview(request):
    print "here"
    res=None
   
    if request.method == 'POST':
       
        form = fibform(request.POST)
        print 'got post'
        print form
        print form.cleaned_data
        # check whether it's valid:
        if form.is_valid():
           

            print form.cleaned_data
            que=form.cleaned_data
            asked = que['fin']
            res,t=fiblogic(asked)

            print res
        return render(request, 'fib/index.html', {'res': res,'t':t})
