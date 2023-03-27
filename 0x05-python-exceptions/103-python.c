#include <Python.h>

/**
 * print_python_list - Prints information about a Python list
 * @p: A pointer to the PyObject list
 */
void print_python_list(PyObject *p)
{
    size_t i, size;
    PyObject *obj;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        fflush(stdout);
        return;
    }
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %lu\n", size);
    printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %lu: %s\n", i, Py_TYPE(obj)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
        else if (PyFloat_Check(obj))
            print_python_float(obj);
    }
    fflush(stdout);
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: A pointer to the PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
    size_t i, size;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        fflush(stdout);
        return;
    }
    size = PyBytes_Size(p);
    printf("  size: %lu\n", size);
    str = PyBytes_AsString(p);
    printf("  trying string: %s\n", str);
    printf("  first %lu bytes:", size + 1 > 10 ? 10 : size + 1);
    for (i = 0; i < size + 1 && i < 10; i++)
        printf(" %02x", str[i] & 0xff);
    printf("\n");
    fflush(stdout);
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: A pointer to the PyObject float object
 */
void print_python_float(PyObject *p)
{
    double value;
    char *str;
    Py_ssize_t size;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        fflush(stdout);
        return;
    }
    value = PyFloat_AsDouble(p);
    str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, &size, NULL);
    if (str == NULL)
    {
        printf("  [ERROR] Float conversion failed\n");
        fflush(stdout);
        return;
    }
    printf("  value: %s\n", str);
    fflush(stdout);
}

