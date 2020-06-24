# Are licenses packaged using %%license?
%if 0%{?fedora} >= 22 || 0%{?rhel} >= 8
%global with_license 1
%endif # 0%%{?fedora} >= 22 || 0%%{?rhel} >= 8

# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir	%{_docdir}/%{name}-%{version}}

Name:		garmintools
Version:	0.10
Release:	17%{?dist}
Summary:	Tools for Garmin GPS-devices
%if 0%{?rhel} && 0%{?rhel} <= 5
%endif # 0%%{?rhel} && 0%%{?rhel} <= 5

License:	GPLv2+
URL:		https://%{name}.googlecode.com
Source0:	%{url}/files/%{name}-%{version}.tar.gz

# Fix for gpx_laps_hr_cad
# See:  https://code.google.com/p/garmintools/issues/detail?id=15
Patch0:		garmintools-0.10_gpx-laps-hr-cad.patch
# Fix for garmin_save_runs
# See:  https://code.google.com/p/garmintools/issues/detail?id=35
Patch1:		garmintools-0.10_fix-gcc-48.patch

%if 0%{?rhel} && 0%{?rhel} <= 5
%endif # 0%%{?rhel} && 0%%{?rhel} <= 5

BuildRequires:  gcc
BuildRequires:	libusb-devel
BuildRequires:	perl-generators
Requires:	%{_sysconfdir}/modprobe.d
Requires:	%{_sysconfdir}/udev/rules.d


%description
This software provides Linux users with the ability to communicate
with the Garmin Forerunner 305 via the USB interface.  It
implements all of the documented Garmin protocols as of Rev C
(May 19, 2006) over the USB physical link.

This means that if you have a Garmin with a USB connection to a PC,
you ought to be able to use this software to communicate with it.


%package	devel
Summary:	Development-files for %{name}
%if 0%{?rhel} && 0%{?rhel} <= 5
%endif # 0%%{?rhel} && 0%%{?rhel} <= 5

Requires:	%{name}%{?_isa}		== %{version}-%{release}
Requires:	libusb-devel%{?_isa}

%description	devel
This package contains files for developing application using
lib%{name}.


%prep
%setup -q
%patch0 -p1 -b .gpx_laps_hr_cad
%patch1 -p1 -b .fix-gcc-48


%build
%configure --disable-static

# Kill rpath.
%{__sed} -i -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g'	\
	-e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g'		\
	libtool

%{__make} %{?_smp_mflags}


%install
%if 0%{?rhel} && 0%{?rhel} <= 5
%{__rm} -rf %{buildroot}
%endif # 0%%{?rhel} && 0%%{?rhel} <= 5

%{__make} install DESTDIR=%{buildroot}

# We intentionally do NOT ship libtool-dumplings.
%{__rm} -f %{buildroot}%{_libdir}/*.{,l}a

# Install additional tools.
%{__install} -pm 0755 extras/fore2gmn.pl %{buildroot}%{_bindir}/fore2gmn

# Create needed dirs.
%{__mkdir} -p %{buildroot}%{_pkgdocdir}						\
	%{buildroot}%{_sysconfdir}/modprobe.d					\
	%{buildroot}%{_sysconfdir}/udev/rules.d

# Create needed config.
%{__cat} >> 51-garmin.rules << EOF
SYSFS{idVendor}=="091e", SYSFS{idProduct}=="0003", MODE="0666"
EOF

%{__cat} >> %{name}.conf << EOF
# stop garmin_gps serial from loading for USB garmin devices
blacklist garmin_gps
EOF

%{__install} -pm 0644 51-garmin.rules %{buildroot}%{_sysconfdir}/udev/rules.d
%{__install} -pm 0644 %{name}.conf %{buildroot}%{_sysconfdir}/modprobe.d

# Install documentation-files.
%{__install} -pm 0644 AUTHORS ChangeLog COPYING NEWS README TODO		\
	%{buildroot}%{_pkgdocdir}
%if 0%{?with_license}
%{__rm} -f %{buildroot}%{_pkgdocdir}/COPYING
%endif # 0%%{?with_license}

%post
/sbin/ldconfig
# Remove garmin_gps module if loaded, see README.
/sbin/rmmod garmin_gps &>/dev/null || :

%postun -p /sbin/ldconfig


%files
%config(noreplace) %{_sysconfdir}/modprobe.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/udev/rules.d/51-garmin.rules
%doc %dir %{_pkgdocdir}
%if 0%{?with_license}
%license COPYING
%else  # 0%%{?with_license}
%doc %{_pkgdocdir}/COPYING
%endif # 0%%{?with_license}
%doc %{_pkgdocdir}/README
%{_bindir}/fore2gmn
%{_bindir}/garmin_*
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/*.1*

%files		devel
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/NEWS
%doc %{_pkgdocdir}/TODO
%{_includedir}/garmin.h
%{_libdir}/lib%{name}.so


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Björn Esser <bjoern.esser@gmail.com> - 0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 30 2015 Björn Esser <bjoern.esser@gmail.com> - 0.10-7
- added needed stuff for el5

* Mon Jun 29 2015 Björn Esser <bjoern.esser@gmail.com> - 0.10-6
- re-import after unretirement (#1236294)
- added Patch0 and Patch1 as suggested in review

* Sat Jun 27 2015 Björn Esser <bjoern.esser@gmail.com> - 0.10-5.1
- unretire in Fedora (#1236294)

* Fri Feb 18 2011 Fabian Affolter <fabian@bernewireless.net> - 0.10-5
- Fixed build issue with libusb

* Sat Jul 17 2010 Fabian Affolter <fabian@bernewireless.net> - 0.10-4
- Rename garmintools to garmintools.conf to fix #615119

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.10-3
- Explicitly BR libgarmin-static in accordance with the Packaging
  Guidelines (libgarmin-devel is still static-only).

* Tue Sep 22 2009 Fabian Affolter <fabian@bernewireless.net> - 0.10-2
- Fixed ldconfig stuff
- Fixed ownership of files
- Fixed rpath

* Sat May 02 2009 Fabian Affolter <fabian@bernewireless.net> - 0.10-1
- Updated to new upstream version 0.10

* Thu Sep 11 2008 Fabian Affolter <fabian@bernewireless.net> - 0.09-2
- Fix spec file acc. #461849 Comment #1

* Wed Sep 10 2008 Fabian Affolter <fabian@bernewireless.net> - 0.09-1
- Initial spec for Fedora
