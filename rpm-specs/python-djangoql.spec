%global srcname djangoql

Name:           python-%{srcname}
Version:        0.14.0
Release:        2%{?dist}
Summary:        DjangoQL: Advanced search language for Django

License:        MIT
URL:            https://github.com/ivelum/djangoql
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-django >= 1.8
BuildRequires:  python3-ply >= 3.8

%description
Advanced search language for Django, with auto-completion.
Supports logical operators, parenthesis, table joins,
works with any Django models.


%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-django >= 1.8
Requires:       python3-ply >= 3.8
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Advanced search language for Django, with auto-completion.
Supports logical operators, parenthesis, table joins,
works with any Django models.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build

%install
%py3_install

%check
export PYTHONPATH=$(pwd)
%{__python3} test_project/manage.py test core.tests

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Viliam Krizan <vkrizan@redhat.com> - 0.14.0-1
- New release 0.14.0 (#1851319)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Viliam Krizan <vkrizan@redhat.com> - 0.13.1-1
- Support for Django 3.0

* Tue Sep 10 2019 Viliam Krizan <vkrizan@redhat.com> - 0.13.0-2
- New release 0.13.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Viliam Krizan <vkrizan@redhat.com> 0.12.6-1
- New release 0.12.6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Viliam Krizan <vkrizan@redhat.com> 0.12.3-1
- New release 0.12.3

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.12.0-2
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Mon Nov 12 2018 Viliam Krizan <vkrizan@redhat.com> 0.12.0-1
- New release 0.12.0

* Wed Oct 24 2018 Viliam Krizan <vkrizan@redhat.com> 0.10.2-1
- New release 0.10.2
- .DS_Store files removed in upstream

* Wed Oct 24 2018 Viliam Krizan <vkrizan@redhat.com> 0.10.1-1
- New release 0.10.1
- Added tests

* Mon Oct 22 2018 Viliam Krizan <vkrizan@redhat.com> 0.10.0-1
- Initial packaging

