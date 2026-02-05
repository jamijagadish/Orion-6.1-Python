import time
import threading

#Without multithreading
# def download(file):
#     print(f"Downloading {file}")
#     time.sleep(2)
#     print("Downloading completed")

# start = time.time()
# # print(start)

# download("file1")
# download("file2")
# download("file3")
# end = time.time()

# print("Time", end - start)

#With multithreading
def downloading(file):
    print(f"Downloading {file}")
    time.sleep(2)
    print("Downloading completed")

startTime = time.time()

t1 = threading.Thread(target=downloading, args=("file1",))
t2 = threading.Thread(target=downloading, args=("file2",))
t3 = threading.Thread(target=downloading, args=("file3",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.time()
print("Time", end - startTime)


#Without Multiprocessing
# def square(num):
#     return num * num

# for i in range(1000000):
#     print(square(i))

#With Multiprocessing
# from multiprocessing import Process

# def square():
#     for i in range(500000):
#         print(i * i)

# if __name__ == "__main__":
#     p1 = Process(target=square)
#     p2 = Process(target=square)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()