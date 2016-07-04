import FaBoProximity_VCNL4010
import time

vcnl4010 = FaBoProximity_VCNL4010.VCNL4010()

while True:
    prox = vcnl4010.readProx()
    ambi = vcnl4010.readAmbi()

    print "Prox = ", prox,
    print "Ambi = ", ambi

    time.sleep(1)
