Name:           crudini
Version:        0.9.3
Release:        3%{?dist}
Summary:        A utility for manipulating ini files

License:        GPLv2
URL:            https://github.com/pixelb/%{name}
Source0:        https://github.com/pixelb/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  diffutils
BuildRequires:  grep
%if 0%{?rhel} == 6 || 0%{?rhel} == 7
BuildRequires:  python2-devel
BuildRequires:  python-iniparse
Requires:       python-iniparse
%else
BuildRequires:  python3-devel
BuildRequires:  python3-iniparse >= 0.3.2
Requires:       python3-iniparse >= 0.3.2
%endif

Patch0:         crudini-el6.patch
Patch1:         crudini-py2.patch
Patch2:         crudini-py3.patch

%description
A utility for easily handling ini files from the command line and shell
scripts.

%prep
%setup -q
%if 0%{?rhel} == 6
%patch0 -p1
%endif
%if 0%{?rhel} == 6 || 0%{?rhel} == 7
%patch1 -p1
%else
%patch2 -p1
%endif

%build

%install
install -p -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
pushd tests
LC_ALL=en_US.utf8 ./test.sh
popd

%files
%doc README COPYING TODO NEWS example.ini
%{_bindir}/%{name}
%{_mandir}/man1/*


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Pádraig Brady <P@draigBrady.com> - 0.9.3-1
- Latest upstream: python 3 support

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Pádraig Brady <P@draigBrady.com> - 0.9-7
- Add missing test dependencies

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 03 2017 Pádraig Brady <P@draigBrady.com> - 0.9-1
- Latest upstream

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 23 2016 Pádraig Brady <P@draigBrady.com> - 0.8-1
- Latest upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 Pádraig Brady <pbrady@redhat.com> - 0.7-1
- Latest upstream
- Fixes race condition avoiding stale lock files and blocked edits

* Wed Jan 28 2015 Pádraig Brady <pbrady@redhat.com> - 0.5-1
- Latest upstream
- Fixes race condition causing stale lock files and blocked edits

* Mon Sep 08 2014 Pádraig Brady <pbrady@redhat.com> - 0.4-1
- Latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Jakub Ruzicka <jruzicka@redhat.com> - 0.3-2
- Added BuildRequires python-iniparse.

* Fri Mar 08 2013 Jakub Ruzicka <jruzicka@redhat.com> - 0.3-1
- New version 0.3 includes COPYING licence file.
- Improved description.
- Added python-iniparse dependency.
- Added tests check.

* Thu Mar 07 2013 Jakub Ruzicka <jruzicka@redhat.com> - 0.1-1
- Initial package release
