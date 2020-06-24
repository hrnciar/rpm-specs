%global libname tickit

# Unibilium by default, otherwise ncurses
%bcond_without unibilium

Name:           lib%{libname}
Version:        0.3.2
Release:        3%{?dist}
Summary:        Terminal Interface Construction Kit

License:        MIT
URL:            http://www.leonerd.org.uk/code/%{name}/
Source0:        %{url}/%{name}-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(Convert::Color)
BuildRequires:  perl(Convert::Color::XTerm)
BuildRequires:  perl(List::UtilsBy)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(termkey)
%if %{with unibilium}
BuildRequires:  pkgconfig(unibilium) >= 1.1.0
%else
BuildRequires:  ncurses-devel
%endif
# Tests
BuildRequires:  %{_bindir}/prove

%description
This library provides an abstracted mechanism for building interactive
full-screen terminal programs. It provides a full set of output drawing
functions, and handles keyboard and mouse input events.

%package devel
Summary:        Development files needed for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libtermkey-devel%{?_isa}
%if %{with unibilium}
Requires:       unibilium-devel%{?_isa}
%endif

%description devel
%{summary}.

%prep
%autosetup
rm -f src/linechars.inc src/xterm-palette.inc

%build
CFLAGS="%{__global_cflags}" LDFLAGS="%{__global_ldflags}" %make_build VERBOSE=1

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%check
CFLAGS="%{__global_cflags} -D_XOPEN_SOURCE" LDFLAGS="%{__global_ldflags}" make test VERBOSE=1
make examples

%files
%license LICENSE
%doc CHANGES examples
%{_libdir}/%{name}.so.2*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{libname}.h
%{_includedir}/%{libname}-*.h
%{_libdir}/pkgconfig/%{libname}.pc
%{_mandir}/man3/%{libname}_*.3*
%{_mandir}/man7/%{libname}.7*
%{_mandir}/man7/%{libname}_*.7*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.2-2
- Add unibilium to run-require for libtickit-devel

* Tue Jul 23 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.2-1
- Initial release
