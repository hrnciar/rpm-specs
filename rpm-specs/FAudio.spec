Name:     FAudio
Version:  20.10
Release:  1%{?dist}
Summary:  FNA is a reimplementation of the Microsoft XNA Game Studio 4.0 Refresh libraries

License:  zlib
URL:      https://fna-xna.github.io/
Source0:  https://github.com/FNA-XNA/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++

BuildRequires: SDL2-devel
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel


%description
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.


%package -n libFAudio
Summary:  %{summary}


%description -n libFAudio
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.


%package -n libFAudio-devel
Summary:  Development files for the FAudio library
Requires: libFAudio%{?_isa} = %{version}-%{release}


%description -n libFAudio-devel
Development files for the FAudio library.


%prep
%autosetup


%build
%cmake \
 -DGSTREAMER=ON
%cmake_build


%install
%cmake_install


%files -n libFAudio
%license LICENSE
%doc README
%{_libdir}/libFAudio.so.0*


%files -n libFAudio-devel
%{_libdir}/libFAudio.so
%{_libdir}/cmake/FAudio/
%{_includedir}/F3DAudio.h
%{_includedir}/FACT.h
%{_includedir}/FACT3D.h
%{_includedir}/FAPO.h
%{_includedir}/FAPOBase.h
%{_includedir}/FAPOFX.h
%{_includedir}/FAudio.h
%{_includedir}/FAudioFX.h


%changelog
* Fri Oct 02 2020 Michael Cronenworth <mike@cchtml.com> - 20.10-1
- Update to 20.10

* Wed Sep 02 2020 Michael Cronenworth <mike@cchtml.com> - 20.09-1
- Update to 20.09

* Mon Aug 03 2020 Michael Cronenworth <mike@cchtml.com> - 20.08-1
- Update to 20.08
- Enable GStreamer backend

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Michael Cronenworth <mike@cchtml.com> - 20.07-1
- Update to 20.07

* Mon Jun 01 2020 Michael Cronenworth <mike@cchtml.com> - 20.06-1
- Update to 20.06

* Thu Apr 02 2020 Michael Cronenworth <mike@cchtml.com> - 20.04-1
- Update to 20.04

* Mon Mar 02 2020 Michael Cronenworth <mike@cchtml.com> - 20.03-1
- Update to 20.03

* Mon Feb 03 2020 Michael Cronenworth <mike@cchtml.com> - 20.02-1
- Update to 20.02

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Michael Cronenworth <mike@cchtml.com> - 20.01-1
- Update to 20.01

* Mon Dec 02 2019 Michael Cronenworth <mike@cchtml.com> - 19.12-1
- Update to 19.12

* Sat Nov 02 2019 Michael Cronenworth <mike@cchtml.com> - 19.11-1
- Update to 19.11

* Fri Sep 13 2019 Michael Cronenworth <mike@cchtml.com> - 19.09-1
- Update to 19.09

* Sun Aug 04 2019 Michael Cronenworth <mike@cchtml.com> - 19.08-1
- Update to 19.08

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Michael Cronenworth <mike@cchtml.com> - 19.03-1
- Update to 19.03

* Thu Feb 28 2019 Michael Cronenworth <mike@cchtml.com> - 19.02-1
- Initial spec file.

