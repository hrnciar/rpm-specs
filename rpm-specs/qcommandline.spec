Name:           qcommandline
Version:        0.3.0
Release:        21%{?dist}
Summary:        Command line parser for Qt programs
License:        LGPLv2+
URL:            http://xf.iksaif.net/dev/qcommandline.html
Source0:        http://xf.iksaif.net/dev/qcommandline/qcommandline-%{version}.tar.bz2
# http://dev.iksaif.net/issues/253
Patch1:         0001-fix-pkg-config-paths.patch
# http://dev.iksaif.net/issues/252 -- enhancements for PhantomJS
Patch2:         0002-new-ParameterFence-flag.patch
Patch3:         0003-new-NoShortName-flag-to-allow-options-with-no-short-.patch
Patch4:         0004-new-SuppressHelp-flag.patch
# https://gitorious.org/qcommandline/qcommandline/merge_requests/3
Patch5:         0005-qt5.patch
BuildRequires:  cmake
BuildRequires:  qt-devel
BuildRequires:  qt5-qtbase-devel

%description
QCommandLine is a command line parsing library for Qt programs (like getopt). 
Features include options, switches, parameters and automatic --version/--help 
generation.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       cmake

%description devel
Development files for building against %{name}.

%package qt5
Summary:        Command line parser for Qt5 programs

%description qt5
QCommandLine is a command line parsing library for Qt5 programs (like getopt). 
Features include options, switches, parameters and automatic --version/--help 
generation.

%package qt5-devel
Summary:        Development files for %{name}-qt5
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       cmake

%description qt5-devel
Development files for building against %{name}.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%global qt5dir %{_builddir}/qt5-%{name}-%{version}
rm -rf %{qt5dir}
cp -a . %{qt5dir}
cd %{qt5dir}
%patch5 -p1
# rename the library to libqcommandline-qt5 to distinguish it from the Qt4 build
echo "set_target_properties(qcommandline PROPERTIES OUTPUT_NAME qcommandline-qt5)" >>CMakeLists.txt
sed -i -e 's/-lqcommandline/-lqcommandline-qt5/' QCommandLine.pc.in
sed -i -e 's/QCommandLine\.pc$/QCommandLine-qt5.pc/' CMakeLists.txt

%build
mkdir build
cd build
%cmake .. -DCMAKE_MODULES_INSTALL_DIR=%{_datadir}/cmake/Modules
make %{?_smp_mflags}

cd %{qt5dir}
mkdir build
cd build
%cmake .. -DCMAKE_MODULES_INSTALL_DIR=%{_datadir}/cmake/Modules
make %{?_smp_mflags}

%install
cd build
make DESTDIR=%{buildroot} install

cd %{qt5dir}/build
make DESTDIR=%{buildroot} install

%files
%doc COPYING
%{_libdir}/lib%{name}.so.*

%files qt5
%doc COPYING
%{_libdir}/lib%{name}-qt5.so.*

%files devel
%doc examples/
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/QCommandLine.pc
%{_datadir}/cmake/Modules/FindQCommandLine.cmake

%files qt5-devel
%{_libdir}/lib%{name}-qt5.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/QCommandLine-qt5.pc
%{_datadir}/cmake/Modules/FindQCommandLine.cmake

%ldconfig_scriptlets

%ldconfig_scriptlets -n %{name}-qt5

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Dan Callaghan <dcallagh@redhat.com> - 0.3.0-17
- removed deprecated qt5_use_modules() macro to fix the build with Qt 5.11

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.0-10
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Dan Callaghan <dcallagh@redhat.com> - 0.3.0-7
- separate subpackage for Qt5 build, base package reverted to Qt4

* Sun May 25 2014 Dan Callaghan <dcallagh@redhat.com> - 0.3.0-6
- build against Qt5

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 08 2013 Dan Callaghan <dcallagh@redhat.com> - 0.3.0-4
- use parallel make

* Mon Jan 14 2013 Dan Callaghan <dcallagh@redhat.com> - 0.3.0-3
- enhancements for PhantomJS

* Thu Jan 10 2013 Dan Callaghan <dcallagh@redhat.com> - 0.3.0-2
- fixed pkg-config paths

* Thu Sep 20 2012 Dan Callaghan <dcallagh@redhat.com> - 0.3.0-1
- initial version
