# Sheffield RSE talk for UoS Physics seminar series

Phil Tooley and Will Furnass

Research Software Engineering team, University of Sheffield

2019-01-24

---
## Outline

1. Introducing RSE@Sheffield
2. Writing performant code
    * Gauging Performance
    * Parallelising code
    * Other acceleration techniques
3. Creating sustainable software
    * Version control
    * Testing
    * Documentation
    * Packaging and dissemination
4. Further Resources

---
## RSE@Sheffield

* What RSE team is/does
  * Variety of projects and skills
  * UK RSE
  * EPSRC Fellowships

---
## Writing Performant Code

* "Premature optimisation is the root of all evil." -- Donald Knuth
* Ignore performance until your code works
* Once it works, look for "hot spots"
* Parts of the code that:
    * Take a long time to execute
    * Are executed many times

???

Write correct code then make it fast, pass on wisom from MathWorks

## Profiling Code

* *Is* my code genuinely slow?
* *Where* is my code slow?
* *Why* is my code slow?
*
* Lots of tools to help with this...

???

Sometimes code is as fast as it can really be, in that case look for other approaches like
parallelism

---
## Profiling Tools

* Various types of profiling tool:
  * Line profilers - time taken to run each line
  * Function profilers - time spent in different functions
  * Memory profilers - look at memory use of the program
  * Instrumentation - add code to the program to output extra information

* Use results to guide where time is spent on improving code

???

---

* Flamegraph example figure??

---
## Parallelising Code

* Traditionally HPC has used data parallelism
* All processes in the application perform same tasks on different sections of problem
* Data parallelism can be achieved by:
  * Shared memory (SHM) - all processes can access same memory space
  * Message passing (MP) - processes must explictly communicate all shared data
  * Parallel accelerators - GPUs and intel MIC
* Common low level libs
  * OpenMP - SHM primitives for C/C++/Fortran
  * MPI - MPI standard implemented by many vendors, for many languages
  * CUDA - Run many parallel threads on Nvidia GPUs
  * OpenACC - OpenMP-like primitives for GPU/Intel MIC offload
  * Intel TBB - threading building blocks for parallel applications

---
## But don't reinvent the wheel...

* Lots of high level libraries already available, e.g:
  * General high performance math - GSL, MKL, FFTW
  * Linear Algebra - LaPACK, BLAS, Intel MKL, PETSc, SLEPc
  * ODE/PDE solvers - PETSc, PVODE, FEniCS
  * Domain specific frameworks - OpenFOAM, Code_Saturne, CP2K
  * General purpose parallel frameworks - PETSc, Trilinos, Dask

* Use appropriate frameworks to develop faster, more reliable code

---
 Conclusions
