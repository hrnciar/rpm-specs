%undefine __cmake_in_source_build

Name:		vrpn
Version:	07.33
Release:	26%{?dist}
Summary:	The Virtual-Reality Peripheral Network

# linking to wiiuse (GPLv3+) and gpm (GPLv2+) libraries makes the vrpn server
# (libvrpnserver.so and vrpn_server binary, as well as python and java modules)
# GPLv3+-licensed. The rest of files is supplied under the Boost license.
License:	Boost and GPLv3+
URL:		https://github.com/vrpn/vrpn/
Source0:	https://github.com/vrpn/vrpn/archive/version_%{version}.tar.gz#/%{name}-version_%{version}.tar.gz
Source1:	vrpn.service
Patch0:		vrpn-find_modbus.patch
Patch1:		vrpn-find_hidapi.patch
Patch2:		vrpn-find_jsoncpp.patch
# patch3 from upstream commit 7f961a3
Patch3:		vrpn-fix_library_install_rules.patch
Patch4:		vrpn-java_install.patch
Patch5:		vrpn-python_install.patch
Patch6:		vrpn-soversion.patch
Patch7:		vrpn-config_install.patch
Patch8:		vrpn-dont_install_garbage.patch
Patch9:		vrpn-wait.patch

BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	gcc
BuildRequires:	glut-devel
BuildRequires:	gpm-devel
BuildRequires:	graphviz
BuildRequires:	help2man
BuildRequires:	hidapi-devel
BuildRequires:	java-devel
BuildRequires:	jsoncpp-devel
BuildRequires:	libGL-devel
BuildRequires:	libmodbus-devel
BuildRequires:	libudev-devel
BuildRequires:	libusb-devel
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	python3-devel
BuildRequires:	systemd
BuildRequires:	swig
BuildRequires:	wiiuse-devel

%{?systemd_requires}

%description
The Virtual-Reality Peripheral Network (VRPN) is a set of classes within a
library and a set of servers that are designed to implement a
network-transparent interface between application programs and the set of
physical devices (tracker, etc.) used in a virtual-reality (VR) system. The
idea is to have a PC or other host at each VR station that controls the
peripherals (tracker, button device, haptic device, analog inputs, sound, etc).
VRPN provides connections between the application and all of the devices using
the appropriate class-of-service for each type of device sharing this link. The
application remains unaware of the network topology. Note that it is possible
to use VRPN with devices that are directly connected to the machine that the
application is running on, either using separate control programs or running
all as a single program.


%package devel
Summary:	Development files for the Virtual-Reality Peripheral Network
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The Virtual-Reality Peripheral Network (VRPN) is a set of classes within a
library and a set of servers that are designed to implement a
network-transparent interface between application programs and the set of
physical devices (tracker, etc.) used in a virtual-reality (VR) system.

This package contains development files for VRPN libraries.


%package doc
Summary:	Developer's documentation for VRPN
BuildArch:	noarch

%description doc
The Virtual-Reality Peripheral Network (VRPN) is a set of classes within a
library and a set of servers that are designed to implement a
network-transparent interface between application programs and the set of
physical devices (tracker, etc.) used in a virtual-reality (VR) system.

This package contains generated VRPN source code documentation.


%package java
Summary:	Java bindings for the Virtual-Reality Peripheral Network
License:	GPLv3+

Requires:	java-headless
Requires:	javapackages-tools

%description java
The Virtual-Reality Peripheral Network (VRPN) is a set of classes within a
library and a set of servers that are designed to implement a
network-transparent interface between application programs and the set of
physical devices (tracker, etc.) used in a virtual-reality (VR) system.

This package contains Java bindings for VRPN libraries.


%package -n python3-%{name}
Summary:	Python 3 bindings for the Virtual-Reality Peripheral Network
License:	GPLv3+

%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
The Virtual-Reality Peripheral Network (VRPN) is a set of classes within a
library and a set of servers that are designed to implement a
network-transparent interface between application programs and the set of
physical devices (tracker, etc.) used in a virtual-reality (VR) system.

This package contains Python 3 bindings for VRPN libraries.


%prep
%autosetup -n %{name}-version_%{version} -p1


%build
%cmake \
    -DVRPN_GPL_SERVER=ON \
    -DBUILD_TESTING=ON \
    -DVRPN_BUILD_PYTHON_HANDCODED_3X=ON \
    -DVRPN_PYTHON_INSTALL_DIR=%{python3_sitearch} \
    -DJAVA_INSTALL_LIBDIR=%{_libdir}/%{name} \
    -DJAVA_INSTALL_JNIDIR=%{_jnidir} \
%ifarch %{arm}
    -DJAVA_AWT_LIBRARY=%{_libdir}/jvm/java/lib/aarch32/libjawt.so \
%endif # arch %%{arm}
    %{nil}
%cmake_build
%cmake_build --target doc


%install
%cmake_install
install -D %{_vpath_builddir}/python/vrpn.so %{buildroot}%{python3_sitearch}/vrpn.so
install -D -m644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

# generate man pages
mkdir -p %{buildroot}%{_mandir}/man1
for prog in ./%{_vpath_builddir}/server_src/vrpn_server \
            ./%{_vpath_builddir}/client_src/run_auxiliary_logger \
	    ./%{_vpath_builddir}/client_src/vrpn_print_{devices,messages,performance}
do
    progname=$(basename "$prog")
    help2man \
        --version-string=%{version} \
        --no-info \
        --no-discard-stderr \
        --output="%{buildroot}%{_mandir}/man1/$progname.1" \
        "$prog"
done


%check
%ctest


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%doc ChangeLog Format
%license README.Legal
%{_libdir}/*.so.*
%{_bindir}/*
%{_datadir}/%{name}-%{version}
%config(noreplace) %{_sysconfdir}/vrpn.cfg
%{_unitdir}/%{name}.service
%{_mandir}/man1/*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files doc
%doc %{_docdir}/%{name}-%{version}
%exclude %{_docdir}/%{name}-%{version}/source-docs/html/*.map
%exclude %{_docdir}/%{name}-%{version}/source-docs/html/*.md5

%files java
%{_libdir}/%{name}/libjava_%{name}.so
%{_jnidir}/*.jar

%files -n python3-%{name}
%{python3_sitearch}/*.so


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-26
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 07.33-24
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 07.33-23
- Rebuild (jsoncpp)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 07.33-22
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Björn Esser <besser82@fedoraproject.org> - 07.33-20
- Rebuild (jsoncpp)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 07.33-19
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 07.33-17
- Rebuild (jsoncpp)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 07.33-15
- Subpackage python2-vrpn has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 07.33-13
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 26 2017 Björn Esser <besser82@fedoraproject.org> - 07.33-11
- Rebuilt for jsoncpp.so.20

* Sat Sep 02 2017 Björn Esser <besser82@fedoraproject.org> - 07.33-10
- Fix problems with finding JNI on %%arm

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 07.33-9
- Rebuilt for jsoncpp-1.8.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 07.33-5
- Rebuild for Python 3.6

* Mon Oct 03 2016 Björn Esser <fedora@besser82.io> - 07.33-4
- Rebuilt for libjsoncpp.so.11

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 07.33-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 8 2016 Dmitry Mikhirev <mikhirev@gmail.com> 07.33-2
- Fix build for fc25 (#1341988)
- Fix installation of python 3 module (#1342509)

* Wed Feb 24 2016 Dmitry Mikhirev <mikhirev@gmail.com> 07.33-1
- Initial package
