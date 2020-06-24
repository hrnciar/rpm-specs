Name:           gnome-pkg-tools
Version:        0.21.2
Release:        3%{?dist}
Summary:        Tools for the Debian GNOME Packaging Team

BuildArch:      noarch
License:        GPLv2+
URL:            http://packages.debian.org/unstable/%{name}
Source0:        http://ftp.de.debian.org/debian/pool/main/g/%{name}/%{name}_%{version}.tar.xz

BuildRequires:  perl-generators
Requires:       debhelper
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This package contains some tools useful for the Debian GNOME Packaging Team
including:
 * Documentation.
 * The list of team members.
 * A number of rules files for CDBS that are helpful for GNOME
   packages - but may also be useful for others.
This package is useful when building Debian packages on Fedora, for instance
via pbuilder.


%prep
%setup -q -n %{name}-%{version}


%build
# Nothing to build

%install
install -d %{buildroot}%{_datadir}/%{name}
install -pm 0644 pkg-gnome.team %{buildroot}%{_datadir}/%{name}/pkg-gnome.team
install -pm 0644 control.header  %{buildroot}%{_datadir}/%{name}/control.header
cp -a 1 %{buildroot}%{_datadir}/%{name}/1
install -Dpm 0755 desktop-check-mime-types %{buildroot}%{_bindir}/desktop-check-mime-types
install -Dpm 0755 dh/dh_gnome %{buildroot}%{_bindir}/dh_gnome
install -Dpm 0755 dh/dh_gnome_clean %{buildroot}%{_bindir}/dh_gnome_clean
install -Dpm 0755 dh/gnome.pm %{buildroot}%{perl_vendorlib}/Debian/Debhelper/Sequence/gnome.pm
install -Dpm 0644 dh/dh_gnome.1 %{buildroot}%{_mandir}/man1/dh_gnome.1
install -Dpm 0644 dh/dh_gnome_clean.1 %{buildroot}%{_mandir}/man1/dh_gnome_clean.1
install -Dpm 0644 debian/desktop-check-mime-types.1 %{buildroot}%{_mandir}/man1/desktop-check-mime-types.1

%files
%license debian/copyright
%{_bindir}/desktop-check-mime-types
%{_bindir}/dh_gnome
%{_bindir}/dh_gnome_clean
%{_datadir}/%{name}/
%{perl_vendorlib}/Debian/Debhelper/Sequence/gnome.pm
%{_mandir}/man1/dh_gnome.1*
%{_mandir}/man1/dh_gnome_clean.1*
%{_mandir}/man1/desktop-check-mime-types.1*


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.21.2-3
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Sandro Mani <manisandro@gmail.com> - 0.21.2-1
- Update to 0.21.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.21.1-3
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Sandro Mani <manisandro@gmail.com> - 0.21.1-1
- Update to 0.21.1

* Wed Nov 28 2018 Sandro Mani <manisandro@gmail.com> - 0.21-1
- Update to 0.21

* Mon Oct 22 2018 Sandro Mani <manisandro@gmail.com> - 0.20.3-1
- Update to 0.20.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.20.2-2
- Perl 5.28 rebuild

* Thu Feb 08 2018 Sandro Mani <manisandro@gmail.com> - 0.20.2-1
- Update to 0.20.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Sandro Mani <manisandro@gmail.com> - 0.20.1-1
- Update to 0.20.1

* Fri Dec 22 2017 Sandro Mani <manisandro@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Mon Oct 30 2017 Sandro Mani <manisandro@gmail.com> - 0.19.12-1
- Update to 0.19.12

* Fri Sep 15 2017 Sandro Mani <manisandro@gmail.com> - 0.19.11-1
- Update to 0.19.11

* Thu Aug 31 2017 Sandro Mani <manisandro@gmail.com> - 0.19.10-1
- Update to 0.19.10

* Fri Aug 04 2017 Sandro Mani <manisandro@gmail.com> - 0.19.9-1
- Update to 0.19.9

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Sandro Mani <manisandro@gmail.com> - 0.19.8-1
- Update to 0.19.8

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.19.7-4
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.19.7-2
- Perl 5.24 rebuild

* Mon Apr 25 2016 Sandro Mani <manisandro@gmail.com> - 0.19.7-1
- Update to 0.19.7

* Fri Feb 19 2016 Sandro Mani <manisandro@gmail.com> - 0.19.6-1
- Update to 0.19.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 27 2015 Sandro Mani <manisandro@gmail.com> - 0.19.5-1
- Update to 0.19.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.19.4-3
- Perl 5.22 rebuild

* Fri Sep 05 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.19.4-2
- Perl 5.20 rebuild

* Thu Sep 04 2014 Sandro Mani <manisandro@gmail.com> - 0.19.4-1
- Update to 0.19.4

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.19.3-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Sandro Mani <manisandro@gmail.com> - 0.19.3-3
- Add description

* Mon Feb 10 2014 Sandro Mani <manisandro@gmail.com> - 0.19.3-2
- Added gnome-policy.html to %%doc

* Sun Feb 9 2014 Sandro Mani <manisandro@gmail.com> - 0.19.3-1
- Initial package
