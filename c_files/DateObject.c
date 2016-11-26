#include <Python.h>
#include "structmember.h"
#include <math.h>

typedef struct
{
    PyObject_HEAD
    PyObject *d;
    PyObject *m;
    PyObject *y;
    PyObject *day;
    PyObject *leap;
    PyObject *ad;
} DateObject;

static void
DateObject_dealloc(DateObject* self)
{
    Py_XDECREF(self->d);
    Py_XDECREF(self->m);
    Py_XDECREF(self->y);
    Py_XDECREF(self->leap);
    Py_XDECREF(self->ad);
    Py_XDECREF(self->day);
    self->ob_type->tp_free((PyObject*) self);
}

static PyObject*
DateObject_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    DateObject *self;

    self = (DateObject *)type->tp_alloc(type,0);
//    if (self != NULL)
//    {
//        self->d = 1;
//        if (self->d == NULL)
//        {
//            Py_DECREF(self);
//            return NULL;
//        }
//        self->m = 1;
//        if (self->m == NULL)
//        {
//            Py_DECREF(self);
//            return NULL;
//        }
//        self->y = 1;
//        if (self->y == NULL)
//        {
//            Py_DECREF(self);
//            return NULL;
//        }
//        self->leap = 0;
//        if (self->leap == NULL)
//        {
//            Py_DECREF(self);
//            return NULL;
//        }
//        self->ad = 1;
//        if (self->ad == NULL)
//        {
//            Py_DECREF(self);
//            return NULL;
//        }
//        self->day = PyString_FromString("");
//        if (self->day == NULL)
//        {
//            Py_DECREF(self);
//            return NULL;
//        }
//    }
    return (PyObject *) self;
}

static int
DateObject_init(DateObject *self, PyObject *args, PyObject *kwds)
{
    int y, m, d, leap, ad;
    leap = 0;
    ad = 1;
    static char *kwlist[] = {"y", "m", "d", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "iii", kwlist, &y, &m, &d))
        return -1;


    if (y % 4 == 0)
        leap = 1;
    if (y % 100 == 0)
    {
        leap = 0;
    }
    if (y % 400 == 0)
    {
        leap = 1;
    }

    if (m < 1)
    {
        PyErr_SetString(PyExc_ValueError, "Invalid month value");
        return NULL;
    }
    if (m > 12)
    {
        PyErr_SetString(PyExc_ValueError, "Invalid month value");
        return NULL;
    }
    if (d < 1)
    {
        PyErr_SetString(PyExc_ValueError, "Invalid day value");
        return NULL;
    }
    if (m == 1)
    {
        if (d > 31)
        {
            PyErr_SetString(PyExc_ValueError, "Invalid day value");
            return NULL;
        }
    }
    if (m == 3)
    {
        if (d > 31)
        {
            PyErr_SetString(PyExc_ValueError, "Invalid day value");
            return NULL;
        }
    }
    if (m == 4)
    {
        if (d > 30)
        {
            PyErr_SetString(PyExc_ValueError, "Invalid day value");
            return NULL;
        }
    }
    if (m == 5)
    {
        if (d > 31)
        {
            PyErr_SetString(PyExc_ValueError, "Invalid day value");
            return NULL;
        }
    }
    if (m == 6)
    {
        if (d > 30)
        {
            PyErr_SetString(PyExc_ValueError, "Invalid day value");
            return NULL;
        }
    }
    if (m == 7)
    {
        if (d > 31)
        {
            PyErr_SetString(PyExc_ValueError, "Invalid day value");
            return NULL;
        }
    }
    if (m == 8)
    {
        if (d > 31)
        {
            PyErr_SetString(PyExc_ValueError, "Invalid day value");
            return NULL;
        }
    }
    if (m == 9)
    {
        if (d > 30)
        {
            PyErr_SetString(PyExc_ValueError, "Invalid day value");
            return NULL;
        }
    }
    if (m == 10)
    {
        if (d > 31)
        {
            PyErr_SetString(PyExc_ValueError, "Invalid day value");
            return NULL;
        }
    }
    if (m == 11)
    {
        if (d > 30)
        {
            PyErr_SetString(PyExc_ValueError, "Invalid day value");
            return NULL;
        }
    }
    if (m == 12)
    {
        if (d > 31)
        {
            PyErr_SetString(PyExc_ValueError, "Invalid day value");
            return NULL;
        }
    }
    if (m == 2)
    {
        if (leap)
            if (d > 29)
            {
                PyErr_SetString(PyExc_ValueError, "Invalid day value");
                return NULL;
            }
        else
        {
            if (d > 28)
            {
                PyErr_SetString(PyExc_ValueError, "Invalid day value");
                return NULL;
            }
        }

    }

    if (y < 0)
    {
        ad = 0;
    }

    PyObject *y2, *m2, *d2, *leap2, *ad2;
    y2 = PyInt_FromLong((long)y);
    m2 = PyInt_FromLong((long)m);
    d2 = PyInt_FromLong((long)d);
    if (!leap)
    {
        leap2 = Py_False;
    }
    else
    {
        leap2 = Py_True;
    }

    if (!ad)
    {
        ad2 = Py_False;
    }
    else
    {
        ad2 = Py_True;
    }

    PyObject *day;
    long day_week = day_of_the_week(y2, m2, d2, leap2);
    if (day_week == 6)
        day = PyString_FromString("Saturday");
    else if (day_week == 0)
        day = PyString_FromString("Sunday");
    else if (day_week == 1)
        day = PyString_FromString("Monday");
    else if (day_week == 2)
        day = PyString_FromString("Tuesday");
    else if (day_week == 3)
        day = PyString_FromString("Wednesday");
    else if (day_week == 4)
        day = PyString_FromString("Thursday");
    else if (day_week == 5)
        day = PyString_FromString("Friday");

    self->y = y2;
    self->m = m2;
    self->d = d2;
    self->ad = ad2;
    self->leap = leap2;
    self->day = day;

    return 0;
}

static PyMemberDef DateObject_members[] = {
    {"y", T_OBJECT_EX, offsetof(DateObject, y), READONLY, "year"},
    {"m", T_OBJECT_EX, offsetof(DateObject, m), READONLY, "month"},
    {"d", T_OBJECT_EX, offsetof(DateObject, d), READONLY, "day"},
    {"leap", T_OBJECT_EX, offsetof(DateObject, leap), READONLY, "Boolean of leap year or not"},
    {"ad", T_OBJECT_EX, offsetof(DateObject, ad), READONLY, "AD or not"},
    {"day", T_OBJECT_EX, offsetof(DateObject, day), READONLY, "day"},
    {NULL}
};

static PyObject*
DateObject_getyear(DateObject *self, void *closure)
{
    Py_INCREF(self->y);
    return self->y;
}

static PyObject*
DateObject_getmonth(DateObject *self, void *closure)
{
    Py_INCREF(self->m);
    return self->m;
}

static PyObject*
DateObject_getday(DateObject *self, void *closure)
{
    Py_INCREF(self->d);
    return self->d;
}

static PyObject*
DateObject_getday2(DateObject *self, void *closure)
{
    Py_INCREF(self->day);
    return self->day;
}

static PyObject*
DateObject_getleap(DateObject *self, void *closure)
{
    Py_INCREF(self->leap);
    return self->leap;
}

static PyObject*
DateObject_getad(DateObject *self, void *closure)
{
    Py_INCREF(self->ad);
    return self->ad;
}

static int
DateObject_setyear(DateObject *self, PyObject *value, void *closure)
{
    PyErr_SetString(PyExc_AttributeError, "year is not a writable attribute");
    return -1;
}

static int
DateObject_setmonth(DateObject *self, PyObject *value, void *closure)
{
    PyErr_SetString(PyExc_AttributeError, "month is not a writable attribute");
    return -1;
}

static int
DateObject_setday(DateObject *self, PyObject *value, void *closure)
{
    PyErr_SetString(PyExc_AttributeError, "day is not a writable attribute");
    return -1;
}

static int
DateObject_setad(DateObject *self, PyObject *value, void *closure)
{
    PyErr_SetString(PyExc_AttributeError, "AD is not a writable attribute");
    return -1;
}

static int
DateObject_setleap(DateObject *self, PyObject *value, void *closure)
{
    PyErr_SetString(PyExc_AttributeError, "leap is not a writable attribute");
    return -1;
}

static int
DateObject_setday2(DateObject *self, PyObject *value, void *closure)
{
    PyErr_SetString(PyExc_AttributeError, "day of the week is not a writable attribute");
    return -1;
}

static PyGetSetDef DateObject_getsetters[] = {
    {"y", (getter)DateObject_getyear, (setter)DateObject_setyear, "year", NULL},
    {"m", (getter)DateObject_getmonth, (setter)DateObject_setmonth, "month", NULL},
    {"d", (getter)DateObject_getday, (setter)DateObject_setday, "day", NULL},
    {"day", (getter)DateObject_getday2, (setter)DateObject_setday2, "day of the week", NULL},
    {"leap", (getter)DateObject_getleap, (setter)DateObject_setleap, "leap", NULL},
    {"ad", (getter)DateObject_getad, (setter)DateObject_setad, "ad", NULL},
    {NULL}
};

static PyMethodDef DateObject_methods[] = {
    {NULL}
};

static PyTypeObject DateObjectType = {
    PyObject_HEAD_INIT(NULL)
    0,                         /*ob_size*/
    "DateObject.DateObject",             /*tp_name*/
    sizeof(DateObject),             /*tp_basicsize*/
    0,                         /*tp_itemsize*/
    (destructor)DateObject_dealloc, /*tp_dealloc*/
    0,                         /*tp_print*/
    0,                         /*tp_getattr*/
    0,                         /*tp_setattr*/
    0,                         /*tp_compare*/
    0,                         /*tp_repr*/
    0,                         /*tp_as_number*/
    0,                         /*tp_as_sequence*/
    0,                         /*tp_as_mapping*/
    0,                         /*tp_hash */
    0,                         /*tp_call*/
    0,                         /*tp_str*/
    0,                         /*tp_getattro*/
    0,                         /*tp_setattro*/
    0,                         /*tp_as_buffer*/
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /*tp_flags*/
    "DateObject objects",           /* tp_doc */
    0,		               /* tp_traverse */
    0,		               /* tp_clear */
    0,		               /* tp_richcompare */
    0,		               /* tp_weaklistoffset */
    0,		               /* tp_iter */
    0,		               /* tp_iternext */
    DateObject_methods,             /* tp_methods */
    DateObject_members,             /* tp_members */
    DateObject_getsetters,           /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)DateObject_init,      /* tp_init */
    0,                         /* tp_alloc */
    DateObject_new,                 /* tp_new */
};

static long
day_of_the_week(PyObject *in_y, PyObject *in_m, PyObject *in_d, PyObject *leap)
{
    long y = PyInt_AsLong(in_y);
    long m = PyInt_AsLong(in_m) - 2;

    if (m == 0)
        m = 12;
        y = y - 1;
    if (m == -1)
        m = 11;
        y = y - 1;

    long d = PyInt_AsLong(in_d);

    long lasty = y % 100;

    long stuff = d + floor(2.6 * m - 0.2) + 5 * (lasty % 4) + 4 * (y % 100) + 6 * (y % 400);

    return stuff % 7;
}


static PyMethodDef module_methods[] = {
    {"day", day_of_the_week, METH_VARARGS, "test"},
    {NULL}  /* Sentinel */
};


#ifndef PyMODINIT_FUNC	/* declarations for DLL import/export */
#define PyMODINIT_FUNC void
#endif
PyMODINIT_FUNC
initDateObject(void)
{
    PyObject* m;

    if (PyType_Ready(&DateObjectType) < 0)
        return;

    m = Py_InitModule3("DateObject", module_methods,
                       "DateObject module");

    if (m == NULL)
      return;

    Py_INCREF(&DateObjectType);
    PyModule_AddObject(m, "DateObject", (PyObject *)&DateObjectType);
}