# Threads_Review Questions

Name: _Muni Bhupathi Reddy Dandu_

Date: _08 Apr 2016_

ID:M20228454

#### Question 1. Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation.
Difference between thread1 and thread2

    def run(self):
        for k in xrange(10000000):
            if k % 100000 == 0:
                print 'A:', k

    def run(self):
        global sharedCounter
        for k in xrange(10000000):
            if k % 100000 == 0:
                print 'A:', k, sharedCounter
            sharedCounter += 1


In the first program thread1.py, the run method in both the classes A and B just prints the k values which are independent of both the threads.

Where as in the second example, as the sharedCounter is the global variable which is shared by both the Threadclasses A and B,
i.e., when Threadclass A is implementing the run method, Threadclass B is parallely implementing the run method,which modifies the shared global variable.

This results in the rendundancy(printing the same shared counter value twice).

#### Question 2. After running Thread3.py does it fix the problems that occured in Threads2.py? What's the down-side?
Yes, after running the thread3.py program, the redundancy problem(printing same shared counter value twice in thread1.py is solved with the help of lock()

In thready2.py, while one class is executing run method i.e., when it is about to print the global shared value, the other class is also printing it at the same time, which results in the printing of the same data.

In thread3.py, the lock() function blocks the modification of the shared global variable among the classes. So, here the redundancy problem is solved. Hence the modification takes place only after the release of the resources.


#### Question 3. Comment out the join statements at the bottom of the program and describe what happens.
The main function of the join() method in threading is to block the calling thread until the thread whose join() method is called is terminated.

So, if the join statements are used, the main program will wait for the execution of all threads.

And if the join statements are not used, the main program will complete the execution while the threads are computing their exection. And the threads will print the output after the main is executed.

#### Question 4. What happens if you try to Ctrl-C out of the program before it terminates?
If Ctrl-C is tried out of the program before it terminates, the program simply continue running and prints the keyboard interrupt at the thread.join function, which shows that the join function waited for that particular thread to return. But due to keyboardInterrupt it fails to acquire the output from that particular thread.

#### Question 5. Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.
In the program Threads4.py, a lock has been called on the shared resources and the other threads are not using acquire method for accessing the resources. So, this makes the resources available to all the threads.

#### Question 6.Does uncommenting the lock operations clear up the problem in question 5?
Yes, uncommenting the lock operations clear up the problem in question 5. As the lock prevent shared memory from modifying by the other thread, which assigns the shared memory value evrytime the loop rotates. Hence the error message is not displayed and the problem is solved.
