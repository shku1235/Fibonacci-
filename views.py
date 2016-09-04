from django.shortcuts import render
from fibpro import fiblogic
from forms import fibform

# Create your views here.

def index(request):
    return render(request, 'fib/search.html',)


def fibview(request):
    print "here"
    res=None
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = fibform(request.POST)
        print 'got post'
        print form
        print form.cleaned_data
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            print form.cleaned_data
            que=form.cleaned_data
            asked = que['fin']
            res,t=fiblogic(asked)

            print res
        return render(request, 'fib/index.html', {'res': res,'t':t})
