/*
 * MATLAB Compiler: 5.0 (R2013b)
 * Date: Wed May 11 16:22:03 2016
 * Arguments: "-B" "macro_default" "-W" "lib:read_bf_file" "-T" "link:lib"
 * "read_bf_file.m" 
 */

#include <stdio.h>
#define EXPORTING_read_bf_file 1
#include "read_bf_file.h"

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
#ifndef LIB_read_bf_file_C_API
#define LIB_read_bf_file_C_API /* No special import/export declaration */
#endif

LIB_read_bf_file_C_API 
bool MW_CALL_CONV read_bf_fileInitializeWithHandlers(
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
            mclGetEmbeddedCtfStream((void *)(read_bf_fileInitializeWithHandlers));
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

LIB_read_bf_file_C_API 
bool MW_CALL_CONV read_bf_fileInitialize(void)
{
  return read_bf_fileInitializeWithHandlers(mclDefaultErrorHandler, 
                                            mclDefaultPrintHandler);
}

LIB_read_bf_file_C_API 
void MW_CALL_CONV read_bf_fileTerminate(void)
{
  if (_mcr_inst != NULL)
    mclTerminateInstance(&_mcr_inst);
}

LIB_read_bf_file_C_API 
void MW_CALL_CONV read_bf_filePrintStackTrace(void) 
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


LIB_read_bf_file_C_API 
bool MW_CALL_CONV mlxRead_bf_file(int nlhs, mxArray *plhs[], int nrhs, mxArray *prhs[])
{
  return mclFeval(_mcr_inst, "read_bf_file", nlhs, plhs, nrhs, prhs);
}

LIB_read_bf_file_C_API 
bool MW_CALL_CONV mlfRead_bf_file(int nargout, mxArray** ret, mxArray* filename)
{
  return mclMlfFeval(_mcr_inst, "read_bf_file", nargout, 1, 1, ret, filename);
}

