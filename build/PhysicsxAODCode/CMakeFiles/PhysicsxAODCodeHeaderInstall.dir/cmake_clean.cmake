file(REMOVE_RECURSE
  "../x86_64-slc6-gcc62-opt/include/PhysicsxAODCode"
  "../x86_64-slc6-gcc62-opt/python/PhysicsxAODCode/__init__.py"
  "../x86_64-slc6-gcc62-opt/include/PhysicsxAODCode"
)

# Per-language clean rules from dependency scanning.
foreach(lang )
  include(CMakeFiles/PhysicsxAODCodeHeaderInstall.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
