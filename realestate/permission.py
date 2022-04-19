
from django.shortcuts import render,redirect
from django.core.exceptions import PermissionDenied

def is_agent(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.agent.is_approved:
            return function(request, *args, **kwargs)
        else:
            # raise PermissionDenied
            return redirect('applyagent')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


