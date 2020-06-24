# -*-Mode: rpm-spec-mode; -*-

%global commit 9c3a4e7d66f44824abece72adb810f368d437525
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:     ydotool
Version:  0.1.9
Release:  0.2.20200405.git.%{shortcommit}%{?dist}
Summary:  Generic command-line automation tool (no X!)
License:  MIT
URL:      https://github.com/ReimuNotMoe/ydotool
Source0:  %{url}/archive/%{commit}/%{name}-%{version}.tar.gz

# This patch removes the static elements from the build and applies a
# version number to the shared library. To this date, upstream has
# not responded to a request to do this:
# https://github.com/ReimuNotMoe/ydotool/issues/60

# Create patch with:
# diff -rNu -x build ydotool-%%{version}-orig ydotool-%%{version}
Patch0:   ydotool-patch0-cmakelist.patch

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(evdevPlus) >= 0.1.1
BuildRequires: pkgconfig(uInputPlus) >= 0.1.4
BuildRequires: make
BuildRequires: scdoc
BuildRequires: systemd-rpm-macros

%description

Performs some of the functions of xdotool(1) without requiring X11 -
however, it generally requires root permission (to open /dev/uinput)

Currently implemented command(s):

- type - Type a string
- key - Press keys
- mousemove - Move mouse pointer to absolute position
- mousemove_relative - Move mouse pointer to relative position
- mouseup - Generate mouse up event
- mousedown - Generate mouse down event
- click - Click on mouse buttons
- recorder - Record/replay input events

N.B. optionally, you can start the ydotoold daemon with:

- systemctl enable ydotool
- systemctl start ydotool

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains header files for %{name}.

%prep
%autosetup -n %{name}-%{commit}
mkdir -p %{_target_platform}

%build
pushd %{_target_platform}
%cmake ..
popd
%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}

mkdir -p %{buildroot}/%{_unitdir}
install -p -m 0644 Daemon/%{name}.service %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man8
scdoc < manpage/%{name}.1.scd > %{buildroot}/%{_mandir}/man1/%{name}.1
scdoc < manpage/%{name}d.8.scd > %{buildroot}/%{_mandir}/man8/%{name}d.8
mkdir -p %{buildroot}/%{_includedir}/ydotool
find . -name '*.hpp' -exec cp --parents {} %{buildroot}/%{_includedir}/ydotool/ ';'

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_libdir}/lib%{name}.so.0*
%{_unitdir}/%{name}.service
%{_bindir}/%{name}*
%license LICENSE
%doc README.md
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man8/%{name}d.8.*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/

%changelog
* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 0.1.9-0.2.20200405.git.9c3a4e7
- Rebuilt for Boost 1.73

* Sun Apr 05 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.1.20200405.git.9c3a4e7
- Changes per RHBZ#1807753 - %{?systemd_requires} and ldconfig are no longer required

* Fri Apr 03 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.1.20200403.git.9c3a4e7
- Changes per RHBZ#1807753

* Wed Apr 01 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.1.20200401.git.9c3a4e7
- Changes per RHBZ#1807753

* Mon Mar 30 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.1.20200330.git.9c3a4e7
- Changes per RHBZ#1807753

* Sun Mar 22 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.1.20200322.git.9c3a4e7
- fix Source to get git tag directly

* Sat Feb 29 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.1.20200229.git.9c3a4e7
- Add a note on how to get source from upstream
- use lib*-devel packages in BuildRequires

* Tue Feb 18 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.9-0.1.20200218.git.9c3a4e7
- rebuild from head to pick up manuals & service file
- remove static build
- strip binaries (rpmlint complained about them)

* Mon Feb 17 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.8.20200211.3
- add BuildRequires: systemd-rpm-macros; add dist to release

* Sun Feb 16 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.8.20200211.2
- use %%_unitdir

* Sun Feb 16 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.8.20200211.1
- Initial version of the package
