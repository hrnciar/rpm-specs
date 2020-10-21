Name:       yubikey-val
Version:    2.39
Release:    8%{?dist}
Summary:    The YubiKey Validation Server

License:    BSD
URL:        https://developers.yubico.com/yubikey-val
Source0:    https://developers.yubico.com/yubikey-val/Releases/yubikey-val-%{version}.tgz
# Apache config file
Source1:    yubikey-val.conf
# Remove --group from install
Patch0:     yubikey-val-install.patch
BuildArch:  noarch

BuildRequires:  httpd-devel
Requires:   httpd
Requires:   php php-curl php-pear php-pdo

%description
This is a server that validates Yubikey OTPs. It is written in PHP, for use
with web servers such as Apache

%package munin
Summary:    Munin plugins for the YubiKey Validation Server
Requires:   %{name} = %{version}-%{release}
Requires:   munin

%description munin
Munin plugins for the YubiKey Validation Server.

%prep
%setup -q
%patch0 -p1 -b .install

%build

%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_docdir}
chmod 644 $RPM_BUILD_ROOT%{_datadir}/*/*php
mkdir -p $RPM_BUILD_ROOT%{_httpd_confdir}
install -p -m 0644 %SOURCE1 $RPM_BUILD_ROOT%{_httpd_confdir}/yubikey-val.conf


%files
%license COPYING
%doc ChangeLog NEWS README doc/* ykval-db.sql
%dir %{_sysconfdir}/yubico
%dir %{_sysconfdir}/yubico/val
%config(noreplace) %attr(0640,root,apache) %{_sysconfdir}/yubico/val/ykval-config.php
%config(noreplace) %{_httpd_confdir}/yubikey-val.conf
%{_datadir}/yubikey-val/
%{_sbindir}/*
%{_mandir}/man1/*.1*

%files munin
%{_datadir}/munin/plugins/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.39-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.39-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.39-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@nwra.com> - 2.39-4
- Use upstream install locations
- Fix group of ykval-config.php
- Add apache config file
- Package munin plugins
- Add %%license

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Dennis Gilmore <dennis@ausil.us> - 2.10-1
- update to 2.10 security fix

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 06 2011 Dennis Gilmore <dennis@ausil.us> - 2.7-2
- Requires php-pdo
- remove -template from config file name

* Fri Sep 24 2010 Dennis Gilmore <dennis@ausil.us> - 2.7-1
- update to 2.7
- use macros

* Tue Aug 31 2010 Mike McGrath <mmcgrath@redhat.com> - 2.6-1
- Initial packaging
