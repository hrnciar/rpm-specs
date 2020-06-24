Name:           autoarchive
Version:        1.3.0
Release:        13%{?dist}
Summary:        A simple backup tool that uses tar

License:        GPLv3
URL:            http://autoarchive.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Fix tests. Cannot submit upstream as issue tracker is locked
Patch0:         autoarchive-1.3.0-fix_tests.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-mock

Requires:       lzma%{?_isa}
Requires:       tar%{?_isa}
Requires:       gzip%{?_isa}
Requires:       bzip2%{?_isa}
Requires:       xz%{?_isa}

%description
AutoArchive is a simple utility for making backups more easily. It
uses tar for creating archives. The idea of the program is that every 
information needed for making a backup is in one file - the archive 
spec file. Path to this file is passed as a parameter to 'aa' command 
which reads information from it and creates desired backup.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{_defaultdocdir}/%{name}-%{version}/

%check
pushd AutoArchive
%{__python3} tests/run_tests.py
popd

%files
%doc NEWS README README.sk
%license COPYING
%config(noreplace) %{_sysconfdir}/aa/
%{_mandir}/man?/*.*
%{_bindir}/autoarchive
%{_bindir}/aa
%{python3_sitelib}/AutoArchive/
%{python3_sitelib}/%{name}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-13
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-10
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.0-7
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 Adam Williamson <awilliam@redhat.com> - 1.3.0-1
- Update to 1.3.0
- Set LANG when calling setup.py (to fix build)
- Patch tests to run properly, enable tests

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 22 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-1
- Update to latest upstream release 1.2.1 (rhbz#1310010)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Apr 20 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Update to latest upstream version 1.1.1

* Sat Mar 01 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Update to latest upstream version 1.1.0

* Mon Aug 05 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-2
- Update pec file
- Fix FTBFS (#992000)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 02 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Update to latest upstream version 1.0.1

* Tue Feb 19 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-3
- Bogus date entry fix

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 07 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Update to new upstream version 1.0.0

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.5.2-4
- Rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Wed Aug 01 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.5.2-3
- Avoid UTF-8 in setup.cfg, distutils doesn't seem to like it.
- Drop example config from docs, it's now installed in %%{_sysconfdir}/aa.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.2-1
- Update to new upstream version 0.5.2

* Tue Feb 28 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.1-1
- Update to new upstream version 0.5.1

* Fri Feb 24 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-2
- Update to new upstream version 0.5.0

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Apr 03 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-1
- Update to new upstream version 0.3.1

* Mon Mar 28 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-2
- This package requires Python 3

* Sun Mar 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Update to new upstream version 0.3.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Mar 20 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Change man page compression format
- Add xz as a BR
- Update to new upstreaqm version 0.2.0

* Sun Jul 26 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-2
- Modify BR and requirements
- Switch from define to global
- Clean up macros and removed ./ 
- Readd COPYING

* Wed Apr 15 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Upstream renamed some parts from aa to autoarchive (symlinks)
- Add examples
- Update to new upstream version 0.1.2

* Sun Mar 22 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-2
- Fix issues from #473835

* Sun Nov 30 2008 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-1
- Initial package for Fedora
