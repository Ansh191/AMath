#include "Python.h"
#include <stdio.h>
#include <Windows.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

static HANDLE hInterruptEvent = NULL;
static BOOL WINAPI PyCtrlHandler(DWORD dwCtrlType)
{
    SetEvent(hInterruptEvent);
    return FALSE;
}
static long main_thread;

static int
floatsleep(double secs)
{
    #if defined(HAVE_SELECT) && !defined(__BEOS__) && !defined(__EMX__)
    struct timeval t;
    double frac;
    frac = fmod(secs, 1.0);
    secs = floor(secs);
    t.tv_sec = (long)secs;
    t.tv_usec = (long)(frac*1000000.0);
    Py_BEGIN_ALLOW_THREADS
    if (select(0, (fd_set *)0, (fd_set *)0, (fd_set *)0, &t) != 0) {
#ifdef EINTR
        if (errno != EINTR) {
#else
        if (1) {
#endif
            Py_BLOCK_THREADS
            PyErr_SetFromErrno(PyExc_IOError);
            return -1;
        }
    }
    Py_END_ALLOW_THREADS
#elif defined(__WATCOMC__) && !defined(__QNX__)
    /* XXX Can't interrupt this sleep */
    Py_BEGIN_ALLOW_THREADS
    delay((int)(secs * 1000 + 0.5));  /* delay() uses milliseconds */
    Py_END_ALLOW_THREADS
#elif defined(MS_WINDOWS)
    {
        double millisecs = secs * 1000.0;
        unsigned long ul_millis;

        if (millisecs > (double)ULONG_MAX) {
            PyErr_SetString(PyExc_OverflowError,
                            "sleep length is too large");
            return -1;
        }
        Py_BEGIN_ALLOW_THREADS
        /* Allow sleep(0) to maintain win32 semantics, and as decreed
         * by Guido, only the main thread can be interrupted.
         */
        ul_millis = (unsigned long)millisecs;
        if (ul_millis == 0 ||
            main_thread != PyThread_get_thread_ident())
            Sleep(ul_millis);
        else {
            DWORD rc;
            ResetEvent(hInterruptEvent);
            rc = WaitForSingleObject(hInterruptEvent, ul_millis);
            if (rc == WAIT_OBJECT_0) {
                /* Yield to make sure real Python signal
                 * handler called.
                 */
                Sleep(1);
                Py_BLOCK_THREADS
                errno = EINTR;
                PyErr_SetFromErrno(PyExc_IOError);
                return -1;
            }
        }
        Py_END_ALLOW_THREADS
    }
#elif defined(PYOS_OS2)
    /* This Sleep *IS* Interruptable by Exceptions */
    Py_BEGIN_ALLOW_THREADS
    if (DosSleep(secs * 1000) != NO_ERROR) {
        Py_BLOCK_THREADS
        PyErr_SetFromErrno(PyExc_IOError);
        return -1;
    }
    Py_END_ALLOW_THREADS
#elif defined(__BEOS__)
    /* This sleep *CAN BE* interrupted. */
    {
        if( secs <= 0.0 ) {
            return;
        }

        Py_BEGIN_ALLOW_THREADS
        /* BeOS snooze() is in microseconds... */
        if( snooze( (bigtime_t)( secs * 1000.0 * 1000.0 ) ) == B_INTERRUPTED ) {
            Py_BLOCK_THREADS
            PyErr_SetFromErrno( PyExc_IOError );
            return -1;
        }
        Py_END_ALLOW_THREADS
    }
#elif defined(RISCOS)
    if (secs <= 0.0)
        return 0;
    Py_BEGIN_ALLOW_THREADS
    /* This sleep *CAN BE* interrupted. */
    if ( riscos_sleep(secs) )
        return -1;
    Py_END_ALLOW_THREADS
#elif defined(PLAN9)
    {
        double millisecs = secs * 1000.0;
        if (millisecs > (double)LONG_MAX) {
            PyErr_SetString(PyExc_OverflowError, "sleep length is too large");
            return -1;
        }
        /* This sleep *CAN BE* interrupted. */
        Py_BEGIN_ALLOW_THREADS
        if(sleep((long)millisecs) < 0){
            Py_BLOCK_THREADS
            PyErr_SetFromErrno(PyExc_IOError);
            return -1;
        }
        Py_END_ALLOW_THREADS
    }
#else
    /* XXX Can't interrupt this sleep */
    Py_BEGIN_ALLOW_THREADS
    sleep((int)secs);
    Py_END_ALLOW_THREADS
#endif

    return 0;
}
}
static PyObject*
amath_sleep(PyObject *self, PyObject *arg)
{
    double t = PyFloat_AsDouble(arg);
    if (!t)
    {
        return NULL;
    }
    if (floatsleep(t) != 0)
        return NULL;
    Py_INCREF(Py_None);
    return Py_None;
}

void _system(char *comm, FILE *fp)
{
    system(comm);
}

static PyObject*
amath_system(PyObject *self, PyObject *args)
{
    char *comm;

    if (!PyArg_ParseTuple(args, "s:system", &comm))
        return NULL;

    _system(comm);
    Py_RETURN_NONE;
}

static char sleep_docs[] =
        "sleep(s): sleep for s seconds\n";

static char system_docs[] =
        "system(comm): run comm in terminal or command prompt\n";

static PyMethodDef system_funcs[] = {
        {"system", amath_system, METH_VARARGS, system_docs},
        {"sleep", amath_sleep, METH_O, sleep_docs},
        {NULL}
};

PyMODINIT_FUNC
init_system(void)
{
    PyObject *m;

    m = Py_InitModule("_system", system_funcs);
    if (m == NULL)
        return;
}