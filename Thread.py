import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: Dimulai", name)
    time.sleep(2)
    logging.info("Thread %s: Diakhiri", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : Sebelum Membuat Thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : Sebelum Menjalankan Thread")
    x.start()
    logging.info("Main    : Menunggu Thread Untuk Selesai")
    x.join()
    logging.info("Main    : Thread Selesai")