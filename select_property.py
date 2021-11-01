# %%
#######################################
def select_property(obj: object, *args):
    """From a given namedtuple object, returns the properties/attributes referenced for the given object.

    Examples:
        >>> results = new_objects_from_csv('brandnew.csv')\n
        >>> pprint(results)\n
        [CustObj(NAME='bob', AGE='21', JOB=' janitor', DEPARTMENT=' sanitization team', PAY='2'),\n
        CustObj(NAME='alice', AGE='22', JOB=' secretary', DEPARTMENT=' admin team', PAY='3'),\n
        CustObj(NAME='chuck', AGE='23', JOB=' plumber', DEPARTMENT=' construction team', PAY='4')]\n

        >>> select_property(results[0], "NAME","PAY")\n
        [('bob', '2')]\n
        >>>\n
        >>> select_property(results, "NAME","PAY")\n
        [('bob', '2'), ('alice', '3'), ('chuck', '4')]\n

    References:
        # Showed the use of "getattr()" which I used in this function:
        https://stackoverflow.com/questions/44634972/how-to-access-a-field-of-a-namedtuple-using-a-variable-for-the-field-name

    Args:
        obj (object): Reference a single custom object or a list of custom objects
        
    Returns:
        list: Returns a list of selected property/attribute values for each object
    """
    results_list = []
#    
    if not isinstance(obj, list):
        templist = []
        for arg in args:
            templist.append(getattr(obj, arg))
        results_list.append(tuple(templist))
#
    elif isinstance(obj, list):
        for eachitem in obj: 
            templist = []
            for arg in args:
                templist.append(getattr(eachitem, arg))
            results_list.append(tuple(templist))
#            
    return results_list

