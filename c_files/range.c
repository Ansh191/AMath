#include <Python.h>
#include "structmember.h"

typedef struct {
	PyObject_HEAD
	int start;
	int stop;
	int step;
	int length;
} range;

static void
range_dealloc(range* self)
{
	Py_XDECREF(self->start);
	Py_XDECREF(self->stop);
	Py_XDECREF(self->step);
	Py_XDECREF(self->length);
	self->ob_type->tp_free((PyObject*)self);
}

static PyObject *
range_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
	range *self;

	self = (range *)type->tp_alloc(type, 0);

	return (PyObject *)self;
}

static int
range_init(range *self, PyObject *args, PyObject *kwds)
{
	int start = 0, stop = 0, step = 1, lo, hi;

	static char *kwlist[] = { "start", "stop", "step", NULL };

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "i|ii", kwlist,
		&stop,
		&start,
		&step))
		return -1;

	if (step < 0)
	{
		lo, hi = stop, start;
	}
	else
	{
		lo, hi = start, stop;
	}

	self->length = ((hi - lo - 1) / abs(step)) + 1;

	self->start = start;
	self->stop = stop;
	self->step = step;

	return 0;
}

static PyObject *
range_repr(range *self)
{
	if (self->step == 1)
	{
		return PyString_FromFormat("range(%i, %i)", self->start, self->stop);
	}
	else
	{
		return PyString_FromFormat("range(%i, %i, %i)", self->start, self->stop, self->step);
	}
}

static PyMemberDef range_members[] = {
	{ "start", T_INT, offsetof(range, start), 0, "start" },
	{ "stop", T_INT, offsetof(range, stop), 0, "stop" },
	{ "step", T_INT, offsetof(range, step), 0, "range step" },
	{ "length", T_INT, offsetof(range, length), 0, "length"},
	{ NULL }  /* Sentinel */
};

static PyMethodDef range_methods[] = {
	{ NULL }  /* Sentinel */
};

static PyTypeObject rangeType = {
	PyObject_HEAD_INIT(NULL)
	0,                         /*ob_size*/
	"range.range",             /*tp_name*/
	sizeof(range),             /*tp_basicsize*/
	0,                         /*tp_itemsize*/
	(destructor)range_dealloc, /*tp_dealloc*/
	0,                         /*tp_print*/
	0,                         /*tp_getattr*/
	0,                         /*tp_setattr*/
	0,                         /*tp_compare*/
	range_repr,                /*tp_repr*/
	0,                         /*tp_as_step*/
	0,                         /*tp_as_sequence*/
	0,                         /*tp_as_mapping*/
	0,                         /*tp_hash */
	0,                         /*tp_call*/
	0,                         /*tp_str*/
	0,                         /*tp_getattro*/
	0,                         /*tp_setattro*/
	0,                         /*tp_as_buffer*/
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /*tp_flags*/
	"range objects",           /* tp_doc */
	0,						   /* tp_traverse */
	0,		                   /* tp_clear */
	0,		                   /* tp_richcompare */
	0,		                   /* tp_weaklistoffset */
	0,		                   /* tp_iter */
	0,		                   /* tp_iternext */
	range_methods,             /* tp_methods */
	range_members,             /* tp_members */
	0,                         /* tp_getset */
	0,                         /* tp_base */
	0,                         /* tp_dict */
	0,                         /* tp_descr_get */
	0,                         /* tp_descr_set */
	0,                         /* tp_dictoffset */
	(initproc)range_init,      /* tp_init */
	0,                         /* tp_alloc */
	range_new,                 /* tp_new */
};

static PyMethodDef module_methods[] = {
	{ NULL }  /* Sentinel */
};

#ifndef PyMODINIT_FUNC	/* declarations for DLL import/export */
#define PyMODINIT_FUNC void
#endif
PyMODINIT_FUNC
initrange(void)
{
	PyObject* m;

	if (PyType_Ready(&rangeType) < 0)
		return;

	m = Py_InitModule3("range", module_methods,
		"range");

	if (m == NULL)
		return;

	Py_INCREF(&rangeType);
	PyModule_AddObject(m, "range", (PyObject *)&rangeType);
}