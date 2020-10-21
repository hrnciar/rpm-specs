# This spec file has been automatically updated
Version:        184
Release: 1%{?dist}
Name: cockpit-ostree
BuildArch: noarch
Summary: Cockpit user interface for rpm-ostree
License: LGPLv2+
Requires: cockpit-bridge >= 125
Requires: cockpit-system >= 125
# On RHEL Atomic 7, the package name is different (curiously not on CentOS Atomic)
%if 0%{?rhel} == 7
Requires: rpm-ostree-client
%else
Requires: rpm-ostree
%endif

# Download from https://github.com/cockpit-project/cockpit-ostree/releases
Source: cockpit-ostree-%{version}.tar.gz

%define debug_package %{nil}

%description
Cockpit component for managing software updates for ostree based systems.

%prep
%setup -n cockpit-ostree

%install
%make_install

# drop source maps, they are large and just for debugging
find %{buildroot}%{_datadir}/cockpit/ -name '*.map' | xargs rm --verbose

%files
%{_datadir}/cockpit/*

%changelog
* Mon Oct 12 2020 Martin Pitt <martin@piware.de> - 184-1

- NPM updates
- Release to Fedora 33

* Mon Oct 05 2020 Martin Pitt <martin@piware.de> - 183-3
- Rebuilt after accidental test release 999

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 183-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Martin Pitt <martin@piware.de> - 183-1

- Rewrite with PatternFly 4
- Send update availability to Overview Health notifications

* Sun Jun 14 2020 Martin Pitt <martin@piware.de> - 182-1

- Stop importing cockpit's deprecated base1/patternfly.css
- Use Red Hat font
- npm module updates

* Wed Mar 04 2020 Martin Pitt <martin@piware.de> - 181-1

- Fix building under NODE_ENV=production
- NPM updates
- Move translations to weblate
- Translation updates

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 180-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Martin Pitt <martin@piware.de> - 180-1

- timeline: Use PF4 inspired background color
- NPM dependency updates

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 179-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Martin Pitt <martin@piware.de> - 179-1
- Update to upstream 179 release

* Fri Jul 12 2019 Martin Pitt <martin@piware.de> - 178-1
- new upstream release: 178

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 176-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 Martin Pitt <martin@piware.de> - 176-1

- RPM spec fixes
- Drop python3 build requirement

* Thu Aug 02 2018 Martin Pitt <martin@piware.de> - 175-1

- Simplify spec file
- Adjust tests for new rpm-ostree on RHEL Atomic

* Thu Jul 19 2018 Martin Pitt <martin@piware.de> - 173-1

- Split out into a separate upstream project:
  https://github.com/cockpit-project/cockpit-ostree
  (rhbz#1603146)
- No behaviour changes
