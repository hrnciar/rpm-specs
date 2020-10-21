%global	peclName   gmagick
%global ini_name  40-%{peclName}.ini
%global upstream_version 2.0.5
%global upstream_prever  RC1

Summary:		Provides a wrapper to the GraphicsMagick library
Name:		php-pecl-%peclName
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:		3%{?dist}
License:		PHP
Source0:		http://pecl.php.net/get/%peclName-%{upstream_version}%{?upstream_prever}.tgz
Source1:		%peclName.ini
Patch0:         %{peclName}-bug78465.patch
URL:			http://pecl.php.net/package/%peclName
BuildRequires:	php-pear
BuildRequires:	php-devel >= 7
BuildRequires:	GraphicsMagick-devel >= 1.3.17
Requires:		php(zend-abi) = %{php_zend_api}
Requires:		php(api) = %{php_core_api}
Provides:		php-pecl(%peclName) = %{version}

Conflicts:	php-pecl-imagick
Conflicts:	php-magickwand


%description
%peclName is a php extension to create, modify and obtain meta information of
images using the GraphicsMagick API.

%prep
%setup -qc
cd %peclName-%{upstream_version}%{?upstream_prever}
%patch0 -p1 -b .bug78465

%build
cd %peclName-%{upstream_version}%{?upstream_prever}
phpize
%{configure} --with-%peclName
make %{?_smp_mflags}

%install
cd %peclName-%{upstream_version}%{?upstream_prever}

make install \
	INSTALL_ROOT=%{buildroot}

# Install XML package description
install -m 0755 -d %{buildroot}%{pecl_xmldir}
install -m 0664 ../package.xml %{buildroot}%{pecl_xmldir}/%peclName.xml
install -d %{buildroot}%{_sysconfdir}/php.d/
install -m 0664 %{SOURCE1} %{buildroot}%{_sysconfdir}/php.d/%{ini_name}


%check
php --no-php-ini \
	--define extension_dir=%{buildroot}%{php_extdir} \
	--define extension=gmagick.so \
	-m | grep %peclName


%files
%license %peclName-%{upstream_version}%{?upstream_prever}/LICENSE
%doc %peclName-%{upstream_version}%{?upstream_prever}/*.md
%{_libdir}/php/modules/%peclName.so
%{pecl_xmldir}/%peclName.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php.d/%{ini_name}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5~RC1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5~RC1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct  3 2019 Remi Collet <remi@remirepo.net> - 2.0.5~RC1-1
- update to 2.0.5RC1
- build for https://fedoraproject.org/wiki/Changes/php745
- add workaround to https://bugs.php.net/78465

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.11.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.10.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 2.0.4-0.9.RC1
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.8.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.7.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 2.0.4-0.6.RC1
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.5.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.4.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-0.3.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 2.0.4-0.2.RC1
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 2.0.4-0.1.RC1
- update to 2.0.4RC1
- rebuild for https://fedoraproject.org/wiki/Changes/php70
- spec cleanup
- fix license installation

* Thu Feb 25 2016 Remi Collet <remi@fedoraproject.org> - 1.1.7-0.6.RC2
- drop scriptlets (replaced by file triggers in php-pear #1310546)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-0.5.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 05 2015 Rex Dieter <rdieter@fedoraproject.org> 1.1.7-0.4.RC2
- rebuild (GraphicsMagick)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-0.3.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-0.2.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 1.1.7-0.1.RC2
- update to 1.1.7RC2
- rebuild for https://fedoraproject.org/wiki/Changes/Php56
- add numerical prefix to extension configuration file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.10.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.9.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 1.1.0-0.8.RC2
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.7.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 24 2012 Rex Dieter <rdieter@fedoraproject.org> 1.1.0-0.6.
- rebuild (GraphicsMagick)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.5.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 26 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 1.1.0-0.4.RC2
- Made pecl installation/deinstallation silent (bz#804919).

* Sat Mar 17 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 1.1.0-0.3.RC2
- Check module loading also for epel in single way. Thanks to Remi Collet for the hint.

* Sat Mar 10 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 1.1.0-0.2.RC2
- Skip %%check on epel5.

* Sat Mar 10 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 1.1.0-0.1.RC2
- Update to 1.1.0RC2 by request bz#751376

* Thu Jan 19 2012 Remi Collet <remi@fedoraproject.org> - 1.0.10-0.1.b1
- update to 1.0.10b1 for php 5.4
- add filter to avoid private-shared-object-provides

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7b1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0.7b1-9
- Fix FBFS f16-17. Bz#716217

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7b1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 10 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0.7b1-7
- Update to 1.0.7b1 version due to previous mentioned bug.

* Tue Aug 10 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0.5b1-6
- Add simple %%check section by suggestion from Remi Collet (http://pecl.php.net/bugs/17991).

* Mon Jul 26 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0.5b1-5
- Update to 1.0.5b1
- Add Conflicts: php-pecl-imagick - BZ#559675

* Sun Jan 31 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0.3b3-4
- Update to 1.0.3b3

* Tue Nov 3 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0.2b1-3
- Fedora Review started, thanks to Andrew Colin Kissa.
- Remove macros %%{__make} in favour to plain make.
- Add %%{?_smp_mflags} to make.

* Mon Oct 12 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0.2b1-2
- New version 1.0.2b1 - author include license text by my request. Thank you Vito Chin.
- Include LICENSE.

* Fri Oct 2 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0.1b1-1
- Initial release.
- License text absent, but I ask Vito Chin by email to add it into tarball.
