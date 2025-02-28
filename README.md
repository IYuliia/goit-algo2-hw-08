### Task 1: Implementing a Rate Limiter Using the Sliding Window Algorithm to Restrict Message Frequency in a Chat  

A chat system requires a mechanism to limit the frequency of messages sent by users to prevent spam. The implementation should use the **Sliding Window** algorithm for precise time interval control. This algorithm will track the number of messages within a given time window and restrict users from sending messages if the limit is exceeded.  

---

### **Technical Requirements**  

1. The implementation must use the **Sliding Window** algorithm for accurate time interval control.  
2. **System parameters**:  
   - **Window size (`window_size`)**: 10 seconds  
   - **Maximum messages allowed (`max_requests`)**: 1 per window  
3. Implement a class **`SlidingWindowRateLimiter`**.  
4. Implement the following class methods:  

   - **`_cleanup_window`** – Removes outdated requests from the window and updates the active time window.  
   - **`can_send_message`** – Checks if a message can be sent within the current time window.  
   - **`record_message`** – Records a new message and updates the user’s message history.  
   - **`time_until_next_allowed`** – Calculates the wait time before the user can send the next message.  

5. The **data structure** used for storing message history should be **`collections.deque`**.


### **Task 2: Implementing a Rate Limiter Using the Throttling Algorithm to Restrict Message Frequency in a Chat**  

A chat system requires a mechanism to limit the frequency of messages sent by users to prevent spam. The implementation should use the **Throttling** algorithm to control time intervals between messages. This ensures a **fixed waiting time** between consecutive messages, restricting message frequency if the interval is not respected.  

---

### **Technical Requirements**  

1. The implementation must use the **Throttling** algorithm to enforce time interval control.  
2. **System parameter**:  
   - **Minimum interval between messages (`min_interval`)**: 10 seconds  
3. Implement a class **`ThrottlingRateLimiter`**.  
4. Implement the following class methods:  

   - **`can_send_message`** – Checks if a message can be sent based on the timestamp of the last message.  
   - **`record_message`** – Records a new message and updates the timestamp of the last message.  
   - **`time_until_next_allowed`** – Calculates the remaining wait time before the next message can be sent.  

5. The **data structure** for storing the last message timestamp should be **`Dict[str, float]`**.