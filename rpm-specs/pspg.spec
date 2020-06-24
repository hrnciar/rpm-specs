Summary:	A unix pager optimized for psql
Name:		pspg
Version:	3.0.4
Release:	1%{?dist}
License:	BSD
URL:		https://github.com/okbob/%{name}
Source:		https://github.com/okbob/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	ncurses-devel readline-devel
BuildRequires:	gcc


%description
pspg is a unix pager optimized for psql. It can freeze rows, freeze
columns, and lot of color themes are included.


%prep
%setup -q


%build
%configure
%make_build


%install
%make_install


%files
%if 0%{?rhel} && 0%{?rhel} <= 6
%doc README.md LICENSE
%else
%license LICENSE
%doc README.md
%endif
%{_bindir}/*


%changelog
* Sat Apr 11 2020 Pavel Raiskup <praiskup@redhat.com> - 3.0.4-1
- new upstream release, per release notes:
  https://github.com/okbob/pspg/releases/tag/3.0.4
  https://github.com/okbob/pspg/releases/tag/3.0.3
  https://github.com/okbob/pspg/releases/tag/3.0.2
  https://github.com/okbob/pspg/releases/tag/3.0.1
  https://github.com/okbob/pspg/releases/tag/2.7.2
  https://github.com/okbob/pspg/releases/tag/2.7.1
  https://github.com/okbob/pspg/releases/tag/2.7.0
  https://github.com/okbob/pspg/releases/tag/2.6.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Pavel Raiskup <praiskup@redhat.com> - 2.6.6-1
- new upstream release, per release notes:
  https://github.com/okbob/pspg/releases/tag/2.6.5
  https://github.com/okbob/pspg/releases/tag/2.6.6
- Fix of drawing vertical cursor on last column when border is 0 or 1

* Sun Jan 05 2020 Pavel Raiskup <praiskup@redhat.com> - 2.6.4-1
- new upstream release, per release notes:
  https://github.com/okbob/pspg/releases/tag/2.6.2
  https://github.com/okbob/pspg/releases/tag/2.6.3
  https://github.com/okbob/pspg/releases/tag/2.6.4

* Sun Dec 15 2019 Pavel Raiskup <praiskup@redhat.com> - 2.6.1-1
- new upstream release, per release notes:
  https://github.com/okbob/pspg/releases/tag/2.6.1

* Sun Nov 24 2019 Pavel Raiskup <praiskup@redhat.com> - 2.6.0-1
- new upstream release, per release notes:
  https://github.com/okbob/pspg/releases/tag/2.6.0

* Tue Nov 19 2019 Pavel Raiskup <praiskup@redhat.com> - 2.5.5-1
- new upstream release, per release notes:
  https://github.com/okbob/pspg/releases/tag/2.5.3
  https://github.com/okbob/pspg/releases/tag/2.5.4
  https://github.com/okbob/pspg/releases/tag/2.5.5

* Sun Nov 03 2019 Pavel Raiskup <praiskup@redhat.com> - 2.5.2-1
- new upstream release, per release notes:
  https://github.com/okbob/pspg/releases/tag/2.5.2
  https://github.com/okbob/pspg/releases/tag/2.5.0
  https://github.com/okbob/pspg/releases/tag/2.1.8
  https://github.com/okbob/pspg/releases/tag/2.1.7

* Sat Oct 05 2019 Pavel Raiskup <praiskup@redhat.com> - 2.1.3-1
- new upstream release, per release notes:
  https://github.com/okbob/pspg/releases/tag/2.1.3
  https://github.com/okbob/pspg/releases/tag/2.1.2
  https://github.com/okbob/pspg/releases/tag/2.1.1
  https://github.com/okbob/pspg/releases/tag/2.1.0
  https://github.com/okbob/pspg/releases/tag/2.0.5
  https://github.com/okbob/pspg/releases/tag/2.0.4

* Thu Sep 19 2019 Pavel Raiskup <praiskup@redhat.com> - 2.0.3-1
- https://github.com/okbob/pspg/releases/tag/2.0.3
- https://github.com/okbob/pspg/releases/tag/2.0.2

* Mon Sep 09 2019 Pavel Raiskup <praiskup@redhat.com> - 2.0.1-1
- https://github.com/okbob/pspg/releases/tag/2.0.1

* Fri Sep 06 2019 Pavel Raiskup <praiskup@redhat.com> - 1.9.0-1
- new upstream release, per release notes:
  https://github.com/okbob/pspg/releases/tag/1.9.0
  https://github.com/okbob/pspg/releases/tag/1.7.2
  https://github.com/okbob/pspg/releases/tag/1.7.1
  https://github.com/okbob/pspg/releases/tag/1.7.0
  https://github.com/okbob/pspg/releases/tag/1.6.8
  https://github.com/okbob/pspg/releases/tag/1.6.7
  https://github.com/okbob/pspg/releases/tag/1.6.6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 09 2019 Pavel Raiskup <praiskup@redhat.com> - 1.6.5-1
- new upstream release, per release notes:
  https://github.com/okbob/pspg/releases/tag/1.6.5

* Thu Mar 21 2019 Pavel Raiskup <praiskup@redhat.com> - 1.6.4-1
- new upstream release, per release notes:
  https://github.com/okbob/pspg/releases/tag/1.6.4

* Thu Feb 28 2019 Pavel Raiskup <praiskup@redhat.com> - 1.6.3-4
- rebuild for libreadline.so.8

* Thu Feb 14 2019 Pavel Raiskup <praiskup@redhat.com> - 1.6.3-3
- review updates from rhbz#1677259

* Thu Feb 14 2019 Pavel Raiskup <praiskup@redhat.com> - 1.6.3-2
- cleanup before Fedora proposal

* Thu Nov 29 2018 Devrim Gündüz <devrim@gunduz.org> - 1.6.3
- Update to 1.6.3

* Mon Oct 15 2018 Devrim Gündüz <devrim@gunduz.org> - 1.6.1-1.1
- Rebuild against PostgreSQL 11.0

* Fri Sep 7 2018 Devrim Gündüz <devrim@gunduz.org> 1.6.1-1
- Update to 1.6.1, per #3626

* Thu Aug 23 2018 Devrim Gündüz <devrim@gunduz.org> 1.3.0-1
- Update to 1.3.0

* Fri Jul 27 2018 Devrim Gündüz <devrim@gunduz.org> 1.2.2-1
- Update to 1.2.2, per #3517

* Tue May 1 2018 Devrim Gündüz <devrim@gunduz.org> 1.1.1-1
- Update to 1.1.1, per #3315 ( RHEL 7 only)

* Sun Apr 29 2018 Devrim Gündüz <devrim@gunduz.org> 1.1.0-1
- Update to 1.1.0, per #3315

* Fri Mar 16 2018 Devrim Gündüz <devrim@gunduz.org> 1.0.0-1
- Update to 1.0.0, per #3210

* Mon Feb 12 2018 Devrim Gündüz <devrim@gunduz.org> 0.9.3-1
- Update to 0.9.3, per #3102.

* Fri Jan 12 2018 Devrim Gündüz <devrim@gunduz.org> 0.9.2-1
- Update to 0.9.2, per #3006 .

* Mon Dec 4 2017 Devrim Gündüz <devrim@gunduz.org> 0.7.5-1
- Update to 0.7.5, per #2932 .

* Sun Nov 26 2017 Devrim Gündüz <devrim@gunduz.org> 0.7.2-1
- Update to 0.7.2, per #2912.

* Fri Nov 17 2017 Devrim Gündüz <devrim@gunduz.org> 0.5-1
- Update to 0.5

* Fri Sep 15 2017 Devrim Gündüz <devrim@gunduz.org> 0.1-1
- Initial packaging for PostgreSQL RPM repository, based on the spec
  file written by Pavel. Fixes #2704
