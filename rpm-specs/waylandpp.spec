Name:           waylandpp
Version:        0.2.7
Release:        3%{?dist}
Summary:        Wayland C++ bindings

# waylandpp includes part of Wayland under MIT, wayland-scanner++ is GPLv3+
License:        BSD and MIT and GPLv3+
URL:            https://github.com/NilsBrause/%{name}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Fix pugixml detection during build
Patch0:         %{name}-0.2.7-pugixml.patch
Patch1:		%{name}-0.2.7-gcc10.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  mesa-libEGL-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pugixml-devel

%description
Wayland is an object oriented display protocol, which features request and
events. Requests can be seen as method calls on certain objects, whereas events
can be seen as signals of an object. This makes the Wayland protocol a perfect
candidate for a C++ binding.

The goal of this library is to create such a C++ binding for Wayland using the
most modern C++ technology currently available, providing an easy to use C++ API
to Wayland.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
The %{name}-doc package contains development documentation for %{name}.


%prep
%autosetup -p0


%build
%cmake . -DCMAKE_INSTALL_DOCDIR=%{_defaultdocdir}/%{name}-doc/
%make_build


%install
%make_install

# Drop LaTeX documentation (HTML documentation is already built)
rm -r $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-doc/latex/


%check
ctest -V %{?_smp_mflags}


%files
%doc README.md
%license LICENSE
%{_libdir}/*.so.*


%files devel
%doc example/
%{_bindir}/wayland-scanner++
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/%{name}/
%{_mandir}/man3/*.3.*


%files doc
%doc README.md
%license LICENSE
%{_defaultdocdir}/%{name}-doc/*


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 0.2.7-2
- Fix missing #include for gcc-10

* Wed Dec 04 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.7-1
- Update to 0.2.7

* Fri Aug 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.5-1
- Update to 0.2.5

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 08 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Tue Mar 06 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.2-2
- Fix License tag
- Fix documentation installation path

* Mon Mar 05 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.2-1
- Initial RPM release
