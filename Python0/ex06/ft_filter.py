def ft_filter(function, params):
    """filter() function re coded
    We filter for function() by the given params.
    If the function is none it returns truthy item"""
    if function is None:
        return [item for item in params if item]
    return [item for item in params if function(item)]