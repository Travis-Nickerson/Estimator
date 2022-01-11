import math

def Pricing(setup, prep, paint, gallons,paintCost, burdenRate, discount):
    data = {}
    print('Setup: '+ str(setup) + '\nPrep: ' + str(prep) + '\nPaint Amount: ' + str(paint) + '\nCost per Gallon: $' + str(paintCost) + '\nRate: $' + str(burdenRate) + '/hr')
    totalHours = setup + prep + paint
    twoCoatPaint = setup + prep + ((paint) * 1.75)
    print('\nTotal Hours for job: ' + str(totalHours) + '\n')

    # 1 Coat Pricing
    # Labor Budget
    data['1c LB'] = str(totalHours * burdenRate)
    # Material Budget
    data['1c MB'] = str(gallons * paintCost)
    # Price 1c
    data['1c Price'] = str(round(totalHours * burdenRate)/0.375)
    # Price 1c with materials
    data['1c mat Price'] = str(round(float((twoCoatPaint * burdenRate) + gallons * 1.75 * paintCost) / 0.375))

    # 2 Coat Pricing
    # Labor Budget
    data['2c LB'] = str(round(twoCoatPaint * burdenRate))
    # Material Budget
    data['2c MB'] = str(gallons * paintCost)
    # Price 2c
    data['2c Price'] = str(round(twoCoatPaint * burdenRate) / 0.375)
    # Price 2c with materials
    data['2c mat Price'] = str(round(float(((setup + prep + paint * 1.75) * burdenRate) + gallons * 1.75 * paintCost) / 0.375))

    # Apply discount to pricing if applicable
    if discount != 0:
        # 1 Coat Pricing
        # Price 1c
        data['1c Price dis'] = round(float(data['1c Price']) - (float(data['1c Price']) * discount))
        # Amount Saved
        data['1c Price dis saving'] = round(float(data['1c Price']) * discount)
        # Price 1c with materials
        data['1c mat Price dis'] = round(float(data['1c mat Price']) - (float(data['1c mat Price']) * discount))
        # Amount Saved
        data['1c mat Price dis saving'] = float(data['1c mat Price']) * discount

        # 2 Coat Pricing
        # Price 2c
        data['2c Price dis'] = round(float(data['2c Price']) - (float(data['2c Price']) * discount))
        # Amount Saved
        data['2c Price dis saving'] = round(float(data['2c Price']) * discount)
        # Price 2c with materials
        data['2c mat Price dis'] = round(float(data['2c mat Price']) - (float(data['2c mat Price']) * discount))
        # Amount Saved
        data['2c mat Price dis saving'] = round(float(data['2c mat Price']) * discount)

    Export(data)

def Export(pricing):
    for x in pricing:
        # First Coat data
        if x == '1c LB':
            print('1 Coat Labor Budget: $' + str(pricing[x]))
        if x == '1c MB':
            print('1 Coat Materials Budget: $' + str(pricing[x]))
        if x == '1c Price':
            print('1 Coat Price no materials: $' + str(pricing[x]))
        if x == '1c mat Price':
            print('1 Coat Price with materials: $' + str(pricing[x]))
        # Second Coat data
        if x == '2c LB':
            print('2 Coat Labor Budget: $' + str(pricing[x]))
        if x == '2c MB':
            print('2 Coat Materials Budget: $' + str(pricing[x]))
        if x == '2c Price':
            print('2 Coat Price no materials: $' + str(pricing[x]))
        if x == '2c mat Price':
            print('2 Coat Price with materials: $' + str(pricing[x]))
        # One Coat discount data
        if x == '1c Price dis':
            print('1 Coat Price no materials discount: $' + str(pricing[x]))
        if x == '1c Price dis saving':
            print('1 Coat Price Savings: $' + str(pricing[x]))
        if x == '1c mat Price dis':
            print('1 Coat Price with materials discount: $' + str(pricing[x]))
        if x == '1c mat Price dis saving':
            print('1 Coat Price with materials Savings: $' + str(pricing[x]))
        # Second Coat discount data
        if x == '2c Price dis':
            print('2 Coat Price no materials discount: $' + str(pricing[x]))
        if x == '2c Price dis saving':
            print('2 Coat Price Savings: $' + str(pricing[x]))
        if x == '2c mat Price dis':
            print('2 Coat Price with materials discount: $' + str(pricing[x]))
        if x == '2c mat Price dis saving':
            print('2 Coat Price with materials Savings: $' + str(pricing[x]))

def round(x):
    return(math.ceil(x*4)/4)
    
setup = input('Enter the setup hours: ')
setup = round(float(setup))
prep = input('Enter the prep hours: ')
prep = round(float(prep))
painting = input('Enter the paint Hours: ')
painting = round(float(painting))
gallons = input('Enter gallons needed for job: ')
gallons = round(float(gallons))
paintCost = input('Enter the Paint cost before overhead: ')
paintCost = round(int(paintCost))
burdenRate = input('Enter the burden rate hourly, ex. 30 for $30/hr: ')
burdenRate = round(float(burdenRate))
discount = input('Enter a discount if desired, .1 is 10 percent off, enter 0 if no discount: ')
discount = float(discount)

Pricing(setup,prep,painting, gallons, paintCost,burdenRate,discount)


