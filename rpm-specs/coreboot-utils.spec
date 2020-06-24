Name:           coreboot-utils
Version:        4.11
Release:        2%{?dist}
Summary:        Various utilities from coreboot project

# superiotool is GPLv2+, rest is GPLv2
License:        GPLv2 and GPLv2+
URL:            https://www.coreboot.org/
Source0:        https://www.coreboot.org/releases/coreboot-%{version}.tar.xz
Source1:        https://www.coreboot.org/releases/coreboot-%{version}.tar.xz.sig
# https://review.coreboot.org/c/coreboot/+/39162
Patch1:		coreboot-utils-0001-msrtool-Fix-enum-type-declaration.patch
# backported from master
Patch2:		coreboot-utils-0002-cbfstool-Bump-C-version-to-C11.patch
BuildRequires:  gcc
BuildRequires:  pciutils-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Provides:       superiotool = %{version}-%{release}
Obsoletes:      superiotool <= 0

%description
coreboot is a Free Software project aimed at replacing the proprietary BIOS
(firmware) found in most computers. This package contains various utilities
used to develop and configure systems with coreboot.

%package devel
Summary: Headers for coreboot
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers used by projects using coreboot.

%prep
%autosetup -p1 -n coreboot-%{version}


%build
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/romcc romcc
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/cbmem
make %{?_smp_mflags} CFLAGS="%{optflags} -I../../src/commonlib/include -I../cbfstool/flashmap -include ../../src/commonlib/include/commonlib/compiler.h" -C util/ifdtool
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/cbfstool
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/amdfwtool
make %{?_smp_mflags} CFLAGS="%{optflags} -I../../src/commonlib/include" -C util/intelvbttool
# These need sys/io.h, notably missing on power64, aarch64 and probably more
%ifarch %{ix86} x86_64
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/ectool
make %{?_smp_mflags} CC="%{__cc} %{optflags}" -C util/superiotool
make %{?_smp_mflags} CFLAGS="%{optflags} -DCMOS_HAL=1 -I." -C util/nvramtool
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/inteltool
make %{?_smp_mflags} CFLAGS="%{optflags} -I." -C util/viatool
make %{?_smp_mflags} CFLAGS="%{optflags}" -C util/intelmetool
(cd util/msrtool && %configure && make %{?_smp_mflags})
(cd util/me_cleaner && %py3_build)
%endif


%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}
install -d %{buildroot}%{_mandir}/man1

# header files
install -d %{buildroot}%{_includedir}/coreboot/commonlib
install src/commonlib/include/commonlib/*.h %{buildroot}%{_includedir}/coreboot/commonlib

# ifdtool & viatool install targets try to install a nonexistent manpage...
install util/ifdtool/ifdtool %{buildroot}%{_bindir}
install util/cbfstool/cbfstool %{buildroot}%{_bindir}
install util/amdfwtool/amdfwtool %{buildroot}%{_bindir}
install util/intelvbttool/intelvbttool %{buildroot}%{_bindir}
install util/cbmem/cbmem %{buildroot}%{_bindir}
install util/romcc/romcc %{buildroot}%{_bindir}
install -pm644 util/romcc/romcc.1 %{buildroot}%{_mandir}/man1/
%ifarch %{ix86} x86_64
install -d %{buildroot}%{_sbindir}
make %{?_smp_mflags} DESTDIR=%{buildroot} PREFIX=%{_prefix} -C util/superiotool install
make %{?_smp_mflags} DESTDIR=%{buildroot} PREFIX=%{_prefix} -C util/nvramtool install
make %{?_smp_mflags} PREFIX=%{buildroot}/%{_prefix} -C util/ectool install
make %{?_smp_mflags} DESTDIR=%{buildroot} PREFIX=%{_prefix} -C util/inteltool install
install util/viatool/viatool %{buildroot}%{_bindir}
make %{?_smp_mflags} DESTDIR=%{buildroot} PREFIX=%{_prefix} -C util/intelmetool install
make -C util/msrtool DESTDIR=%{buildroot} PREFIX=%{_prefix} install
(cd util/me_cleaner && %py3_install)
install -pm644 util/me_cleaner/man/me_cleaner.1 %{buildroot}%{_mandir}/man1/
%endif

install -pm644 util/superiotool/README README.superiotool
install -pm644 util/superiotool/COPYING COPYING.superiotool
install -pm644 util/nvramtool/README README.nvramtool
install -pm644 util/nvramtool/COPYING COPYING.nvramtool
install -pm644 util/nvramtool/DISCLAIMER DISCLAIMER.nvramtool
install -pm644 util/romcc/COPYING COPYING.romcc
%ifarch %{ix86} x86_64
install -pm644 util/viatool/README README.viatool
install -pm644 util/msrtool/COPYING COPYING.msrtool
%endif


%files
%{_bindir}/*
%{_mandir}/man1/*
%ifarch %{ix86} x86_64
%{_mandir}/man8/*
%{_sbindir}/*
%endif
%doc README.superiotool COPYING.superiotool
%doc README.nvramtool COPYING.nvramtool DISCLAIMER.nvramtool
%doc COPYING.romcc
%ifarch %{ix86} x86_64
%doc README.viatool
%doc COPYING.msrtool
%{python3_sitelib}/*
%endif

%files devel
%{_includedir}/coreboot/commonlib/*.h

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.11-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Peter Lemenkov <lemenkov@gmail.com> - 4.11-1
- Update to the 4.11 release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Richard Hughes <richard@hughsie.com> - 4.10-1
- Update to the 4.10 release

* Tue Sep 10 2019 Richard Hughes <richard@hughsie.com> - 4.9-1
- Update to the 4.9 release

* Tue Sep 10 2019 Richard Hughes <richard@hughsie.com> - 4.8-7
- Include the commonlib headers needed by fwupd

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.8-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.8-2
- Rebuilt for Python 3.7

* Wed May 16 2018 Lubomir Rintel <lkundrak@v3.sk> - 4.8-1
- Update to the 4.8 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Peter Lemenkov <lemenkov@gmail.com> - 4.6-1
- Update to the 4.6 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Lubomir Rintel <lkundrak@v3.sk> - 4.5-2
- Fix power64 build

* Thu Dec 15 2016 Lubomir Rintel <lkundrak@v3.sk> - 4.5-1
- Update to the 4.5 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Lubomir Rintel <lkundrak@v3.sk> - 4.2-1
- Update to the 4.2 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-7.20150109git78c5d58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 10 2015 Lubomir Rintel <lkundrak@v3.sk> - 4.0-6.20150109git78c5d58
- Update to a Git snapshot
- Add many new tools

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 28 2014 Lubomir Rintel <lkundrak@v3.sk> - 4.0-3
- Patch around wrong addresses in licenses and bad permissions

* Mon Jan 27 2014 Lubomir Rintel <lkundrak@v3.sk> - 4.0-2
- Adjust comment on generating source tree
- Fix executable modes
- Fix superio provide versioning

* Sat Jan 25 2014 Lubomir Rintel <lkundrak@v3.sk> - 4.0-1
- Initial packaging
