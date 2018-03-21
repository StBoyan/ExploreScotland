from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def child_is_selected(function):
    def wrap(request, *args, **kwargs):
        try:
            child_name = request.session['child_session']
        except KeyError:
            return HttpResponseRedirect(reverse('children_area'))

        if child_name is None:
            return HttpResponseRedirect(reverse('children_area'))

        return function(request, *args, **kwargs)

    wrap.__doc__=function.__doc__
    wrap.__name__=function.__name__
    return wrap
