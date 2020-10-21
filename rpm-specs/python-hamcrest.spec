%global modname hamcrest
%global origname PyHamcrest

Name:           python-%{modname}
Version:        1.9.0
Release:        15%{?dist}
Summary:        Hamcrest matchers for Python

License:        BSD
URL:            https://github.com/hamcrest/PyHamcrest
Source0:        %{url}/archive/V%{version}/%{name}-%{version}.tar.gz

# https://github.com/hamcrest/PyHamcrest/commit/37a4d0dbeb9a92b959edfb9b1aceba4eaacf9f78
Patch0001:      0001-Add-boolean-matchers.patch
# https://github.com/hamcrest/PyHamcrest/commit/f71c3c6f8af716435b6d44c007d502b6fb362e20
Patch0002:      0002-Silence-warnings-from-tests-due-to-use-of-old-pytest.patch

BuildArch:      noarch

%global _description \
PyHamcrest is a framework for writing matcher objects, allowing you to\
declaratively define "match" rules. There are a number of situations where\
matchers are invaluable, such as UI validation, or data filtering, but it is\
in the area of writing flexible tests that matchers are most commonly used.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-mock
BuildRequires:  python3-six
Requires:       python3-six

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{origname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
# Drop coverage and other presets
mv pytest.ini pytest.ini~
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v

%files -n python3-%{modname}
%{python3_sitelib}/%{origname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-12
- Subpackage python2-hamcrest has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-2
- Rebuild for Python 3.6

* Mon Oct 03 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.9.0-1
- Update to 1.9.0

* Sun Aug 21 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.8.5-2
- Backport couple of upstream patches

* Fri Aug 19 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.8.5-1
- Initial package
