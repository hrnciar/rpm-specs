Name:           ddpt
Version:        0.96
Release:        1%{?dist}
Summary:        Variant of the dd utility for SCSI/storage devices

License:        BSD
URL:            http://sg.danny.cz/sg/ddpt.html
Source0:        http://sg.danny.cz/sg/p/%{name}-%{version}.tgz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  sg3_utils-devel


%description
The ddpt utility is a variant of the standard Unix command dd which copies
files. The ddpt utility specializes in files that are block devices. For block
devices that understand the SCSI command set, finer grain control over the
copy may be available via a SCSI pass-through interface. Note that recent
(S)ATA disks can often be driven by SCSI commands due to SCSI to ATA
translation (SAT) implemented in the kernel.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc AUTHORS COPYING CREDITS ChangeLog README TODO doc/ddpt_examples.txt
%{_bindir}/%{name}*
%{_mandir}/man8/%{name}*.8*


%changelog
* Mon Mar 09 2020 Dan Horák <dan[at]danny.cz> - 0.96-1
- updated to 0.96 (#1590043)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 04 2015 Dan Horák <dan@danny.cz> - 0.95-1
- udpated to 0.95 (#1178331)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Dan Horák <dan@danny.cz> - 0.94-1
- udpated to 0.94 (#1085263)

* Fri Nov 15 2013 Dan Horák <dan@danny.cz> - 0.93-1
- udpated to 0.93 (#1030841)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 02 2013 Dan Horák <dan@danny.cz> - 0.92-5
- modernize spec
- rebuilt for aarch64 (#925243)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 18 2011 Dan Horák <dan@danny.cz> - 0.92-1
- initial Fedora package
