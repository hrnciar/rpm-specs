%global srcname tasklib
%global sum Python Task Warrior library

Name:           python-%{srcname}
Version:        1.3.0
Release:        2%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests
BuildRequires:  python3-tzlocal
BuildRequires:  python3-six
BuildRequires:  python3-pytz
BuildRequires:  task


%description
tasklib is a Python library for interacting with taskwarrior databases, using a
queryset API similar to that of Django’s ORM.

Supports Python 2.6, 2.7, 3.2, 3.3 and 3.4 with taskwarrior 2.1.x and above.
Older versions of taskwarrior are untested and may not work.

%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       task
Requires:       python3-tzlocal  python3-six python3-pytz
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
tasklib is a Python library for interacting with taskwarrior databases, using a
queryset API similar to that of Django’s ORM.

Supports Python 2.6, 2.7, 3.2, 3.3 and 3.4 with taskwarrior 2.1.x and above.
Older versions of taskwarrior are untested and may not work.


%prep
%autosetup -n %{srcname}-%{version}
rm *egg-info -rf

%build
%py3_build

%install
%py3_install

# %{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.9

* Thu Apr 30 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.0-1
- Update to 1.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.1-1
- Update to 1.2.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.0-6
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 24 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.0-2
- Update requires

* Sun Dec 24 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.0-1
- Initial build

