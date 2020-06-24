Summary: Firmware Test Suite

Name:    fwts
Version: 20.02.00
Release: 2%{?dist}
# Asked upstream for inclusion of full license texts:
# https://bugs.launchpad.net/bugs/1712604
# The ACPICA code is licensed under both GPLv2 and Intel ACPI, a few
# files are licensed under the LGPL. Please see copyright file for details.
License: GPLv2 and LGPLv2 and (GPLv2 or Intel ACPI)
URL: https://wiki.ubuntu.com/FirmwareTestSuite
Source0: http://fwts.ubuntu.com/release/fwts-V%{version}.tar.gz
# Upstream refuses to remove -Werror: https://bugs.launchpad.net/bugs/1687052
Patch0: fwts-Remove-Werror-from-build.patch

Patch10:       0001-apica-Fix-symbol-visibility-and-declaration-issues.patch
Patch11:       fwts-20.02.00-json_0_14_compat.patch

BuildRequires: acpica-tools glib-devel glib2-devel glib json-c-devel libtool automake autoconf dkms kernel-devel git bison flex
BuildRequires: libbsd-devel
# The tests in this package only make sense on the below architectures.
ExclusiveArch: x86_64 %{arm} aarch64 s390x %{power64}

%description
Firmware Test Suite (FWTS) is a test suite that performs sanity checks on
Intel/AMD PC firmware. It is intended to identify BIOS and ACPI errors and if
appropriate it will try to explain the errors and give advice to help
workaround or fix firmware bugs. It is primarily intended to be a Linux-specific
firmware troubleshooting tool.

%prep
%autosetup -a 0 -c -p1

%build
autoreconf -ivf
%configure
%make_build

%check
%make_build check

%install
%make_install

%files
%{_bindir}/*
%{_datadir}/fwts*
%{_datadir}/bash-completion/completions/fwts*
%{_libdir}/*
%exclude %{_libdir}/fwts/*.so
%exclude %{_libdir}/fwts/*.la
%exclude %{_libdir}/fwts/*.a
%{_mandir}/*/*
%doc README
%doc README_ACPICA.txt
# README_SOURCE.txt is not useful in the binary package
# per-file specific copyright information:
%doc debian/copyright

%changelog
* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 20.02.00-2
- Rebuild (json-c)
- Add patch for compatibility with json-c 0.14

* Tue Mar 03 2020 Benjamin Berg <bberg@redhat.com> - 20.02.00-1
- New upstream release 20.02.00
  Resolves: #1690806
- Add patch to fix linking issues due to symbol visibility/declarations
  Resolves: #1799379

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.02.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 08 2019 Benjamin Berg <bberg@redhat.com> - 19.02.00-3
- Drop i686 support as it requires an i686 kernel build (#1735231)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.02.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Benjamin Berg <bberg@redhat.com> - 19.02.00-1
- New upstream release (19.02.00) (#1593747)
- Include upstream patches to fix linking issues (#1674912)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.06.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.06.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Benjamin Berg <bberg@redhat.com> - 18.06.02-1
- New upstream release 18.06.02 (#1593747)

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 18.01.00-2
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Tue Feb 06 2018 Benjamin Berg <bberg@redhat.com> - 18.01.00-1
- Package new upstream version 18.01.00.

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 17.09.00-2
- Rebuilt for libjson-c.so.3

* Mon Aug 21 2017 Benjamin Berg <bberg@redhat.com> - 17.09.00-1
- Initial package version for 17.09.00.

