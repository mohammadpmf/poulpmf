import time
import threading
def count10():
    for i in range(5):
        time.sleep(1)
        print(i)

radmehr = threading.Thread(target=count10)
amirreza = threading.Thread(target=count10)
radmehr.start()
amirreza.start()

#  5s