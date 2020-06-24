# Fedora spec file for php-pecl-gearman
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#

%global gh_commit   1f1293c2fc0bc2aee90eb17fe571628cecdf97bf
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date     20160816
%global gh_owner    wcgallego
%global gh_project  pecl-gearman
%global with_tests  0%{?_with_tests:1}
%global with_zts    0%{!?_without_zts:%{?__ztsphp:1}}
%global pecl_name   gearman
%global ini_name    40-%{pecl_name}.ini

Name:		php-pecl-gearman
Version:	2.0.6
Release:	3%{?dist}
Summary:	PHP wrapper to libgearman

License:	PHP
URL:		https://github.com/%{gh_owner}/%{gh_project}
Source0:	https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{pecl_name}-%{version}%{?prever}-%{gh_short}.tar.gz

BuildRequires:	gcc
BuildRequires:	libgearman-devel > 1.1.0
BuildRequires:	php-devel
BuildRequires:	php-pear
# Required by phpize
BuildRequires:	autoconf, automake, libtool

Requires:	php(zend-abi) = %{php_zend_api}
Requires:	php(api) = %{php_core_api}

Provides:	php-%{pecl_name} = %{version}
Provides:	php-%{pecl_name}%{?_isa} = %{version}
Provides:	php-pecl(%{pecl_name}) = %{version}
Provides:	php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
This extension uses libgearman library to provide API for
communicating with gearmand, and writing clients and workers

Documentation: http://php.net/gearman


%prep
%setup -q -c
mv %{gh_project}-%{gh_commit} NTS
%{__php} -r '
  $pkg = simplexml_load_file("NTS/package.xml");
  $pkg->date = substr("%{gh_date}",0,4)."-".substr("%{gh_date}",4,2)."-".substr("%{gh_date}",6,2);
  $pkg->version->release = "%{version}";
  $pkg->asXML("package.xml");
'

# Fix lib directory
# https://github.com/wcgallego/pecl-gearman/pull/39
sed -e '/GEARMAN_LIB_DIR/s/lib/$PHP_LIBDIR/' -i NTS/config.m4

# Dont register tests on install
sed -e 's/role="test"/role="src"/' \
    %{?_licensedir:-e '/LICENSE/s/role="doc"/role="src"/' } \
    -i package.xml

# Upstream often forget to change this
extver=$(sed -n '/#define PHP_GEARMAN_VERSION/{s/.* "//;s/".*$//;p}' NTS/php_gearman.h)
if test "x${extver}" != "x%{version}"; then
   : Error: Upstream version is ${extver}, expecting %{version}.
   exit 1
fi

cat >%{ini_name} <<EOF
; enable %{pecl_name} extension
extension=%{pecl_name}.so
EOF

%if %{with_zts}
cp -pr NTS ZTS
%endif


%build
cd NTS
%{_bindir}/phpize
%configure --with-libdir=%{_lib} --with-php-config=%{_bindir}/php-config
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure --with-libdir=%{_lib} --with-php-config=%{_bindir}/zts-php-config
make %{?_smp_mflags}
%endif


%install
make -C NTS install INSTALL_ROOT=%{buildroot}

# Install XML package description
install -Dpm 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# install config file
install -Dpm644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

%if %{with_zts}
make -C ZTS install INSTALL_ROOT=%{buildroot}
install -Dpm644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

# Documentation
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

%if %{with_zts}
: Minimal load test for ZTS extension
%{__ztsphp} --no-php-ini \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}
%endif


%files
%license NTS/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%{php_ztsextdir}/%{pecl_name}.so
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%endif


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 2.0.6-2
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Sep  6 2019 Remi Collet <remi@remirepo.net> - 2.0.6-1
- update to 2.0.6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 2.0.5-3
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Remi Collet <remi@remirepo.net> - 2.0.5-1
- update to 2.0.5

* Wed Jun 27 2018 Remi Collet <remi@remirepo.net> - 2.0.4-1
- update to 2.0.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 2.0.3-5
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- update to 2.0.3

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- update to 2.0.2

* Tue Sep 20 2016 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1 for PHP 7
- use sources from https://github.com/wcgallego/pecl-gearman fork
- spec cleanup

* Wed Feb 10 2016 Remi Collet <remi@fedoraproject.org> - 1.1.2-4
- F24: drop scriptlets (replaced by file triggers in php-pear)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep  9 2014 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- update to 1.1.2
- cleanup and modernize the spec file
- build ZTS extension
- install doc in pecl_docdir

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 1.1.1-4
- rebuild for https://fedoraproject.org/wiki/Changes/Php56
- add numerical prefix to extension configuration file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 1.1.1-1
- update to 1.1.1
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Tom Callaway <spot@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Sat Aug 04 2012 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- update to 1.0.2
- add BR on libgearman-1.0, workaround for https://bugzilla.redhat.com/819209
- add missing provides php-pecl(gearman)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 19 2012 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1 for php 5.4
- add %%check for php extension
- add filter to fix private-shared-object-provides
- use %%setup -c because package.xml is outside the tree

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 12 2011 Jesse Keating <jkeating@redhat.com> - 0.7.0-5
- Rebuild for broken deps

* Mon Apr 11 2011 Paul Whalen <paul.whalen@senecac.on.ca> 0.7.0-4
- fix setup and package.xml install

* Mon Apr 11 2011 Paul Whalen <paul.whalen@senecac.on.ca> 0.7.0-3
- correct macros, add license to files

* Fri Apr 08 2011 Paul Whalen <paul.whalen@senecac.on.ca> 0.7.0-2
- correct package following pecl packaging guidelines

* Fri Mar 11 2011 Paul Whalen <paul.whalen@senecac.on.ca> 0.7.0-1
- Initial Packaging

