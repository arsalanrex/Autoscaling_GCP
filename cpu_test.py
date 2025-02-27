import multiprocessing
import time

def cpu_intensive_task():
    while True:
        _ = [x**2 for x in range(10**6)]  # CPU-heavy computation

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()  # Get number of CPU cores
    print(f"Using {num_cores} CPU cores for high utilization...")
    
    processes = []
    for _ in range(num_cores):
        p = multiprocessing.Process(target=cpu_intensive_task)
        p.start()
        processes.append(p)
    
    try:
        while True:
            time.sleep(10)  # Keep the script running
    except KeyboardInterrupt:
        print("Stopping stress test...")
        for p in processes:
            p.terminate()
            p.join()
