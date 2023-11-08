#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
* print_python_bytes - prints info about python lists
* @p: address of pyobject struct
*/
void print_python_bytes(PyObject *p)
{
	size_t i, len, size;
	char *str;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	len =  size + 1 > 10 ? 10 : size + 1;
	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %lu bytes: ", len);
