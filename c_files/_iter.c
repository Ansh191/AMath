#include <Python.h>
#include "structmember.h"

typedef struct {
    PyObject_HEAD
    PyObject *start;
    PyObject *value;
    PyObject *step;
} Count;

static void
Count_dealloc(Count* self)
{
    Py_XDECREF(self->start);
    Py_XDECREF(self->value);
    Py_XDECREF(self->step);
    self->ob_type->tp_free((PyObject*)self);
}

static PyObject *
Count_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    Count *self;

    self = (Count *)type->tp_alloc(type, 0);

    return (PyObject *)self;
}

static int
Count_init(Count *self, PyObject *args, PyObject *kwds)
{
    PyObject *start=NULL, *step=NULL, *tmp;

    static char *kwlist[] = {"start", "step", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O|O", kwlist,
                                      &start, &step))
        return -1; 

    if (start) {
        tmp = self->start;
        Py_INCREF(start);
        self->start = start;
        Py_XDECREF(tmp);
    }

    if (step) {
        tmp = self->step;
        Py_INCREF(step);
        self->step = step;
        Py_XDECREF(tmp);
    }

    return 0;
}


static PyMemberDef Count_members[] = {
    {"start", T_OBJECT_EX, offsetof(Count, start), 0,
     "start number"},
    {"step", T_OBJECT_EX, offsetof(Count, step), 0,
     "step"},
    {"value", T_INT, offsetof(Count, value), 0,
     "Current Value on"},
    {NULL}  /* Sentinel */
};

static PyMethodDef Count_methods[] = {
    {NULL}  /* Sentinel */
};

static PyObject *
Countitem(register Count *a, register Py_ssize_t t)
{
    if (t < 0)
    {
        PyErr_SetString(PyExc_IndexError, "Count index out of range");
        return NULL;
    }
    PyObject *p = PyNumber_Add(a->start, PyNumber_Multiply(a->step, t));
    if (!p)
    {
        PyErr_SetString(PyExc_TypeError, "its too bad");
        return NULL;
    }
    return p;

}

static int
Countcontains(Count *a, PyObject *el)
{
    PyObject *thing = PyNumber_Subtract(el, PyNumber_Float(a->start));
    thing = PyNumber_TrueDivide(thing, PyNumber_Float(a->step));
    double thing2 = PyFloat_AsDouble(PyNumber_Float(thing));
    if (!thing2)
    {
        PyErr_SetString(PyExc_TypeError, "step, and start must be numerical");
        return NULL;
    }

    if (floor(thing2) == thing2)
    {
        return 1;
    }
    return 0;
}

static PySequenceMethods Count_as_sequence = {
    0,                                          /* sq_length */
    0,                                          /* sq_concat */
    0,                                          /* sq_repeat */
    (ssizeargfunc)Countitem,                    /* sq_item */
    0,                                          /* sq_slice */
    0,                                          /* sq_ass_item */
    0,                                          /* sq_ass_slice */
    (objobjproc)Countcontains,                  /* sq_contains */
};

static PyTypeObject CountType = {
    PyObject_HEAD_INIT(NULL)
    0,                         /*ob_size*/
    "Count.Count",             /*tp_name*/
    sizeof(Count),             /*tp_basicsize*/
    0,                         /*tp_itemsize*/
    (destructor)Count_dealloc, /*tp_dealloc*/
    0,                         /*tp_print*/
    0,                         /*tp_getattr*/
    0,                         /*tp_setattr*/
    0,                         /*tp_compare*/
    0,                         /*tp_repr*/
    0,                         /*tp_as_number*/
    &Count_as_sequence,        /*tp_as_sequence*/
    0,                         /*tp_as_mapping*/
    0,                         /*tp_hash */
    0,                         /*tp_call*/
    0,                         /*tp_str*/
    0,                         /*tp_getattro*/
    0,                         /*tp_setattro*/
    0,                         /*tp_as_buffer*/
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /*tp_flags*/
    "Count objects",           /* tp_doc */
    0,		               /* tp_traverse */
    0,		               /* tp_clear */
    0,		               /* tp_richcompare */
    0,		               /* tp_weaklistoffset */
    0,		               /* tp_iter */
    0,		               /* tp_iternext */
    Count_methods,             /* tp_methods */
    Count_members,             /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)Count_init,      /* tp_init */
    0,                         /* tp_alloc */
    Count_new,                 /* tp_new */
};

static PyMethodDef module_methods[] = {
    {NULL}  /* Sentinel */
};

#ifndef PyMODINIT_FUNC	/* declarations for DLL import/export */
#define PyMODINIT_FUNC void
#endif
PyMODINIT_FUNC
init_iter(void)
{
    PyObject* m;

//    if (PyType_Ready(&Count) < 0)
//        return;

    m = Py_InitModule3("_iter", module_methods,
                       "Contains iteration stuffs");

    if (m == NULL)
      return;

    Py_INCREF(&CountType);
    PyModule_AddObject(m, "Count", (PyObject *)&CountType);
}