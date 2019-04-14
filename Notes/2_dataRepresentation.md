#### Objectives
- Understand the fundamentals of numerical data representation and manipulation in digital computers
- Master the skill of converting between various radix systems. 
- Understand how errors can occur in computations because of overflow and truncation
- Understand the fundamental concepts of floating-point representation
- Gain familiarity with the most popular character codes 
- Understand the concepts of error detecting and correcting codes

---

### Introduction
- A **bit** is the most basic unit of information in a computer
- A **byte** is a group of **eight** bits. 
- A **Word**:
  - **16, 32, or 64** bits are most common
  - In a word-addressable system, a word is the smallest addressable unit of storage
- A **nibble**
  - Bytes,
    - **high-order nibble**
    - **low-order nibble**
  
    | 7 | 6 | 5 | 4 |   | 3 | 2 | 1 | 0 |
    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
    |H.O|H.O|H.O|H.O|   |L.O|L.O|L.O|L.O|

### Positional numbering systems

| $10^2$ | $10^1$ | $10^0$ |  | $10^{-1}$ | $10^{-2}$ |
| :----: | :----: | :----: |:-:|:---------:|:---------:|
| 1      | 2      | 3      | . | 4         | 5         |
`<----------------------------------------->`
- The binary system (base-2 system)
- The decimal system (base-10 system)
- Any integer quantity can be represented exactly using any base (or *radix*)
- The decimal number 947 in powers of 10 is:
  > $(9 * 10^2) + (4 * 10^1) + (7 * 10^0)$
- The decimal number 5836.47 in powers of 10 is:
  > $(5*10^3) + (8*10^2) + (3*10^1) + (6*10^0) + (4*10^{-1}) + (7*10^{-2})$
- The binary number 11001 in powers of 2 is:
  > $(1*2^4) + (1*2^3) + (0*2^2) + (0*2^1) + (1*2^0)$
    $= 16 + 8 + 0 + 0 + 1$
    $= 25$
- When the radix of a number is something other than 10, the base is denoted by a subscript. 
  - Sometimes, the subscript 10 is added for emphasis:
    $11001_2 = 25_{10}$

---

**Exercise:**
Suppose that you are an employee of some bank in Canada. The system you are using is not familiar with the current currency standards $(\$0.10, \$0.25, \$1, \$2, \$5, \$10, \$20, ...)$. Instead, it computer values using the decimal numbering system. **How would the system represent $823.28 CAD?**

$\$823.28 = (8*10^2) + (2*10^1) + (3*10^0) + (2*10^{-1}) + (8*10^{-2})$
- What if we wanted to the system be able to convert CAD to USD? 
  - The system will then need to be able to convert the currency

---

### Converting between bases
- Base conversion
- Subtraction 
- Division remainder
- Let's use the subtraction method to convert 190 in decimal to base 3. 
  - $3^5 = 243$
  - $3^4 = 81$
  - $81 * 2 = 162$
    - Write down the 2 and subtract 162 from 190. 
    - $190 - 162 = 28$
    - $3^4 *$ **2**
  - The next power of 3 is $3^3 = 27$
    - $28 - 27 = 1$
    - $3^3 *$ **1**
  - $3^2 = 9$
    - $3^2 *$ **0**
  - $3^1 = 3$
    - $3^1 *$ **0**
  - $3^0 = 1$
    - $1-1=0$
    - $3^0 *$ **1**
  - Our result, reading from top to bottom is:
    - $190_{10} = 21001_3$

---

- Now, let's use the **division remainder method** to convert 190 in decimal to base 3.
  - $190/3 = 63 \text{ remainder } 1$
  - $63/3 = 21 \text{ remainder } 0$
    - Continue this way until the quotient is 0...
  - $21/3 = 7 \text{ remainder } 0$
  - $7/3 = 2 \text{ remainder } 1$
  - $2/3 = 0 \text{ remainder } 2$
- In the final calculation we note that 3 divides 2 zero times with a remainder of 2.
- Our result, reading from bottom to top is:
  - $190_{10} = 21001_3$

---
- **Fractional** values can be approximated in all base systems
- Unlike integer values, fractions do no necessarily have exact representations under all radices. 
- The quantity $1\over2$ is exactly representable in binary and decimal systems, but not in the ternary (base 3) numbering system
- Fractional decimal values have nonzero digits to the right of the decimal point
- Fractional values of other radix systems have nonzero digits to the right of the *radix point* .
- Numerals to the right of a radix point represent negative powers of the radix:
  > $0.47_{10} = (4^10^{-1}) + (7*10^{-2})$
  $0.11_2 = (1*2^{-1}) + (1*2^{-2})$
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$= {1\over2} + {1\over4}$
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$= 0.5 + 0.25 = 0.75$
- As with the whole-number conversions, you can use either of the two methods: a **subtraction method** or an easy **multiplication method**.
  - The subtraction method for **fractions** is identical to the subtraction method for **whole numbers**.
  - Instead of subtraction positive powers of the target radix, we subtract negative powers of the radix. 
- We always start out with the largest value first, $n^{-1}$, where $n$ is our radix, and work our way along using larger negative exponents. 
- The calculation here is an example of using the subtraction method to convert the decimal $0.8125$ to binary.
  - $0.8125 - 0.5000 = 0.3125$
    - $2^{-1}*$ **1**
  - $0.3125 - 0.2500 = 0.0625$
    - $2^{-2}*$ **1**
  - $0.0625 - 0 = 0.0625$
    - $2^{-3}*$ **0**
  - $0.0625 - 0.0625 = 0$
    - $2^{-4}*$ **1**

- Our result, reading from top to bottom is: 
  - $0.8125 = 0.1101_2$
- Of course, this method works with any base, not just binary. 

---

- Using the **multiplication method** to convert the decimal $0.8125$ to binary, we multiply by the radix 2.
  - &nbsp;
    - $0.8125 * 2 = 1.6250$
    - $0.6250 * 2 = 1.2500$
    - $0.2500 * 2 = 0.5000$
    - $0.5000 * 2 = 1.0000$
  - The first product carries into the units place.
  - Ignoring the value in the units place at each step, continue multiplying each fractional part by the radix. 
  - you are finished when the product is zero, or until you have reached the desired number of decimal places.
  - Our result here, reading from top to bottom is:
    - $0.8125_{10} = 0.1101_2$
  - This method also works with any base. Just use the target radix as the multiplier. 
- The binary numbering system is the most important radix system for digital computers. 
- However, it is difficult to read long string of binary numbers.
  - For example: $11010100011011_2 = 13595_{10}$
- For compactness and ease of reading, binary values are usually expressed using **hexadecimal**, or **base-16** numbering system. 
&nbsp;
- The **hexadecimal numbering system** uses the numerals 0-9 and the letters A-F. 
- To convert from binary to hex, all we need to do is group the binary digits into groups of 4. 
  - Why? Because $16 = 2^4$
  > A group of four binary digits is called a hextet
- Using groups of hextets, the binary number $0011010100011011_2 (13595_{10})$ in hexadecimal is:
  ```r
  0011 0101 0001 1011
     3    5    1    B
  ```
  > If the number of bits is not a multiple of 4, pad on the left with zeros. 
- Similary, **Octal** (**base-8**) values are derived from binary using groups of three bits ($8=2^3$)
  ```r
  011 010 100 011 011
    3   2   4   3   3
  ```

---

### Binary addition
- Before we continue...
- In binary addition, only four rules apply:
  - $0+0=0$
  - $1+0=1$
  - $0+1=1$
  - $1+1=10$
- We will understand this better soon.

### Signed integer representation
- The conversions we have so far presented have involved only **unsigned values**
  - Numbers that can only be represented in the positive
- The represent **signed values**, computer systems can use three different methods:
  - **Signed Magnitude**
  - **One's Complement**
  - **Two's Complement**

**NOTE:** A system that uses signed magnitude to interpret a given binary message will not understand it in the same manner if it decides to use another method discussed above. We will see this in the next slides. 
- Signed magnitude allocated the leftmost bit, or the most significant bit, of a binary message as the sign bit. 
  - 0 = positive, 1 = negative
  - The remainder contain the absolute value of the number. 
- For example, in 8-bit signed magnitude representation:
  - +3 is: `0 0000011`
  - -3 is: `1 0000011`
- From the above example, can you identify a disadvantage of using signed magnitude? 

**Example:**
Using signed magnitude binary arithmetic, find the sum of 75 and 45. 
- First, convert them both to binary, and arrange as a sum, but separate the (positive) sign bits from the magnitude bits. 
  ```
  0  1001011
  0 +0101110
  ----------
           1
  ```
Just as in decimal arithmetic, we find the sum starting with the rightmost bit and working left. 
  ```
         1
  0  1001011
  0 +0101110
  ----------
          01
  ```
In the second bit, we have a carry, so we note is above the third bit.
  ```
       111
  0  1001011
  0 +0101110
  ----------
        1001
  ```
The third and fourth bits also give us carries
  ```
       111
  0  1001011
  0 +0101110
  ----------
     1111001
  ```
Once we have worked our way through all eight bits, we are done. 
> In this example, we were careful to pick two values whose sum would fit into seven bits. If that is not the case, we have a problem. 

**Example: **
Using signed magnitude binary arithmetic, find the sum of 107 and 46. 
We see that the carry from the seventh bit overflows and is discarded, giving us the erroneous result: 107+26=25
```
    1 111
0   1101011
0 + 0101110
------------------
0   0011001
```
The signs in signed magnitude representation work just like the signs in pencil and paper arithmetic. 
Ex. Using signed magnitude arithmetic, find the sum of -46 and -25.
```
     11
1   0101110
1 + 0011001
-----------
1   1000111
```
> Because the signs are the same, all we do is add the numbers and supply the negative sign when we are done. 

Mixed sign addition is done the same way...
**Example:**
Using signed magnitude binary arithmetic, find the sume of 46 and -25
```  
     12  02
0   0101110
1 + 0011001
-----------
0   0010101
```
> The sign of the result gets the sign of the number that is larger. Note the "borrows" from the second and sixth bits.

1. Signed magnitude representation is easy for people to understand, but it requires complicated computer hardware. 
2. Another disadvantage of signed magnitude is that it allows two different representations for zero: positive zero and negative zero. 
3. For these reasons (among others) **computer systems employ *complement* systems for numeric value representation.**

---
- The *diminished radix complement* - or **one's complement** in our context - of a non-zero number $N$ in base $r$ with $d$ digits is $(r^d-1)-N$
- It amounts to little more than flipping the bits of a binary number. 
- For example, using 8-bit one's complement representation:
  - +3 is: `00000011`
  - -3 is: `11111100`
- In one's complement representation, as with signed magnitude, negative values are indicated by a 1 in the high order bit. 
- Complement systems are useful because they eliminate the need for subtraction. The difference of two values is found by adding the minuend to the complement of the subtrahend. 
- With one's complement addition, the carry bit is "carried around" and added to the sum.
  - **Exmaple:** using one's complement binary arithmetic find the sum of 48 and -19. 
    ```
    00110000
    11101100
    --------
    00011100
          +1
    --------
    00011101
    ```
    > We note that 19 in binary is `00010011`, so -19 in one's complement is `11101100`.
- Although the "end carry around" adds some complexity, one's complement is actually simpler to implement than having signed magnitude. 
- But it still has the disadvantage of having two different representations for zero: positive 0 and negative 0.

---

- **Two's complement** solves this problem.
- Two's complement is the radix complement of the binary numbering system; the *radix complement* of a non-zero number $N$ in base $r$ digits is $r^d-N$.
  - This means taking one's complement of a binary sequence, and adding 1 after. 
- To express a value in two's complement representation:
  - If the number is positive, just convert it to binary and you're done. 
  - If the number is negative, find the one's complement of the number and then add 1. 
- **Exmaple:** 
  - In 8-bit binary, 3 is: `00000011`
  - -3 using one's complement representation is: `11111100`
  - Adding 1 gives us -3 in two's complement form: `11111101`
- With two's complement arithmetic, all we do is add our two binary numbers. Just discard any carries emitting from the high order bit. 
  - **Example:** Using two's complement binary arithmetic, find the sum of 48 and -19.
  ```
    1
    00110000
  + 11101101
  ----------
    00011101
  ```
  > We note that 19 in binary is `00010011`
  So -19 using one's complement is: `11101100`
  and -19 using two's complement is: `11101101`
- Wen we use any finite number of bits to represent a number, we always run the risk of the result of our calculations becoming too large or too small to be stored in the computer. 
- While we can't always prevent overflow, we can always ***detect*** overflow.
- In complement arithmetic, an overflow condition is easy to detect. 
- **Example:**
  - Using two's complement binary arithmetic, find the sum of 107 and 46. 
  ```
    11 111
    01101011
  + 00101110
  ----------
    10011001
  ```
  - We see that the nonzero carry from the seventh bit *overflows* into the sign bit, giving us the erroneous result: 107 + 46 = -103
    > But overflow into the sign bit does not always mean that we have an error. 
- **Example:**
  - Using two's complement binary arithmetic, find the sum of 23 and -9
  ```
  1<111 111
    00010111
  + 11110111
  ----------
    00001110
  ```
  - We see that there is carry into the sign bit and carry out. The final result is correct: 23 + (-9) = 14
  > Rule for detecting signed two's complement overflow: when the "carry in" and the "carry out" of the sign bit differ, overflow has occured. If the carry into the sign bit equals the carry out of the sign bit, no overflow has occured. 
- Signed and unsigned numbers are both useful. 
  - For example, memory addresses are always unsigned. 
- Using the same number of bits, unsigned integers can express twice as many "positive" values as signed numbers.
- Trouble arises if an unsigned number "wraps around"
  - In four bits: $1111+1=0000$
- Overflow and carry are tricky ideas
- Signed number overflow means nothing in the context of unsigned numbers, which set a carry flag instead of an overflow tag.
- If a "carry out" of the leftmost bit occurs with an unsigned number, overflow has occured. 
- Carry and overflow occur independently of each other. 
  > the following table summarizes these ideas
- With signed numbers, overflow (two positives produce a negative or two negatives produce a positive) is a problem but carry out does not prove anything by itself. 
- With unsigned number, carry out is always a problem
  | Expression  | Result | Carry? | Overflow? | Correct result? |
  |:------------|:-------|:-------|:----------|:----------------|
  | 0100 + 0010 | 0110   | No     | No        | Yes             |
  | 0100 + 0110 | 1010   | No     | Yes       | No              |
  | 1100 + 1110 | 1010   | Yes    | No        | Yes             |
  | 1100 + 1010 | 0110   | Yes    | Yes       | No              |
- We can do binary multiplication and division by 2 very easily using an ***arithmetic shift* operation**
- A **left arithmetic shift** inserts a 0 in for the rightmost bit and shifts everything else to the left one bit; in effect, it multiplies by two. 
- A **right arithmetic shift** shifts everything one bit to the right, but copies the sign bit; it divides by two. 
- **Example:**
  - Multiply the value 11 (expressed using 8-bit signed two's complement representation) by 2. 
  - We start with the binary value for 11:
    - `00001011 (+11)`
  - We shift one place left, resulting in:
    - `00010110 (+22)`
  - The sign bit has not changed, so the value is valid.
  > To multiply 11 by 4, we simply perform a left shift twice.
- **Example:**
- Divide the value 12 (expressed using 8-bit signed two's complement representation) by 2. 
- We start with the binary value for 12:
  - `00001100 (+12)`
- We shift right one place, resulting in:
  - `00000110 (+6)`
- (Remember, we carry the sign bit to the left as we shift)
  > To divide 12 by 4, we right shift twice. 

---

### Floating-Point Representations
- The signed magnitude, one's complement, and two's complement representation that we have just presented deal with signed integer values only.
- Without modification, these formats are not useful in scientific or business applications that deal with real number values. 
- Floating-point representation solves this problem. 
  - It partitions a binary number into smaller bits. Similar to how we partitioned the leftmost bit as the sign bit, we will see that we can do that for the sign, the absolute value, and the exponent. 
- Floating-point numbers allow and arbitrary number of decimal places to the right of the decimal point
  - For example: $0.5 * 0.25 = 0.125$
- They are often expressed in scientific notation 
  - For example: 
    - $0.125 = 1.25 * 10^{-1}$
    - $5,000,000 = 5.0 * 10^6$
- Computers use a form of scientific notation for floating-point representation
- Numbers written in scientific notation have 3 components:
  ```
  sign           exponent
   v                v
   +  1.25  x   10^-1
       ^
    mantissa
  ```
- Computer representation of a floating-point number consists of three fixed-sized fields:
  ```
  sign
  | |  Exponent  |  Significand  |
  ```
- This is the standard arrangement of these fields
  > **NOTE:** although "significand" and "mantissa" do not technically mean the same thing, many people use these terms interchangably. We use the term "significand" to refer to the fractional part of a floating point number. 
- The one-bit sign field is the sign of the stored value.
- The size of the exponent field determines the range of values that can be represented.
- The size of the significand determines the precision of the representation 
- We introduce a hypothetical "simple mode" to explain the concepts
- In this model:
  - A floating-point number is 14 bits in length. 
  - The exponent field is 5 bits
  - The significand field is 8 bits
- The significand is always preceded by and implied binary point. 
- Thus, the significand always contains a fractional binary value. 
- The exponent indicates the power of 2 by which the significand is multiplied
- **Example:**
  - Express $32_{10}$ in the simplified 14-bit floating point model
  - We know that 32 is $2^5$. So in (binary) scientific notation, $32 = 1.0*2^5 = 0.1*2^6$
    - In a moment, we'll explain why we prefer the second notation versus the first. 
  - Using this information, we put $110~(= 6_{10})$ in the exponent field and 1 in the significand as shown:
  
  | `0` | `0 0 1 1 0` | `1 0 0 0 0 0 0 0` |
  |:---:|:-----------:|:-----------------:|
  - Bellow are all equivalent representations for 32 using our simplified model
  
  | `0` | `0 0 1 1 0` | `1 0 0 0 0 0 0 0` |
  |:---:|:-----------:|:-----------------:|

  | `0` | `0 0 1 1 1` | `0 1 0 0 0 0 0 0` |
  |:---:|:-----------:|:-----------------:|

  | `0` | `0 1 0 0 0` | `0 0 1 0 0 0 0 0` |
  |:---:|:-----------:|:-----------------:|

  | `0` | `0 1 0 0 1` | `0 0 0 1 0 0 0 0` |
  |:---:|:-----------:|:-----------------:|

  - Not only do these synonymous representations waste space, but they can also cause confusion. 
  - Another problem with our system is that we have made no allowances for negative exponents. We have no way to express fractional numbers > 1 such as $0.5 (= 2^{-1})!$ (notice that there is no sign in the exponent field)
  > All of these problems can be fixed with no changes to our basic model
  - To resolve the problem of synonymous forms, we establish a rule that the first digit of the significand must be 1, with no ones to the left of the radix point. 
  - This process, called *normalization*, results in a unique pattern for each floating-point number. 
    - In our simple model, all significands must have the form `0.1xxxxxxxx`
    - For example, $4.5 = 100.1*2^0 = 1.001*2^2 = 0.1001*2^3$. The last expression is correctly normalized.
    > *In our simple intructional model, we use no implied bits*
- to provide for negative exponents, we will use a *biased exponent*
- A bias is a number that is approximately midway in the range of values expressible by the exponent. We subtract the bias from the value in the exponent to determine it's true value. 
  - In our case, we have a 5-bit exponent. We will use 16 for our bias. This is called excess-16 representation. 
- In our model, exponent values less than 16 are negative, representing fractional numbers. 
- **Example:**
  - Express $32_{10}$ in the revised 14-bit floating point model.
  - We know that $32 = 1.0*2^5 = 0.1*2^6$
  - To use our excess 16 biased exponent, we add 16 to 6, giving $22_{10} (= 10110_2)$
  - So we have: 
  
  | `0` | `1 0 1 1 1` | `1 0 0 0 0 0 0 0` |
  |:---:|:-----------:|:-----------------:|
- **Example:**
  - Express $0.0625_{10}$ in the revised 14-bit floating point model 
  - We know that $0.0625$ is $2^{-4}$. So in (binary) scientific notation $0.0625 = 1.0*2^{-4} = 0.1*2^{-3}$
  - To use our excess 16 biased exponent, we add 16 to -3, giving $13_{10} (= 01101_2)$
  
  | `0` | `1 0 1 1 1` | `1 0 0 0 0 0 0 0` |
  |:---:|:-----------:|:-----------------:|
- **Example:**
  - Express $-26.625_{10}$ in the revised 14-bit floating-point model. 
  - We find $26.625_{10} = 11010.101_2$. Normalizing, we have $26.625_{10} = 0.11010101*2^5$.
  - To use our excess 16 biased exponent, we add 16 to 5, giving $21_{10} (=10101_2)$. We also need a 1 in the sign bit.
  
  | `1` | `1 0 1 0 1` | `1 1 0 1 0 1 0 1` |
  |:---:|:-----------:|:-----------------:|

- The IEEE has established a standard for floating-point numbers.
- The IEEE-754 *single precision* floating point standard uses an 8-bit exponent (with a bias of 127) and a 23-bit significand. 
- The IEEE-754 *double precision* standard uses an 11-bit exponent (with a bias of 1023) and a 52-bit significand. 
- In both IEEE single-precision and double-precision floating-point standard, the significant has an implied 1 to the LEFT of the radix point. 
  - The format for a significand using the IEEE format is: `1.xxx...`
  - For example, $4.5 = .1001*2^3$ in IEEE format is $4.5 = 1.001*2^2$. The 1 is implied, which means it does not need to be listed in the significand (the significand would include only 001).
- **Example:** 
  - Express $-3.75$ as a floating-point number using IEEE single-precision.
  - First, let's normalize according to IEEE rules:
    - $3.75 = -11.11_2 = -1.111*2^1$
    - The bias is 127, so we add 127+1=128 (this is our exponent) 
    - The first 1 in the significand is implied, so we have:
  
    | 1 | `1 0 0 0 0 0 0 0` | `1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0` |
    |:-:|:-----------------:|:-----------------------------------------------:|

    - Since we have an implied 1 in the significand, this equates to $-(1).111_2*2^{(128-127)} = -1.111_2*2^1=-11.11_2=-3.75$
- Using the IEEE-754 single-precision floating-point standard:
  - An exponent of 255 indicated a special value
    - If the significand is zero, the value is ${+\over}\infty$ 
    - If the significand is non-zero, the value is NaN, "Not a Number", often used to flag and error condition. 
- Using the double-precision standard:
  - The "special" exponent value for a double precision number is 2047, instead of 255 used by the single-precision standard. 
- Both the 14-bit model that we have presented and the IEEE-754 floating-point standard allow two representations for zero. 
  - Zero is indicated by all zeros in the exponent and the significand, but the sign bit can be either 0 or 1. 
- This is why programmers should avoid testing a floating-point value for the equality to zero.
  - Negative zero does not equal positive zero. 
- Floating-point addition and subtraction are done using methods analogous to how we perform calculations using pencil and paper. 
- The first thing that we do is express both operands in the same exponential power, then add the numbers, preserving the exponent in the sume. 
- If the exponent requires adjustment, we do so at the end of the calculation. 
- **Example:**
  - Find the sum of $12_{10}$ and $1.25_{10}$ using the 14-bit "simple" floating-point model.
  - We find $12_{10} = 0.1100*2^4$ and $1.25_{10} = 0.101*2^1=0.000101$

  |                          | `0` | `1 0 1 0 0` | `1 1 0 0 0 0 0 0` |
  |--------------------------|:---:|:-----------:|:-----------------:|
  | `+`                      | `0` | `1 0 1 0 0` | `0 0 0 1 0 1 0 0` |
  `---------------------------------------------`
  | &nbsp;&nbsp;&nbsp;&nbsp; | `0` | `1 0 1 0 0` | `1 1 0 0 0 0 0 0` |
  |--------------------------|:---:|:-----------:|:-----------------:|
  > Thus, our sum is $0.110101*2^4$

- Floating point multiplication is also carried out in a manner akin to how we perform multiplication using pencil and paper
- We multiply the two operands and add their exponents
- If the exponent requires adjustment, we do so at the end of the calculation. 
- **Example:** 
  - Find the product of $12_{10}$ and $1.25_{10}$ using the 14-bit floating-point model. 
  - We find $12_{10} = 0.1100*2^4$ and $1.25_{10} = 0.101*2^1$
  
  |                          | `0` | `1 0 1 0 0` | `1 1 0 0 0 0 0 0` |
  |--------------------------|:---:|:-----------:|:-----------------:|
  | `x`                      | `0` | `1 0 0 0 1` | `1 0 1 0 0 0 0 0` |
  `---------------------------------------------`
  | &nbsp;&nbsp;&nbsp;&nbsp; | `0` | `1 0 1 0 1` | `0 1 1 1 1 0 0 0` |
  |--------------------------|:---:|:-----------:|:-----------------:|
  > - Thus, our product is $0.0111100*2^5 = 0.1111*2^4$
  > - The normalized product requires an exponent of $20_{10} = 10100_2$

- No matter how many bits we use in a floating-point representation, our model must be finite. 
- The real number system is, of course, infinite, so our models can give nothing more than an approximation of a real value. 
- At some point, every model breaks down, introducing errors into our calculations. 
- By using a greater number of bits in our model, we can reduce these errors, but we can never totally eliminate them. 
- Our job becomes one of reducing error, or at least being aware of the possible magnitude of errors in our calculations. 
- We must also be aware that error can compound through repetitive arithmetic operations. 
- For example, our 14-bit model cannot exactly represent the decimal value 128.5. In binary, it is 9 bits wide:
  - $10000000.1_2 = 128.5_{10}$
- When we try to express 128.5 in our 14-bit model, we lose the low-order bit, giving a relative error of:
  - $\displaystyle \frac{128.5 - 128}{128.5} \approx .39\%$
- If we had a procedure that repetitively added $0.5$ to $128.5$, we would have an error of nearly $2\%$ after only four iterations.
- Floating point errors can be reduced when we use operands that are similar in magnitude.
- If we were repetitively adding $0.5$ to $128.5$, it would have been better to iteratively add $0.5$ to iteself and then add $128.5$ to this sum.
- In this example, the error was caused by loss of the low-order bit. 
- Loss of the high-order bit is more problematic. 
- Floating-point overflow and underflow can cause programs to crash. 
- Overflow occurs when there is no room to store the high-order bits resulting from a calculation.
- Underflow occurs when a value is too small to store, possibly resulting in division by zero
  > Experienced programmers know that it's better for a program to crash than to have it produce incorrect, but plausible, results. 
- When discussing floating-point numbers, it is important to understand the terms **range, precision, and accuracy**.
- The **range** of a numeric integer format is the difference between the largest and smallest values that can be expressed. 
- **Accuracy** refers to how closely a numeric representation approximates a true value. 
- The **precision** of a number indicated how much information we have about a value. 
- Most of the time, greater precision leads to greater accuracy, but this is not always true.
  - For example, 3.1333 is a value of pi that is accurate to two digits, but has 5 digits precision. 
- There are other problems with floating-point numbers:
  - Beaucause of truncated bits, you cannot assume that a particular floating point operation is commutative or distributive.
- This means that we cannot assume:
    $(a+b) +c = a+(b+c)$
    OR
    $a*(b+c) = ab+ac$
- Moreover, to test a floating-point value for equality to some other number, it is best to declare a "nearness to x" epsilon value. For example, instead of checking to see if floating-point x is equal to 2 as follows: 
  - if x = 2 then...
    - It is better to use:
  - if (abs(x-2) < epsilon) then...
    - (assuming we have epsilon defined correctly!)

---

### Character Codes
- Calculations aren't useful until their results can be displayed in a manner that is meaningful to people. 
- We also need to store the results of calculations, and provide a means for data input. 
- This, human-understandable characters must be converted to computer-understandable bit patterns using some sort of character encoding scheme. 
- As computers have evolved, character codes have evolved. 
- Larger computer memories and storage devices permit richer character codes. 
- The earliest computer encoding system used six bits. 
- Binary-encoded decimal was one of these early codes. It was used by IBM mainframes in the 1950s and 1960s
- In 1964. BCD was extended to an 8-bit code, extended binary-coded decimal interchange code (EBCDIC)
- EBCDIC was one of the first widely-used computer codes that supported upper and lowercase alphabetic character, in addition to special characters, such as punctuation and controls. 
- EBCDIC and CBD are still in use by IBM mainframes today. 
- Other computer manufacturers chose the 7-bit ASCII (American Standard Code for Information Interchange) as a replacement for 6-bit codes. 
- While BCD and EBCDIC were based upon punched card codes, ASCII was based upon telecommunications (Telex) codes. 
- Until recently, ASCII was the dominant character code outside the IBM mainframe world. 
- Many of today's systems embrace unicode, a 16-bit system that can encode characters of every language in the world.
  - The Java programming language, and some operating systems now use unicode as their default character code.
- The unicode codespace is divided into six parts. The first part is for Western alphabet codes, including English, Greek, and Russian. 
- The unicode code space allocation is shown below.

    | Character types | Language                    | Number of Characters | Hexadecimal values |
    |:----------------|:----------------------------|:---------------------|:-------------------|
    | Alphabets       | Latin, greek, cyrillic, etc | 8192                 | 0000 to 1FFF       |
    | Symbols         | Dingbats, mathematical, etc | 4096                 | 2000 to 2FFF       |
    | CJK             | Chinese, Japanese, Korean,..| 4096                 | 3000 to 3FFF       |
    | Han             | Unified CH, JA, KOR         | 40960                | 4000 to DFFF       |
    |                 | Han Expansion               | 4096                 | E000 to EFFF       |
    | User defined    |                             | 4095                 | F000 to FFFE       |

- The lowest-numbered unicode characters comprise the ASCII code.
- The highest provide for user-defined codes. 

---

### Error Detection and Correction
- It is physically impossible for any data recording or transmission medium to be 100% perfect 100% of the time over its entire expected useful life. 
- As more bits are packing onto a square centimeter of disk storage, as communications transmission speeds increase, the likelihood of error increases - sometimes geometrically.
- Thus, **error detection and correction** is critical to accurate data transmission, storage and retrieval. 
- Check digits, appended to the end of a long number, can provide some protection against data input errors.
  - The last characters of UPC barcodes and ISBNs are check digits 
- Long data streams require more economical and sophisticaled error detection mechanisms. 
- Cyclic redundancy checking (CRC) codes provide error detection for large blocks of data. 
- Checksums and CRCs are examples of *systematic error detection*.
- In *systematic error detection* a group of error control bits is appended to the end of the block of transmitted data. 
  - This group of bits is called a *syndrome*.
- CRCs are polynomials over the modulo 2 arithmetic field
  > The mathematical theory behind modulo 2 polynomials is beyond our scope. However, we can easily work it without knowing it's theoretical underpinnings. 
- Modulo 2 arithmetic works like clock arithmetic.
- In clock arithmetic, if we add 2 hours to 11:00, we get 1:00.
- In modulo 2 arithmetic, if we add 1 to 1 we get 0. The addition rules couldn't be simpler. 
  - $0+0=0$
  - $1+0=1$
  - $0+1=1$
  - $1+1=10$
  > You will fully understand why modulo 2 arithmetic is so handy after you study digital circuits in chapter 3.
- Find the quotient and remainder when 1111101 is divided by 1101 in modulo 2 arithmetic.
  - As with traditional division, we note that the dividened is divisible once by the divisor. 
  - We place the divisor under the dividend and perform modulo 2 subtraction. 
  ```
            1
       +--------
  1101 | 1111101
       - 1101
         ----
         0010
  ```
  - Now we bring down the next bit of the dividend.
  - We see that 00101 is not divisible by 1101. So we place a zero in the quotient. 
  ```
            10
       +--------
  1101 | 1111101
       - 1101
         ----
         00101
  ```
  - 1010 is divisibly by 1101 in modulo 2.
  - We perform modulo 2 subtraction.
  ```
            101
       +--------
  1101 | 1111101
       - 1101 
         ---- 
         001010
           1101
           ----
           0111
  ```
  - We find the quotient is 1011 and the remainder is 0010. 
  ```
            1011
       +--------
  1101 | 1111101
       - 1101 
         ---- 
         001010
        -  1101
           ----
           01111
          - 1101
            ----
            0010
  ```
- This procedure is very useful to use in calculating CRC syndromes. 
  > Note: The divisor in this example corresponds to a modulo 2 polynomial: $x^3+x^2+1$
- Suppose we want to transmit the information string 1111101. 
- The receiver and sender decide to use the (arbitrary) polynomial pattern, 1101. 
- The information string is shifted left by one position less than the number of positions in the divisor. 
- The remainder is found through modulo 2 division and added to the information string: 
  $1111101000 + 111 = 1111101111$
  ```
            1011011
       +------------
  1101 | 1111101000
        -1101
         ----
         001010
        -  1101
           ----
           01111
          - 1101
            ----
            001000
           -  1101
              ----
              01010
             - 1101
               ----
               0111
  ```
- If no bits are lost or corrupted, dividing the received informtion string by the agreed upon patter will give a remainder of zero. 
- We see this is so in the calculation at the right. 
- Real applications use longer polynomials to cover larger information string. 
  - Some of the standard polynomials are listed in the text. 
- Data transmission errors are easy to fix once an error is detected. 
  - Just ask the sender to transmit the data again. 
- In computer memory and data storage, this cannot be done. 
  - Too often the only copy of something important is in memory or one disk 
- Thus, to provide data integrity over the long term, error *correcting* codes are required. 
- Hamming codes and reed-solomon codes are two important error correcting codes. 
- Reed-Solomon codes are particularly useful in correcting *burst errors* that occur when a series of adjacent bits are damaged. 
  - Because CD-ROMs are easily scratched, they simply employ a type of Reed-Solomon error correction. 
- Because the mathematics of Hamming codes is much simpler than Reed-Solomon, we discuss Hamming codes in detail. 
- Hamming codes are code words formed by adding redundant check bits, or parity bits, to a data word. 
- The *Hamming Distance* between two code words is the number of bits in which two code words differ
  > This pair of bytes has a hamming distance of 3. 
- The minimum hamming distance for a code is the smallest Hamming distance between *all* pairs of words in the code. 
  ```
     vvv
  10|001|001
  10|110|001
     ^^^
  ```
- The minumum Hamming distance for a code, D(min), determines its error detecting and error correcting capability. 
- For any code word, X, to be interpreted as a different valid code word, Y, at least D(min) single-bit errors must occur in X. 
- Thus, to detect k (or fewer) single-bit errors, the code must have a Hamming distance of D(min) = k+1.
- Hamming codes can detect D(min)-1 errors and *correct* $\displaystyle\Big\lfloor\frac{D(min)-1}{2}\Big\rfloor$ errors.
- Thus, a Hamming ditance of 2k+1 is required to be able to correct *k* errors in any data word. 
- Hamming distance is provided by adding a suitable number of parity bits to a data word. 
- Suppose we have a set of $n$-bit code words consisting of $m$ data bits and $r$ (redundant) parity bits. 
- Suppose also that we wish to detect and correct one single bit error only. 
- An error could occur in any of the $n$ bits, so each code word can be associated with $n$ invalid code words at a Hamming distance of 1. 
- Therefore, we have $n+1$ bit patterns for each code word: one valid code word, and $n$ invalid code words. 
- Using $n$ bits, we have $2^n$ possible bit patterns. We have $2^m$ valid code words with $r$ check bits (where $n = m+r$)
- For each valid code word, we have $(n+1)$ bit patterns (1 legal and $n$ illegal)
- This gives us the inequality: $(n+1)*2^m\leq 2^n$
- Because $n=m+r$, we can rewrite the inequality as:
  - $(m+r+1) * 2^m \leq 2^{m+r}$ or $(m+r+1) \leq 2^r$
  - This inequality gives us a lower limit on the number of check bits that we need in our code words. 
- Suppose we have data words of length $m=4$. Then:
  - $(4+r+1) \leq 2^r$
  - Implies that $r$ must be greater than or equal to 3.
  - We should always use the smallest value of $r$ that makes the inequality true. 
- This means to build a code with 4-bit data words that will correct single-bit errors, we must add 3 check bits. 
- Finding the number of check bits is the hard part. The rest is easy. 
- Suppose we have data words of length $m=8$. Then:
  - $(8+r+1)\leq2^r$
  implies that $r$ must be greater than or rqual to 4. 
- This means to build a code with **8-bit data words** that will correct **single-bit errors**, we **must add 4 check bits**, creating code words of length 12. 
- So how do we assign values to these check bits?
- With code words of length 12, we observe that each of the bits, numbered 1 through 12, can be expressed in powers of 2. This:
  - $1=2^0~~~~~~~~~~~~~~~~5=2^2+2^0~~~~~~~~~~~~~~9=2^3+2^0$
  - $2=2^1~~~~~~~~~~~~~~~~6=2^2+2^1~~~~~~~~~~~~~~10=2^3+2^1$
  - $3=2^1+2^0~~~~~~~~7=2^2+2^1+2^0~~~~~11=2^3+2^1+2^0$
  - $4=2^4~~~~~~~~~~~~~~~~8=2^3~~~~~~~~~~~~~~~~~~~~~~~12=2^3+2^2$
  - $1 (= 2^0)$ contributes to all of the odd-numbered digits. 
  - $2 (= 2^1)$ contributes to the digits, 2,3,6,7,10,11
  - ... and so forth ...
- We can use this idea in the creation of our check bits. 
- Using our code words of length 12, number each bit position starting with 1 in the low order bit. 
- Each bit position corresponding to a power of 2 will be occupied by a check bit. 
- These check bits contain the parity of each bit position for which it participates in the sum.
  |  |  |  | |P| | | |P| |P|P|
  |--|--|--|-|-|-|-|-|-|-|-|-|
  |12|11|10|9|8|7|6|5|4|3|2|1|
- Since $1(=2^0)$ contributes to the values 1,3,5,7,9 and 11, bit 1 will check parity over bits in these positions. 
- Since $2(=2^1)$ contributes to the values 2,3,6,7,10 and 11, but 2 will check parity over these bits. 
- For the word $11010110$, assuming even parity, we have a check value of 1 for check bit 1, and a value of 0 for check bit 2. 
  |1 |1 |0 |1| |0|1|1| |0|0|1|
  |--|--|--|-|-|-|-|-|-|-|-|-|
  |12|11|10|9|8|7|6|5|4|3|2|1|
  > What are the values for the other parity bits?

  |1 |1 |0 |1|1|0|1|1|1|0|0|1|
  |--|--|--|-|-|-|-|-|-|-|-|-|
  |12|11|10|9|8|7|6|5|4|3|2|1|
- Suppose an error occurs in bit 5, as shown above. Our parity bits are:
  - Bit 1 check 1,3,5,7,9 and 11. *This is incorrect as we have a total of 3 ones (which is not even parity)* 
  - Bit 2 checks 2,3,6,7,10 and 11. The parity is correct.
  - Bit 4 checks 4,5,6,7 and 12. *This parity is incorrect, as we have 3 ones.*
  - Bit 8 checks bit 8,9,10,11 and 12. This parity is correct.
  
    |1 |1 |0 |1|1|0|1|1|1|0|0|1|
    |--|--|--|-|-|-|-|-|-|-|-|-|
    |12|11|10|9|8|7|6|5|4|3|2|1|
- The completed code word is shown above. 
  - Bit 1 checks the bits 3,5,7,9 and 11, so its value is 1 to ensure even parity within this group. 
  - Bit 4 checks the bits 5,6,7 and 12, so its value is 1. 
  - Bit 8 check the bits 9, 10, 11 and 12, so it's value is also 1.
- Using the Hamming algorithm, we can not only detect single bit errors in this code word, but also correct them! 
    |1 |1 |0 |1|1|0|1|1|1|0|0|1|
    |--|--|--|-|-|-|-|-|-|-|-|-|
    |12|11|10|9|8|7|6|5|4|3|2|1|
- We have erroneous parity check for bits 1 and 4.
- With *two* parity bits that don't check, we know that the error is in the data, and not in the parity bit. 
- Which data bits are in error? We find out by adding the bit positions of the erroneous bits. 
- Simplify, $1+4=5$. This tells us that the error is in bit 5. If we change bit 5 to a 1, all parity bits check and our data is restored. 

---

### Conclusion

- Computers store data in the form of bits, bytes and words using the binary numbering system. 
- Hexadecimal numbers are formed using four-bit groups called nibbles. 
- Signed integers can be stored in one's complement, two's complement or signed magnitude representation. 
- Floating-point numbers are usually coded using the IEEE 754 floating-point standard. 
- Floating-point operations are not necessarily commutative or distributive. 
- Character encoding is stored using ASCII, EBCDIC or Unicode. 
- Error detecting and correcting codes are necessary because we can expect no transmission or storage medium to be perfect. 
- CRC, Reed-Soloman and Hamming codes are three important error control codes. 