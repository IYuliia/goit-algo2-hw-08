import time
import random
from typing import Dict

class ThrottlingRateLimiter:
    def __init__(self, min_interval: float = 10.0):
        self.min_interval = min_interval
        self.last_message_time: Dict[str, float] = {}

    def can_send_message(self, user_id: str) -> bool:
        if user_id not in self.last_message_time:
            return True
        return time.time() - self.last_message_time[user_id] >= self.min_interval

    def record_message(self, user_id: str) -> bool:
        if self.can_send_message(user_id):
            self.last_message_time[user_id] = time.time()
            return True
        return False

    def time_until_next_allowed(self, user_id: str) -> float:
        if user_id not in self.last_message_time:
            return 0.0
        return max(0.0, self.min_interval - (time.time() - self.last_message_time[user_id]))

def test_throttling_limiter():
    limiter = ThrottlingRateLimiter(min_interval=10.0)

    print("\n=== Message Flow Simulation (Throttling) ===")
    for message_id in range(1, 11):
        user_id = message_id % 5 + 1
        result = limiter.record_message(str(user_id))
        wait_time = limiter.time_until_next_allowed(str(user_id))

        print(f"Message {message_id:2d} | User {user_id} | "
              f"{'✓' if result else f'× (waiting {wait_time:.1f}s)'}")

        time.sleep(random.uniform(0.1, 1.0))

    print("\nWaiting 10 seconds...")
    time.sleep(10)

    print("\n=== New Message Series After Waiting ===")
    for message_id in range(11, 21):
        user_id = message_id % 5 + 1
        result = limiter.record_message(str(user_id))
        wait_time = limiter.time_until_next_allowed(str(user_id))
        
        print(f"Message {message_id:2d} | User {user_id} | "
              f"{'✓' if result else f'× (waiting {wait_time:.1f}s)'}")

        time.sleep(random.uniform(0.1, 1.0))

if __name__ == "__main__":
    test_throttling_limiter()
