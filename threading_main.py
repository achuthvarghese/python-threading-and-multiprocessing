# %% [markdown]
# # Python Threading
#

# %%
# imports
import time
import threading


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
x = 5  # number of threads
threads = []  # empty list to store threads

for _ in range(x):
    t = threading.Thread(target=do_something, kwargs={"sleep_seconds": 1})
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


# %%
# End time of script
end = time.perf_counter()

print(f"completed in {round(end-start, 2)} second(s)")
