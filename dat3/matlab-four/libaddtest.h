/*
 * MATLAB Compiler: 5.0 (R2013b)
 * Date: Thu May 12 10:16:17 2016
 * Arguments: "-B" "macro_default" "-W" "lib:libaddtest" "-T" "link:lib"
 * "addtest.m" 
 */

#ifndef __libaddtest_h
#define __libaddtest_h 1

#if defined(__cplusplus) && !defined(mclmcrrt_h) && defined(__linux__)
#  pragma implementation "mclmcrrt.h"
#endif
#include "mclmcrrt.h"
#ifdef __cplusplus
extern "C" {
#endif

#if defined(__SUNPRO_CC)
/* Solaris shared libraries use __global, rather than mapfiles
 * to define the API exported from a shared library. __global is
 * only necessary when building the library -- files including
 * this header file to use the library do not need the __global
 * declaration; hence the EXPORTING_<library> logic.
 */

#ifdef EXPORTING_libaddtest
#define PUBLIC_libaddtest_C_API __global
#else
#define PUBLIC_libaddtest_C_API /* No import statement needed. */
#endif

#define LIB_libaddtest_C_API PUBLIC_libaddtest_C_API

#elif defined(_HPUX_SOURCE)

#ifdef EXPORTING_libaddtest
#define PUBLIC_libaddtest_C_API __declspec(dllexport)
#else
#define PUBLIC_libaddtest_C_API __declspec(dllimport)
#endif

#define LIB_libaddtest_C_API PUBLIC_libaddtest_C_API


#else

#define LIB_libaddtest_C_API

#endif

/* This symbol is defined in shared libraries. Define it here
 * (to nothing) in case this isn't a shared library. 
 */
#ifndef LIB_libaddtest_C_API 
#define LIB_libaddtest_C_API /* No special import/export declaration */
#endif

extern LIB_libaddtest_C_API 
bool MW_CALL_CONV libaddtestInitializeWithHandlers(
       mclOutputHandlerFcn error_handler, 
       mclOutputHandlerFcn print_handler);

extern LIB_libaddtest_C_API 
bool MW_CALL_CONV libaddtestInitialize(void);

extern LIB_libaddtest_C_API 
void MW_CALL_CONV libaddtestTerminate(void);



extern LIB_libaddtest_C_API 
void MW_CALL_CONV libaddtestPrintStackTrace(void);

extern LIB_libaddtest_C_API 
bool MW_CALL_CONV mlxAddtest(int nlhs, mxArray *plhs[], int nrhs, mxArray *prhs[]);



extern LIB_libaddtest_C_API bool MW_CALL_CONV mlfAddtest(int nargout, mxArray** ret, mxArray* a, mxArray* b);

#ifdef __cplusplus
}
#endif
#endif
