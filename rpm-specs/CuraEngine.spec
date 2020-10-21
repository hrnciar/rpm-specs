Name:           CuraEngine
Epoch:          1
Version:        4.7.1
Release:        2%{?dist}
Summary:        Engine for processing 3D models into G-code instructions for 3D printers
License:        AGPLv3+
URL:            https://github.com/Ultimaker/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# The cmake stuff would attempt to git clone this:
# TODO package on it's own
%global stb_commit e6afb9cbae4064da8c3e69af3ff5c4629579c1d2
Source1:        https://github.com/nothings/stb/archive/%{stb_commit}.tar.gz
Provides:       bundled(stb) = %stb_commit

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libarcus-devel == %{version}
BuildRequires:  polyclipping-devel >= 6.1.2
BuildRequires:  protobuf-devel
BuildRequires:  rapidjson-devel
BuildRequires:  cmake
BuildRequires:  git-core

Patch0:         %{name}-rpath.patch
Patch1:         %{name}-static-libstdcpp.patch

# Get Fedora 33++ behavior on anything older
%undefine __cmake_in_source_build

%description
%{name} is a C++ console application for 3D printing G-code generation. It
has been made as a better and faster alternative to the old Skeinforge engine.

This is just a console application for G-code generation. For a full graphical
application look at cura with is the graphical frontend for %{name}.

%prep
%autosetup -p1 -S git
tar -xf %{SOURCE1}
mv stb-%{stb_commit} stb

# bundled libraries
rm -rf libs

# The -DCURA_ENGINE_VERSION does not work, so we sed-change the default value
sed -i 's/"DEV"/"%{version}"/' src/settings/Settings.h

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DCURA_ENGINE_VERSION:STRING=%{version} -DUSE_SYSTEM_LIBS:BOOL=ON -DCMAKE_CXX_FLAGS_RELEASE_INIT:STRING="%{optflags} -fPIC" -DStb_INCLUDE_DIRS:PATH=${PWD}
%cmake_build


%install
%cmake_install


%check
# Smoke test
%{buildroot}%{_bindir}/%{name} help

%files
%doc LICENSE README.md
%{_bindir}/%{name}

%changelog
* Wed Sep 23 2020 Adrian Reber <adrian@lisas.de> - 1:4.7.1-2
- Rebuilt for protobuf 3.13

* Thu Sep 03 2020 Miro Hrončok <mhroncok@redhat.com> - 1:4.7.1-1
- Update to 4.7.1

* Mon Aug 31 2020 Gabriel Féron <feron.gabriel@gmail.com> - 4.7.0-1
- Update to 4.7.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1:4.6.1-2
- Rebuilt for protobuf 3.12

* Tue May 5 2020 Gabriel Féron <feron.gabriel@gmail.com> - 4.6.0-1
- Update to 4.6.1

* Tue Apr 21 2020 Gabriel Féron <feron.gabriel@gmail.com> - 4.6.0-1
- Update to 4.6.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 1:4.4.0-2
- Rebuild for protobuf 3.11

* Thu Nov 21 2019 Gabriel Féron <feron.gabriel@gmail.com> - 4.4.0-1
- Update to 4.4.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Gabriel Féron <feron.gabriel@gmail.com> - 4.1.0-1
- Update to 4.1.0

* Wed Apr 03 2019 Gabriel Féron <feron.gabriel@gmail.com> - 4.0.0-1
- Update to 4.0.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Gabriel Féron <feron.gabriel@gmail.com> - 1:3.6.0-1
- Update to 3.6.0

* Thu Nov 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.5.1-3
- Rebuild for protobuf 3.6

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.5.1-2
- Rebuild for protobuf 3.6

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.5.1-1
- Fix the error in epoch/release

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 0:3.5.1-2
- Update to 3.5.1 (#1644323)

* Tue Aug 28 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.4.1-1
- Update to 3.4.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.3.0-1
- Updated to 3.3.0
- Make sure Fedora CXXFLAGS are used, also -fPIC
- Use new USE_SYSTEM_LIBS option instead of patch+sed

* Mon Mar 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.2.1-1
- Updated to 3.2.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Miro Hrončok <mhroncok@redhat.com> - 1:3.1.0-1
- Updated to 3.1.0

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:3.0.3-3
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.0.3-2
- Rebuild for protobuf 3.4

* Mon Oct 23 2017 Miro Hrončok <mhroncok@redhat.com> - 1:3.0.3-1
- Updated to 3.0.3

* Wed Aug 30 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.7.0-1
- Update to 2.7.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.6.1-1
- Updated to 2.6.1

* Tue Jun 27 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.6.0-1
- Updated to 2.6.0

* Wed Jun 14 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.5.0-2
- Rebuilt for new protobuf 3.3.1

* Wed May 03 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.5.0-1
- Updated to 2.5.0

* Sun Dec 04 2016 Miro Hrončok <mhroncok@redhat.com> - 1:2.3.1-1
- New version scheme -> Introduce Epoch
- Updated
- SPEC rewritten

* Sun Sep 18 2016 Miro Hrončok <mhroncok@redhat.com> - 15.04-4
- Rebuilt for new polyclipping (#1159525)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 06 2015 Miro Hrončok <mhroncok@redhat.com> - 15.04-2
- Set the VERSION variable

* Sun Jul 05 2015 Miro Hrončok <mhroncok@redhat.com> - 15.04-1
- Update to 15.04

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 14.12.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Dec 29 2014 Miro Hrončok <mhroncok@redhat.com> - 14.12.1-1
- Update to 14.12.1

* Thu Oct 23 2014 Miro Hrončok <mhroncok@redhat.com> - 14.03-3
- Rebuilt for new polyclipping

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Miro Hrončok <mhroncok@redhat.com> - 14.03-1
- New version 14.03

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 09 2014 Miro Hrončok <mhroncok@redhat.com> - 14.01-1
- New version 14.01
- polyclipping 6.1.x
- Now with make test
- Rebuilt against new polyclipping release

* Sat Dec 14 2013 Miro Hrončok <mhroncok@redhat.com> - 13.11.2-1
- New version 13.11.2
- Makefile seding changed to reflect changes
- Clipper usage no longer need patching

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.06.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Miro Hrončok <mhroncok@redhat.com> - 13.06.3-3
- Rebuilt for new polyclipping

* Thu Jul 04 2013 Miro Hrončok <mhroncok@redhat.com> - 13.06.3-2
- Added some explaining comments

* Sun Jun 23 2013 Miro Hrončok <mhroncok@redhat.com> - 13.06.3-1
- New package
