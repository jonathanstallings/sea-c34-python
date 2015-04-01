#creating module with four errors
#how to tell if she is a whitch?
whitch="Burn her!"
#resolve name error by defining *whitch*
#she=whitch()  this creates a type error - str object not callable
she=[]    #type error resolved
#setattr(she, 'turned_me_into_a_newt', True)    resolve attribute error
#list object has no attribute 'turned_me_into_a_newt'
var1='turned_me_into_a_newt'
she.append(var1)    #resolve syntax error
print(she)
if var1 in she:
    print(whitch)
else:
    print('got better')
