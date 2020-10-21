%define prerelease r77
%define relcand rc2
%define realname xmpphp
%define REALNAME XMPPHP

Name:           php-%{realname}
Version:        0.1
Release:        0.24.%{relcand}.%{prerelease}%{?dist}
Summary:        XMPPHP is the successor to Class.Jabber.PHP

License:        GPLv2+
URL:            http://code.google.com/p/xmpphp/
Source0:        http://xmpphp.googlecode.com/files/%{realname}-%{version}%{relcand}-%{prerelease}.tgz

Patch0:         %{name}-php7.patch

BuildArch:      noarch

Requires:       php-curl
Requires:       php-date
Requires:       php-dom
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-session
Requires:       php-simplexml
Requires:       php-spl
Requires:       php-xml


%description
XMPPHP is the successor to Class.Jabber.PHP which can connect to XMPP
1.0 server (google talk, jabber.orgf, LJ Talk, etc, supports TLS,
several XML processing approaches and supported styles, persistent
connection, etc.


%prep
%setup -qn %{realname}-%{version}%{relcand}-%{prerelease}

%patch0 -p1


%build
# Empty build


%install
rm -rf %{buildroot}

# Library
mkdir -p %{buildroot}%{_datadir}/php/%{realname}
install -p -m 644 %{REALNAME}/*.php %{buildroot}%{_datadir}/php/%{realname}/

# Examples (for doc)
mkdir examples
cp -p *.php examples



%files
%doc README LICENSE examples
%{_datadir}/php/%{realname}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.24.rc2.r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.23.rc2.r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.22.rc2.r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.21.rc2.r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.20.rc2.r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.19.rc2.r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.18.rc2.r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.17.rc2.r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 26 2016 Remi Collet <remi@fedoraproject.org> - 0.1-0.16.rc2.r77
- add patch to drop dependency on "ereg"
- drop tests from package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.15.rc2.r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.14.rc2.r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.13.rc2.r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.12.rc2.r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jan 30 2013 Remi Collet <remi@fedoraproject.org> - 0.1-0.11.rc2.r77
- fix dependencies
- move tests in /usr/share/tests (outside include_path)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.10.rc2_r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.9.rc2_r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.8.rc2_r77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 03 2010 Rakesh Pandit <rakesh@fedoraproject.org> 0.1-0.7.rc2_r77
- Updated to 0.1rc2-r77

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.6.rc1_r70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.5.rc1_r70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan  8 2009 Rakesh Pandit <rakesh@fedoraproject.org> 0.1-0.4.rc1_r70
- Updated to 0.1rc1-r70

* Thu Dec  4 2008 Michael Schwendt <mschwendt@fedoraproject.org> 0.1-0.3.beta_r50
- Include unowned directories.

* Sat Aug 23 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.1-0.2.beta_r50
 - moved examples to doc

* Sat Aug 23 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.1-0.1.beta_r50
 - Updated to r50, fixed license tag

* Sun Jul 06 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.1-0.1.beta_r21
 - Initial package
