def mean(value):
    # if type(value)==dict:
    if isinstance(value,dict):
        the_mean=sum(value.values())/len(value)
    else:
        the_mean=sum(value)/len(value)
        
    return the_mean


funcall=mean({"sat": 89,"bob":90,"marry":95})
fun_call=mean([0,1,4,2,9,3,7,5,6,8])
print(funcall)
print(fun_call)





