// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME TruthWeightToolsDictReflexDict

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "RConfig.h"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// Since CINT ignores the std namespace, we need to do so in this file.
namespace std {} using namespace std;

// Header files passed as explicit arguments
#include "/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/TruthWeightTools/TruthWeightTools/TruthWeightToolsDict.h"

// Header files passed via #pragma extra_include

namespace ROOT {
   static TClass *TruthWeightToolscLcLIHiggsWeightTool_Dictionary();
   static void TruthWeightToolscLcLIHiggsWeightTool_TClassManip(TClass*);
   static void delete_TruthWeightToolscLcLIHiggsWeightTool(void *p);
   static void deleteArray_TruthWeightToolscLcLIHiggsWeightTool(void *p);
   static void destruct_TruthWeightToolscLcLIHiggsWeightTool(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::TruthWeightTools::IHiggsWeightTool*)
   {
      ::TruthWeightTools::IHiggsWeightTool *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::TruthWeightTools::IHiggsWeightTool));
      static ::ROOT::TGenericClassInfo 
         instance("TruthWeightTools::IHiggsWeightTool", "IHiggsWeightTool.h", 21,
                  typeid(::TruthWeightTools::IHiggsWeightTool), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &TruthWeightToolscLcLIHiggsWeightTool_Dictionary, isa_proxy, 4,
                  sizeof(::TruthWeightTools::IHiggsWeightTool) );
      instance.SetDelete(&delete_TruthWeightToolscLcLIHiggsWeightTool);
      instance.SetDeleteArray(&deleteArray_TruthWeightToolscLcLIHiggsWeightTool);
      instance.SetDestructor(&destruct_TruthWeightToolscLcLIHiggsWeightTool);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::TruthWeightTools::IHiggsWeightTool*)
   {
      return GenerateInitInstanceLocal((::TruthWeightTools::IHiggsWeightTool*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::TruthWeightTools::IHiggsWeightTool*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *TruthWeightToolscLcLIHiggsWeightTool_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::TruthWeightTools::IHiggsWeightTool*)0x0)->GetClass();
      TruthWeightToolscLcLIHiggsWeightTool_TClassManip(theClass);
   return theClass;
   }

   static void TruthWeightToolscLcLIHiggsWeightTool_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *TruthWeightToolscLcLHiggsWeightTool_Dictionary();
   static void TruthWeightToolscLcLHiggsWeightTool_TClassManip(TClass*);
   static void delete_TruthWeightToolscLcLHiggsWeightTool(void *p);
   static void deleteArray_TruthWeightToolscLcLHiggsWeightTool(void *p);
   static void destruct_TruthWeightToolscLcLHiggsWeightTool(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::TruthWeightTools::HiggsWeightTool*)
   {
      ::TruthWeightTools::HiggsWeightTool *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::TruthWeightTools::HiggsWeightTool));
      static ::ROOT::TGenericClassInfo 
         instance("TruthWeightTools::HiggsWeightTool", "HiggsWeightTool.h", 23,
                  typeid(::TruthWeightTools::HiggsWeightTool), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &TruthWeightToolscLcLHiggsWeightTool_Dictionary, isa_proxy, 4,
                  sizeof(::TruthWeightTools::HiggsWeightTool) );
      instance.SetDelete(&delete_TruthWeightToolscLcLHiggsWeightTool);
      instance.SetDeleteArray(&deleteArray_TruthWeightToolscLcLHiggsWeightTool);
      instance.SetDestructor(&destruct_TruthWeightToolscLcLHiggsWeightTool);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::TruthWeightTools::HiggsWeightTool*)
   {
      return GenerateInitInstanceLocal((::TruthWeightTools::HiggsWeightTool*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::TruthWeightTools::HiggsWeightTool*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *TruthWeightToolscLcLHiggsWeightTool_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::TruthWeightTools::HiggsWeightTool*)0x0)->GetClass();
      TruthWeightToolscLcLHiggsWeightTool_TClassManip(theClass);
   return theClass;
   }

   static void TruthWeightToolscLcLHiggsWeightTool_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrapper around operator delete
   static void delete_TruthWeightToolscLcLIHiggsWeightTool(void *p) {
      delete ((::TruthWeightTools::IHiggsWeightTool*)p);
   }
   static void deleteArray_TruthWeightToolscLcLIHiggsWeightTool(void *p) {
      delete [] ((::TruthWeightTools::IHiggsWeightTool*)p);
   }
   static void destruct_TruthWeightToolscLcLIHiggsWeightTool(void *p) {
      typedef ::TruthWeightTools::IHiggsWeightTool current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::TruthWeightTools::IHiggsWeightTool

namespace ROOT {
   // Wrapper around operator delete
   static void delete_TruthWeightToolscLcLHiggsWeightTool(void *p) {
      delete ((::TruthWeightTools::HiggsWeightTool*)p);
   }
   static void deleteArray_TruthWeightToolscLcLHiggsWeightTool(void *p) {
      delete [] ((::TruthWeightTools::HiggsWeightTool*)p);
   }
   static void destruct_TruthWeightToolscLcLHiggsWeightTool(void *p) {
      typedef ::TruthWeightTools::HiggsWeightTool current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::TruthWeightTools::HiggsWeightTool

namespace {
  void TriggerDictionaryInitialization_libTruthWeightToolsDict_Impl() {
    static const char* headers[] = {
0    };
    static const char* includePaths[] = {
0
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "libTruthWeightToolsDict dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_Autoloading_Map;
namespace TruthWeightTools{class __attribute__((annotate("$clingAutoload$IHiggsWeightTool.h")))  IHiggsWeightTool;}
namespace TruthWeightTools{class __attribute__((annotate("$clingAutoload$HiggsWeightTool.h")))  HiggsWeightTool;}
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "libTruthWeightToolsDict dictionary payload"

#ifndef G__VECTOR_HAS_CLASS_ITERATOR
  #define G__VECTOR_HAS_CLASS_ITERATOR 1
#endif
#ifndef HAVE_PRETTY_FUNCTION
  #define HAVE_PRETTY_FUNCTION 1
#endif
#ifndef HAVE_64_BITS
  #define HAVE_64_BITS 1
#endif
#ifndef __IDENTIFIER_64BIT__
  #define __IDENTIFIER_64BIT__ 1
#endif
#ifndef ATLAS
  #define ATLAS 1
#endif
#ifndef GAUDI_V20_COMPAT
  #define GAUDI_V20_COMPAT 1
#endif
#ifndef ATLAS_GAUDI_V21
  #define ATLAS_GAUDI_V21 1
#endif
#ifndef HAVE_GAUDI_PLUGINSVC
  #define HAVE_GAUDI_PLUGINSVC 1
#endif
#ifndef XAOD_ANALYSIS
  #define XAOD_ANALYSIS 1
#endif
#ifndef ROOTCORE_RELEASE_SERIES
  #define ROOTCORE_RELEASE_SERIES 25
#endif
#ifndef PACKAGE_VERSION
  #define PACKAGE_VERSION "TruthWeightTools-00-00-00"
#endif
#ifndef PACKAGE_VERSION_UQ
  #define PACKAGE_VERSION_UQ TruthWeightTools-00-00-00
#endif
#ifndef EIGEN_DONT_VECTORIZE
  #define EIGEN_DONT_VECTORIZE 1
#endif

#define _BACKWARD_BACKWARD_WARNING_H
#ifndef TRUTHWEIGHTTOOLS_TRUTHWEIGHTTOOLSDICT
#define TRUTHWEIGHTTOOLS_TRUTHWEIGHTTOOLSDICT

#include "IHiggsWeightTool.h"
#include "HiggsWeightTool.h"

#endif
#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[]={
"TruthWeightTools::HiggsWeightTool", payloadCode, "@",
"TruthWeightTools::IHiggsWeightTool", payloadCode, "@",
nullptr};

    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("libTruthWeightToolsDict",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_libTruthWeightToolsDict_Impl, {}, classesHeaders);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_libTruthWeightToolsDict_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_libTruthWeightToolsDict() {
  TriggerDictionaryInitialization_libTruthWeightToolsDict_Impl();
}
