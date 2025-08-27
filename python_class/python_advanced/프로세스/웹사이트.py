import asyncio
import aiohttp
import time

websites = [
    
    "https://www.google.com",
    "https://www.naver.com",
    "https://www.daum.net",
    "https://www.github.com",
    "https://www.python.org",
    "https://www.microsoft.com",
    "https://www.amazon.com",
    "https://www.reddit.com",
]


async def fetch(session, url):

    print(f"{url} 요청 시작")
    try:
        start_time = time.time()
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
            content = await response.text()
            elapsed = time.time() - start_time
            print(f"{url} 응답 완료 : {len(content)} 바이트 (소요시간 : {elapsed:.2f}초)")
            return url, len(content), elapsed
    except Exception as e:
        print(f"{url} 오류 발생 : {e}")
        return url, 0, 0
    
async def fetch_all_sequential(urls):

    print("\n --- 순차 처리 --- ")
    start_time = time.time()
    results = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            result = await fetch(session, url)
            results.append(result)

    end_time = time.time()
    print(f"순차 처리 완료 : {end_time - start_time:.2f}초 소요")
    return results

async def fetch_all_parallel(urls):

    print("\n --- 병렬 처리 --- ")
    start_time = time.time()
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"병렬 처리 완료 : {end_time - start_time:.2f}초 소요")
    return results

async def main():

    sequential_results = await fetch_all_sequential(websites)
    await asyncio.sleep(1)
    parallel_results = await fetch_all_parallel(websites)

    print("\n --- 결과 요약 --- ")
    seq_total_bytes = sum(r[1] for r in sequential_results)
    par_total_bytes = sum(r[1] for r in parallel_results)

    print(f"순차 처리 : 총 {seq_total_bytes} 바이트")
    print(f"병렬 처리 : 총 {par_total_bytes} 바이트")
    
if __name__ == "__main__":
    asyncio.run(main())