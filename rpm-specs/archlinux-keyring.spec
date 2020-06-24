Name:           archlinux-keyring
Version:        20200422
Release:        1%{?dist}
Url:            https://projects.archlinux.org/archlinux-keyring.git/
Source0:        https://projects.archlinux.org/%{name}.git/snapshot/%{name}-%{version}.tar.gz
# see https://wiki.archlinux.org/index.php/Pacman-key for introduction
License:        Public Domain
Summary:        GPG keys used by Arch distribution to sign packages
BuildArch:      noarch

BuildRequires:  keyrings-filesystem
Requires:       pacman-filesystem
Requires:       keyrings-filesystem

%description
A set of GPG keys used to sign packages in the Arch distribution,
which can be used to verify that downloaded Arch packages are
valid.

This package simply packages the GPG keyring as published by Arch
developers into an RPM package to allow for safe and convenient
installation on Fedora systems.

%prep
%setup -q


%build


%install
%make_install PREFIX=%{_prefix}
mkdir -p %{buildroot}%{_keyringsdir}/
ln -s %{_datadir}/pacman/keyrings/archlinux.gpg %{buildroot}%{_keyringsdir}/

%files
%{_datadir}/pacman/keyrings
%{_keyringsdir}/archlinux.gpg

%changelog
* Tue May 05 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20200422-1
- New upstream release (#1826747).

* Tue Mar 31 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20200108-1
- New upstream release (#1785315).

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20191219-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20191219-1
- New upstream release (#1785315).

* Sat Oct 19 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20191018-1
- New upstream release (#1747072).

* Sat Aug 17 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20190805-1
- New upstream release (#1595225).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20181003-1
- New upstream release (#1595225).

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180404-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 14 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20180404-1
- New upstream release (#1550956).

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180108-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20180108-1
- New upstream release (#1484591).

* Wed Oct 25 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20171020-1
- New upstream release (#1484591).

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170611-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20170611-1
- New upstream release (#1434187).

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161201-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 01 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20161201-1
- New upstream release (#1400727).

* Tue Nov 01 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20161101-1
- New upstream release (#1323372).

* Sun Mar 06 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20160215-1
- New upstream release (#1308758).

* Wed Feb 03 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20160123-1
- New upstream release (#1293177).

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151206-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 06 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20151206-1
- New upstream release (#1288831).

* Wed Jul 22 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20150605-1
- New upstream release (#1221589).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150212-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 14 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20150212-1
- New upstream release (#1192336).

* Wed Dec 24 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20141218-1
- New upstream release (#1176858).

* Wed Sep 10 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20140908-1
- New upstream release (#1140086).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140220-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20140220-1
- New upstream release (#1067847).

* Sun Jan 26 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20140124-1
- New upstream release (#1057981).

* Thu Jan 09 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20140108-1
- New upstream release (#1050849).

* Tue Oct 29 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20131027-1
- New upstream release (#1023895).

* Sun Sep 29 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20130926-1
- New upstream release (#1013091).
- Provide links to the keyring files in /usr/share/keyrings.

* Sun Aug 25 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20130818-2
- Add Url field and build section.
- Package accepted (#998690).

* Mon Aug 19 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20130818-1
- Initial packaging.
