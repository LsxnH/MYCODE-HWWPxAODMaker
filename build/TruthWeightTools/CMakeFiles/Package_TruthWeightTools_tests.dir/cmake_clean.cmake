file(REMOVE_RECURSE
  "../x86_64-slc6-gcc62-opt/include/TruthWeightTools"
  "../x86_64-slc6-gcc62-opt/python/TruthWeightTools/__init__.py"
  "../x86_64-slc6-gcc62-opt/data/TruthWeightTools/VBF_weights.xml"
  "../x86_64-slc6-gcc62-opt/data/TruthWeightTools/VH_weights.xml"
  "../x86_64-slc6-gcc62-opt/data/TruthWeightTools/ggF_NNLOPS_weights.XMLOLD"
  "../x86_64-slc6-gcc62-opt/data/TruthWeightTools/ggF_NNLOPS_weights.xml"
  "../x86_64-slc6-gcc62-opt/data/TruthWeightTools/ttH_weights.xml"
)

# Per-language clean rules from dependency scanning.
foreach(lang )
  include(CMakeFiles/Package_TruthWeightTools_tests.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()