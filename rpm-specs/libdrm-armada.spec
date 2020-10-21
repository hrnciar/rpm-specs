%global _configure_disable_silent_rules 1

Name:		libdrm-armada
Version:	2.0.0
Release:	4.20190424git607c697%{?dist}
Summary:	DRM driver for Marvell Armada displays

License:	GPLv2 and MIT
URL:		http://git.arm.linux.org.uk/cgit/libdrm-armada.git/
# git clone http://git.arm.linux.org.uk/cgit/libdrm-armada.git/
# cd libdrm-armada
# git reset --hard 607c697
# autoreconf -fi
# ./configure
# make dist
Source0:	libdrm_armada-%{version}.tar.bz2

BuildRequires:	pkgconfig(libdrm)
BuildRequires:	gcc

%description
Marvell Armada libdrm buffer object management module.


%package devel
Summary:	Development files for libdrm-armada


%description devel
Development files for libdrm-armada.


%prep
%setup -q -n libdrm_armada-%{version}


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%{_libdir}/libdrm_armada.so.0*
%license COPYING


%files devel
%{_includedir}/libdrm
%{_libdir}/libdrm_armada.so
%{_libdir}/pkgconfig/libdrm_armada.pc
%exclude %{_libdir}/libdrm_armada.la


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2.20190424git607c697
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Lubomir Rintel <lkundrak@v3.sk> - 2.0.0-1.20190424git607c697
- Dropped the group tag
- Adjusted the release tag snapshot date

* Wed Apr 24 2019 Lubomir Rintel <lkundrak@v3.sk> - 2.0.0-1.20180720git607c697
- Initial packaging
