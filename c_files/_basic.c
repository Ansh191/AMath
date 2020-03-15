#include <Python.h>
#include <math.h>

double _abs(double v)
{
	if (v > 0.0)
	{
		return v;
	}
	else
	{
		return -v;
	}
}

double _gamma(double x)
{
	return tgamma(x);
}


static PyObject *
m_pow(PyObject *self, PyObject *args)
{
	PyObject *in;
	PyObject *exp;
	PyObject *mod = Py_None;
	double value = 0.0;

	if (!PyArg_UnpackTuple(args, "pow", 2, 3, &in, &exp, &mod))
		return NULL;

	PyObject *result = PyNumber_Power(in, exp, mod);
	if (!result)
		return NULL;

	Py_BuildValue("O", result);
}

static PyObject *
m_abs(PyObject *self, PyObject *arg)
{
	if (PyComplex_Check(arg))
	{
		//        Py_BuildValue("d", 0.0);
		//        Py_BuildValue("d", PyComplex_RealAsDouble);
		//        Py_BuildValue("d", PyComplex_ImagAsDouble);
		//        Py_BuildValue("d", pow(PyComplex_RealAsDouble,2));
		//        Py_BuildValue("d", pow(PyComplex_ImagAsDouble,2));
		//        Py_BuildValue("d", pow(PyComplex_RealAsDouble,2)+pow(PyComplex_ImagAsDouble,2));
		Py_BuildValue("d", sqrt(pow(PyComplex_RealAsDouble(arg), 2) + pow(PyComplex_ImagAsDouble(arg), 2)));
		return;
	}

	PyObject *result = PyNumber_Absolute(arg);
	if (!result)
		return NULL;

	Py_BuildValue("O", result);
}

static PyObject *
m_sqrt(PyObject *self, PyObject *arg) {

	if (PyComplex_Check(arg))
	{
		Py_BuildValue("D", _Py_c_pow(PyComplex_AsCComplex(arg), PyComplex_AsCComplex(Py_BuildValue("d", 0.5))));
		return;
	}

	PyObject *result = PyNumber_Power(arg, PyFloat_FromDouble(0.5), Py_None);

	if (!result)
		return NULL;

	Py_BuildValue("O", result);
}


static PyObject *
m_gamma(PyObject *self, PyObject *args)
{
	double value = 0.0;
	if (!PyArg_ParseTuple(args, "d:gamma", &value))
		return NULL;

	Py_BuildValue("d", _gamma(value));
}


static PyObject *
m_a(PyObject *self, PyObject *args)
{
	//Py_Initialize();
	int size = PyTuple_Size(args);
	//    Py_BuildValue("i", size);
	if (size < 2)
	{
		PyErr_SetString(PyExc_TypeError, "a() requires at least two arguments");
		return NULL;
	}
	//    Py_BuildValue("i", size);

	//PyObject *y = PyTuple_GetItem(args, 1);
	//PyObject *y = PyLong_FromLong(500);
	//PyRun_SimpleString("print(5)");
	//if (!y)
	//{
	//	PyErr_SetString(PyExc_TypeError, "a() requires at least two arguments");
	//	return NULL;
	//}
	//    for (Py_ssize_t i=1; i < size; i = i + 1)
	//    {
	//        y = PyNumber_Add(y, PyTuple_GetItem(args, i));
	//        if (!y)
	//            return NULL;
	//    }
	//return Py_BuildValue('O', args);
}


static PyObject *
m_ln(PyObject *self, PyObject *arg)
{
	double value;
	PyObject *val = PyNumber_Float(arg);
	if (!val)
	{
		PyErr_SetString(PyExc_TypeError, "Argument must be a number");
		return NULL;
	}
	value = PyFloat_AsDouble(val);
	return Py_BuildValue("d", log(value));
}

static PyObject *
m_log(PyObject *self, PyObject *args)
{
	PyObject *base1;
	PyObject *value1;
	double value;
	double base;
	if (!PyArg_UnpackTuple(args, "log", 2, 2, &value1, &base1))
	{
		return NULL;
	}
	PyObject *value2 = PyNumber_Float(value1);
	PyObject *base2 = PyNumber_Float(base1);
	if (!value2)
	{
		return NULL;
	}
	if (!base2)
	{
		return NULL;
	}
	value = PyFloat_AsDouble(value2);
	base = PyFloat_AsDouble(base2);
	double result = log(value) / log(base);
	return Py_BuildValue("d", result);
}

static PyObject *
m_log10(PyObject *self, PyObject *arg)
{
	PyObject *tuple = PyTuple_Pack(2, arg, PyLong_FromLong(10));
	return m_log(self, tuple);
}

static PyObject *
m_log2(PyObject *self, PyObject *arg)
{
	PyObject *tuple = PyTuple_Pack(2, arg, PyLong_FromLong(2));
	return m_log(self, tuple);
}

static PyObject *
m_fib(PyObject *self, PyObject *arg)
{
    double gr = (1 + sqrt(5)) / 2.0;
    double value;
    PyObject *val = PyNumber_Float(arg);
    if (!val)
    {
        PyErr_SetString(PyExc_TypeError, "Argument must be a number");
		return NULL;
    }
    value = PyFloat_AsDouble(val);
    double result = floor((pow(gr, value) - pow(1 - gr, value)) / sqrt(5));
    return Py_BuildValue("d", result);
}

static PyObject *
m_exp(PyObject *self, PyObject *arg)
{
    double e = 2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466;
    double value;
    PyObject *val = PyNumber_Float(arg);
    if (!val)
    {
        PyErr_SetString(PyExc_TypeError, "Argument must be a number");
		return NULL;
    }
    value = PyFloat_AsDouble(val);
    double result = floor((pow(e, value) - pow(1 - e, value)) / sqrt(5));
    return Py_BuildValue("d", result);
}


static PyMethodDef _basicMethods[] = {
	{ "sqrt", m_sqrt, METH_O, "Sqrt of x" },
	{ "abs", m_abs, METH_O, "Absolute value of x" },
	{ "pow", m_pow, METH_VARARGS, "Pow Function" },
	{ "gamma", m_gamma, METH_VARARGS, "Gamma Function" },
	{ "ln", m_ln, METH_O, "Natural Logarithm of x" },
	{ "log", m_log, METH_VARARGS, "Base Logarithm of x" },
	{ "log10", m_log10, METH_O, "Base 10 Logarithm of x" },
	{ "log2", m_log2, METH_O, "Base 2 Logarithm of x" },
	{ "fib", m_fib, METH_O, "xth fibonacci number" },
	{ "exp", m_exp, METH_O, "e to the xth power"},
	{ NULL, NULL, 0, NULL }        /* Sentinel */
};

static struct PyModuleDef _basicmodule = {
    PyModuleDef_HEAD_INIT,
    "_basic",
    NULL,
    -1,
    _basicMethods
};

PyMODINIT_FUNC PyInit__basic(void)
{
	PyObject* m;

	m = PyModule_Create(&_basicmodule);

	if (m == NULL)
		return NULL;
	return m;
}