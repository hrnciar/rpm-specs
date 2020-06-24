%global commit 55248db8f3492f98dd7cdf68a815b1cc65cfaead
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20200506

Name:           libvmi
Version:        0.13.0
Release:        1.%{commit_date}git%{short_commit}%{?dist}
Summary:        A library for performing virtual-machine introspection

License:        LGPLv3+
URL:            http://libvmi.com/
Source0:        https://github.com/%{name}/%{name}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
# Cannot presently build on other architectures.
ExclusiveArch: x86_64

BuildRequires:  cmake
BuildRequires:  gcc bison flex xen-devel fuse-devel
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(libvirt)

%description
LibVMI is a C library with Python bindings that makes it easy to monitor
the low-level details of a running virtual machine by viewing its memory,
trapping on hardware events, and accessing the vCPU registers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        utils
Summary:        Utilities which make use of %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
The %{name}-utils package contains a number of programs which make
use of %{name}.

%prep
%autosetup -n libvmi-%{commit} -p1

%build
%cmake .
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -delete -print
find %{buildroot}%{_libdir} -name '*.a' -delete -print

%ldconfig_scriptlets

%files
%license COPYING.LESSER
%doc README
%{_libdir}/libvmi.so.*

%files devel
%doc examples/*.c
%{_includedir}/%{name}/
%{_libdir}/libvmi.so
%{_libdir}/pkgconfig/libvmi.pc

%files utils
%{_bindir}/*

%changelog
* Fri May 08 2020 W. Michael Petullo <mike@flyn.org> - 0.13.0-1.20200506git55248db8
- Update to Git master, now called 0.13.0

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 0.11.0-18.20170706gite919365
- Rebuild (json-c)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-17.20170706gite919365
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-16.20170706gite919365
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-15.20170706gite919365
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-14.20170706gite919365
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 0.11.0-13.20170706gite919365
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-12.20170706gite919365
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 0.11.0-11.20170706gite919365
- Rebuilt for libjson-c.so.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-10.20170706gite919365
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-9.20170706gite919365
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 W. Michael Petullo <mike@flyn.org> - 0.11.0-8.20170706gite919365
- Bump Release so NVR is bigger than the previous release

* Thu Jul 06 2017 W. Michael Petullo <mike@flyn.org> - 0.11.0-1.20170706gite919365
- Update to Git master

* Thu Mar 16 2017 W. Michael Petullo <mike@flyn.org> - 0.11.0-7.20170214git1a85386
- Update to Git master

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-6.20170208gitd7d5714
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 09 2017 W. Michael Petullo <mike@flyn.org> - 0.11.0-5.20170208gitd7d5714
- Update to Git master
- Add utils sub-package

* Tue Jan 24 2017 W. Michael Petullo <mike@flyn.org> - 0.11.0-4.20170124git42cd3b2
- Update to Git master

* Tue Jan 24 2017 W. Michael Petullo <mike@flyn.org> - 0.11.0-3.20161206gitb4bf45e
- Build with Rekall support

* Wed Dec 21 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.11.0-2.20161206gitb4bf45e
- Bump Release so NVR is bigger than the previous release

* Mon Dec 19 2016 W. Michael Petullo <mike@flyn.org> - 0.11.0-1.20161206gitb4bf45e
- Update to Git master

* Sun Dec 11 2016 W. Michael Petullo <mike@flyn.org> - 0.11.0-2.20161202gitb9b020c
- Rebuild for Xen 4.8

* Mon Dec 05 2016 W. Michael Petullo <mike@flyn.org> - 0.11.0-1.20161202gitb9b020c
- New upstream release
- Fix incorrect version in previous log entry
- Remove patch merged upstream
- Fix Source0

* Tue Jul 12 2016 W. Michael Petullo <mike@flyn.org> - 0.11.0-1.20161003git5ad492c
- Initial package 
