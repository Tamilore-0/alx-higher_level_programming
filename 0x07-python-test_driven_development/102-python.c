#include <python3.10/Python.h>

/**
* print_python_string - Print information about a Python string object
* @p: Pointer to the PyObject representing the string
*
* This function prints information about a Python string object, including
* its type, length, and value. It checks if the string is compact ASCII or
* compact Unicode and prints the corresponding type.
*/
void print_python_string(PyObject *p)
{
	const char *string;

	const char *type_name;

	Py_ssize_t length;

	if (!PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		fprintf(stderr, "\t[ERROR] Invalid String Object\n");
		return;
	}

	string = PyUnicode_AsUTF8(p);
	if (string == NULL)
	{
		printf("NULL string\n");
		return;
	}

	length = PyObject_Length(p);

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		type_name = "compact ascii";
	}
	else if (PyUnicode_IS_COMPACT(p))
	{
		type_name = "compact unicode object";
	}
	else
	{
		type_name = "Non-compact Unicode string";
	}

	printf("[.] string object info\n\ttype: %s.\n\tlength: %zd\n\tvalue: %s\n"
	, type_name, length, string);

}
