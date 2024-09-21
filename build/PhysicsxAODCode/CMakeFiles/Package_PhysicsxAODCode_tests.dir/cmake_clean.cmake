file(REMOVE_RECURSE
  "../x86_64-slc6-gcc62-opt/include/PhysicsxAODCode"
  "../x86_64-slc6-gcc62-opt/python/PhysicsxAODCode/__init__.py"
)

# Per-language clean rules from dependency scanning.
foreach(lang )
  include(CMakeFiles/Package_PhysicsxAODCode_tests.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
