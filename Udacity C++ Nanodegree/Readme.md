# Artical about linux composition for system monitor project

--- 

## System Data
```
Linux stores a lot of system data in files within the (/proc) directory. Most of the data that this project 
requires exists in those files.
```
## Operating System

```
information about the operating system exists outside of the (/proc) directory, in the (/etc/os-release) file.
```
## Kernel

```
Information about the kernel exists (/proc/version) file.
```
  
## Memory Utilization
```
Information about memory utilization exists in the (/proc/meminfo) file.
```
## Total Processes
```
Information about the total number of processes on the system exists in the (/proc/meminfo) file.

```
## Running Processes
``` 
Information about the number of processes on the system that are currently running exists in the (/proc/meminfo) file.
```
## Up Time
```
Information about system up time exists in the (/proc/uptime) file.
```
> This file contains two numbers (values in seconds): the uptime of the system (including time spent in suspend) and the amount of time spent in the idle process.








