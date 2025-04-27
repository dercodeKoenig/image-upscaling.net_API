# Usage example
res = submit(client_id, "Hello world", "am_adam", speed=1.2)
print(res)

import time
while True:
    statuses = get_status(client_id)
    for job in statuses:
        print(job)
    time.sleep(2)