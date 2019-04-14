## COMP 228 - System Hardware

### Overview
#### Why study computer organization and architecture? 
- Design better programs, including system software such as compilers, operating systems and device drivers. 
- Optimize program behaviour
- Evaluate (benchmark) computer system performance.
- Understand time, space, and price tradeoffs. 
#### Computer Organization
- Encompasses all physical aspects of computer systems. 
- eg. circuit design, control signals, memory types
- *How does a computer work?*
#### Computer Architecture 
- Logical aspects of system implementation as seen by the programmer
- Eg. Instruction sets, instruction formats, data types, addressing modes
- How do I design a computer? 

### Computer Components 
#### At the most basic level, a computer is a device consisting of 3 pieces
- A processor to interpret and execute programs 
- A memory to store both data and programs 
- A mechanism for transferring data to and from the outside world

**Example:**
<img src="https://cdn.discordapp.com/attachments/517047603867811899/534088969009364992/unknown.png">
What does all of this mean?

#### Measures of capacity and speed:
|  Prefix   |    Written    |  Base 10  |  Base 2  |
| :-------: | :-----------: | :-------: | :------: |
| Kilo (K)  |  1 thousand   |  $10^3$   | $2^{10}$ |
| Mega (M)  |   1 million   |  $10^6$   | $2^{20}$ |
| Giga (G)  |   1 billion   |  $10^9$   | $2^{30}$ |
| Tera (T)  |  1 trillion   | $10^{12}$ | $2^{40}$ |
| Peta (P)  | 1 quadrillion | $10^{15}$ | $2^{50}$ |
|  Exa (E)  | 1 quintillion | $10^{18}$ | $2^{60}$ |
| Zetta (Z) | 1 sextillion  | $10^{21}$ | $2^{70}$ |
| Yotta (Y) | 1 septillion  | $10^{24}$ | $2^{80}$ |
**\*** Whether a metric refers to a power of ten or a power of two typically depends upon what's being measured. 

#### Hertz = clock cycles per second (frequency)
- 1MHz = 1,000,000Hz
- Processor speeds are measured in MHz or GHz

#### Byte = a unit of storage
- 1KB = $2^{10}$ = 1024 bytes
- 1MB = $2^{20}$ = 1,048,576 bytes
- 1GB = $2^{30}$ = 1,099,511,627,776 bytes
- Main memory (RAM) is measured in GB
- Disk storage is measured in GB for small systems, TB ($2^{40}$) for large systems. 

#### Measures of time and space
|  Prefix   |     Written     |  Base 10   |
| :-------: | :-------------: | :--------: |
| Milli (m) |  1 thousandth   | $10^{-3}$  |
| Micro (µ) |   1 millionth   | $10^{-6}$  |
| Nano (n)  |   1 billionth   | $10^{-9}$  |
| Pico (p)  |  1 trillionth   | $10^{-12}$ |
| Femto (f) | 1 quadrillionth | $10^{-15}$ |
| Atto (a)  | 1 quintillionth | $10^{-18}$ |
| Zepto (z) | 1 sextillionth  | $10^{-21}$ |
| Tocto (y) | 1 septillionth  | $10^{-24}$ |

- Millisecond = 1 thousandth of a second
  - Hard disk drive access times are often 10 to 20 milliseconds 
  - The end to end video conference is around 150 milliseconds 
- Nanosecond = 1 billionth of a second
  - Main memory access times are often 50 to 70 nanoseconds 
- Micron (micrometer) = 1 millionth of a meter
  - Circuits on computer chips are measured in microns 

- We note that cycle time is the reciprocal of clock frequency
- A bus operating at 133MHz has a cycle time of 7.52 nanoseconds.

#### Back to the example...
- The microprocessor is the "brain" of the system. It executes program instructions. The one here is an Intel i7 running at 3.9GHz.
  
- This system has 32GB of (fast) synchronous dynamic RAM and two levels of cache memory; the level 1 (L1) cache is smaller and (probably) faster than the L2 cache. Note that these cache sizes are measured in KB and MB. 
  - Computers with large main memory capacity can run larger programs with greater speed than computers having small memories. 
  - RAM is an acronym for Random Access Memory. Random access means that memoty contents can be accessed directly if you know it's location.
  - Cache is a type of temporary memory that can be accessed faster than RAM. 

- Hard disk capacity determines the amount of data and size of the programs you can store. This one can store 1TB. 7200 RPM is the rotational speed of the disk. Generally, the faster a disk rotates, the faster it can deliver data to RAM. (There are many ofther factors involved)

- ATA stands for *advanced technology attachment*, which describes how the hard disk interfaces with (or connects to) other system components. 

- A DVD can store about 4.7GB of data. This drive supports rewritable DVDs, +/-RW, the can be written to many times.. 16x describes the speed. 

- Ports allow movement of data between a system and its external devices. This system has 10 ports. 
  - Serial ports send data as a series of pulses along one or two data lines. 
  - Parallel ports send data as a single pulse along at least eight data lines. 
  - USB - Universal Serial Bus, is an intelligent serial interface that is self-configruing (It supports "plug and play")
- System buses can be augmented by dedicated I/O buses. PCI, *peripheral component interface*, is one such bus. This system has two PCIe (PCI express) devices: a video card and a sound card. 
- Active matrix technology uses one transistor per picture element (pixel). The *resolution* of a monitor determines the amount of text and graphics that the monitor can display. 
  - Super VGA (SVGA) tells us this monitor has a resulution of 1280x1024 pixels. 
  - The video card contains memory and programs that support the monitor. 

When you bought a computer:
1. What assurance do we have the computer components will operate as we expect? 
2. And what assurance do we have that computer components will operate together? 

### Standards Organizations
- There are many organizations that set computer hardware standards -- to include the interoperability of computer components.
- Some of the most important standard-setting groups are:
  - The Institute of Electrical and Electronic Engineers (**IEEE**)
    - Promotes the interests of the worldwide electrical engineering community.
    - Establishes standards for computer components, data representation, and signaling protocols, among many other things. 
  - The International Telecommunications Union (**ITU**)
    - Concerns itself with the interoperability of telecommunications systems, including data communications and telephony.
  - National groups establish standards withing their respective countries:
    - The American Nation Standards Institute (**ANSI**)
    - The British Standards Institution (**BSI**)
  - The International Organization for Standardization (**ISO**)
    - Establishes worldwide standards for everything from screw threads to photographic film.
    - Is influential in formulating standards for computer hardware and software, including their methods or manufacture. 

#### Historical Development
- To full appreciate the computers of today, it is helpful to understand how things got the way they are. 
- The evolution of computing machinery has taken place over several centuries. 
- In modern times computer evolution is usually classified into four generations according to the salient technology of the era.

- Generation Zero: Mechanical Calculating Machines (1642 - 1945)
  - Calculating clock - Wilhelm Schickard (1592-1653)
  - Pascaline - Blaise Pascal (1623-1662)
  - Difference Machine - Charles Babbage (1791-1871) 
  - Punched card tabulating machines - Herman Hollerith (1860-1929)
- First Generation: Vacuum tube computers (1945-1953)
  - Atanasoff Berry Computer (1937-1938) solved systems of linear equations 
  - John Atanasoff and Clifford Berry of Iowa State University 
  - Electronic Numerical Integrator and Computer (ENIAC)
    - John Mauchly and J. Presper Eckert, University of Pennsylvania, 1946
    - The ENIAC was the first general-purpose computer 
  - The IBM 650 first mass-produced computer (1955)
    - Phased out in 1969
  - Other major computer manufacturers of this period included UNIVAC, Engineering Research Associates (ERA), and Computer Research Corporation (CRC)
    - UNIVAC and ERA were bought by Remington Rand, the ancestor of the Unisys Corporation.
    - CRC was bought by the Underwood (typewriter) Corporation, which left the computer business. 
- Second Generation: Transistorized Computers (1954-1965)
  - IBM 7094 (scientific) and 1401 (business)
  - Digital Equipment Corporation (DEC) PDP-1
  - UNIVAC 1100
  - Control Data Corporation 1604
  - ...and many more
- Third Generation: Integrated Circuit Computers (1965-1980)
  - IBM 360
  - DEC PDP-8 and PDP-11
  - Cray-1 supercomputer
  - ... and many more
  - By this time, IBM had gained overwhelming dominance in the industry
    - Computer manufacturers of this era were characterized as IBM and the BUNCH (Burroughs, Unisys, NRC, Control Data, and Honeywell)
- Fourth Generation: VLSI Computers (1980-???)
  - Very large scale integrated circuits (VLSI) have more than 10,000 components per chip.
  - Enabled the creation of microprocessors 
  - The first was the 4-bit Intel 4004
  - Later versions such as the 8080, 8086, and 8088 spawned the idea of "personal computing"
- Moore's Law (1965)
  - Gordon Moore, Intel founder
  - "The density of transistors in an integrated circuit will double every year"
  - Contemporary version:
    - "The density of silicon chips doubles every 18 months"
  - But this law cannot hold forever...
- Rock's Law
  - Arthur Rock, Intel financer
  - "The cost of capital equipment to build semiconductors will double every four years
  - In 1968, a new chip plant cost about $12,000.
  - At the time, $12,000 would buy a nice home in the suburbs. An executive earning $12,000 per year was "making a very comfortable living" 
  - In 2012, a chip plants under construction cost well over $5 billion.
    - $5 billion is more than the gross domestic product (GDP) of some small countries including Barbadoz, Mauritania, and Rwanda. 
  - For Moore's Law to hold, Rock's Law must fall or vice versa. But no one can say which will give out first.

### The Computer Level Hierarchy 
- Computer consist of many things besides chips
- Before a computer can do anything worthwhile, it must also use software. 
- Writing complex programs require a "divide and conquer" approach, where each program module solves a smaller problem
- Complex computer systems empliy a similar technique through a series of virtual layers. 
- Each virtual layer is an abtraction of the level below it. 
- The machines at each level execute their own particular instructions, calling upon machines at lower levels to perform tasks as required. 
- Computer circuits ultimately carry out the work. 

- Level 6: The user level
  - Program execution and user interface level
  - The level with which we are most familiar 
- Level 5: High-level language level
  - The level with which we interact when we write programs in languages such as C, Pascal, Lisp and Java
- Level 4: Assembly language level
  - Acts upon assembly language produced from level 5, as well as instructions programmed directly at this level. 
- Level 3: System software level
  - Controls executing processes on the system
  - Protects system resources
  - Assembly language instructions often pass through level 3 without modification
- Level 2: Machine level
  - Also known as the instruction set architecture (ISA) level
  - Consists of instructions that are particular to the architecture of the machine
  - Programs written in machine language need no compilers, interpreters or assemblers. 
- Level 1: Control level
  - A *control unit* decodes and executes instructions and moves data through the system. 
  - Control units can be *microprogrammed* or *hardwired*
  - A microprogram is a program written in a low-level language that is implemented by the hardware 
  - Hardwired control units consist of hardware that directly executes machine instructions
- Level 0: Digital logic level
  - This level is where we find digital circuits (the chips)
  - Digital circuits consist of gates and wires. 
  - These components implement the mathematical logic of all other levels. 

### Computing as a Service: Cloud Computing
- The ultimate aim of every computer system is to deliver functionality to it's users. 
- Computer users typically do not care about terabytes of storage and gigahertz of processor speed. 
- Many companies outsource their data centers to third-party specialists, who agree to provide computing services for a fee. 
- These arrangements are managed through *service-level agreements* (SLAs)
- Rather than pay a 3rd party to run a company-owned data center, another company is to buy computing services from someone else's data center and connect to it via the internet. 
- This is the idea behind a collection of service models known as cloud computing. 
  - The "cloud" is a visual metaphore traditionally used for the internet. It is even more apt for service-defined computing. 

### The Von Neumann Model
- On the ENIAC, all programming was done at the digital logic level
- Programming the computer involved moving plugs and wires 
- A different hardware configuration was needed to solve every unique problem type. 
- Configuring the ENIAC to solve a "simple" problem required many days labour by skilled technicians. 
- Inventors of the ENIAC, John Mauchley and J. Presper Eckert, conceived a computer that could store instructions in memory. 
- The invention of this idea has since been ascribed to a mathematician, John Von Neumann, who was a contemporary of Mauchley and Eckert. 
- Store-program computers have become known as Von Neumann Architecture systems.
- Today's stored-program computers have the following characteristics:
  - Three hardware systems:
    - A central processing unit (CPU)
    - A main memory system
    - An I/O system
  - The capacity to carry out sequential instruction processing 
  - A single data path between the CPU and main memory
    - This single path is known as the Von Neumann Bottleneck. 
- This is a general depiction of a von Neumann system:
    <img src="https://cdn.discordapp.com/attachments/517047603867811899/534146970214727685/unknown.png">
- These computers deploy a **fetch-decode-execute** cycle ro run programs as follows...
- The control unit fetches the next instruction from memory using the program counter to determine where the instruction is located. 
  <img src="https://cdn.discordapp.com/attachments/517047603867811899/534147388080652298/unknown.png">
- The instruction is decoded into a language that the ALU can understand. 
  <img src="https://cdn.discordapp.com/attachments/517047603867811899/534149951848972309/unknown.png">
- Any data operands required to execute the instruction are fetched from memory and placed into registers within the CPU
  <img src="https://cdn.discordapp.com/attachments/517047603867811899/534150414564589568/unknown.png">
- The ALU executes the instructions and places results in registers or memory.
  <img src="https://cdn.discordapp.com/attachments/517047603867811899/534150673223122954/unknown.png">

### Non-Von Neumannn Models
- Conventional stored-program computers have undergone many incremental improvements over the years. 
- These improvements include adding specialized buses, floating point units, and cache memories, to name only a few. 
- But enormous improvements in computational power require departure from the classic Von Neumann architecture. 
- Adding processors is one approach
- Some of today's systems have separate buses for data and instructions. 
  - Called a Harvard architecture 
- Other non-Von Neumann systems provide special-purpose processors to offload work from the main CPU.
- More radical departures include dataflow computing, quantum computing, cellular automata, and parallel computing. 