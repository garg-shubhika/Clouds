import logging
import math
import azure.functions as func
N1=[10,100, 100, 1000, 10000, 100000, 1000000]
def fun(lower,upper):
    str1=' '
    N=[10,100, 100, 1000, 10000, 100000, 1000000]
    A=0.0
    lower=float(lower)
    upper=float(upper)
    I=[]
    for j in N:
        A=0.0
        for i in range(1,j):
            A=A+(-math.cos(i*upper/j)+math.cos((i-1)*upper/j + lower))
        I.append(A)
    for x in I:
        str1=str(x)+' '+str1
    return str1

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    start = req.params.get('start')
    end = req.params.get('end')

    if not start and not end:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            start = req_body.get('start')
            end = req_body.get('end')

    if start and end:

        for N in N1:
            res = fun(float(start), float(end))
            print("result: " + str(res))
            return func.HttpResponse(f"Finished, {start} , {end} , {res}. Numerical integration fuction app.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response",
             status_code=200
        )


