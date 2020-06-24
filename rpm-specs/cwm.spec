Summary: Calm Window Manager by OpenBSD project
Name: cwm
Version: 6.3
Release: 7%{?dist}
# The entire source code is licensed under ISC license, except queue.h which is
# BSD
License: ISC and BSD
Url: https://github.com/chneukirchen/cwm
Source0: http://chneukirchen.org/releases/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
Source2: LICENSE
BuildRequires: gcc
BuildRequires: pkgconf
BuildRequires: byacc
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama
BuildRequires: libXft-devel

%description
cwm (calm window manager) is a window manager for X11 which contains many
features that concentrate on the efficiency and transparency of window
management, while maintaining the simplest and most pleasant aesthetic.

This package contains a Linux port of the official project, which changes the
source for the port portion but doesn't touches the original functionality
provided by the original OpenBSD's project.

%prep
%setup -q
cp -a %{SOURCE2} .

%build
make %{?_smp_mflags}

%install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install
install -d %{buildroot}/%{_datadir}/xsessions
install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/xsessions

%files
%doc README
%license LICENSE
%{_bindir}/*
%{_datadir}/xsessions/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Bruno E. O. Meneguele <bmeneguele@gmail.com> - 6.3-4
- Add build requirement for gcc, since it was removed from buildroot and mock
  (BZ#1603731)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Bruno E. O. Meneguele <bmeneguele@gmail.com> - 6.3-2
- New source file

* Thu May 17 2018 Bruno E. O. Meneguele <bmeneguele@gmail.com> - 6.3-1
- New upstream (OpenBSD) package release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Bruno E. O. Meneguele <bmeneguele@gmail.com> - 6.2-1
- Initial package
