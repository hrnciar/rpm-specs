Name:           ansible-review
Version:        0.13.9
Release:        5%{?dist}
Summary:        Reviews Ansible playbooks, roles and inventory and suggests improvements
License:        MIT
URL:            https://github.com/willthames/ansible-review
Source0:        https://files.pythonhosted.org/packages/source/a/%{name}/%{name}-%{version}.tar.gz
# https://github.com/willthames/ansible-review/pull/85
Patch0:         ansible-review-0.13.9-ansible-2.4-inventory.patch
# https://github.com/willthames/ansible-review/pull/90
Patch1:         ansible-review-0.13.9-dict-size-changed.patch
BuildArch:      noarch

%global _description\
Tool to review Ansible playbooks, roles, and inventory and suggest improvements.

%description %_description

%package -n python3-%{name}

Summary:        %summary
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-nose
Requires:       python3-ansible-lint >= 3.4.19-2
Requires:       python3-appdirs
Requires:       python3-flake8
Requires:       python3-unidiff
Requires:       python3-yaml
# Runtime requirements also needed in the build to run tests:
BuildRequires:  python3-ansible-lint >= 3.4.19-2
BuildRequires:  python3-appdirs
BuildRequires:  python3-flake8
BuildRequires:  python3-unidiff
BuildRequires:  python3-yaml
%{?python_provide:%python_provide python3-%{name}}

%description  -n python3-%{name} %_description

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install
# Symlink old Python 3 command for compatibility
ln -s %{name} %{buildroot}%{_bindir}/%{name}-3

%check
nosetests-%{python3_version} -v test/

%files -n python3-%{name}
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-3
%{python3_sitelib}/ansiblereview
%{python3_sitelib}/ansible_review*.egg-info

%changelog
* Tue Jun 09 2020 Nils Philippsen <nils@redhat.com> - 0.13.9-5
- fix crash caused by removing elements while iterating over a dictionary

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.9-4
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 2019 Nils Philippsen <nils@redhat.com> - 0.13.9-2
- cope with how Ansible >= 2.4 deals with inventories internally

* Wed Dec 04 2019 Nils Philippsen <nils@redhat.com> - 0.13.9-1
- upstream bugfix release 0.13.9:
  https://github.com/willthames/ansible-review/blob/master/CHANGELOG.md#0139
- get rid of Python 2 support in the spec file
- sort deps

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.7-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.7-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Dan Callaghan <dcallagh@redhat.com> - 0.13.7-3
- fix tests when run in Python 2 and C locale

* Tue Jul 17 2018 Dan Callaghan <dcallagh@redhat.com> - 0.13.7-2
- remove unnecessary Python 3 fix

* Tue Jul 17 2018 Dan Callaghan <dcallagh@redhat.com> - 0.13.7-1
- upstream bug fix release 0.13.7:
  https://github.com/willthames/ansible-review/blob/master/CHANGELOG.md#0137

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13.4-7
- Rebuilt for Python 3.7

* Tue Jun 26 2018 Dan Callaghan <dcallagh@redhat.com> - 0.13.4-6
- add Conflicts to fix upgrade path when /usr/bin/ansible-review moves

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13.4-5
- Rebuilt for Python 3.7

* Tue Apr 03 2018 Dan Callaghan <dcallagh@redhat.com> - 0.13.4-4
- no longer building Python 2 bits in releases which have dropped Python 2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Jan Beran <jberan@redhat.com> - 0.13.4-2
- Python 2 binary package renamed to python2-ansible-review
- Python 3 subpackage

* Tue Oct 03 2017 Dan Callaghan <dcallagh@redhat.com> - 0.13.4-1
- upstream bug fix release 0.13.4, with ansible 2.4 compatibility:
  https://github.com/willthames/ansible-review/blob/master/CHANGELOG.md#0134

* Wed Jul 26 2017 Dan Callaghan <dcallagh@redhat.com> - 0.13.0-5
- depend on flake8 binary not package

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Timo Trinks <ttrinks@redhat.com> - 0.13.0-2
- RHBZ#1410896: depend on python-flake8

* Wed Dec 21 2016 Timo Trinks <ttrinks@redhat.com> - 0.13.0-1
- upstream release 0.13.0:
  https://github.com/willthames/ansible-review/blob/master/CHANGELOG.md#0130

* Tue Nov 08 2016 Timo Trinks <ttrinks@redhat.com> - 0.12.2-1
- upstream bug fix release 0.12.2:
  https://github.com/willthames/ansible-review/blob/master/CHANGELOG.md#0122

* Wed Aug 24 2016 Dan Callaghan <dcallagh@redhat.com> - 0.10.1-1
- upstream bug fix release 0.10.1:
  https://github.com/willthames/ansible-review/blob/master/CHANGELOG.md#0101

* Wed Aug 24 2016 Dan Callaghan <dcallagh@redhat.com> - 0.10.0-1
- upstream release 0.10.0:
  https://github.com/willthames/ansible-review/blob/master/CHANGELOG.md#0100

* Mon Aug 01 2016 Dan Callaghan <dcallagh@redhat.com> - 0.9.0-1
- upstream release 0.9.0
- use %%license properly

* Wed Jun 29 2016 Dan Callaghan <dcallagh@redhat.com> - 0.7.5-1
- updated to upstream release 0.7.5
- depend on ansible-lint >= 3.0, removed patch for 2.x compatibility

* Wed Jun 22 2016 Dan Callaghan <dcallagh@redhat.com> - 0.7.2-1
- initial version
