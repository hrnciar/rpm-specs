Name:           dh-make
# Squeeze
Version:        2.202001

Release:        1%{?dist}
Summary:        Tool that converts source archives into Debian package source

License:        GPLv3+
URL:            http://packages.qa.debian.org/d/dh-make.html
Source0:        http://ftp.de.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
BuildArch:      noarch
BuildRequires:      perl-generators

Requires:       debhelper
Requires:       dpkg-dev
Requires:       %{_bindir}/make

%description
This package allows you to take a standard (or upstream) source
package and convert it into a format that will allow you to build
Debian packages.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_datadir}/debhelper/dh_make/
install -m 755 dh_make %{buildroot}/%{_bindir}
cp -a lib/* %{buildroot}/%{_datadir}/debhelper/dh_make/

# Fix permissions of rules files
find %{buildroot}/%{_datadir}/debhelper/dh_make \
	-type f -name 'rules*' \
	-exec chmod 755 '{}' ';'

find %{buildroot}/%{_datadir}/debhelper/dh_make/debian \
	-type f -name '*.ex' \
	-exec chmod 755 '{}' ';'

mkdir -p %{buildroot}/%{_mandir}/man1
install -m 644 -p dh_make.1 %{buildroot}/%{_mandir}/man1

%files
%doc debian/README.Debian
%{_bindir}/dh_make
%{_mandir}/man1/*.1*
%dir %{_datadir}/debhelper
%{_datadir}/debhelper/dh_make

%changelog
* Sat Feb 29 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.202001-1
- Update to 2.202001 (#1808626)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.201903-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.201903-1
- Update to 2.201903 (#1771187)

* Sun Oct 13 2019 Sérgio Basto <sergio@serjux.com> - 2.201902-1
- Update to dh-make-2.201902 (#1742709)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.201801-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.201801-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Sérgio Basto <sergio@serjux.com> - 2.201801-1
- Update to 2.201801 (#1589433)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.201701-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.201701-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Sérgio Basto <sergio@serjux.com> - 2.201701-1
- Update to 2.201701 (#1527706)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.201608-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.201608-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Sérgio Basto <sergio@serjux.com> - 2.201608-1
- Update dh-make to 2.201608 (#1297114)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20140617-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 27 2015 Sérgio Basto <sergio@serjux.com> - 1.20140617-1
- Update to dh-make_1.20140617 (Debian 8 stable).
- Some spec clean up.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.61-2
- Perl 5.18 rebuild

* Thu May 23 2013 Oron Peled <oron@actcom.co.il> - 0.61-1
- Upstream bumped to latest Debian/wheezy version
- Update for 'dpkg >= 1.16.x' (Requires: dpkg-dev)
- Don't install the whole ./debian/ directory as doc, only README.Debian
- Fix permissions of all 'rules*' templates

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 18 2010 Oron Peled <oron@actcom.co.il> - 0.55-2
- Minor changes to spec file: glob man pages, don't specify compression.

* Sun Oct 10 2010 Oron Peled <oron@actcom.co.il> - 0.55-1
- Bump to Squeeze version (0.55) as per review.

* Sat Jul 17 2010 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.46-2
- Fix package during review (#591192)

* Tue May 11 2010 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.46-1
- First package
