// Generated by gencpp from file ur5_notebook/blocks_poses.msg
// DO NOT EDIT!


#ifndef UR5_NOTEBOOK_MESSAGE_BLOCKS_POSES_H
#define UR5_NOTEBOOK_MESSAGE_BLOCKS_POSES_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ur5_notebook
{
template <class ContainerAllocator>
struct blocks_poses_
{
  typedef blocks_poses_<ContainerAllocator> Type;

  blocks_poses_()
    : x()
    , y()
    , z()  {
    }
  blocks_poses_(const ContainerAllocator& _alloc)
    : x(_alloc)
    , y(_alloc)
    , z(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> _x_type;
  _x_type x;

   typedef std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> _y_type;
  _y_type y;

   typedef std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> _z_type;
  _z_type z;





  typedef boost::shared_ptr< ::ur5_notebook::blocks_poses_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ur5_notebook::blocks_poses_<ContainerAllocator> const> ConstPtr;

}; // struct blocks_poses_

typedef ::ur5_notebook::blocks_poses_<std::allocator<void> > blocks_poses;

typedef boost::shared_ptr< ::ur5_notebook::blocks_poses > blocks_posesPtr;
typedef boost::shared_ptr< ::ur5_notebook::blocks_poses const> blocks_posesConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ur5_notebook::blocks_poses_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ur5_notebook::blocks_poses_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ur5_notebook::blocks_poses_<ContainerAllocator1> & lhs, const ::ur5_notebook::blocks_poses_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.z == rhs.z;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ur5_notebook::blocks_poses_<ContainerAllocator1> & lhs, const ::ur5_notebook::blocks_poses_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ur5_notebook

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ur5_notebook::blocks_poses_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ur5_notebook::blocks_poses_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ur5_notebook::blocks_poses_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ur5_notebook::blocks_poses_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur5_notebook::blocks_poses_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur5_notebook::blocks_poses_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ur5_notebook::blocks_poses_<ContainerAllocator> >
{
  static const char* value()
  {
    return "615bdf149c8f78fd88df8f8f89a7e200";
  }

  static const char* value(const ::ur5_notebook::blocks_poses_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x615bdf149c8f78fdULL;
  static const uint64_t static_value2 = 0x88df8f8f89a7e200ULL;
};

template<class ContainerAllocator>
struct DataType< ::ur5_notebook::blocks_poses_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ur5_notebook/blocks_poses";
  }

  static const char* value(const ::ur5_notebook::blocks_poses_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ur5_notebook::blocks_poses_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# message type to describe 3-D position of the cylinder blocks\n"
"# variable length array, length decided by topic /current_cylinder_blocks\n"
"# to be published as a topic\n"
"\n"
"float64[] x  # x coordinate in the world\n"
"float64[] y  # y coordinate in the world\n"
"float64[] z  # z coordinate in the world\n"
;
  }

  static const char* value(const ::ur5_notebook::blocks_poses_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ur5_notebook::blocks_poses_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.z);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct blocks_poses_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ur5_notebook::blocks_poses_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ur5_notebook::blocks_poses_<ContainerAllocator>& v)
  {
    s << indent << "x[]" << std::endl;
    for (size_t i = 0; i < v.x.size(); ++i)
    {
      s << indent << "  x[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.x[i]);
    }
    s << indent << "y[]" << std::endl;
    for (size_t i = 0; i < v.y.size(); ++i)
    {
      s << indent << "  y[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.y[i]);
    }
    s << indent << "z[]" << std::endl;
    for (size_t i = 0; i < v.z.size(); ++i)
    {
      s << indent << "  z[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.z[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // UR5_NOTEBOOK_MESSAGE_BLOCKS_POSES_H
