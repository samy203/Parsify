# Parsify

Parsify is a Python tool to deal with File parsing, It's easily extendable to parse different types of formats.

## Usage

```python
parser.py <file extension> <output destination> <file1> <file2>.....<file5>
```
**File Extension** : the extension of input file(s).

**Output Destination** : "db" for save parsed data in MongoDB or "json" to save data in output/< extension >/ relative directory

 **File Arguments** : < n > amount of files that a parser will handle



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



## Extending
Parsify could be extended by inheriting from `ParserBase` class and implementing all abstract methods, by defining a parser, it will be detected during run time and if it matches the input file extension, it will be used to parse input file(s)

## License
[MIT](https://choosealicense.com/licenses/mit/)
