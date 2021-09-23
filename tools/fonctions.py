from datetime import date

#Convert string xxxx-xx-xx to python date()
def convertDateTime(value):
    inter = str(value).split('-')
    result = [ int(x) for x in inter ] #numbers = list(map(int, numbers))
    return date(result[0], result[1], result[2])

def which(self):
    try:
        self = list(iter(self))
    except TypeError as e:
        raise Exception("""'which' method can only be applied to iterables.
        {}""".format(str(e)))
    indices = [i for i, x in enumerate(self) if bool(x) == True]
    return(indices[0])
