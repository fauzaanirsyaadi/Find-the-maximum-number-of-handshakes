
<script>
 
 // JavaScript program to find maximum
 // number of handshakes.
  
 // Calculating the maximum number of
 // handshake using derived formula.
 function maxHandshake(n)
 {
     return (n * (n - 1)) / 2;
 }
   
 // Driver Code
 let n = 10;
  
 document.write( maxHandshake(n));
  
 // This code is contributed by souravghosh0416 
  
 </script>