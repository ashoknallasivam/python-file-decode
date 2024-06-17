# python-file-decode

The text file contains words paired with numbers. To decode the message and form a single sentence, you need to create a pyramid structure. Use the last number in each row and its corresponding word to construct a sentence, with each word separated by a space.
<img width="101" alt="image" src="https://github.com/ashoknallasivam/python-file-decode/assets/21120803/92099cf6-c022-4fd2-9939-731402f50844">


* I created a decode function that takes a text file as a parameter. Inside the decode function, I defined another function to create a pyramid structure. This inner function takes a maximum number and an object with key-value pairs, where the key is a number and the value is a word.

* The outer loop in the pyramid function iterates from 1 to the total number of rows. The inner loop runs from 1 to i + 1, where i is the current row number. After each iteration, the number value is incremented. The row is then reversed, and only the first element of the reversed row is taken to form an array of these numbers.

* In the final loop, the array of numbers is used to fetch values from the dictionary using the respective keys. These values are then joined in the expected format and returned.

The final output shoud be 'young system present student lot experiment strong crease sun company hurry remember milk us repeat clothe against meant history indicate pitch print bread would'
  

