%global srcname msrest
%global common_description %{summary}.

Name:           python-%{srcname}
Version:        0.6.13
Release:        2%{?dist}
Summary:        The runtime library "msrest" for AutoRest generated Python clients

License:        MIT
URL:            https://github.com/Azure/msrest-for-python
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Disable tests requiring an Internet connection
Patch0:         %{name}-0.6.1-tests.patch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist aiodns}
BuildRequires:  %{py3_dist aiohttp}
BuildRequires:  %{py3_dist certifi}
BuildRequires:  %{py3_dist httpretty}
BuildRequires:  %{py3_dist isodate}
BuildRequires:  %{py3_dist pytest-asyncio}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist requests-oauthlib}
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist trio}
# Required for documentation
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist recommonmark}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  %{py3_dist sphinx}
BuildArch:      noarch

%description
%{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       %{py3_dist trio}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_description}


%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.


%prep
%autosetup -p1 -n %{srcname}-for-python-%{version}


%build
%py3_build

pushd doc/
sphinx-build-3 -b html -d _build/doctrees/ . _build/html/
rm _build/html/.buildinfo
popd


%install
%py3_install


%check
py.test-3


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/


%files doc
%doc doc/_build/html/
%license LICENSE.md


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.13-2
- Rebuilt for Python 3.9

* Fri Apr 17 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.13-1
- Update to 0.6.13

* Fri Jan 31 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.11-1
- Update to 0.6.11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.10-1
- Update to 0.6.10
- Spec cleanup
- Fix tests
- Add explicit dependency on trio (for async support)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.9-2
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.9-1
- Update to 0.6.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.6-1
- Update to 0.6.6
- Spec cleanup

* Mon Feb 04 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Tue Nov 13 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-6
- Fix typo in Requires for python-isodate

* Sun Nov 11 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-5
- Fix Requires for Fedora <= 27

* Sun Nov 11 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-4
- Fix comments

* Sat Nov 10 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-3
- Build documentation
- Fix BuildRequires for Fedora <= 27

* Sat Nov 10 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-2
- Enable dependency on python3-trio for Fedora >= 29 only

* Sat Nov 10 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1
