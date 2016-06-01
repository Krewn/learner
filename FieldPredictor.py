###########################################################    ____                   ______ _      _     _
##   Author : Kevin Nelson                             ####  / ____|                 |  ____(_)    | |   | |
#		kpie314@gmail.com   ArtisticLicense             ### | |  __  ___ _ __   ___  | |__   _  ___| | __| |___
##      Creating predictive fields from given data     #### | | |_ |/ _ \ '_ \ / _ \ |  __| | |/ _ \ |/ _` / __|
########################################################### | |__| |  __/ | | |  __/ | |    | |  __/ | (_| \__ \
###########################################################  \_____|\___|_| |_|\___| |_|    |_|\___|_|\__,_|___/

def Min(a):
    m = None
    for k in a:
        if (k != None):
            m = k if (k < m or m is None)else m
    return m


def Max(a):
    m = None
    for k in a:
        if (k != None):
            m = k if (k > m or m is None)else m
    return m


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def colMin(data, col):
    return (Min([data[k][col] for k in range(0, len(data))]))


def colMax(data, col):
    return (Max([data[k][col] for k in range(0, len(data))]))


def EucAB(a, b):
    dist = 0.
    if (len(a) != len(b)): raise ValueError('Vectors are not of similar dimensionality.')
    for k in range(0, len(a)):
        if (a[k] != None and b[k] != None):
            dist += (a[k] - b[k]) ** 2
    dist = dist ** 0.5
    return (dist)


def EucABdims(a, b):
    dist = 0.
    d = 0
    if (len(a) != len(b)): raise ValueError('Vectors are not of similar dimensionality.')
    for k in range(0, len(a)):
        if (a[k] != None and b[k] != None):
            dist += (a[k] - b[k]) ** 2
            d += 1
    dist = dist ** 0.5
    return ((dist, d))


def fetchpPrediction(data, row, col):                          # Rows of models, columns of output layer.
    p = 0.  # prediction = 0
    bot = 0.
    m = colMax(data, col) - colMin(data, col)
    if(m == 0):
        return(colMax(data, col))
    for k in range(0, len(data)):
        temp = EucABdims(data[k], data[row])
        euc = temp[0]                                          # the euclidean distance between two samples
        dims = temp[1]                                         # the number of genes in the union of two samples data
        if (k != row and dims != 0 and data[k][col] != None):  # does not use samples with 0** common genes to make predictions.
            p += data[k][col] / ((euc+0.000001) ** 2)          # Adds to a weighted sum
            bot += m / ((euc+0.000001) ** 2)                   # Adds to a weighted averager    ## poorMan's limit : p Im2lz7
	if(bot == 0):
		return(colMin(data, col)+m/2.)
    return ( colMin(data, col)+m*(p / bot) )


a = [[0., 0., 1.],
     [0., None, 1.],
     [0., 1, 0.]]

print(str(fetchpPrediction(a, 1, 1))) #Example filling in a blank value

def cook(data):
    r = [ k[:] for k in data ] #makes a detached copy from
    for k in range(0,len(r)):
        for k2 in range(0,len(r[k])):
            if(r[k][k2]==None):
                r[k][k2]=fetchpPrediction(a, k, k2)
    return(r)

def pr(data):
    s = ""
    for k in data:
        for k2 in k:
            s += str(round(k2,5) if k2!= None else "Nan")+"\t"*3
        s += "\n"
    return(s)

print("In:")
print(pr(a))
print("Out:")
print(pr(cook(a))) # example batch run for a table