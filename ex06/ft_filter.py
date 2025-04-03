def ft_filter(function, params):
    """filter() function re coded"""
    if function is None:
        return (item for item in params if item)
    return (item for item in params if function(item))