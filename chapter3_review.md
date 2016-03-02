# Chapter 3 Review Questions

Name: _Muni Bhupathi Reddy Dandu_

Course: _5143 Operating Systems_

Date: _02 March 2016_

#### Question 1. What does it mean to preempt a process?

Process preemption is defined as the interruption of the executing process by the operating system so that another process can be executed.


#### Question 2. What is swapping and what is its purpose?

Swapping is defined as the moving a part or all of a process from main memory to disk.

When none of the processes in main memory is in the Ready state, the operating system swaps one of the blocked processes out into disk into a suspend queue, so that another process may be brought into main memory to execute.

#### Question 3. List three general categories of information in a process control block.

The three general categories of information in a process control block are as follows:-

Process identification: It includes the id of the process, id of the parent process and the user id.

Processor state information: It includes the program counter, status registers, and general-purpose registers.

Process control information: This includes

>i.Scheduling & state information

>ii.Data structuring

>iii.Memory management

>iv.Resource ownership and utilization

>v.Process privileges

>vi.Interprocess communication

#### Question 4. Why are two modes (user and kernel) needed?

The user mode has restrictions on the instructions that can be executed and the memory areas that can be accessed. This is to protect the operating system from  damage or alteration.

In kernel mode, the operating system does not have these restrictions, so that it can perform its tasks.

#### Question 5. What is the difference between an interrupt and a trap?

An interrupt is due to some sort of event that is external to and independent of the currently running process, such as the completion of an I/O operation. 

A trap relates to an error or exception condition generated within the currently running process, such as an illegal file access attempt.

#### Question 6. Give three examples of an interrupt.

Three examples of an interrupt are:

>-Clock interrupt

>-I/O interrupt

>-Memory fault

#### Question 7. What is the difference between a mode switch and a process switch?

A mode switch may occur without changing the state of the process that is currently in the Running state.

A process switch involves taking the currently executing process out of the Running state in favor of another process and also involves saving more state information.
