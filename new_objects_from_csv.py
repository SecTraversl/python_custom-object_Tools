# %%
#######################################
def new_objects_from_csv(csv_file: str):
    """For each row in the .csv, returns a list of custom objects with properties/attributes corresponding to the header names of each column.

    Example:
        >>> results = new_objects_from_csv('brandnew.csv')\n
        >>> pprint(results)\n
        [CustObj(NAME='bob', AGE='21', JOB=' janitor', DEPARTMENT=' sanitization team', PAY='2'),\n
        CustObj(NAME='alice', AGE='22', JOB=' secretary', DEPARTMENT=' admin team', PAY='3'),\n
        CustObj(NAME='chuck', AGE='23', JOB=' plumber', DEPARTMENT=' construction team', PAY='4')]\n

    Reference:
        # I retrieved the full body of the code below from here; this article has some great info
        https://realpython.com/python-namedtuple/\n

    Args:
        csv_file (str): Reference an existing .csv.

    Returns:
        object: Returns a custom object.
    """
    import csv
    from collections import namedtuple
    
    results_list = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        CustObj = namedtuple('CustObj', next(reader), rename=True)
        for row in reader:
            myobj = CustObj(*row)
            results_list.append(myobj)
    return results_list

