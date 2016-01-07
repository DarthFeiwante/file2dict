# file2dict
Program is intended for transformation of the file into dictionary

Requirements: python3

Program contains following functions:
file2dict(name, split_sign)

Its input parameters:
1) name - name of the file to be transformed
2) limiter - final string of the transformation; below this strig rest strings will not be transformed 
(default=lusta, which means that the whole file will be transformed)
3) split_sign (e.g. ;) - sign of split for the dictionary building; keys are string parts that placed before the sign, and
values - after the sign.
Result of the function is dictionary with name assigned to the returned object 
The program is importable only
