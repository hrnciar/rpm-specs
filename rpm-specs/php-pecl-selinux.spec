# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%define pecl_name selinux
%global ini_name  40-%{pecl_name}.ini

Summary: SELinux binding for PHP scripting language
Name:    php-pecl-selinux
Version: 0.5.0
Release: 1%{?dist}
License: PHP
URL:     https://pecl.php.net/package/%{pecl_name}
Source:  https://pecl.php.net/get/%{pecl_name}-%{version}.tgz

BuildRequires: gcc
BuildRequires: php-devel >= 7.0.0
BuildRequires: php-pear
BuildRequires: libselinux-devel >= 2.0.80

Requires: php(zend-abi) = %{php_zend_api}
Requires: php(api) = %{php_core_api}

Provides: php-pecl(%{pecl_name}) = %{version}-%{release}


%description
This package is an extension to the PHP Hypertext Preprocessor.
It wraps the libselinux library and provides a set of interfaces
to the PHP runtime engine.
The libselinux is a set of application program interfaces towards in-kernel
SELinux, contains get/set security context, communicate security server,
translate between raw and readable format and so on.


%prep
%setup -c -q


%build
pushd %{pecl_name}-%{version}
%{_bindir}/phpize
%configure  --enable-selinux
make %{?_smp_mflags}
(echo "; Enable SELinux extension module"
 echo "extension=selinux.so") > %{ini_name}
popd


%install
pushd %{pecl_name}-%{version}
install -D -p -m 0755 modules/selinux.so %{buildroot}%{php_extdir}/selinux.so
install -D -p -m 0644 %{ini_name} %{buildroot}%{_sysconfdir}/php.d/%{ini_name}

# Install XML package description
%{__mkdir_p} %{buildroot}%{pecl_xmldir}
%{__install} -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
popd


%check
cd %{pecl_name}-%{version}
php -n \
    -d extension_dir=modules \
    -d extension=%{pecl_name}.so \
    --modules | grep %{pecl_name}


%files
%doc %{pecl_name}-%{version}/LICENSE %{pecl_name}-%{version}/README
%config(noreplace) %{_sysconfdir}/php.d/%{ini_name}
%{php_extdir}/selinux.so
%{pecl_xmldir}/%{name}.xml


%changelog
* Wed Apr 22 2020 Remi Collet <remi@remirepo.net> - 0.5.0-1
- update to 0.5.0 (stable)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 0.4.2-5
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 0.4.2-2
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 0.4.2-1
- update to 0.4.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Remi Collet <remi@remirepo.net> - 0.4.1-8
- undefine _strict_symbol_defs_build

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 0.4.1-7
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.4.1-4
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 0.4.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 0.4.1-1
- update to 0.4.1
- rebuild for https://fedoraproject.org/wiki/Changes/php70

* Thu Feb 25 2016 Remi Collet <remi@fedoraproject.org> - 0.3.1-18
- drop scriptlets (replaced by file triggers in php-pear) #1310546

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 0.3.1-14
- rebuild for https://fedoraproject.org/wiki/Changes/Php56
- add numerical prefix to extension configuration file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 0.3.1-11
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 19 2012 Remi Collet <remi@fedoraproject.org> - 0.3.1-8
- build against php 5.4
- add filter to fix private-shared-object-provides
- add %%check for php extension

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar  3 2010 KaiGai Kohei <kaigai@kaigai.gr.jp> - 0.3.1-5
- Rebuilt for package 

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Remi Collet <Fedora@FamilleCollet.com> - 0.3.1-2
- rebuild for new PHP 5.3.0 ABI (20090626)

* Thu Apr 16 2009 KaiGai Kohei <kaigai@kaigai.gr.jp> - 0.3.1-1
- The "permissive" tag was added to selinux_compute_av
- The selinux_deny_unknown() was added
- README is updated for the new features

* Thu Mar 12 2009 KaiGai Kohei <kaigai@kaigai.gr.jp> - 0.2.1-1
- Specfile to build RPM package is added.

* Thu Mar  5 2009 KaiGai Kohei <kaigai@kaigai.gr.jp> - 0.1.2-1
- The initial release of SELinux binding for PHP script language.
