#Heap/P-queue 
- Stop the tasks in a max heap according to remaining. This is because we want to reduce the waiting time by completing the biggest set of tasks
- When taken from a max heap if there are still some sub-tasks for that tasks, store in the queue
- Stop timelapse and use the timelapse to get back the tasks that can we scheduled again from the queue
- The time complexity is O(n logn) because 