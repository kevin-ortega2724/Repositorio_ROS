execute_process(COMMAND "/home/ko/ur_ws/build/hrl-kdl/pykdl_utils/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/ko/ur_ws/build/hrl-kdl/pykdl_utils/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
