# spec file for php-pear-File-Find
#
# Copyright (c) 2013-2014 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%global pear_name File_Find

Summary:        Class which facilitates the search of filesystems
Summary(fr):    Classe facilitant la recherche dans le système de fichiers
Name:           php-pear-File-Find
Version:        1.3.3
Release:        12%{?dist}
License:        PHP
URL:            http://pear.php.net/package/File_Find

Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
Source2:        xml2changelog

BuildRequires:  php-pear
BuildArch:      noarch

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pear(PEAR)
Requires:       php-pcre
Provides:       php-pear(%{pear_name}) = %{version}


%description
File_Find, created as a replacement for its Perl counterpart, also named
File_Find, is a directory searcher, which handles, globbing, recursive
directory searching, as well as a slew of other cool features.


%description -l fr
File_Find, créé comme un équivalent à son homologue perl, aussi nommé
Find_File, est un outil de recherche de répertoire qui gère les motifs,
les recherches récursives aussi bien que beaucoup d'autres fonctionnalités
sympathiques.


%prep
%setup -c -q
%{_bindir}/php -n %{SOURCE2} package.xml | tee CHANGELOG | head -n 5

cd %{pear_name}-%{version}
# package.xml is V2
mv ../package.xml %{name}.xml


%build
# Empty build section


%install
rm -rf %{buildroot} docdir

pushd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}

popd



%check
cd %{pear_name}-%{version}
%{__pear} \
   run-tests \
   -i "-d include_path=%{buildroot}%{pear_phpdir}:%{pear_phpdir}" \
   tests | tee ../tests.log

# run-tests doesn't set a return value
grep -q "7 PASSED TESTS" ../tests.log

%post
%{__pear} install --nodeps --soft --force --register-only %{pear_xmldir}/%{name}.xml >/dev/null || :


%postun
if [ "$1" -eq "0" ]; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only %{pear_name} >/dev/null || :
fi


%files
%doc CHANGELOG
%dir %{pear_phpdir}/File
%{pear_phpdir}/File/Find.php
%{pear_testdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Remi Collet <remi@fedoraproject.org> - 1.3.3-1
- Version 1.3.3 (stable) no code change (fixed archive)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 23 2012 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- Version 1.3.2 (stable) - API 1.3.0 (stable)

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 1.3.1-5
- rebuilt for new pear_testdir

* Fri Jul 27 2012 Remi Collet <Fedora@FamilleCollet.com> 1.3.1-4
- fix "Array to string conversion" (upstream bug #19530)
- fix FTBFS (#843253)
- spec cleanup

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 05 2010 Remi Collet <Fedora@FamilleCollet.com> 1.3.1-1
- upstream Version 1.3.1 (stable) - API 1.3.0 (stable)
- package.xml is now V2
- set timezone during build
- run tests in %%check

* Sat May 22 2010 Remi Collet <Fedora@FamilleCollet.com> 1.3.0-4
- spec cleanup
- rename File_Find.xml to php-pear-File-Find.xml

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Apr 04 2008 Remi Collet <Fedora@FamilleCollet.com> 1.3.0-1
- initial RPM

