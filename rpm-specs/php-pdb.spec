Name:           php-pdb
Version:        1.3.4
Release:        25%{?dist}
Summary:        PHP classes for manipulating Palm OS databases

License:        LGPLv2+
URL:            http://php-pdb.sourceforge.net/
Source0:        http://downloads.sourceforge.net/php-pdb/php-pdb-1_3_4.tar.gz

# Fix incorrect FSF addresses. Submitted upstream:
#   https://github.com/fidian/php-pdb/pull/5
Patch0:         php-pdb-licence.patch

BuildArch:      noarch

Requires:       php >= 4.0.1

%description
PHP-PDB is a set of PHP classes that manipulate Palm OS databases. It lets you
read, write, alter, and easily use data that is meant to be sent to or
retrieved from a handheld.

%prep
%setup -qn php-pdb
%patch0 -p1

%build
# nothing to do

%install

# install php-pdb library
install -m 0755 -d %{buildroot}%{_datadir}/php/php-pdb
install -p -m 644 -t %{buildroot}%{_datadir}/php/php-pdb php-pdb.inc

# install modules
install -m 0755 -d %{buildroot}%{_datadir}/php/php-pdb/modules
install -p -m 644 -t %{buildroot}%{_datadir}/php/php-pdb/modules modules/*.inc

%files
%{_datadir}/php/php-pdb
%doc pdb-test.php
%license doc/{COPYING,LEGAL}

%changelog
* Sun Feb 02 2020 Richard Fearn <richardfearn@gmail.com> 1.3.4-25
- Use %%doc / %%license

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Richard Fearn <richardfearn@gmail.com> 1.3.4-21
- Don't remove buildroot in %%install section

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> 1.3.4-18
- Remove unnecessary Group: tag, BuildRoot: tag, and %%clean section

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 06 2016 Richard Fearn <richardfearn@gmail.com> 1.3.4-15
- Fix incorrect FSF addresses

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Richard Fearn <richardfearn@gmail.com> 1.3.4-13
- Remove unnecessary %%defattr

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 29 2013 Richard Fearn <richardfearn@gmail.com> 1.3.4-10
- Install documentation in unversioned docdir (rhbz 994037)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May  1 2008 Richard Fearn <richard.fearn@gmail.com> 1.3.4-2
- update install args

* Sun Mar  2 2008 Richard Fearn <richard.fearn@gmail.com> 1.3.4-1
- initial packaging for Fedora

