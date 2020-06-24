Name:           fabtests
Version:        1.10.1
Release:        1%{?dist}
Summary:        Test suite for libfabric API
# include/jsmn.h and common/jsmn.c are licensed under MIT.
# All other source files permit distribution under BSD. Some of them
# additionaly expressly allow the option to be licensed under GPLv2.
# See the license headers in individual source files to see which those are.
License:        BSD and (BSD or GPLv2) and MIT
Url:            https://github.com/ofiwg/libfabric
Source:         https://github.com/ofiwg/libfabric/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Patch0:         0001-adjust-shebang-lines-in-rft_yaml_to_junit_xml-and-ru.patch
BuildRequires:  libfabric-devel >= %{version}
BuildRequires:  valgrind-devel
BuildRequires:  gcc

%description
Fabtests provides a set of examples that uses libfabric - a high-performance
fabric software library.

%prep
%setup -q
%patch0 -p2

%build
%configure --with-valgrind
make %{?_smp_mflags} V=1

%install
%make_install
# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

%files
%{_datadir}/%{name}/
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man7/*
%doc AUTHORS README
%license COPYING

%changelog
* Sat May 09 2020 Honggang Li <honli@redhat.com> - 1.10.1-1
- Rebase to upstream release v1.10.1

* Fri Apr 24 2020 Honggang Li <honli@redhat.com> - 1.10.0-1
- Rebase to upstream release v1.10.0

* Sun Apr 12 2020 Honggang Li <honli@redhat.com> - 1.10.0rc2-1
- Rebase to upstream release v1.10.0rc2

* Sat Apr 04 2020 Honggang Li <honli@redhat.com> - 1.10.0rc1-1
- Rebase to upstream release v1.10.0rc1

* Mon Mar 09 2020 Honggang Li <honli@redhat.com> - 1.9.1
- Rebase to upstream release v1.9.1

* Mon Feb 17 2020 Honggang Li <honli@redhat.com> - 1.9.1rc1-1
- Rebase to upstream release v1.9.1rc1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0rc1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Honggang Li <honli@redhat.com> - 1.9.0rc1-1
- Rebase to upstream release v1.9.0rc1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Honggang Li <honli@redhat.com> - 1.8.0-1
- Rebase to upstream release v1.8.0

* Mon Apr 15 2019 Honggang Li <honli@redhat.com> - 1.7.1-1
- Rebase to upstream release v1.7.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 31 2019 Honggang Li <honli@redhat.com> - 1.7.0-1
- Rebase to upstream release v1.7.0
- Resolves: bz1671197

* Tue Oct  9 2018 Honggang Li <honli@redhat.com> - 1.6.2-1
- Rebase to upstream release v1.6.2
- Resolves: bz1637336

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Honggang Li <honli@redhat.com> - 1.6.1-1
- Rebase to upstream release v1.6.1
- Resolves: bz1448975

* Thu May 10 2018 Honggang Li <honli@redhat.com> - 1.6.0-1
- Rebase to upstream release v1.6.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 11 2017 Honggang Li <honli@redhat.com> - 1.4.1-1
- Rebase to latest upstream release.
- Resolves: bz1428619

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov  8 2016 Honggang Li <honli@redhat.com> - 1.4.0-1
- Rebase to latest upstream release.

* Tue Apr 19 2016 Honggang Li <honli@redhat.com> - 1.3.0-3
- Provide precise license information.

* Thu Apr 14 2016 Honggang Li <honli@redhat.com> - 1.3.0-2
- Remove license comment in file section.
- Merge duplicated file entries.

* Thu Apr 14 2016 Honggang Li <honli@redhat.com> - 1.3.0-1
- Import fabtests for Fedora.
