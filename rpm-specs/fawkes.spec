%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Architectures from OpenNI spec file
%ifarch %{ix86} x86_64 %{arm}
%define have_openni 1
%endif
# Package not yet available on Fedora
# define have_openprs 1
# RHEL does not have some of the prerequisites
%if ! 0%{?rhel}
%define have_clips 1
%define have_gazebo 1
%define have_xmlrpc 1
%define have_kdl 1
%else
%define have_clips 0
%define have_gazebo 0
%define have_xmlrpc 0
%define have_kdl 0
%endif

%define have_player 0

%bcond_with mongodb
%bcond_with festival
%bcond_with ros


%global plugin_dir %{_libdir}/fawkes/plugins
%global interface_dir %{_libdir}/fawkes/interfaces
%global protobuf_dir %{_libdir}/fawkes/protobuf
%global gazebo_dir %{_libdir}/fawkes/gazebo
%global luamod_dir %{_libdir}/fawkes/lua
%global openprs_dir %{_libdir}/fawkes/openprs

%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{plugin_dir}|%{gazebo_dir}|%{luamod_dir}|%{openprs_dir}

%define include_req_spec() %{expand:%(sed -e 's/^R/%2: /g' %1)}

Name:           fawkes
Version:        1.3.0
Release:        13%{?dist}
Summary:        Robot Software Framework

License:        GPLv2+ and GPLv2+ with exceptions
URL:            https://www.fawkesrobotics.org
Source0:        https://github.com/fawkesrobotics/fawkes/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        build_requires.txt
Source2:        meta_requires.txt
Patch0:         fawkes.freeglut.patch
Patch1:         fawkes.cgal-header-only.patch
# Bump version to 1.3.0 (commit is missing from 1.3 release)
Patch2:         fawkes.version-1.3.patch
Patch3:		fawkes.gcc10.patch

%{include_req_spec %{SOURCE1} BuildRequires}

# s390(x) doesn't FireWire and other necessary parts
ExcludeArch:    s390 s390x

# The base package is a meta package pulling in other packages
%{include_req_spec %{SOURCE2} Requires}

%description
Fawkes is a component-based software framework for robotic real-time
applications for various platforms and domains.

It was developed for cognitive robotics real-time applications like soccer
and service robotics and supports fast information exchange and efficient
combination and coordination of different components to suit the needs of
mobile robots operating in uncertain environments.

Install this meta package to get a useful Fawkes base system.

%package        core
Summary:        Fawkes base system

%description    core
This package contains the Fawkes base libraries, interfaces and programs.
This package allows to run a basic Fawkes instance, but does not provide
much functionality. Install the requires plugins. The fawkes meta package
allows for installing a useful base set.

%package        devel
Summary:        Development files for Fawkes
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        devenv
Summary:        Development environment Fawkes
# All build requires are requirements for the development environment
%{include_req_spec %{SOURCE1} Requires}
# Additional packages required to build with even more dependencies,
# most notably with ROS and OpenRAVE support.
Requires:       ccache, cmake, hostname
Requires:       git, gitk, screen
Requires:       python3-pyyaml, libxml2-devel, python3-libxml2
Requires:       poco-devel, bzip2-devel, tbb-devel, log4cxx-devel
Requires:       python3-setuptools, python3-numpy, python3-pyopengl, python3-collada, python3-empy
Requires:       python3-sip-devel, python3-netifaces
Requires:       compat-lua, emacs-lua, clips-emacs
Requires:       libmodbus-devel 
Requires:       qt-devel, fltk-devel
%if %{with mongodb}
Requires:       mongodb-server
%endif
%if %{with ros}
Requires:       ros-release, python3-rospkg, console-bridge-devel
Requires:       rospack, rospack-devel, python3-rosdistro, python3-rosinstall
Requires:       python3-rosinstall_generator, python3-wstool, python3-rosdep, python3-rosdistro
%endif
Requires:       python-qt5-devel, python3-qt5-devel, python3-defusedxml
%if 0%{?have_openni} >= 1
Requires:       openni-primesense
%endif

%description    devenv
The %{name}-devenv packages causes the installation of all dependencies
to develop Fawkes in-tree (e.g. cloned from git repository).

%package        doc
Summary:        Fawkes API documentation
%if ! 0%{?rhel} || 0%{?rhel} >= 6
%ifnarch ppc ppc64
BuildArch:      noarch
%endif
%endif
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the full API documentation for Fawkes.

%package        firevision
Summary:        Computer vision sub-system
%description    firevision
This package contains the Fawkes vision system named FireVision. It contains
the libraries and tools used to build image processing pipelines.

%package        firevision-tools
Summary:        Computer vision sub-system tools
%description    firevision-tools
This package contains the console tools for FireVision.

%package        guis
Summary:        GUI applications to control Fawkes
Requires:       %{name}-firevision = %{version}-%{release}
%description    guis
This package contains a GUI application which are used to remotely control
Fawkes.

%package        lua
Summary:        Lua libraries and scripts for Fawkes
%description    lua
This package contains libraries to enable Lua usage from Fawkes as well as
common Lua modules.

%package        protobuf
Summary:        Google protobuf libraries and integration for Fawkes
%description    protobuf
This package contains libraries to communicate over the network using
protobuf-encoded messages.

%package        plugin-amcl
Summary:        Fawkes plugin providing adaptive Monte Carlo Localization
%description    plugin-amcl
This package contains a Fawkes plugin to self-localize a robot using
Adaptive Monte Carlo Localization (AMCL).

%package        plugin-bblogger
Summary:        Fawkes plugin to log data from blackboard
%description    plugin-bblogger
This package contains a Fawkes plugin to log data written to the blackboard.

%package        plugin-bbsync
Summary:        Fawkes plugin to synchronize multiple instances
%description    plugin-bbsync
This package contains a Fawkes plugin to synchronize multiple Fawkes
instances, for example running on multiple robots.

%package        plugin-cedar
Summary:        Fawkes plugin for system status monitoring
%description    plugin-cedar
This package contains a Fawkes plugin for system status monitoring.

%if 0%{?have_clips}
%package        plugin-clips
Summary:        Fawkes plugin providing CLIPS environments
%description    plugin-clips
This package contains a Fawkes plugin that provides CLIPS environments
to other plugins.

%package        plugin-clips-agent
Summary:        Fawkes plugin to run a CLIPS-based agent
Requires:       %{name}-plugin-clips = %{version}-%{release}
%description    plugin-clips-agent
This package contains a Fawkes plugin that provides a CLIPS-based
framework for specifying a task-level reasoner and an executive.

%package        plugin-clips-executive
Summary:        Fawkes plugin to run the Clips Executive
Requires:       %{name}-plugin-clips = %{version}-%{release}
Recommends:     %{name}-plugin-clips-protobuf = %{version}-%{release}
Recommends:     %{name}-plugin-clips-tf = %{version}-%{release}
Recommends:     %{name}-plugin-clips-robot-memory = %{version}-%{release}
%description    plugin-clips-executive
This package contains a Fawkes plugin that runs the CLIPS Executive.

%package        plugin-clips-navgraph
Summary:        Fawkes plugin to provide the CLIPS navgraph feature
Requires:       %{name}-plugin-clips = %{version}-%{release}
%description    plugin-clips-navgraph
This package contains a Fawkes plugin that provides navgraph access
in CLIPS contexts.

%package        plugin-clips-pddl-parser
Summary:        Fawkes plugin to parse PDDL from CLIPS
Requires:       %{name}-plugin-clips = %{version}-%{release}
%description    plugin-clips-pddl-parser
This package contains a Fawkes plugin that allows PDDL parsing from within CLIPS.

%package        plugin-clips-protobuf
Summary:        Fawkes plugin to access protobuf messages from CLIPS
Requires:       %{name}-plugin-clips = %{version}-%{release}
Requires:       %{name}-protobuf = %{version}-%{release}
%description    plugin-clips-protobuf
This package contains a Fawkes plugin that provides access to protobuf
messaging from within CLIPS.

%if %{with mongodb}
%package        plugin-clips-robot-memory
Summary:        Fawkes plugin to access robot memory from CLIPS
Requires:       %{name}-robot-memory = %{version}-%{release}
%description    plugin-clips-robot-memory
This package contains a Fawkes plugin that allows accessing robot memory from
within CLIPS.
%endif

%package        plugin-clips-tf
Summary:        Fawkes plugin to access coordinate transforms from CLIPS
Requires:       %{name}-plugin-clips = %{version}-%{release}
%description    plugin-clips-tf
This package contains a Fawkes plugin that provides access to coordinate
transforms from within CLIPS.
%endif

%package        plugin-colli
Summary:        Fawkes plugin for local path planning with collision avoidance
%description    plugin-colli
This package contains a Fawkes plugin that provides an A*-based local
planner with collision avoidance based on 2D laser data.

%package        plugin-dynamixel
Summary:        Fawkes plugin generic access to Dynamixel servos
%description    plugin-dynamixel
This package contains a Fawkes plugin that provides blackboard
interfaces for any number of Dynamixel servos.

%if %{with festival}
%package        plugin-festival
Summary:        Fawkes Festival speech synthesis plugin
%description    plugin-festival
This package contains a Fawkes plugin that integrates the Festival speech
synthesis engine.
%endif

%package        plugin-flite
Summary:        Fawkes Flite speech synthesis plugin
%description    plugin-flite
This package contains a Fawkes plugin that integrates the flite speech
synthesis engine.

%if 0%{?have_gazebo}
%package        plugin-gazebo
Summary:        Fawkes plugin for Gazebo simulation integration
%description    plugin-gazebo
This package contains a Fawkes plugin that provides basic access to a
Gazebo-based simulation environment.

%package        plugin-gazsim-comm
Summary:        Fawkes plugin to simulate network communication
%description    plugin-gazsim-comm
This package contains a Fawkes plugin that allows to proxy any number
of protobuf_comm-based communication channels with configurable packet
loss.

%package        plugin-gazsim-depthcam
Summary:        Fawkes plugin to simulate a depth camera
%description    plugin-gazsim-depthcam
This package contains a Fawkes plugin to access a depth camera in
a Gazebo-based simulation.

%package        plugin-gazsim-laser
Summary:        Fawkes plugin to simulate a laser range finder
%description    plugin-gazsim-laser
This package contains a Fawkes plugin to access laser range finder
data from a Gazebo-based simulation.

%package        plugin-gazsim-localization
Summary:        Fawkes plugin to provide localization data
%description    plugin-gazsim-localization
This package contains a Fawkes plugin to access positions from objects
based on the position of their respective model in a Gazebo-based
simulation.

%package        plugin-gazsim-robotino
Summary:        Fawkes plugin to simulate Robotino robot
%description    plugin-gazsim-robotino
This package contains a Fawkes plugin to access a Robotino simulated
in Gazebo (using gazebo-rcll).

%package        plugin-gazsim-timesource
Summary:        Fawkes plugin to use simulation time
%description    plugin-gazsim-timesource
This package contains a Fawkes plugin to replace the system clock with
a simulated one from Gazebo.

%package        plugin-gazsim-vis-localization
Summary:        Fawkes plugin to visualize localization info
%description    plugin-gazsim-vis-localization
This package contains a Fawkes plugin that shows a little circle indicating
a robot's current belief about its position.

%package        plugin-gazsim-webcam
Summary:        Fawkes plugin to provide images from simulated webcam
%description    plugin-gazsim-webcam
This package contains a Fawkes plugin to access image data from a simulated
webcam in Gazebo.
%endif

%package        plugin-gossip
Summary:        Fawkes plugin for Gossip communication
%description    plugin-gossip
This package contains a Fawkes plugin to enable Gossip-based
communication based on protobuf_comm.

%package        plugin-imu
Summary:        Fawkes plugin for access IMU sensors
%description    plugin-imu
This package contains a Fawkes plugin to access inertia measurement
units (IMU). In particular, this plugins supports the Cruizcore XG1010.

%package        plugin-jaco
Summary:        Fawkes plugin to access a Kinova Jaco arm
%description    plugin-jaco
This package contains a Fawkes plugin to access Kinova Jaco robotic
arms.

%package        plugin-joystick
Summary:        Fawkes plugin to access joysticks
%description    plugin-joystick
This package contains a Fawkes plugin to access joysticks, e.g. for
remotely controlling robots.

%package        plugin-joystick-teleop
Summary:        Fawkes plugin to move a robot by joystick
%description    plugin-joystick-teleop
This package contains a Fawkes plugin to map joystick inputs to
locomotion commands.

%package        plugin-katana
Summary:        Fawkes plugin to control the Katana robot arm
%description    plugin-katana
This package contains a Fawkes plugin to access and control the Katana
robot arm.

%package        plugin-laser
Summary:        Fawkes plugin to access laser range finders
%description    plugin-laser
This package contains a Fawkes plugin to access laser range finders
like the Hokuyo URG.

%package        plugin-laser-cluster
Summary:        Fawkes plugin to extract clusters from laser data
%description    plugin-laser-cluster
This package contains a Fawkes plugin to extract configurable
euclidean clusters from 2D laser range finder data.

%package        plugin-laser-filter
Summary:        Fawkes plugin providing laser data filtering
%description    plugin-laser-filter
This package contains a Fawkes plugin to setup filter cascades for
laser scanner data, for example to merge multiple lasers or project
a laser to a horizontal plane.

%package        plugin-laser-lines
Summary:        Fawkes plugin to extract lines from laser data
Obsoletes:      %{name}-plugin-laserht < 1.0.0
%description    plugin-laser-lines
This package contains a Fawkes plugin to extract lines from 2D
laser range finder data.

%package        plugin-laser-pointclouds
Summary:        Fawkes plugin to convert laser data to point clouds
%description    plugin-laser-pointclouds
This package contains a Fawkes plugin to convert laser data to 3D
point clouds.

%package        plugin-luaagent
Summary:        Agent framework written in Lua
Requires:       %{name}-lua = %{version}-%{release}
%description    plugin-luaagent
This package contains a Fawkes plugin which provides an agent
framework to write agents in Lua.

%package        plugin-map-lasergen
Summary:        Fawkes plugin to generate fake laser data
%description    plugin-map-lasergen
This package contains a Fawkes plugin that takes a map and generates a
laser scan that the robot would perceive when being at a given
location in the map. It can optionally add gaussian noise. Useful for
testing localization under idealized conditions or just having a fake
localization.

%if %{with mongodb}
%package        plugin-mongodb
Summary:        Fawkes plugin to access MongoDB databases
%description    plugin-mongodb
This package contains a Fawkes plugin that provides an aspect
to access MongoDB databases from within plugins.

%package        plugin-mongodb-log
Summary:        Fawkes plugin to log data to MongoDB
%description    plugin-mongodb-log
This package contains a Fawkes plugin that can log data from the
blackboard and other sources to a MongoDB database.

%package        plugin-mongodb-rrd
Summary:        Fawkes plugin to generate MongoDB performance data
%description    plugin-mongodb-rrd
This package contains a Fawkes plugin that monitors a MongoDB database
and writes performance data to an RRD.
%endif

%package        plugin-navgraph
Summary:        Fawkes plugin for a 2D navigation graph
%description    plugin-navgraph
This package contains a Fawkes plugin that maintains a 2D topological
graph for global path planning and augmentation with relevant information.

%package        plugin-navgraph-clusters
Summary:        Fawkes plugin to convert clusters to obstacles
%description    plugin-navgraph-clusters
This package contains a Fawkes plugin that uses clusters (e.g., detected
by laser-cluster) to update the graph costs or blocked edges.

%package        plugin-navgraph-generator
Summary:        Fawkes plugin to generate a navgraph from POIs
%description    plugin-navgraph-generator
This package contains a Fawkes plugin that provides an interface to
create a navgraph based on given obstacles and points of interests.

%package        plugin-navgraph-static-constraints
Summary:        Fawkes plugin to apply static constraints on navgraph
%description    plugin-navgraph-static-constraints
This package contains a Fawkes plugin that allows to specify constraints
for a navgraph which are applied statically.

%package        plugin-openni
Summary:        Fawkes plugin providing access to OpenNI
%description    plugin-openni
This package contains a Fawkes plugin integrates OpenNI and provides
access to the framework.

%if 0%{?have_openni} >= 1
%package        plugin-openni-data
Summary:        Fawkes plugin for data acquisition using OpenNI
Requires:       fawkes-plugin-openni
%description    plugin-openni-data
This package contains a Fawkes plugin uses OpenNI to acquire data like
color and depth images and 3D point clouds from sensors like the Kinect.

%package        plugin-openni-handtracker
Summary:        Fawkes plugin to track hands using OpenNI
Requires:       fawkes-plugin-openni
%description    plugin-openni-handtracker
This package contains a Fawkes plugin uses OpenNI to acquire data like
color and depth images and 3D point clouds from sensors like the Kinect.
Note that this plugin requires the proprietary OpenNI tracking software
or equivalent to be installed and working with OpenNI.

%package        plugin-openni-pcl-frombuf
Summary:        Fawkes plugin to create point clouds from FireVision buffer
Requires:       fawkes-plugin-openni
%description    plugin-openni-pcl-frombuf
This package contains a Fawkes plugin reads a FireVision buffer and creates
a point cloud from it. This can be used for example to split acquisition
and processing in separate Fawkes instances.

%package        plugin-openni-usertracker
Summary:        Fawkes plugin to track humans using OpenNI
Requires:       fawkes-plugin-openni
%description    plugin-openni-usertracker
This package contains a Fawkes plugin uses OpenNI to detect and track
humans in front of a sensor like the Kinect.
Note that this plugin requires the proprietary OpenNI tracking software
or equivalent to be installed and working with OpenNI.
%endif

%if 0%{?have_openprs} >= 1
%package        plugin-openprs
Summary:        Fawkes plugin with OpenPRS framework
%description    plugin-openprs
This package contains a Fawkes plugin to create OpenPRS-based
task-level executives.

%package        plugin-openprs-agent
Summary:        Fawkes plugin with OpenPRS task-level executive
%description    plugin-openprs-agent
This package contains a Fawkes plugin to run an OpenPRS
task-level executive.

%package        plugin-openprs-example
Summary:        Fawkes plugin with OpenPRS example
%description    plugin-openprs-example
This package contains a Fawkes plugin with an OpenPRS example.
%endif

%package        plugin-pantilt
Summary:        Fawkes plugin to control pan-tilt units
%description    plugin-pantilt
This package contains a Fawkes plugin to access and control various
pan-tilt units, for example the DirectedPerception PTU, the Sony Evi-D
(and others based on the Visca protocol) and custom-made with Robotis
RX-28 servos.

%if %{with mongodb}
%package        plugin-pcl-db
Summary:        Fawkes plugins to store and retrieve pointclouds from MongoDB
%description    plugin-pcl-db
This package contains a Fawkes plugin to store, retrieve, and merge
pointclouds in MongoDB.
%endif

%if 0%{?have_player}
%package        plugin-player
Summary:        Integration of Player framework
%description    plugin-player
This package contains a Fawkes plugin which integrates Fawkes with the
Player robot software framework.
%endif

%package        plugin-realsense
Summary:        Fawkes plugin to use older Intel RealSense cameras
%description    plugin-realsense
This package contains a Fawkes plugin that adds support for fetching RGB/D
images from an Intel RealSense camera, using the legacy librealsense1 for oler
cameras.

%package        plugin-realsense2
Summary:        Fawkes plugin to use newer Intel RealSense cameras
%description    plugin-realsense2
This package contains a Fawkes plugin that adds support for fetching RGB/D
images from an Intel RealSense camera, using librealsense2 for newer RealSense
cameras.

%package        plugin-refboxcomm
Summary:        RoboCup referee box integration
%description    plugin-refboxcomm
This package contains a Fawkes plugin which listens to messages from the
RoboCup Middle-Size League (MSL) referee box (refbox) or the Standard
Platform League (SPL) GameController.

%package        plugin-robotino
Summary:        Fawkes driver for the Festo Robotino
%description    plugin-robotino
This package contains a Fawkes plugin to access hardware of the
Festo Robotino robot platform.

%package        plugin-robotino-ir-pcl
Summary:        Fawkes plugin for Robotino IR data as pointcloud
%description    plugin-robotino-ir-pcl
This package contains a Fawkes plugin that creates a pointcloud from
the Robotino's infrared distance sensor data.

%if %{with mongodb}
%package        plugin-robot-memory
Summary:        Fawkes plugin for a mongodb-based world model storage
Requires:       fawkes-plugin-mongodb = %{version}-%{release}
%description    plugin-robot-memory
This package contains a Fawkes plugin for a mongodb-based world model storage.
%endif

%package        plugin-robot-state-publisher
Summary:        Fawkes plugin to publish transforms based on model
%description    plugin-robot-state-publisher
This package contains a Fawkes plugin publishes transforms given a
robot model and joint angles.

%package        plugin-roomba
Summary:        Fawkes plugin to control a Roomba
%description    plugin-roomba
This package contains a Fawkes plugin that connects to a Roomba using
a USB or Bluetooth connection (RooStick or RooTooth). The also included
roombajoy plugin can be used to remote-control the Roomba.

%package        plugin-rrd
Summary:        Fawkes plugin providing tools to create RRD graphs
%description    plugin-rrd
This package contains a Fawkes plugin which provides access to RRDtool
from within Fawkes plugins.

%package        plugin-skiller
Summary:        Fawkes behavior engine plugin
Requires:       %{name}-lua = %{version}-%{release}
%description    plugin-skiller
This package contains a Fawkes plugin implementing a Lua-based behavior
engine for writing control programs for robots.

%package        plugin-skiller-simulator
Summary:        Fawkes plugin to simulate skill execution
Requires:       %{name}-lua = %{version}-%{release}
%description    plugin-skiller-simulator
This package contains a Fawkes plugin that simulates skill execution and
thereby allows simulating everything but the high-level decision making.

%package        plugin-static-transforms
Summary:        Fawkes plugin to publish static transforms
%description    plugin-static-transforms
This package contains a Fawkes plugin that reads static coordinate frame
transformations from the config file and periodically publishes them.

%package        plugin-tabletop-objects
Summary:        Fawkes plugin for table top scene analysis on 3D point clouds
%description    plugin-tabletop-objects
This package contains a Fawkes plugin that uses 3D point clouds to detect
objects on a tabletop plane.

%package        plugin-ttmainloop
Summary:        Time tracking main loop
%description    plugin-ttmainloop
This package contains a Fawkes plugin which replaces the default main loop
which one that operates similarly but outputs timing information at regular
intervals.

%package        plugin-webview
Summary:        Fawkes polugin to provide a web interface
%description    plugin-webview
This package contains a Fawkes plugin which provides a web interface to view
log messages, manage plugins, inspect the Clips Executive, and inspect
blackboard data.

%if 0%{?have_xmlrpc}
%package        plugin-xmlrpc
Summary:        XML-RPC communication plugin
%description    plugin-xmlrpc
This package contains a Fawkes plugin which enables communication with
Fawkes via XML-RPC. This is for demonstration purposes and has only limited
functionality.
%endif


%prep
%autosetup -p1 -n %{name}-%{version}

%build
%define feature_flags HAVE_ROS=0 HAVE_OPENRAVE=0 %{!?have_openni:HAVE_OPENNI=0} %{!?have_openprs: HAVE_OPENPRS=0}
%ifarch x86_64 aarch64 ppc64 ppc64le
%global libbits LIBBITS=64
%endif
make uncolored-switch-buildtype-sysinstall
make uncolored-all uncolored-gui CFLAGS_EXT="%{optflags}" PREFIX=%{_prefix} \
     VERBOSE=1 %{feature_flags} %{?libbits} %{?_smp_mflags}
# Ignore documentation errors until fresh doxygen release hits build machines.
# Doxygen 1.7.1 is totally buggy and reports hundreds of false positives.
make uncolored-apidoc || true

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} EXEC_DOCDIR=%{_pkgdocdir} %{feature_flags} %{?libbits}
install -pm 644 README.md doc/DEPENDENCIES doc/LICENSE.* %{buildroot}%{_pkgdocdir}

# We do not package OpenRAVE, yet.
rm -f %{buildroot}%{interface_dir}/libOpenRaveInterface*
rm -f %{buildroot}%{luamod_dir}/interfaces/OpenRaveInterface*
rm -f %{buildroot}%{_libdir}/libfawkesopenraveaspect.so*

# PLEXIL is not packaged for Fedora, remove the config file, useless without the plugin
rm -rf %{buildroot}%{_sysconfdir}/%{name}/plexil

# Use xargs instead of exec to abort the build on desktop-file-validate fail
find %{buildroot}%{_datadir}/applications -name '*.desktop' | xargs -L 1 desktop-file-validate

ls src/libs/interfaces/*.xml | sed -e "s|^src/libs/interfaces/\([^.]\+\)\.xml|%{interface_dir}/lib\1.so*|" > builtin-interfaces.files
ls src/libs/interfaces/*.xml | sed -e "s|^src/libs/interfaces/\([^.]\+\)\.xml|%{luamod_dir}/interfaces/\1.so|" > builtin-interfaces-lua.files

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/fawkes/protobuf > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

# Required to avoid .objs_* and .deps_* dirs in debuginfo package
make clean %{?_smp_mflags}


%files

%files core -f builtin-interfaces.files
%dir %{_pkgdocdir}
%{_pkgdocdir}/README.md
%{_pkgdocdir}/LICENSE.*
%dir %{_sysconfdir}/%{name}
%dir %{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config.yaml
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/*.yaml
%config %{_sysconfdir}/%{name}/examples
%config %{_sysconfdir}/%{name}/navgraph-example.yaml
%config %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
%{_bindir}/fawkes
%{_bindir}/ffconfig
%{_bindir}/ffgenplugin
%{_bindir}/ffinfo
%{_bindir}/ffkbjoystick
%{_bindir}/fflogview
%{_bindir}/ffplugin
%{_bindir}/ffset_pose
%{_bindir}/ffbb2calib
%{_bindir}/laser_calibration
%{_bindir}/pddl_parser
%dir %{_libdir}/%{name}
%dir %{plugin_dir}
%dir %{interface_dir}
#{_libdir}/{name}/interfaces/*.so*
%{_libdir}/libfawkesaspects.so.*
%{_libdir}/libfawkesbaseapp.so.*
%{_libdir}/libfawkesblackboard.so.*
%{_libdir}/libfawkesconfig.so.*
%{_libdir}/libfawkescore.so.*
%{_libdir}/libfawkesinterface.so.*
%{_libdir}/libfawkeslogging.so.*
%{_libdir}/libfawkesnetcomm.so.*
%{_libdir}/libfawkesnetworklogger.so.*
%{_libdir}/libfawkespddl_parser.so.*
%{_libdir}/libfawkesplugin.so.*
%{_libdir}/libfawkessyncpoint.so.*
%{_libdir}/libfawkestf.so.*
%{_libdir}/libfawkesutils.so.*
%{_libdir}/libfawkespcl_utils.so.*
%if 0%{?have_kdl}
%{_libdir}/libfawkeskdl_parser.so.*
%endif
%{interface_dir}/libHumanSkeletonProjectionInterface.so*
%{interface_dir}/libNaoJointPositionInterface.so*
%{interface_dir}/libNaoJointStiffnessInterface.so*
%{interface_dir}/libNaoSensorInterface.so*
%{interface_dir}/libOpenCVStereoParamsInterface.so*
%{_mandir}/man8/fawkes.8*
%{_mandir}/man1/ffinfo.1*
%{_mandir}/man1/ffconfig.1*
%{_mandir}/man1/ffgenplugin.1*
%{_mandir}/man1/ffplugin.1*
%{_mandir}/man1/fflogview.1*
%{_mandir}/man1/ffset_pose.1*
%{_mandir}/man1/ffkbjoystick.1*

%files firevision
%{_libdir}/libfvcams.so.*
%{_libdir}/libfvclassifiers.so.*
%{_libdir}/libfvfilters.so.*
%{_libdir}/libfvmodels.so.*
%{_libdir}/libfvstereo.so.*
%{_libdir}/libfvutils.so.*
%{plugin_dir}/fvbase.so
%{plugin_dir}/fvfountain.so
%{plugin_dir}/fvretriever.so

%files firevision-tools
%{_bindir}/fvbb2gettric
%{_bindir}/fvbb2info
%{_bindir}/fvbb2rectlut
%{_bindir}/fvcmpp
%{_bindir}/fvconverter
%{_bindir}/fvlistfwcams
#{_bindir}/fvlistsrcams
%{_bindir}/fvnet
%{_bindir}/fvshmem
%{_bindir}/fvstereodecoder
%{_mandir}/man1/fvbb2gettric.1*
%{_mandir}/man1/fvbb2info.1*
%{_mandir}/man1/fvbb2rectlut.1*
%{_mandir}/man1/fvcmpp.1*
%{_mandir}/man1/fvconverter.1*
%{_mandir}/man1/fvlistfwcams.1*
%{_mandir}/man1/fvnet.1*
%{_mandir}/man1/fvshmem.1*
%{_mandir}/man1/fvstereodecoder.1*

%files guis
%{_bindir}/ffbatterymon
%{_bindir}/ffeclipse-debugger
%{_bindir}/ffnaogui
%{_bindir}/ffnetloggui
%{_bindir}/ffpclviewer
%{_bindir}/ffskelgui
%{_bindir}/fflasergui
%if ! 0%{?rhel} || 0%{?rhel} >= 6
%{_bindir}/skillgui
%{_bindir}/skillgui_batch_render
%{_bindir}/fvviewer
%{_bindir}/fvscaled_viewer
%{_bindir}/fvshowyuv
%{_mandir}/man1/fvviewer.1*
%{_mandir}/man1/fvshowyuv.1*
%{_mandir}/man1/skillgui.1*
%{_mandir}/man1/skillgui_batch_render.1*
%endif
%{_bindir}/firestation
%{_bindir}/fvfuseviewer
%{_libdir}/libfvwidgets.so.*
%{_libdir}/libfawkesguiutils.so.*
%{_datadir}/%{name}/res/guis
%{_datadir}/applications/*
%{_mandir}/man1/ffbatterymon.1*
%{_mandir}/man1/ffplugingui.1*
%{_mandir}/man1/ffnetloggui.1*
%{_mandir}/man1/fflasergui.1*
%{_mandir}/man1/firestation.1*
%{_mandir}/man1/fvfuseviewer.1*

%files lua -f builtin-interfaces-lua.files
%dir %{luamod_dir}
%dir %{luamod_dir}/interfaces
%dir %{_datadir}/%{name}/lua
%{luamod_dir}/*.so
%{_libdir}/libfawkeslua.so.*
%{_datadir}/%{name}/lua/fawkes
%{_datadir}/%{name}/lua/predicates
%{luamod_dir}/interfaces/HumanSkeletonProjectionInterface.so
%{luamod_dir}/interfaces/NaoJointPositionInterface.so
%{luamod_dir}/interfaces/NaoJointStiffnessInterface.so
%{luamod_dir}/interfaces/NaoSensorInterface.so
%{luamod_dir}/interfaces/OpenCVStereoParamsInterface.so

%files protobuf
%{_libdir}/libfawkes_protobuf_comm.so.*


%files plugin-amcl
%{plugin_dir}/amcl.so
%{_libdir}/libfawkes_amcl_map.so.*
%{_libdir}/libfawkes_amcl_pf.so.*
%{_libdir}/libfawkes_amcl_sensors.so.*
%{_libdir}/libfawkes_amcl_utils.so.*

%if 0%{?have_clips}
%files plugin-clips
%{plugin_dir}/clips.so
%{_libdir}/libfawkesclipsaspect.so.*
%dir %{_datadir}/%{name}/clips
%{_datadir}/%{name}/clips/clips

%files plugin-clips-agent
%{plugin_dir}/clips-agent.so
%{_datadir}/%{name}/clips/clips-agent

%files plugin-clips-executive
%{plugin_dir}/clips-executive.so
%{_datadir}/%{name}/clips/clips-executive

%files plugin-clips-navgraph
%{plugin_dir}/clips-navgraph.so
%{_datadir}/%{name}/clips/clips-navgraph

%files plugin-clips-pddl-parser
%{plugin_dir}/clips-pddl-parser.so

%files plugin-clips-protobuf
%{plugin_dir}/clips-protobuf.so
%{_libdir}/libfawkes_protobuf_clips.so.*
%{_datadir}/%{name}/clips/clips-protobuf

%if %{with mongodb}
%files plugin-clips-robot-memory
%{plugin_dir}/clips-robot-memory.so
%endif

%files plugin-clips-tf
%{plugin_dir}/clips-tf.so

%endif

%files plugin-bblogger
%{_bindir}/ffbblog
%{plugin_dir}/bblogger.so
%{plugin_dir}/bblogreplay.so
%{_mandir}/man1/ffbblog.1*

%files plugin-bbsync
%{plugin_dir}/bbsync.so

%files plugin-cedar
%{plugin_dir}/cedar.so
%config %{_sysconfdir}/%{name}/cedar

%files plugin-colli
%{plugin_dir}/colli.so

%files plugin-dynamixel
%{plugin_dir}/dynamixel.so
%{interface_dir}/libDynamixelServoInterface.so*
%{luamod_dir}/interfaces/DynamixelServoInterface.so

%if %{with festival}
%files plugin-festival
%{plugin_dir}/festival.so
%endif

%files plugin-flite
%{plugin_dir}/flite.so

%if 0%{?have_gazebo}
%files plugin-gazebo
%{plugin_dir}/gazebo.so
%{protobuf_dir}/libgazsim_msgs.so*
%{_libdir}/libfawkesgazeboaspect.so.*

%files plugin-gazsim-comm
%{plugin_dir}/gazsim-comm.so

%files plugin-gazsim-depthcam
%{plugin_dir}/gazsim-depthcam.so

%files plugin-gazsim-laser
%{plugin_dir}/gazsim-laser.so

%files plugin-gazsim-localization
%{plugin_dir}/gazsim-localization.so
%{gazebo_dir}/libgps.so*

%files plugin-gazsim-robotino
%{plugin_dir}/gazsim-robotino.so
%{gazebo_dir}/libgyro.so*
%{gazebo_dir}/libmotor.so*

%files plugin-gazsim-timesource
%{plugin_dir}/gazsim-timesource.so

%files plugin-gazsim-vis-localization
%{plugin_dir}/gazsim-vis-localization.so

%files plugin-gazsim-webcam
%{plugin_dir}/gazsim-webcam.so
%endif

%files plugin-gossip
%{plugin_dir}/gossip.so
%{_libdir}/libfawkesgossip.so.*
%{_libdir}/libfawkesgossipaspect.so.*

%files plugin-imu
%{plugin_dir}/imu.so

%files plugin-jaco
%{plugin_dir}/jaco.so
%{interface_dir}/libJacoBimanualInterface.so*
%{luamod_dir}/interfaces/JacoBimanualInterface.so
%{interface_dir}/libJacoInterface.so*
%{luamod_dir}/interfaces/JacoInterface.so

%files plugin-joystick
%{_bindir}/ffjoystick
%{plugin_dir}/joystick.so
%{_mandir}/man1/ffjoystick.1*

%files plugin-joystick-teleop
%{plugin_dir}/joystick-teleop.so

%files plugin-katana
%{plugin_dir}/katana.so
%{interface_dir}/libKatanaInterface.so*
%dir %{luamod_dir}/interfaces
%{luamod_dir}/interfaces/KatanaInterface.so

%files plugin-laser
%{plugin_dir}/laser.so

%files plugin-laser-cluster
%{plugin_dir}/laser-cluster.so
%{interface_dir}/libLaserClusterInterface.so*
%{luamod_dir}/interfaces/LaserClusterInterface.so

%files plugin-laser-filter
%{_bindir}/fflaser_deadspots
%{plugin_dir}/laser-filter.so
%{interface_dir}/libLaserBoxFilterInterface.so*
%{luamod_dir}/interfaces/LaserBoxFilterInterface.so
%{_mandir}/man1/fflaser_deadspots.1*

%files plugin-laser-lines
%{plugin_dir}/laser-lines.so
%{interface_dir}/libLaserLineInterface.so*
%{luamod_dir}/interfaces/LaserLineInterface.so

%files plugin-laser-pointclouds
%{plugin_dir}/laser-pointclouds.so

%files plugin-luaagent
%{plugin_dir}/luaagent.so
%{_datadir}/%{name}/lua/luaagent
%{_datadir}/%{name}/lua/agents

%files plugin-map-lasergen
%{plugin_dir}/map-lasergen.so

%if %{with mongodb}
%files plugin-mongodb
%{plugin_dir}/mongodb.so
%{_libdir}/libfawkesmongodbaspect.so.*
%{interface_dir}/libMongoDBManagedReplicaSetInterface.so.*

%files plugin-mongodb-log
%{plugin_dir}/mongodb-log.so

%files plugin-mongodb-rrd
%{plugin_dir}/mongodb-rrd.so
%endif

%files plugin-navgraph
%{plugin_dir}/navgraph.so
%{_libdir}/libfawkesnavgraph.so.*
%{_libdir}/libfawkesnavgraphaspect.so.*

%files plugin-navgraph-clusters
%{plugin_dir}/navgraph-clusters.so

%files plugin-navgraph-generator
%{plugin_dir}/navgraph-generator.so
%{_libdir}/libfawkesnavgraphgenerators.so.*
%{interface_dir}/libNavGraphGeneratorInterface.so*
%{luamod_dir}/interfaces/NavGraphGeneratorInterface.so

%files plugin-navgraph-static-constraints
%{plugin_dir}/navgraph-static-constraints.so

%if ! 0%{?have_openni}
%files plugin-openni
%{_libdir}/libfawkesopenni_client_utils.so.*
%else
%files plugin-openni
%{plugin_dir}/openni.so
%{_libdir}/libfawkesopenni_client_utils.so.*
%{_libdir}/libfawkesopenni_utils.so.*
%{_libdir}/libfawkesopenniaspect.so.*

%files plugin-openni-data
%{plugin_dir}/openni-data.so

%files plugin-openni-handtracker
%{plugin_dir}/openni-handtracker.so

%files plugin-openni-pcl-frombuf
%{plugin_dir}/openni-pcl-frombuf.so

%files plugin-openni-usertracker
%{plugin_dir}/openni-usertracker.so
%endif

%if 0%{?have_openprs} >= 1
%files plugin-openprs
%{plugin_dir}/openprs.so
%{openprs_dir}/mod_blackboard.so*
%{openprs_dir}/mod_time.so*
%{openprs_dir}/mod_utils.so*
%{openprs_dir}/mod_config.so*
%{_libdir}/libfawkesopenprsutils.so.*
%{_libdir}/libfawkesopenprsaspect.so.*
%dir %{_datadir}/%{name}/openprs
%{_datadir}/%{name}/openprs/data

%files plugin-openprs-agent
%{plugin_dir}/openprs-agent.so
%{openprs_dir}/mod_navgraph.so*
%{openprs_dir}/mod_protobuf.so*
%{openprs_dir}/mod_skiller.so*
%{_datadir}/%{name}/openprs/openprs-agent

%files plugin-openprs-example
%{plugin_dir}/openprs-example.so
%endif

%files plugin-pantilt
%{_bindir}/ffptu
%{plugin_dir}/pantilt.so
%{interface_dir}/libPanTiltInterface.so*
%dir %{luamod_dir}/interfaces
%{luamod_dir}/interfaces/PanTiltInterface.so

%if %{with mongodb}
%files plugin-pcl-db
%{_bindir}/ffmongodb-save-imgs
%{_mandir}/man1/ffmongodb-save-imgs.1*
%{plugin_dir}/pcl-db-*.so
%{interface_dir}/libPclDatabase*Interface.so*
%{luamod_dir}/interfaces/PclDatabase*Interface.so
%endif

%if 0%{?have_player}
%files plugin-player
%{plugin_dir}/player.so
%endif

%files plugin-realsense
%{plugin_dir}/realsense.so

%files plugin-realsense2
%{plugin_dir}/realsense2.so

%files plugin-refboxcomm
%{plugin_dir}/refboxcomm.so

%files plugin-robotino
%{plugin_dir}/robotino.so
%{interface_dir}/libRobotinoSensorInterface.so*
%{luamod_dir}/interfaces/RobotinoSensorInterface.so

%if %{with mongodb}
%files plugin-robot-memory
%{plugin_dir}/robot-memory.so
%endif

%files plugin-robotino-ir-pcl
%{plugin_dir}/robotino-ir-pcl.so

%files plugin-robot-state-publisher
%{plugin_dir}/robot-state-publisher.so

%files plugin-roomba
%{plugin_dir}/roomba.so
%{plugin_dir}/roombajoy.so
%{interface_dir}/libRoomba500Interface.so*
%{luamod_dir}/interfaces/Roomba500Interface.so

%files plugin-rrd
%{plugin_dir}/rrd.so
%{_libdir}/libfawkesrrdaspect.so.*

%files plugin-skiller
%{plugin_dir}/skiller.so
%{_bindir}/skillet
%{_datadir}/%{name}/lua/skiller
%{_datadir}/%{name}/lua/skills
%{interface_dir}/libSkillerDebugInterface.so*
%dir %{luamod_dir}/interfaces
%{luamod_dir}/interfaces/SkillerDebugInterface.so
%{_mandir}/man1/skillet.1*

%files plugin-skiller-simulator
%{plugin_dir}/skiller-simulator.so

%files plugin-static-transforms
%{plugin_dir}/static-transforms.so

%files plugin-tabletop-objects
%{plugin_dir}/tabletop-objects.so

%files plugin-ttmainloop
%{plugin_dir}/ttmainloop.so

%files plugin-webview
%{_libdir}/libfawkeswebview.so*
%{plugin_dir}/webview.so
%config %{_sysconfdir}/%{name}/grafana
%config %{_sysconfdir}/%{name}/prometheus

%if 0%{?have_xmlrpc}
%files plugin-xmlrpc
%{plugin_dir}/xmlrpc.so
%endif

%files devel
%{_pkgdocdir}/DEPENDENCIES
%{_bindir}/ffifacegen
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/%{name}/buildsys
%{_mandir}/man1/ffifacegen.1*

%files devenv

%files doc
%{_pkgdocdir}/*
%exclude %{_pkgdocdir}/DEPENDENCIES
%exclude %{_pkgdocdir}/README.md
%exclude %{_pkgdocdir}/LICENSE.*

%changelog
* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-13
- Rebuilt for OpenCV 4.3

* Tue Apr 28 2020 Till Hofmann <thofmann@fedoraproject.org> - 1.3.0-12
- Switch to gtkmm30

* Sat Mar 07 2020 Till Hofmann <thofmann@fedoraproject.org> - 1.3.0-11
- Rebuild for librealsense 2.33

* Mon Feb 24 2020 Rich Mattes <richmattes@gmail.com> - 1.3.0-10
- Rebuild for gazebo-10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-8
- Rebuild for OpenCV 4.2

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-7
- Disable for opencv4

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 1.3.0-6
- Rebuild for protobuf 3.11

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 1.3.0-5
- Fix missing #include for gcc-10

* Tue Oct 29 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.3.0-4
- Remove unused dependency on PyQt4-devel to remove Python2 dependency

* Fri Oct 18 2019 Richard Shaw <hobbes1069@gmail.com> - 1.3.0-3
- Rebuild for yaml-cpp 0.6.3.

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 1.3.0-2
- Rebuild for mpfr 4

* Sun Oct 06 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0
- Add sub-packages for plugins realsense, realsense2, skiller-simulator

* Sat Oct 05 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.2.0-11
- Add patch for CGAL 5.0

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.2.0-10
- Rebuild and patch for freeglut 3.2.0

* Tue Aug 20 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.2.0-9
- Remove dependencies on ROS packages by default (reenable with --with-ros)
- Remove dependency on player (FTBFS)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.2.0-7
- Update sub-packages required by meta package

* Tue Jun 04 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.2.0-6
- Do not require plugin-pcl-db sub-package from devenv

* Sat May 11 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.2.0-5
- Add patch to use correct build flags for flite/ALSA

* Thu May 09 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.2.0-4
- Switch all devenv dependencies from python2 to python3

* Thu May 09 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.2.0-3
- Install plugins that were added with the 1.2.0 release
- Update install target patch so no unnecessary interfaces are built

* Thu May 09 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.2.0-2
- Add patch to fix install target (upstream PR #111)
- Add patch to fix build failure due to git hook directory not existing
- Adapt file list to upstream changes

* Tue May 07 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Sun Feb 24 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.1.0-0.20190223.c8d33e7.2
- Add missing BR: doxygen-latex
- Add patch to fix build order clips -> clips-executive

* Sat Feb 23 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.1.0-0.20190223.c8d33e7.1
- Update to latest upstream snapshot
- Remove upstreamed patch

* Sat Feb 23 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.1.0-0.20190218.799f183.2
- Remove dependency on festival, make festival plugin optional

* Mon Feb 18 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.1.0-0.20190218.799f183.1
- Update to pre-release snapshot of 1.1.0 to fix FTBFS

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-22
- Rebuild for readline 8.0

* Tue Feb 12 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.0.1-21
- Disable building against mongodb by default
  (See https://fedoraproject.org/wiki/Changes/MongoDB_Removal)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-19
- Rebuild for protobuf 3.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.1-17
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 14 2018 Richard Shaw <hobbes1069@gmail.com> - 1.0.1-16
- Rebuild for yaml-cpp 0.6.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Sérgio Basto <sergio@serjux.com> - 1.0.1-14
- Rebuild (opencv-3.3.1)

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.1-13
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-12
- Rebuild for protobuf 3.4

* Sat Oct 21 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.0.1-11
- Rebuild for collada-dom 2.5

* Mon Oct 02 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.0.1-10
- Add patch to replace cmath's HUGE with std::numeric_limits

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-7
- Rebuilt for Boost 1.64

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 1.0.1-6
- Rebuild for protobuf 3.3.1

* Thu Jun 01 2017 Till Hofmann <till.hofmann@posteo.de> - 1.0.1-5
- Rebuilt for CGAL 4.10

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Apr 09 2017 Rich Mattes <richmattes@gmail.com> - 1.0.1-3
- Rebuild for player-3.1.0

* Mon Mar 20 2017 Rich Mattes <richmattes@gmail.com> - 1.0.1-2
- Add missing obsoletes (rhbz#1427699)

* Tue Feb  7 2017 Tim Niemueller <tim@niemueller.de> - 1.0.1-1
- Upgrade to 1.0.1 release
- Fixes automated update checks regarding library deps
- Add post-release patch that fixes parallel builds

* Wed Feb 01 2017 Tim Niemueller <tim@niemueller.de> - 1.0.0-6
- Add ld.so.conf.d file for protobuf messages

* Thu Jan 26 2017 Orion Poplawski <orion@cora.nwra.com> - 1.0.0-5
- Rebuild for protobuf 3.2.0

* Sat Jan 21 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-4
- Rebuild for xmlrpc-c

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-3
- Rebuild for readline 7.x

* Wed Jan 11 2017 Tim Niemueller <tim@niemueller.de> - 1.0.0-2
- Add back log4cxx-devel for -devenv Requires (unretired)

* Fri Dec 23 2016 Tim Niemueller <tim@niemueller.de> - 1.0.0-1
- Upgrade to 1.0.0 release, the 10th anniversary release

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 0.5.0-31
- Rebuild for protobuf 3.1.0

* Tue May 03 2016 Rich Mattes <richmattes@gmail.com> - 0.5.0-30
- Rebuild for opencv-3.1.0

* Wed Feb 10 2016 Rich Mattes <richmattes@gmail.com> - 0.5.0-29
- Remove retired log4cxx-devel from -devenv Requires

* Tue Feb 02 2016 Tim Niemueller <tim@niemueller.de> - 0.5.0-28
- Add backports patch with changes required until upcoming release
- Update requires for devenv package for recent git version

* Mon Feb 01 2016 Tim Niemueller <tim@niemueller.de> - 0.5.0-27
- Build against compat-lua and compat-tolua++

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.5.0-26
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-25
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.5.0-24
- rebuild for Boost 1.58

* Thu Jun 25 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 0.5.0-23
- Added AArch64 into list of 64-bit architectures.
- Fixed handling of 64-bit archs other than x86-64
- Added AArch64 into list of no-openni architectures and simplified spec for it.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.0-21
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 17 2015 Rich Mattes <richmattes@gmail.com> - 0.5.0-20
- Update lua 5.2 patch to detect correct version of lua
- Fix gcc version based c++11 detection logic

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 0.5.0-20
- Rebuild for boost 1.57.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Petr Machata <pmachata@redhat.com> - 0.5.0-17
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.5.0-16
- rebuild for boost 1.55.0

* Sun Feb 09 2014 Rich Mattes <richmattes@gmail.com> - 0.5.0-15
- Rebuild for bullet-2.82

* Wed Dec 11 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.5.0-14
- Install docs to %%{_pkgdocdir} where available (#993748).
- Disable parallel build.

* Wed Oct 09 2013 Rich Mattes <richmattes@gmail.com> - 0.5.0-13
- Rebuild for new geos

* Sat Sep 14 2013 Rich Mattes <richmattes@gmail.com> - 0.5.0-12
- Rebuild for new pcl
- Fix changelog date

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 0.5.0-10
- Rebuild for boost 1.54.0

* Sun Jul 21 2013 Rich Mattes <richmattes@gmail.com> - 0.5.0-9
- Rebuild for new eigen3

* Tue May 14 2013 Tom Callaway <spot@fedoraproject.org> - 0.5.0-8
- rebuild for lua 5.2

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.5.0-7
- Rebuild for Boost-1.53.0

* Sat Jan 26 2013 Rich Mattes <richmattes@gmail.com> - 0.5.0-6
- Fix error due to new graphviz api

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.5.0-6
- rebuild due to "jpeg8-ABI" feature drop

* Sat Dec 22 2012 Rich Mattes <richmattes@gmail.com> - 0.5.0-5
- Rebuild for new flann

* Fri Nov 30 2012 Tom Callaway <spot@fedoraproject.org> - 0.5.0-4
- rebuild for new libgeos

* Sun Oct 14 2012 Rich Mattes <richmattes@gmail.com> - 0.5.0-3
- Rebuild for new bullet

* Fri Sep 28 2012 Tim Niemueller <tim@niemueller.de> - 0.5.0-2
- Bump after branch unification
- Distinguish gearbox/hokuyoaist dependency by distro version

* Wed Sep 26 2012 Tim Niemueller <tim@niemueller.de> - 0.5.0-1
- Update to latest stable release 0.5.0

* Mon Aug 13 2012 Rich Mattes <richmattes@gmail.com> - 0.4.2-12
- Rebuilt for new player, boost, opencv, hokuyoaist

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 26 2012 Rich Mattes <richmattes@gmail.com> - 0.4.2-11
- Rebuild for new libxmlrpc

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-10
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.2-8
- Rebuild for new libpng

* Mon Oct 31 2011 Dan Horák <dan[at]danny.cz> - 0.4.2-7
- exclude s390(x)

* Fri Oct 14 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.4.2-6
- Add patch from Jaroslav Škarvada to get this building on rawhide 
  and fix broken dep/FTBFS (#715874)

* Wed Aug 31 2011 Rex Dieter <rdieter@fedoraproject.org> 0.4.2-5
- rebuild (opencv)

* Sun Apr 17 2011 Kalev Lember <kalev@smartlink.ee> - 0.4.2-4
- Rebuilt for boost 1.46.1 soname bump

* Sun Feb 27 2011 Tim Niemueller <tim@niemueller.de> - 0.4.2-3
- Omit URG support on ppc, package is not available there
- Added patch for ppc64
- On el6 devenv/doc are not noarch packages (urg-devel not available on ppc64)

* Tue Feb 22 2011 Tim Niemueller <tim@niemueller.de> - 0.4.2-2
- Remove skillgui man pages from el5 package (skillgui not available on el5)

* Tue Feb 22 2011 Tim Niemueller <tim@niemueller.de> - 0.4.2-1
- Update to 0.4.2, fixes GCC 4.6.0 and kernel 2.6.38 related build problems

* Wed Feb 16 2011 Tim Niemueller <tim@niemueller.de> - 0.4.1-4
- Udpate build requires and add additional devenv deps

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.4.1-2
- rebuild for new boost

* Sun Jan 09 2011 Tim Niemueller <tim@niemueller.de> - 0.4.1-1
- Update to 0.4.1 (includes all patches of 0.4 package)
- Added more requires to devenv package

* Tue Nov 09 2010 Tim Niemueller <tim@niemueller.de> - 0.4-7
- Rebuild again, libmicrohttpd was not yet tagged into f14 override

* Mon Nov 08 2010 Tim Niemueller <tim@niemueller.de> - 0.4-6
- Add patch and rebuild for new libmicrohttpd

* Sat Nov 06 2010 Tim Niemueller <tim@niemueller.de> - 0.4-5
- Sub-packages should not depend on main package if not necessary

* Fri Nov 05 2010 Tim Niemueller <tim@niemueller.de> - 0.4-4
- EL 5/6 compatibility, omit stuff with unfulfilled dependencies
- Update man pages patch for EL 5/6 and more man pages
- Update desktop files patch for EL 5/6
- BuildRequire graphviz, docbook-style-xsl, libxslt

* Thu Nov 04 2010 Tim Niemueller <tim@niemueller.de> - 0.4-3
- consistent macro usage
- Make fawkes-core own /usr/share/fawkes
- Run desktop-file-validate on .desktop files
- Update man-page patch to latest version
- Add patch for timn/desktop-files branch fixing desktop files
- Use uncolored targets for better Koji readability
- Build all and gui targets in one to have only one tree traversal

* Sat Oct 30 2010 Tim Niemueller <tim@niemueller.de> - 0.4-2
- Added patch to support configs in user homedirs

* Sun Feb 07 2010 Tim Niemueller <tim@niemueller.de> - 0.4-1
- Initial package

