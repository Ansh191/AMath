#include <Python.h>
#include <math.h>
#include <stdio.h>

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
    if(!PyArg_ParseTuple(args, "d:gamma", &value))
        return NULL;

    Py_BuildValue("d", _gamma(value));
}


static PyObject *
m_a(PyObject *self, PyObject *args)
{
    int size = PyTuple_Size(args);
//    Py_BuildValue("i", size);
    if (size < 2)
    {
        PyErr_SetString(PyExc_TypeError, "a() requires at least two arguments");
        return NULL;
    }
//    Py_BuildValue("i", size);

    PyObject *y = PyTuple_GetItem(args, 0);
//    for (Py_ssize_t i=1; i < size; i = i + 1)
//    {
//        y = PyNumber_Add(y, PyTuple_GetItem(args, i));
//        if (!y)
//            return NULL;
//    }
    Py_BuildValue('O', y);
}


static PyMethodDef _basicMethods[] = {
    {"sqrt", m_sqrt, METH_O, "Sqrt of x"},
    {"abs", m_abs, METH_O, "Absolute value of x"},
    {"pow", m_pow, METH_VARARGS, "Pow Function"},
    {"gamma", m_gamma, METH_VARARGS, "Gamma Function"},
    {"a", m_a, METH_VARARGS, "Add Function"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};


PyMODINIT_FUNC
init_basic(void)
{
    PyObject *m;

    m = Py_InitModule("_basic", _basicMethods);
    if (m == NULL)
        return;

}