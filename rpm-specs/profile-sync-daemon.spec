%global shortname psd

Name: profile-sync-daemon
Version: 6.42
Release: 2%{?dist}
Summary: Symlinks and syncs browser profile dirs to RAM thus reducing HDD/SDD calls
BuildArch: noarch

License: MIT
URL: https://github.com/graysky2/profile-sync-daemon
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: rsync
BuildRequires: systemd-rpm-macros

Requires: rsync

%description
Profile-sync-daemon (psd) is a tiny pseudo-daemon designed to manage your
browser's profile in tmpfs and to periodically sync it back to your physical
disc (HDD/SSD). This is accomplished via a symlinking step and an innovative
use of rsync to maintain back-up and synchronization between the two. One of
the major design goals of psd is a completely transparent user experience.


%prep
%autosetup -p1


%build
%make_build


%install
%make_install


%post
%systemd_user_post %{shortname}.service

%preun
%systemd_user_preun %{shortname}.service

%postun
%systemd_user_postun_with_restart %{shortname}.service


%files
%doc README.md
%license MIT LICENSE
%{_bindir}/%{name}
%{_bindir}/%{shortname}
%{_bindir}/%{shortname}-overlay-helper
%{_bindir}/%{shortname}-suspend-sync
%{_datadir}/%{shortname}/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_%{shortname}
%{_mandir}/man1/*.1*
%{_userunitdir}/*.{service,timer}


%changelog
* Wed Oct  7 23:30:38 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 6.42-2
- build(remove dep): do not requre 'systemd' explicitly

* Tue Oct  6 21:30:08 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 6.42-1
- build(update): 6.42

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 Christopher Meng <rpm@cicku.me> - 6.08-1
- Update to 6.08

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Christopher Meng <rpm@cicku.me> - 5.68-1
- Update to 5.68

* Wed Sep 17 2014 Christopher Meng <rpm@cicku.me> - 5.51-1
- Update to 5.51

* Wed Sep 10 2014 Christopher Meng <rpm@cicku.me> - 5.50-1
- Update to 5.50

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 20 2014 Christopher Meng <rpm@cicku.me> - 5.45.1-1
- Update to 5.45.1

* Sat Nov 09 2013 Christopher Meng <rpm@cicku.me> - 5.44-1
- Update to 5.44
    
* Sun Nov 03 2013 Christopher Meng <rpm@cicku.me> - 5.43-1
- Update to 5.43

* Mon Sep 16 2013 Christopher Meng <rpm@cicku.me> - 5.40.1-1
- Update to 5.40.1

* Mon Sep 02 2013 Christopher Meng <rpm@cicku.me> - 5.39-1
- Update to 5.39

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 25 2013 Christopher Meng <rpm@cicku.me> - 5.38.2-1
- Update to 5.38.2

* Sun Jun 16 2013 Christopher Meng <rpm@cicku.me> - 5.36.2-1
- Update to 5.36.2

* Wed May 29 2013 Christopher Meng <rpm@cicku.me> - 5.35-1
- Initial Package.
