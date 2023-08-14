employess=[
    {"name":"a","salary":3000,"destination":"development"},
    {"name":"b","salary":4000,"destination":"development"},
    {"name":"c","salary":3500,"destination":"development"}
    ]

max_employee=max([key["salary"] for key in employess])
arr=[key if key["salary"]==max_employee else None for key in employess]
for i in arr:
    if i:
        print(i)