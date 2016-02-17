
**Question 1. What are three objectives of an OS design?**

The three main objectives of an OS design are as follows:

1.Convenience: The main purpose of an operating system is to provide a convenient interface for users of a computer.

2.Efficiency: An operating system allows the computer system resources to be used in an efficient manner. 

3.Ability to evolve: An operating system should be constructed in such a way as to permit the effective 
development, testing, and introduction of new system functions without interfering with service

**Question 2. What is a kernel?**

The lowest level of any operating system is its kernel. It is the central module of the operating system and the first layer of software loaded into memory when a system boots or starts up.

The kernel provides access to various common core services to all other system and application programs with the help of system calls. 

The services provided by kernel includes disk access, memory management, task scheduling, and access to other hardware devices. 

**Question 3. What is multiprogramming?**

Multiprogramming is a mode of operation that provides for the interleaved execution of two or more computer programs by a single processor.  Since there is only one processor there can be no true simultaneous execution of different programs. Instead, the operating system executes part of one program, then part of another, and so on. To the user it appears that all programs are executing at the same time.

**Question 4. What is a process?**

A process is a program in execution or it is an instance of program that is being executed at an instant of time.

A process consists of 

-An executable program

-Associated data needed by the program

-Execution context of the program (Program State).


**Question 5. How is the execution context of a process used by the OS?**

-The execution context, or process state, is the internal data by which the operating system is able to supervise and control the process. 

-This internal information is separated from the process, because the operating system has information not permitted to the process. 

-The context includes all of the information that the operating system needs to manage the process and that the processor needs to execute the process properly. 

-The context includes the contents of the various processor registers, such as the program counter and data registers. It also includes information of use to the operating system, such as the priority of the process and whether the process is waiting for the completion of a particular I/O event.

**Question 6. List and briefly explain five storage management responsibilities of a typical OS.**

Storage management responsibility of a typical OS

1.Process isolation

This is the prevention of data and instruction from interfering with each other process isolation helps this happen.

2.Automatic allocation and management

This is the process whereby allocation should be transported to the programmer.

3.Support of modular programming

Supports the program to be able to define programs modules and to create, destroy and alter the size of modules dynamically.

4.Protection and access control

This is the process of sharing memory this is desirable when sharing is needed by a particular application it also threatens the integrity of programs.

5.Long term storage

Is a process whereby memory is stored for a long period of time even when the computer is switch off it is stored in the RAM.

**Question 7. Explain the distinction between a real address and a virtual address.**

Physical addresses refer to hardware addresses of physical memory whereas Virtual addresses refer to the virtual store viewed by the process.

Differences are as follows:
| Physical address | Virtual address |
|:--------------:|:-------------:|
|one physical address space per machine|one virtual address space per process|
|valid addresses are usually between 0 and some machine specific maximum|addresses may start at zero, but not necessarily|
|not all addresses have to belong to the machine's main memory; other hardware devices can be mapped into the address space|Space may consist of several segments (i.e., have gaps)|

**Question 8. Describe the round-robin scheduling technique.**

Round Robin is the scheduling algorithm used by the CPU during execution of the process.

Round robin is designed specifically for time sharing systems. It is similar to first come first serve scheduling algorithm
but the preemption is the added functionality to switch between the processes.

In the round robin scheduling, processes are dispatched in a FIFO manner but are given a limited amount of CPU time called a time-slice or a quantum.

If a process does not complete before its CPU-time expires, the CPU is preempted and given to the next process waiting in a queue. 
The preempted process is then placed at the back of the ready list.

Round Robin Scheduling is preemptive (at the end of time-slice) therefore it is effective in time-sharing environments in which the system needs
to guarantee reasonable response times for interactive users.

The efficiency of Round Robin mainly depends upon on the length of the quantum. Setting the quantum too short causes too many context switches 
and lower the CPU efficiency. On the other hand, setting the quantum too long may cause poor response time and approximates FCFS.

**Question 9. Explain the difference between a monolithic kernel and a microkernel.**

-A monolithic kernel is a large kernel containing virtually the complete operating
system, including scheduling, file system, device drivers, and memory
management. All the functional components of the kernel have access to all of its
internal data structures and routines. Typically, a monolithic kernel is implemented
as a single process, with all elements sharing the same address space. 

-A microkernel is a small privileged operating system core that provides process
scheduling, memory management, and communication services and relies on other
processes to perform some of the functions traditionally associated with the
operating system kernel.

**Question 10. What is multithreading?**

Multithreading is defined as the ability of a central processing unit or a single core in a multi-core processor to execute multiple processes or threads concurrently, appropriately supported by the operating system.

**Question 11. List the key design issues for an SMP operating system.**

The key design issues for an SMP operating system are:

1. Simultaneous concurrent processes or threads

2. Scheduling

3. Synchronization

4. Memory Management

5. Reliability and Fault Tolerance
