#include <Python.h>


static PyObject *
m_mean(PyObject *self, PyObject *arg)
{
	double sum = 0.0;
	if (!PyList_Check(arg))
	{
		PyErr_SetString(PyExc_TypeError, "Argument must be a list");
		return NULL;
	}
    Py_ssize_t size = PyList_Size(arg);


	for (int i=0; i < size; i++)
	{
	    PyObject* v = PyNumber_Float(PyList_GetItem(arg, i));
	    if (!v)
	        return NULL;

	    double value = PyFloat_AsDouble(v);

	    sum = sum + value;
	}

	return Py_BuildValue("d", sum / size);
}

static PyObject *
m_median(PyObject *self, PyObject *arg)
{
    double answer;
	if (!PyList_Check(arg))
	{
		PyErr_SetString(PyExc_TypeError, "Argument must be a list");
		return NULL;
	}
    Py_ssize_t size = PyList_Size(arg);
    int s = PyList_Sort(arg);
    if (s == -1)
        return NULL;

    if (size % 2 == 1)
    {
        int index = size / 2;
        PyObject* ans = PyNumber_Float(PyList_GetItem(arg, index));
        if (!ans)
            return NULL;
        answer = PyFloat_AsDouble(ans);
    }
    else
    {
        int index1 = size / 2;
        int index2 = index1 - 1;
        PyObject* n1 = PyNumber_Float(PyList_GetItem(arg, index1));
        PyObject* n2 = PyNumber_Float(PyList_GetItem(arg, index2));
        if (!n1)
            return NULL;
        if (!n2)
            return NULL;

        int num1 = PyFloat_AsDouble(n1);
        int num2 = PyFloat_AsDouble(n2);

        answer = (num1 + num2) / 2.0;
    }
	return Py_BuildValue("d", answer);
}

static PyMethodDef _basicMethods[] = {
	{ "mean", m_mean, METH_O, "Mean of list" },
	{ "median", m_median, METH_O, "Median of list" },
	{ NULL, NULL, 0, NULL }        /* Sentinel */
};

static struct PyModuleDef _statisticsmodule = {
    PyModuleDef_HEAD_INIT,
    "_statistics",
    NULL,
    -1,
    _basicMethods
};

PyMODINIT_FUNC PyInit__statistics(void)
{
	PyObject* m;

	m = PyModule_Create(&_statisticsmodule);

	if (m == NULL)
		return NULL;
	return m;
}