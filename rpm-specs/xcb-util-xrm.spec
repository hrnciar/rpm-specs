%global libname xcb-xrm

Name:           xcb-util-xrm
Version:        1.3
Release:        6%{?dist}
Summary:        XCB utility functions for the X resource manager

License:        MIT
URL:            https://github.com/Airblader/xcb-util-xrm
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(x11)

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup

%build
autoreconf -vfi
%configure --disable-silent-rules --disable-static
%make_build

%install
%make_install
rm -vf %{buildroot}%{_libdir}/lib%{libname}.la

%check
make %{?_smp_mflags} check

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/lib%{libname}.so.*

%files devel
%{_includedir}/xcb/%(n=%{libname}; echo ${n//-/_}).h
%{_libdir}/lib%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3-1
- Update to 1.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.2-1
- Update to 1.2 (RHBZ #1398312)

* Fri Aug 12 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0-1
- Initial package
