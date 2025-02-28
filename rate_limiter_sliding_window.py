import random
import time
from typing import Dict
from collections import deque

class SlidingWindowRateLimiter:
    def __init__(self, window_size: int = 10, max_requests: int = 1):
        self.window_size = window_size
        self.max_requests = max_requests
        self.user_messages: Dict[str, deque] = {}

    def _cleanup_window(self, user_id: str, current_time: float) -> None:
        if user_id in self.user_messages:
            while self.user_messages[user_id] and self.user_messages[user_id][0] <= current_time - self.window_size:
                self.user_messages[user_id].popleft()
            if not self.user_messages[user_id]:
                del self.user_messages[user_id]

    def can_send_message(self, user_id: str) -> bool:
        current_time = time.time()
        self._cleanup_window(user_id, current_time)
        if user_id not in self.user_messages or len(self.user_messages[user_id]) < self.max_requests:
            return True
        return False

    def record_message(self, user_id: str) -> bool:
        if self.can_send_message(user_id):
            if user_id not in self.user_messages:
                self.user_messages[user_id] = deque()
            self.user_messages[user_id].append(time.time())
            return True
        return False

    def time_until_next_allowed(self, user_id: str) -> float:
        current_time = time.time()
        self._cleanup_window(user_id, current_time)
        if user_id not in self.user_messages or len(self.user_messages[user_id]) < self.max_requests:
            return 0.0
        oldest_message_time = self.user_messages[user_id][0]
        wait_time = self.window_size - (current_time - oldest_message_time)
        return max(0.0, wait_time)

def test_rate_limiter():
    limiter = SlidingWindowRateLimiter(window_size=10, max_requests=1)

    print("\n=== Message Flow Simulation ===")
    for message_id in range(1, 11):
        user_id = message_id % 5 + 1
        result = limiter.record_message(str(user_id))
        wait_time = limiter.time_until_next_allowed(str(user_id))

        print(f"Message {message_id:2d} | User {user_id} | "
              f"{'✓' if result else f'× (wait {wait_time:.1f}s)'}")

        time.sleep(random.uniform(0.1, 1.0))

    print("\nWaiting 4 seconds...")
    time.sleep(4)

    print("\n=== New Message Series After Waiting ===")
    for message_id in range(11, 21):
        user_id = message_id % 5 + 1
        result = limiter.record_message(str(user_id))
        wait_time = limiter.time_until_next_allowed(str(user_id))

        print(f"Message {message_id:2d} | User {user_id} | "
              f"{'✓' if result else f'× (wait {wait_time:.1f}s)'}")

        time.sleep(random.uniform(0.1, 1.0))

if __name__ == "__main__":
    test_rate_limiter()
