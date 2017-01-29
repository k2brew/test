from tasks import add

for x in range(100000):
    add.delay(x,x)
# add.delay(4,4)
# add.delay(5,5)
# add.delay(6,5)
