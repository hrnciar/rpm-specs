%global libname domxml-php4-php5

Name:           php-%{libname}
Version:        1.21.2
Release:        16%{?dist}
Summary:        XML transition from PHP4 domxml to PHP5 dom module
Summary(fr):    Transition du XML de PHP4 domxml à PHP5 dom

License:        LGPLv3+
URL:            http://alexandre.alapetite.fr/doc-alex/domxml-php4-php5/
# wget -N http://alexandre.alapetite.fr/doc-alex/domxml-php4-php5/domxml-php4-to-php5.php.txt -O domxml-php4-to-php5.php
# grep Version domxml-php4-to-php5.php
# tar czf domxml-php4-php5-1.21.2.tar.gz domxml-php4-to-php5.php
Source0:        %{libname}-%{version}.tar.gz
BuildArch:      noarch

Requires:       php-xml >= 5.1

%description
XML transition from PHP4 domxml to PHP5 dom module.

%description -l fr
Transition du XML de PHP4 domxml à PHP5 dom.


%prep
%setup -qc

%{__sed} -i -e 's/\r//' *.php


%build
# nothing to build


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_datadir}/php/%{libname}
%{__install} -pm 0644 *.php $RPM_BUILD_ROOT%{_datadir}/php/%{libname}



%files
%{_datadir}/php/%{libname}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 05 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.21.2-1
- update to 1.21.2 (minor bugfix)

* Thu Jun 03 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.21.1-3
- fix URL

* Sat May 15 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.21.1-2
- fix License (review #590777)

* Sun Mar 14 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.21.1-1
- rename to php-domxml-php4-php5

* Mon Dec 21 2009 Eric "Sparks" Christensen <sparks@fedoraproject.org> - 1.21.1-1
- Initial package.
