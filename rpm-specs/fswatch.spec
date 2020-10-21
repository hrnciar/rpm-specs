%global _hardened_build 1

Name:		fswatch
Version:	1.14.0
Release:	4%{?dist}
Summary:	A cross-platform file change monitor
License:	GPLv3+
URL:		https://github.com/emcrisostomo/fswatch
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: autoconf automake libtool
BuildRequires: gcc-c++ gcc gettext-devel

%description
%{name} is a cross-platform file change monitor.

%package devel
Summary:	Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and headers for lib%{name}.

%package static
Summary:	Static library for %{name}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static 
Static library (.a) of lib%{name}.

%prep
%autosetup -n %{name}-%{version}

%build
./autogen.sh
%configure
%make_build

%install
%make_install
mkdir $RPM_BUILD_ROOT%{_mandir}/man1/
mv $RPM_BUILD_ROOT%{_mandir}/man7/%{name}.7 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/*

%find_lang %{name}

%check
make check

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md README.linux AUTHORS NEWS CONTRIBUTING.md ABOUT-NLS
%license COPYING
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*

%files devel
%doc README.libfswatch.md AUTHORS.libfswatch NEWS.libfswatch
%{_libdir}/lib%{name}.so
%{_includedir}/lib%{name}/*

%files static
%{_libdir}/*.a

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Darryl T. Agostinelli <dagostinelli@gmail.com> 1.14.0-3
- Corrections made for package review process

* Sun May 03 2020 Darryl T. Agostinelli <dagostinelli@gmail.com> 1.14.0-2
- Corrections made for package review process

* Sat Apr 11 2020 Darryl T. Agostinelli <dagostinelli@gmail.com> 1.14.0-1
- Created the .spec file for version 1.14.0
