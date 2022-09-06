# %% [markdown]
# # Python Multiprocessing
#

# %%
# imports
import time
import multiprocessing

# %%
# Start time of script
start = time.perf_counter()

# %%
# Simple function which sleeps for {sleep_seconds} second(s)
def do_something(sleep_seconds=0):
    print(f"Start sleeping for {sleep_seconds} second(s)")
    time.sleep(sleep_seconds)
    print(f"Done sleeping for {sleep_seconds} second(s)")


# %%
x = 5  # number of processe
processes = []  # empty list to store threads

for _ in range(x):
    p = multiprocessing.Process(target=do_something, kwargs={"sleep_seconds": 1})
    p.start()
    print(f"Running in Process: {p.name}, PID:{p.pid}")
    processes.append(p)

for process in processes:
    process.join()

# %%
# End time of script
end = time.perf_counter()

print(f"completed in {round(end-start, 2)} second(s)")
