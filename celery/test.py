from tasks import add

#f = open("output.txt","w")

for x in range(10001):
    add.apply_async((x,x), countdown=3)

#f.close()
# add.delay(4,4)
# add.delay(5,5)
# add.delay(6,5)
