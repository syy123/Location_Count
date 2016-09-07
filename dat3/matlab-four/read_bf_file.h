/*
 * MATLAB Compiler: 5.0 (R2013b)
 * Date: Wed May 11 16:22:03 2016
 * Arguments: "-B" "macro_default" "-W" "lib:read_bf_file" "-T" "link:lib"
 * "read_bf_file.m" 
 */

#ifndef __read_bf_file_h
#define __read_bf_file_h 1

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

#ifdef EXPORTING_read_bf_file
#define PUBLIC_read_bf_file_C_API __global
#else
#define PUBLIC_read_bf_file_C_API /* No import statement needed. */
#endif

#define LIB_read_bf_file_C_API PUBLIC_read_bf_file_C_API

#elif defined(_HPUX_SOURCE)

#ifdef EXPORTING_read_bf_file
#define PUBLIC_read_bf_file_C_API __declspec(dllexport)
#else
#define PUBLIC_read_bf_file_C_API __declspec(dllimport)
#endif

#define LIB_read_bf_file_C_API PUBLIC_read_bf_file_C_API


#else

#define LIB_read_bf_file_C_API

#endif

/* This symbol is defined in shared libraries. Define it here
 * (to nothing) in case this isn't a shared library. 
 */
#ifndef LIB_read_bf_file_C_API 
#define LIB_read_bf_file_C_API /* No special import/export declaration */
#endif

extern LIB_read_bf_file_C_API 
bool MW_CALL_CONV read_bf_fileInitializeWithHandlers(
       mclOutputHandlerFcn error_handler, 
       mclOutputHandlerFcn print_handler);

extern LIB_read_bf_file_C_API 
bool MW_CALL_CONV read_bf_fileInitialize(void);

extern LIB_read_bf_file_C_API 
void MW_CALL_CONV read_bf_fileTerminate(void);



extern LIB_read_bf_file_C_API 
void MW_CALL_CONV read_bf_filePrintStackTrace(void);

extern LIB_read_bf_file_C_API 
bool MW_CALL_CONV mlxRead_bf_file(int nlhs, mxArray *plhs[], int nrhs, mxArray *prhs[]);



extern LIB_read_bf_file_C_API bool MW_CALL_CONV mlfRead_bf_file(int nargout, mxArray** ret, mxArray* filename);

#ifdef __cplusplus
}
#endif
#endif
