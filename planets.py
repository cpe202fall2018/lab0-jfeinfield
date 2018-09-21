def weight_on_planets():
   weight = float(input('What do you weigh on earth? '))
   mWeight = .38 * weight
   jWeight = 2.34 * weight

   print('\nOn Mars you would weigh'  , mWeight , 'pounds.\nOn Jupiter you would weigh' , jWeight , 'pounds.')
   
if __name__ == '__main__':
   weight_on_planets()
