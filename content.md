# Make it right, then make it go fast enough

<div class="right">
    <img src="images/rse-logoonly-stroke.png" width="50%" style="padding: 0 15px; float: right;"/>
</div>

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

<div class="middle">
<div class="center">
<img src="images/knuth-evil.png" width="100%">
</div>
</div>

---
## Writing Performant Code
* Ignore code performance until it works
* Once it works, look for "hot spots" that:
    * Take a long time to execute
    * Are executed many times

???

Write correct code then make it fast, pass on wisom from MathWorks

---
## Profiling Code

* *Is* my code genuinely slow?
  * Consider time cost to improve code
  * Performance of similar codes?
<p style="margin-bottom:10px"><p/>
* *Where* is my code slow?
* *Why* is my code slow?
<p style="margin-bottom:10px"><p/>  
* Lots of tools to help with this...

???

Sometimes code is as fast as it can really be, in that case look for other approaches like
parallelism

---
## Profiling Tools

* Various types of profiling tool:
  * Line profilers
  * Function profilers
  * Memory profilers
  * Instrumentation - add code to the program to output extra information

* Use results to guide where time is spent on improving code

???

---
## Example: Flame graph

<img class="center" src="profile.svg" width="100%"/>

---
## Parallelising Code

* Traditional HPC codes are data parallel
* All processes perform same tasks on different sections of problem
* Data parallelism can be achieved by:
  * Shared memory (SHM) - all processes can access same memory space
  * Message passing (MP) - processes must explictly communicate all shared data
  * Parallel accelerators - GPUs and intel MIC

* Choose platform suited to problem problem

---
## Parallelising Code

* Less "traditional" approaches:
  * Cluster computing frameworks
  * Heterogeneous programs
  * Streaming computation
  * Directed acyclic graphs

* All approaches have their place
* Consider program structure to find a good fit


---
## Parallelising Code

* Low level parallel libraries:
  * OpenMP - SHM primitives for C/C++/Fortran
  * MPI - MPI standard implemented by many vendors, for many languages
  * CUDA - Run many parallel threads on Nvidia GPUs
  * OpenACC - OpenMP-like primitives for GPU/Intel MIC offload
  * Intel TBB - threading building blocks for parallel applications

* No maths here, just communication

---
## But don't reinvent the wheel

* Higher level maths libraries available, e.g:
  * General high performance math - GSL, MKL
  * Linear Algebra - LaPACK, BLAS, Intel MKL
  * ODE/PDE solvers - PETSc, PVODE, FEniCS
  * Scientific frameworks - PETSc, Trilinos
  * Cluster computing - Dask, Hadoop, Spark 
  * Domain specific frameworks

* Use appropriate frameworks to develop more reliable code

---
## Other acceleration methods

* Language choices:
  * Python/MATLAB are very common in science
  * C/C++/Fortran used for larger codes
  * Some Mathmatica/IDL/R also

* Typically we consider C/C++/FORTRAN as "fast" while interpreted languages like python are "slow"

---
## Accelerating Python

* Use Numpy/Scipy for numerical work
  * Numpy arrays are speed competitive with C but easier to write and debug

* Use Numba to compile Python code 
  * Speed of C using pure python syntax
  * Numba even works on GPUs!

* Explicitly write numerical code in C/C++

---
## Conclusions
