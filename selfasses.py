try:
    n = int(input('how old are you'))
    percent = round(n*100/80,1)
    print('youve gone through', percent,'%of your life')
except ValueError:
    print('number')
except ZeroDivisionError:
    print('zero')
except:
    print('dd')