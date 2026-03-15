import time
from threading import Thread
from workers.ingestion_worker import run_worker as run_ingestion
from workers.ai_analysis_worker import run_worker as run_ai
from workers.cleanup_worker import run_worker as run_cleanup

def start_thread(target):
    t = Thread(target=target, daemon=True)
    t.start()
    return t

def scheduler():
    print("[Scheduler] Starting all workers")

    # Start workers in parallel
    start_thread(run_ingestion)
    start_thread(run_ai)
    start_thread(run_cleanup)

    print("[Scheduler] All workers running")

    # Keep scheduler alive
    while True:
        time.sleep(60)

if __name__ == "__main__":
    scheduler()
