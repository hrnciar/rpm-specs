# -*-Mode: rpm-spec -*-

%global commit 0be512fb705831b55020e1eaf86eedba0eae4a75
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:     wev
Version:  1.0.1
Release:  0.20200730git%{shortcommit}%{?dist}
Summary:  A tool for debugging events on a sway Wayland window
License:  MIT
URL:      https://git.sr.ht/~sircmpwn/wev
Source0:  %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

%description
A tool for debugging events on a sway Wayland window,
analogous to the X11 tool xev.

%prep
%autosetup -n %{name}-%{commit}

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license LICENSE
%doc README.md

%changelog
* Wed Jul 29 2020 Bob Hepple <bob.hepple@gmail.com> - 1.0.1-0.20200730git0be512f
- changes per RHBZ#1860772

* Tue Jul 28 2020 Bob Hepple <bob.hepple@gmail.com> - 1.0.1-0.20200729git0be512f
- changes per RHBZ#1860772

* Mon Jul 27 2020 Bob Hepple <bob.hepple@gmail.com> - 1.0.1-0.20200727git0be512f
- Initial version of the package
