%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%define pear_name Auth_OpenID

Name: php-pear-Auth-OpenID
Version: 2.3.0
Release: 15%{?dist}
Summary: PHP OpenID
License: ASL 2.0
URL: http://www.janrain.com/openid-enabled
# php-pear-Auth-OpenID is now hosted on github
# https://github.com/openid/php-openid
# downloading the tarball and repacking it from 
# openid-php-openid-2.2.2-0-ga287b2d.tar.gz to php-openid-2.2.2.tar.bz2
Source0: php-openid-%{version}.tar.bz2

BuildArch: noarch
BuildRequires: php-pear >= 1:1.4.9-1.2
BuildRequires: python3
Requires: php-pear(PEAR)
Requires(post): php-pear
Requires(postun): php-pear
# Required for testing, but we need PHPUnit 1.x
#Requires: php-pear-PHPUnit >= 1.1.1
# part of the pear spec, but the version makes no sense
#Requires: php-pear-DB >= 1.80
Requires: php-pgsql
#Requires: php-sqlite
Requires: php-bcmath
Requires: php-pear-Net-Curl
Provides: php-pear(%{pear_name}) = %{version}
Provides: php-composer(openid/php-openid) = %{version}

# Add patch for php7 support
# Upstream PR: https://github.com/openid/php-openid/pull/130/commits/2bf7bafa5e21ed3c01624bd830d84f7e7c93ac34
Patch0: https://patch-diff.githubusercontent.com/raw/openid/php-openid/pull/130.patch

# This patch fixes the paths from Auth -> Auth_OpenID
Patch1: php-openid-2.2.2-requires-paths.patch

# This patch switches to python2 for a helper script
Patch2: php-pear-Auth-OpenID-2.3.0-python3.patch

%description
An implementation of the OpenID single sign-on authentication
protocol.

%prep
%setup -q -n php-openid-%{version}

# Fix the paths from Auth -> Auth_OpenID
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Fix template with correct content
mv Auth %{pear_name}
content=$(
echo -n " <dir name='/'>\\n"
for i in $(find %{pear_name} -type f); do
  echo -n "   <file baseinstalldir='/' name='$i' role='php' />\\n"
done
echo -n " </dir>\\n"
)
sed -e "s:%%(contents)s:$content:" -i admin/package2.xml

#
# needed so we can execute packagexml.py
#
chmod +x admin/packagexml.py
sed -i -e 's|/usr/bin/python|/usr/bin/python3|' admin/packagexml.py
admin/packagexml.py %{version} admin/package2.xml README > %{pear_name}.xml


%build

%install
mkdir -p %{buildroot}/%{pear_phpdir}/%{pear_name}/OpenID \
         %{buildroot}/%{pear_phpdir}/%{pear_name}/Yadis
pear install --nodeps --packagingroot %{buildroot} %{pear_name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{pear_name}.xml %{buildroot}%{pear_xmldir}

%post
pear install --nodeps --offline --soft --force --register-only \
  %{pear_xmldir}/%{pear_name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  pear uninstall --nodeps --ignore-errors --register-only \
  %{pear_name} >/dev/null || :
fi

%files
%doc NEWS COPYING README examples

%{pear_xmldir}/%{pear_name}.xml
%{pear_phpdir}/%{pear_name}

%changelog
* Fri Mar 06 2020 Kevin Fenzi <kevin@scrye.com> - 2.3.0-15
- Drop python2 from BuildRequires. Fixes #1807530

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Kevin Fenzi <kevin@scrye.com> - 2.3.0-11
- Fix FTBFS bug #1605443

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.3.0-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov  9 2017 Remi Collet <remi@remirepo.net> - 2.3.0-7
- fix FTBFS from Koschei fixing package.xml content

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Kevin Fenzi <kevin@scrye.com> - 2.3.0-4
- Add Provides: php-composer(openid/php-openid), fixes bug #1413465

* Thu Jul 14 2016 Kevin Fenzi <kevin@scrye.com> - 2.3.0-3
- Just drop mysql entirely.

* Tue Jul 12 2016 Kevin Fenzi <kevin@scrye.com> - 2.3.0-2
- Drop php-mysql requirement and replace with php-pear-MDB2-Driver-mysql

* Wed Jun 29 2016 Kevin Fenzi <kevin@scrye.com> - 2.3.0-1
- Update to 2.3.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 23 2013 Kevin Fenzi <kevin@scrye.com> 2.2.2-7
- Patch for CVE-2013-4701

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Kevin Fenzi <kevin@scrye.com> 2.2.2-5
- Fixed pear metadata directory location. Fixes FTBFS bug 914351

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 22 2011 Kurt Seifried <kurt@seifried.org> - 2.2.2-1
- Upgrade to 2.2.2
- Corrected file paths for Fedora
- Corrected chmod +x admin/packagexml.py

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug  1 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.1.1-6
- Change documentation handling to use %%doc.

* Wed Jul 30 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.1.1-5
- Upgrade to 2.1.1.
- Use php_dir instead of data_dir (Rakesh Pandit <rakesh.pandit@gmail.com>)
- Fix CRLF (Peter Lemenkov <lemenkov@gmail.com> & R. Pandit)

* Sun Feb 24 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.0.1-4
- Update to 2.0.1.
- Change license.
- PEAR install method has regressed, some manual fixes are neccessary.
- No testing done (needs too old PHPUnit).

* Sat Feb 23 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.2.3-3
- Update to 1.2.3.
- Dropped PHPUnit 1.x dependency.

* Mon Aug  6 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.2.2-2
- Update to 1.2.2.

* Thu Feb  1 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.2.1-1
- Initial build.

