%global __remake_config 1

Name:		mstflint
Summary:	Mellanox firmware burning tool
Version:	4.14.0
Release:	3%{?dist}
License:	GPLv2+ or BSD
Group:		Applications/System
Source: 	https://github.com/Mellanox/mstflint/releases/download/v4.14.0-3/mstflint-4.14.0-3.tar.gz
Patch3: 	extend-buffer.patch
Patch4: 	add-default-link-flags-for-shared-libraries.patch
Patch6: 	replace-mlxfwreset-with-mstfwreset-in-mstflint-message.patch
Url:		https://github.com/Mellanox/mstflint
BuildRequires:	libstdc++-devel, zlib-devel, libibmad-devel, gcc-c++, gcc
BuildRequires:  libcurl-devel, boost-devel, libxml2-devel, openssl-devel
%if %{__remake_config}
BuildRequires:  libtool, autoconf, automake
%endif
Obsoletes:	openib-mstflint <= 1.4 openib-tvflash <= 0.9.2 tvflash <= 0.9.0
ExcludeArch:	s390 s390x %{arm}
Requires:	python3

%description
This package contains firmware update tool, vpd dump and register dump tools
for network adapters based on Mellanox Technologies chips.

%prep
%setup -q -n mstflint-4.14.0-3
%patch3 -p1
%patch4 -p1
%patch6 -p1
find . -type f -iname '*.[ch]' -exec chmod a-x '{}' ';'
find . -type f -iname '*.cpp' -exec chmod a-x '{}' ';'

%build
%if %{__remake_config}
./autogen.sh
%endif
%configure --enable-fw-mgr
%make_build

%install
make DESTDIR=%{buildroot} install
# Remove the devel files that we don't ship
rm -fr %{buildroot}%{_includedir}
find %{buildroot} -type f -name '*.la' -delete
find %{buildroot} -type f -name '*.a' -delete

%files
%doc README
%_bindir/*
%{_sysconfdir}/mstflint
%{_libdir}/mstflint

%{_datadir}/mstflint
%{_mandir}/man1/*

%changelog
* Mon Jun 22 2020 Honggang Li <honli@redhat.com> - 4.14.0-3
- Rebase mstflint to latest upstream release v4.14.0-3

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 4.14.0-2
- Rebuilt for Boost 1.73

* Tue Mar 31 2020 Honggang Li <honli@redhat.com> - 4.14.0-1
- Rebase mstflint to latest upstream release v4.14.0-1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Honggang Li <honli@redhat.com> - 4.13.3-2
- Rebase mstflint to latest upstream release v4.13.3-2

* Sun Jan 05 2020 Honggang Li <honli@redhat.com> - 4.13.3-1
- Rebase mstflint to latest upstream release v4.13.3-1

* Thu Oct 17 2019 Honggang Li <honli@redhat.com> - 4.13.1-1
- Rebase mstflint to latest upstream release v4.13.1-1

* Wed Oct 02 2019 Honggang Li <honli@redhat.com> - 4.13.0-1
- Rebase mstflint to latest upstream release v4.13.0-1
- Resolves: bz1758011

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Honggang Li <honli@redhat.com> - 4.11.0-5
- Rebase mstflint to latest upstream release v4.11.0-4

* Fri Feb 22 2019 Honggang Li <honli@redhat.com> - 4.11.0-4
- Fix mstflint segment fault issue for ConnectX-5 HCA
- Resolves: 1679844

* Tue Feb 12 2019 Honggang Li <honli@redhat.com> - 4.11.0-3
- Rebase mstflint to latest upstream release v4.11.0-3
- Resolves: 1676338

* Fri Feb  1 2019 Honggang Li <honli@redhat.com> - 4.11.0-2
- Rebase mstflint to latest upstream release v4.11.0-2
- Resolves: bz1671710

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 4.10.0-3
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Honggang Li <honli@redhat.com> - 4.10.0-1
- Rebase to latest upstream release v4.10.0-1
- Resolves: bz1550400

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 4.8.0-4
- Rebuilt for Boost 1.66

* Fri Dec 15 2017 Honggang Li <honli@redhat.com> - 4.8.0-3
- Rebase mstflint to latest upstream release v4.8.0-2
- Resolves: bz1526293

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Honggang Li <honli@redhat.com> - 4.6.0-2
- Add man pages.
- Resolves: bz1427063

* Wed Feb 22 2017 Honggang Li <honli@redhat.com> - 4.6.0-1
- Rebase to latest upstream release 4.6.0.
- Update mstflint package from github.
- Resolves: bz1423970

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2.12.gd1edd58.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 24 2016 Honggang Li <honli@redhat.com> - 4.4.0-1.12.gd1edd58.1
- Rebase to latest upstream release 4.4.0-1.12.gd1edd58 (bz1369683).

* Fri Apr  8 2016 Honggang Li <honli@redhat.com> - 4.3.0-1.49.g9b9af70.1
- Rebase to latest upstream version 4.3.0-1.49.g9b9af70.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-0.47.gb1cdaf7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Doug Ledford <dledford@redhat.com> - 4.1.0-0.46.gb1cdaf7.1
- Update to latest upstream sources (enables ConnectX-4 support)
- Drop patch that no longer applies

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.11.g6961daa.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.0-0.10.g6961daa.1
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.9.g6961daa.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 3.0-0.8.g6961daa.1
- Fix FTBFS with -Werror=format-security (#1037207, #1106248)
- ExcludeArch: %%arm aarch64
- Cleanup spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.7.g6961daa.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 Doug Ledford <dledford@redhat.com> - 3.0-0.6.g6961daa.1
- Update to latest upstream version, which resovles some licensing issues
  on some of the source files

* Fri Aug 09 2013 Doug Ledford <dledford@redhat.com> - 3.0-0.5.gff93670.1
- Update to latest upstream version, which include ConnectIB support

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Doug Ledford <dledford@redhat.com> - 1.4-7
- The upstream tarball as provided is broken.  Clean up the tarball so
  the package builds properly

* Fri Jan 06 2012 Doug Ledford <dledford@redhat.com> - 1.4-6
- Initial import into Fedora

* Wed Oct 26 2011 Doug Ledford <dledford@redhat.com> - 1.4-5.el6
- Update to a version that will support the latest Mellanox CX3 hardware
- Resolves: bz748244

* Mon Aug 08 2011 Doug Ledford <dledford@redhat.com> - 1.4-4.el6
- Fix a bug in mmio space unmapping
- Resolves: bz729061
- Related: bz725016

* Fri Feb 19 2010 Doug Ledford <dledford@redhat.com> - 1.4-3.el6
- Don't include mtcr.h as we don't really expect anything to need Mellanox
  card register definitions except this program, and we already have the
  file.
- Change to ExcludeArch instead of ExclusiveArch so we build in all the right
  places.
- Related: bz543948

* Mon Jan 25 2010 Doug Ledford <dledford@redhat.com> - 1.4-2.el6
- Update to tarball from URL instead of from OFED
- Minor tweaks for pkgwrangler import
- Related: bz543948

* Sat Apr 18 2009 Doug Ledford <dledford@redhat.com> - 1.4-1.el5
- Update to ofed 1.4.1-rc3 version
- Related: bz459652

* Tue Apr 01 2008 Doug Ledford <dledford@redhat.com> - 1.3-1
- Update to OFED 1.3 final bits
- Related: bz428197

* Sun Jan 27 2008 Doug Ledford <dledford@redhat.com> - 1.2-2
- Obsolete the old openib-mstflint package

* Fri Jan 25 2008 Doug Ledford <dledford@redhat.com> - 1.2-1
- Initial import into CVS
- Related: bz428197

* Thu Jul 19 2007 - Vladimir Sokolovsky vlad@mellanox.co.il
- Initial Package, Version 1.2
