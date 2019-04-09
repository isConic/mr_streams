# MR Streams

MR Streams is a python utility for composing iterable map reduce filter chains  
  
### Goals:  
The goals of this library are relatively simple:  
- provide a stream composition syntax that supports chaining map,reduce,filter operations 
- a stream object should still look and feel like a list/iterable  
- a stream should have options for delayed evaluation of the stream  
- to support future changes regarding how composition  

### Pronunciation:  

- "Mister Streams" for fun
- "M-R-Streams" to sound professional  

### Supported operations  

- `map` - applies functions to values in iterable with a built-in option for partial evaluation. 
  ```python
    from operator import add
    
    [*mr(range(10)).map(add, 1)] 
   
    >>[1,2,3,4,5,6,7,8,9,10]
  ```
- `filter` - applies a boolean function to values emitted in the chain. If the condition is true, the values are emitted further down the chain.       
    ```python
    is_even = lambda x: x % 2 == 0  
  
    [*mr(range(10)).filter(is_even)]  

    >>[0, 2,4,6,8]
    ```  
    
- `reduce` - reduce iterates through all objects and reduces them using a reduction function.   
   ```python
   mr(range(10)).reduce(sum) 
   
   >> 45
   ```

- `take` - limits the number of values emitted in the stream.  
    ```python
      [*mr(range(10)).take(3)]  
    
      >>[0,1,2] 
    ```

- `tap` - applies a function passively to the stream without altering emitted values.   
    ```python
    mr(range(4)).tap(print).reduce(sum)
    
  >> 0
  >> 1
  >> 2
  >> 3
  >> 6
    ```    
    
- `drain` - runs a no-op iteration that depletes the stream. 
  ```python
  mr(range(4)).tap(print).drain()  
    
   >> 0
   >> 1
   >> 2
   >> 3    
   ```  

- `chunk` - groups items in a stream into groups of size `n`
    
    ```python
    mr(range(4)).chunk(2).tap(print).drain()  
    
    >> [0,1]
    >> [2,3]

    ```

