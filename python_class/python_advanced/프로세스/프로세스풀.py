import multiprocessing
import time
import os

def process_task(task_id):
    process_id = os.getpid()
    print(f"작업 {task_id} 시작 (프로세스 ID : {process_id})")
    
    result = 0
    for i in range(10000000):
        result += 1
    print(f"작업 {task_id} 완료 (프로세스 ID : {process_id})")
    return task_id, result, process_id

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    print(f"시스템 CPU 코어 수 : {num_cores}")

    tasks = range(10)

    start_time = time.time()
    sequential_results = [process_task(i) for i in tasks]
    end_time = time.time()
    print(f"순차 처리 시간 : {end_time - start_time:.2f}초")

    start_time = time.time()
    with multiprocessing.Pool(processes=num_cores) as pool:
        parallel_results = pool.map(process_task, tasks)
    end_time = time.time()
    print(f"병렬 처리 시간 : {end_time - start_time:.2f}초")

    process_ids = set(result[2] for result in parallel_results)
    print(f"사용된 프로세스 수 : {len(process_ids)}")
    print(f"프로세스 ID 목록 : {process_ids}")