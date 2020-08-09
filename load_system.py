#!/usr/bin/env python3
import multiprocessing
import os

def hog():
    while True:
        pass

def main():
    num_processes = len(os.sched_getaffinity(0)) * 8
    with multiprocessing.Pool(processes=num_processes) as pool:
        for _ in range(num_processes):
            pool.apply_async(hog)

        pool.close()
        pool.join()

if __name__ == '__main__':
    main()
