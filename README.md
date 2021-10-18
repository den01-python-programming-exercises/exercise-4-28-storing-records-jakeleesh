# Exercise 4.28 Storing records

In this exercise, we'll be working with files stored in CSV format, which contain names and ages separated by commas. The file format may look like this:

```plaintext
lily,3
anton,5
levi,4
amy,1
```

The exercise template already has a `Person` class, and the main program has a body for the method `def read_records_from_file(file)`. Implement the `read_records_from_file` method such that it reads the persons from the file passed as a parameter, and finally returns them in the list returned by the method.

The final output of the program should be

```plaintext
persons: 4
persons:
lily
anton
levi
amy
```

The exercise template has a `main` method that you can use to test how your program works. In this exercise, only modify the method `read_records_from_file`.
