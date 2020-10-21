Name:               paho-c
Version:            1.3.4
Release:            1%{?dist}
Summary:            MQTT C Client
License:            BSD and EPL
URL:                https://eclipse.org/paho/clients/c/
Source0:            https://github.com/eclipse/paho.mqtt.c/archive/v%{version}.tar.gz#/paho.mqtt.c-%{version}.tar.gz
Source1:            unused.abignore

BuildRequires:      cmake
BuildRequires:      gcc
BuildRequires:      gcc-c++
BuildRequires:      graphviz
BuildRequires:      doxygen
BuildRequires:      openssl-devel

%description
The Paho MQTT C Client is a fully fledged MQTT client written in C.


%package devel
Summary:            MQTT C Client development kit
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and samples for the the Paho MQTT C Client.


%package doc
Summary:            MQTT C Client development kit documentation
BuildArch:          noarch

%description doc
Development documentation files for the the Paho MQTT C Client.

%prep
%setup -n paho.mqtt.c-%{version}

%build
mkdir build.paho && cd build.paho
%cmake -DPAHO_WITH_SSL=TRUE -DPAHO_BUILD_DOCUMENTATION=TRUE -DPAHO_BUILD_SAMPLES=TRUE -DPAHO_ENABLE_CPACK=FALSE ..
%cmake_build

%install
cd build.paho
%cmake_install
install -D -p -m 755 %{SOURCE0} %{buildroot}/%{_datadir}/%{name}/abi/paho-c.abignore
# don't ship cmake artefacts
rm -rf %{buildroot}/usr/lib/cmake


%files
%license LICENSE edl-v10 epl-v20
%{_bindir}/paho*
%{_libdir}/libpaho-mqtt*.so.1*
%{_datadir}/%{name}/abi/paho-c.abignore

%ldconfig_scriptlets

%files devel
%{_bindir}/MQTT*
%{_includedir}/*
%{_libdir}/*.so

%files doc
%license LICENSE edl-v10 epl-v20
%{_defaultdocdir}/*

%changelog
* Tue Aug 04 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Otavio R. Piske <opiske@redhat.com> - 1.3.0-0
- Upgrades paho to version 1.3.0 which supports MQTT 5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Otavio R. Piske <opiske@redhat.com> - 1.2.1-3
- Adjust the location of the abignore file in a location that can be useful for the users

* Mon Apr 30 2018 Otavio R. Piske <opiske@redhat.com> - 1.2.1-2
- Adds ABI check suppression in the package

* Mon Apr 30 2018 Otavio R. Piske <opiske@redhat.com> - 1.2.1-1
- Ignores ABI changes due to unused symbols being removed

* Sat Apr 28 2018 Otavio R. Piske <opiske@redhat.com> - 1.2.1-0
- Updates paho-c package to the latest upstream version 1.2.1
- Adjust the location of the documentation within the documentation dir

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 19 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-10
- Renames the devel-doc package as suggested by reviewer

* Thu Oct 19 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-9
- Reduce description size to less than 80 characters
- Install the Paho client/servers tools in the binary package
- Install the binary examples in the development package only

* Sat Aug 12 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-8
- Added missing ldconfig on the postun section

* Sat Aug 12 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-7
- Replaced build and install commands with respective macros
- Added license to the devel docs packages
- Removed explicit require on OpenSSL
- Move the shared library symlinks to the devel package

* Mon Jul 31 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-6
- Fixed short description of the project license

* Sun Jul 30 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-5
- Renamed the documentation package to -doc

* Sun Jul 30 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-4
- Removed Group tag as required by packaging guidelines
- Prevent the devel package from being used with incompatible versions
- Replaced the doc tag with the license tag

* Thu Jul 27 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-4
- Enabled generation of debuginfo package

* Thu Jul 27 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-3
- Fixed changelog issues pointed by rpmlint

* Thu Jul 27 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-2
- Updated changelog to comply with Fedora packaging guidelines

* Wed Jul 26 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0-1
- Fixed rpmlint warnings: replaced cmake call with builtin macro
- Fixed rpmlint warnings: removed buildroot reference from build section

* Fri Jun 30 2017 Otavio R. Piske <opiske@redhat.com> - 1.2.0
- Updated package to version 1.2.0

* Sat Dec 31 2016 Otavio R. Piske <opiske@redhat.com> - 1.1.0
- Initial packaging
