/*
 * MATLAB Compiler: 5.0 (R2013b)
 * Date: Thu May 12 10:16:17 2016
 * Arguments: "-B" "macro_default" "-W" "lib:libaddtest" "-T" "link:lib"
 * "addtest.m" 
 */

#include <stdio.h>
#define EXPORTING_libaddtest 1
#include "libaddtest.h"

static HMCRINSTANCE _mcr_inst = NULL;


#ifdef __cplusplus
extern "C" {
#endif

static int mclDefaultPrintHandler(const char *s)
{
  return mclWrite(1 /* stdout */, s, sizeof(char)*strlen(s));
}

#ifdef __cplusplus
} /* End extern "C" block */
#endif

#ifdef __cplusplus
extern "C" {
#endif

static int mclDefaultErrorHandler(const char *s)
{
  int written = 0;
  size_t len = 0;
  len = strlen(s);
  written = mclWrite(2 /* stderr */, s, sizeof(char)*len);
  if (len > 0 && s[ len-1 ] != '\n')
    written += mclWrite(2 /* stderr */, "\n", sizeof(char));
  return written;
}

#ifdef __cplusplus
} /* End extern "C" block */
#endif

/* This symbol is defined in shared libraries. Define it here
 * (to nothing) in case this isn't a shared library. 
 */
#ifndef LIB_libaddtest_C_API
#define LIB_libaddtest_C_API /* No special import/export declaration */
#endif

LIB_libaddtest_C_API 
bool MW_CALL_CONV libaddtestInitializeWithHandlers(
    mclOutputHandlerFcn error_handler,
    mclOutputHandlerFcn print_handler)
{
    int bResult = 0;
  if (_mcr_inst != NULL)
    return true;
  if (!mclmcrInitialize())
    return false;
    {
        mclCtfStream ctfStream = 
            mclGetEmbeddedCtfStream((void *)(libaddtestInitializeWithHandlers));
        if (ctfStream) {
            bResult = mclInitializeComponentInstanceEmbedded(   &_mcr_inst,
                                                                error_handler, 
                                                                print_handler,
                                                                ctfStream);
            mclDestroyStream(ctfStream);
        } else {
            bResult = 0;
        }
    }  
    if (!bResult)
    return false;
  return true;
}

LIB_libaddtest_C_API 
bool MW_CALL_CONV libaddtestInitialize(void)
{
  return libaddtestInitializeWithHandlers(mclDefaultErrorHandler, mclDefaultPrintHandler);
}

LIB_libaddtest_C_API 
void MW_CALL_CONV libaddtestTerminate(void)
{
  if (_mcr_inst != NULL)
    mclTerminateInstance(&_mcr_inst);
}

LIB_libaddtest_C_API 
void MW_CALL_CONV libaddtestPrintStackTrace(void) 
{
  char** stackTrace;
  int stackDepth = mclGetStackTrace(&stackTrace);
  int i;
  for(i=0; i<stackDepth; i++)
  {
    mclWrite(2 /* stderr */, stackTrace[i], sizeof(char)*strlen(stackTrace[i]));
    mclWrite(2 /* stderr */, "\n", sizeof(char)*strlen("\n"));
  }
  mclFreeStackTrace(&stackTrace, stackDepth);
}


LIB_libaddtest_C_API 
bool MW_CALL_CONV mlxAddtest(int nlhs, mxArray *plhs[], int nrhs, mxArray *prhs[])
{
  return mclFeval(_mcr_inst, "addtest", nlhs, plhs, nrhs, prhs);
}

LIB_libaddtest_C_API 
bool MW_CALL_CONV mlfAddtest(int nargout, mxArray** ret, mxArray* a, mxArray* b)
{
  return mclMlfFeval(_mcr_inst, "addtest", nargout, 1, 2, ret, a, b);
}

