import threading
import queue
import time
import random

task_queue = queue.Queue()
result_queue = queue.Queue()

def create_tasks():
    print("작업 생성 시작")
    for i in range(10):
        task = f"작업{-1}"
        task_queue.put(task)
        print(f"작업 추가 : {task}")
        time.sleep(random.uniform(0.1, 0.3))

    for _ in range(3):
        task_queue.put(None)
    print("모든 작업 생성 완료")

def worker(worker_id):
    print(f"워커 {worker_id} 시작")
    while True:
        task = task_queue.get()

        if task is None:
            print(f"워커 {worker_id} 종료")
            break

        print(f"워커 {worker_id}가 {task} 처리 중 ...")
        processing_time = random.uniform(0.5, 1.5)
        time.sleep(processing_time)

        result = f"{task} 완료 (소요시간 : {processing_time:.2f}초)"
        result_queue.put((worker_id, result))

        task_queue.task_done()
        print(f"남은 작업 수 : {task_queue.qsize()}")

def result_collector():
    print("\n결과 수집 시작\n")
    results = []

    for _ in range(10):
        worker_id, result = result_queue.get()
        print(f"결과 수신 : 워커 {worker_id} -> {result}")
        results.append(result)
        result_queue.task_done()

        print(f"\n총 {len(results)}개 결과 수집 완료\n")

creator = threading.Thread(target=create_tasks)
workers = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
collector = threading.Thread(target=result_collector)

creator.start()
for w in workers:
    w.start()
collector.start()

creator.join()
for w in workers:
    w.join()
collector.join()

print("\n모든 작업 완료\n")