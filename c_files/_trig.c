#include <Python.h>
#include <math.h>

static PyObject *IorFError;

#define PI 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214
#define E 2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466

double _sin(double x) {
  return sin(x);
}

double _cos(double a)
{
	return cos(a);
}

double _tan(double a)
{
	return tan(a);
}

double _cot(double a)
{
	return 1 / tan(a);
}

double _sec(double a)
{
	return 1 / cos(a);
}

double _csc(double a)
{
	return 1 / sin(a);
}

double _asin(double a)
{
	return asin(a);
}

double _acos(double a)
{
	return acos(a);
}

double _atan(double a)
{
	return atan(a);
}

double _acot(double a)
{
	return (PI/2)-atan(a);
}

double _asec(double a)
{
	return acos(1/a);
}

double _acsc(double a)
{
	return asin(1/a);
}

double _sinh(double a)
{
    return sinh(a);
}

double _cosh(double a)
{
    return cosh(a);
}

double _tanh(double a)
{
    return tanh(a);
}

double _coth(double a)
{
    return cosh(a) / sinh(a);
}

double _sech(double a)
{
    return 1.0 / cosh(a);
}

double _csch(double a)
{
    return 1.0 / sinh(a);
}

static PyObject *
m_sin(PyObject *self, PyObject *args) {
  double in=0.0;
  if (!PyArg_ParseTuple(args, "d:sin", &in))
    return NULL;
  return Py_BuildValue("d", _sin(in));
}

static PyObject *
m_cos(PyObject *self, PyObject *args) {
  double in=0.0;
  if (!PyArg_ParseTuple(args, "d:cos", &in))
    return NULL;
  return Py_BuildValue("d", _cos(in));
}

static PyObject *
m_tan(PyObject *self, PyObject *args) {
  double in=0.0;
  if (!PyArg_ParseTuple(args, "d:tan", &in))
    return NULL;
  return Py_BuildValue("d", _tan(in));
}

static PyObject *
m_cot(PyObject *self, PyObject *args) {
  double in=0.0;
  if (!PyArg_ParseTuple(args, "d:cot", &in))
    return NULL;
  return Py_BuildValue("d", _cot(in));
}

static PyObject *
m_sec(PyObject *self, PyObject *args) {
  double in=0.0;
  if (!PyArg_ParseTuple(args, "d:sec", &in))
    return NULL;
  return Py_BuildValue("d", _sec(in));
}

static PyObject *
m_csc(PyObject *self, PyObject *args) {
  double in=0.0;
  if (!PyArg_ParseTuple(args, "d:csc", &in))
    return NULL;
  return Py_BuildValue("d", _csc(in));
}

static PyObject *
m_asin(PyObject *self, PyObject *args) {
  double in=0.0;
  if (!PyArg_ParseTuple(args, "d:asin", &in))
    return NULL;
  return Py_BuildValue("d", _asin(in));
}

static PyObject *
m_acos(PyObject *self, PyObject *args) {
  double in=0.0;
  if (!PyArg_ParseTuple(args, "d:acos", &in))
    return NULL;
  return Py_BuildValue("d", _acos(in));
}

static PyObject *
m_atan(PyObject *self, PyObject *args) {
  double in=0.0;
  if (!PyArg_ParseTuple(args, "d:atan", &in))
    return NULL;
  return Py_BuildValue("d", _atan(in));
}

static PyObject *
m_acot(PyObject *self, PyObject *args) {
  double in=0.0;
  if (!PyArg_ParseTuple(args, "d:acot", &in))
    return NULL;
  return Py_BuildValue("d", _acot(in));
}

static PyObject *
m_asec(PyObject *self, PyObject *args) {
  double in=0.0;
  if (!PyArg_ParseTuple(args, "d:asec", &in))
    return NULL;
  return Py_BuildValue("d", _asec(in));
}

static PyObject *
m_acsc(PyObject *self, PyObject *args) {
  double in=0.0;
  if (!PyArg_ParseTuple(args, "d:acsc", &in))
    return NULL;
  return Py_BuildValue("d", _acsc(in));
}

//static PyObject *
//m_sinh(PyObject *self, PyObject *args)
//{
//    PyObject *in;
//    if (!PyArg_UnpackTuple(args, "sinh", 1, 1, &in))
//        return NULL;
//
//    if (PyComplex_Check(in))
//    {
//
//    }
//}

static PyMethodDef _trigMethods[] = {
    { "sin", (PyCFunction)m_sin, METH_VARARGS, "Sine of x" },
	{ "cos", (PyCFunction)m_cos, METH_VARARGS, "Cosine of x" },
	{ "tan", (PyCFunction)m_tan, METH_VARARGS, "Tangent of x" },
	{ "cot", (PyCFunction)m_cot, METH_VARARGS, "Cotangent of x" },
	{ "sec", (PyCFunction)m_sec, METH_VARARGS, "Secant of x" },
	{ "csc", (PyCFunction)m_csc, METH_VARARGS, "Cosecant of x" },
	{ "asin", (PyCFunction)m_asin, METH_VARARGS, "Arcsine of x"} ,
	{ "acos", (PyCFunction)m_acos, METH_VARARGS, "Arccosine of x" },
	{ "atan", (PyCFunction)m_atan, METH_VARARGS, "Arctangent of x" },
	{ "acot", (PyCFunction)m_acot, METH_VARARGS, "Arccotangent of x" },
	{ "asec", (PyCFunction)m_asec, METH_VARARGS, "Arcsecant of x" },
	{ "acsc", (PyCFunction)m_acsc, METH_VARARGS, "Arccosecant of x" },
    { NULL, NULL, 0, NULL }        /* Sentinel */
};

static struct PyModuleDef _trigmodule = {
    PyModuleDef_HEAD_INIT,
    "_trig",
    NULL,
    -1,
    _trigMethods
};


PyMODINIT_FUNC PyInit__trig(void)
{
  PyObject *m;

  m = PyModule_Create(&_trigmodule);
  if (m == NULL)
    return;

  return m;
}