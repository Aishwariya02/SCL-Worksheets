import matplotlib.pyplot as plt

values = {'NL': [0,31,61],
          'NM': [31,61,95],
          'NS': [61,95,127],
          'ZE': [95,127,159],
          'PS': [127,159,191],
          'PM': [159,191,223],
          'PL': [191,223,255]}

def plotTriangle():
    count = 0
    for i in values:
        a = values[i][0] 
        b = values[i][1]
        c = values[i][2]
        x = [a,b,c]
        y = [0,1,0]
        if count == 0:
            y = [1,1,0]
        elif count == len(values)-1:
            y = [0,1,1]
        count += 1
        plt.plot(x,y)
    plt.show()

def plotTrapezoid():
    for i in values:
        a = values[i][0]
        b = values[i][1]
        c = values[i][2]
        d = values[i][2] + 32
        x = [a,b,c,d]
        y = [0,1,1,0]
        plt.plot(x,y)
    plt.show()

def calculate(val):
    set1 = []
    for x in values:
        if val in [i for i in range(values[x][0],values[x][2])]:
            set1.append(x)
    return set1

def calculatemu(val,set1):
    res = {}
    for i in set1:
        res[i] = ftri(val,values[i][0],values[i][1],values[i][2])
    return res


def ftri(x,a,b,c):
    return max(min((x-a)/float(b-a),(c-x)/float(c-b)),0)

def ftrap(x,a,b,c,d):
    return max(min((x-a)/float(b-a),1,(d-x)/float(d-c)),0)

def calculate_throttle(speed,acc,speedmuset,accmuset):
    throttle = {}
    for key in values:
        throttle[key] = 0.0
    if 'NL' in speedmuset.keys() and 'ZE' in accmuset.keys():
        throttle['PL'] += min(speedmuset['NL'],accmuset['ZE'])
    if 'ZE' in speedmuset.keys() and 'NL' in accmuset.keys():
        throttle['PL'] += min(speedmuset['ZE'],accmuset['NL'])
    if 'NM' in speedmuset.keys() and 'ZE' in accmuset.keys():
        throttle['PM'] += min(speedmuset['NM'],accmuset['ZE'])
    if 'NS' in speedmuset.keys() and 'PS' in accmuset.keys():
        throttle['PS'] += min(speedmuset['NS'],accmuset['PS'])
    if 'PS' in speedmuset.keys() and 'NS' in accmuset.keys():
        throttle['NS'] += min(speedmuset['PS'],accmuset['NS'])
    if 'PL' in speedmuset.keys() and 'ZE' in accmuset.keys():
        throttle['NL'] += min(speedmuset['PL'],accmuset['ZE'])
    if 'ZE' in speedmuset.keys() and 'NS' in accmuset.keys():
        throttle['PS'] += min(speedmuset['ZE'],accmuset['NS'])
    if 'ZE' in speedmuset.keys() and 'NM' in accmuset.keys():
        throttle['PM'] += min(speedmuset['ZE'],accmuset['NM'])
    return throttle

def calculateArea(dataPoints,val):
    x1 = dataPoints[0]
    y1 = 0
    x2 = dataPoints[1]
    y2 = 1
    m = (y2-y1)/(x2-x1)
    c = y1 - (m*x1)
    v1 = (val - c)/m
    print('v1 = ',v1)
    h = val
    a = dataPoints[2] - dataPoints[0]
    x1 = dataPoints[1]
    y1 = 1
    x2 = dataPoints[2]
    y2 = 0
    m = (y2-y1)/(x2-x1)
    c = y1 - (m*x1)
    v2 = (val - c)/m
    print('v2 = ',v2)
    b = v2 - v1
    print('b = ',b)
    area = 1/2*h*(a+b)
    print('Area = ',area)
    return area

def defuzzification(throttle_val):
    '''num = 0
    den = 0
    for key in throttle_val:
        num += throttle_val[key] * ((values[key][0] + values[key][2]) / 2)
        den += throttle_val[key]
    return num / den if den != 0 else 0'''
    chosenValues = {}
    for val in throttle_val:
        chosenValues[val] = values[val]
    area = []
    for index in chosenValues:
        a = calculateArea(chosenValues[index],throttle_val[index])
        area.append(a)
    cg = 0
    print(area)
    i = 0
    for index in chosenValues:
        cg+= area[i] * chosenValues[index][1]
        i+=1
    cg = cg/sum(area)
    #print('Weighted Average or CG = ',round(cg,2))
    return cg

       
def fuzzy_controller(speed,acc):
    speedmuset = calculatemu(speed,calculate(speed))
    accmuset = calculatemu(acc,calculate(acc))
    print(speedmuset)
    print(accmuset)
    throttle = calculate_throttle(speed,acc,speedmuset,accmuset)
    print(throttle)
    plotTriangle ()
    defuz = defuzzification(throttle)
    print("Defuzzified value: ", defuz)
    

speed = 100
acc = 70
fuzzy_controller(speed,acc)
