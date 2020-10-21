%global         srcname  aioresponses
%global         desc     Aioresponses is a helper to mock/fake web requests in the python\
aiohttp package. The purpose of this package is to provide an\
easy way  to test asynchronous HTTP requests.

Name:           python-%{srcname}
Version:        0.6.4
Release:        3%{?dist}
Summary:        Mock out requests made by ClientSession from aiohttp package

License:        MIT
URL:            https://github.com/pnuckowski/aioresponses
Source0:        %pypi_source

BuildArch:      noarch
# Since python-aiohttp excludes s390x we have to exclude it, as well
# See also:
# https://src.fedoraproject.org/rpms/python-aiohttp/blob/67855c61bee706fcd99305d1715aad02d898cbfc/f/python-aiohttp.spec#_22
# https://fedoraproject.org/wiki/EPEL/FAQ#RHEL_8.2B_has_binaries_in_the_release.2C_but_is_missing_some_corresponding_-devel_package._How_do_I_build_a_package_that_needs_that_missing_-devel_package.3F
%if %{defined el8}
ExcludeArch:    s390x
%endif


# required for py3_build macro
BuildRequires:  python3-devel

# from setup.py
BuildRequires: python3-pbr
BuildRequires: python3-aiohttp

## for tests
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-ddt
# Disable for now since asynctest currently doesn't support Python 3.9
# cf. https://github.com/pnuckowski/aioresponses/issues/162
#BuildRequires: python3-asynctest

%{?python_enable_dependency_generator}

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -p1 -n %{srcname}-%{version}

# disable one test that connects to httpbin.org
sed -i 's/def \(test_address_as_instance_of_url_combined_with_pass_through\)(/def skip_\1(/' tests/test_aioresponses.py

%build
%py3_build


%install
%py3_install

%check
# disable some tests for now because of broken asynctest dependency
rm tests/test_aioresponses.py

%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*-py*.egg-info/


%changelog
* Thu Sep 10 2020 Georg Sauthoff <mail@gms.tf> - 0.6.4-3
- EPEL8: exclude s390x because of aiohttp

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Georg Sauthoff <mail@gms.tf> - 0.6.4-1
- Skip asynctest dependency for Python 3.9
- bump to latest upstream

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-2
- Rebuilt for Python 3.9

* Fri May 01 2020  Georg Sauthoff <mail@gms.tf> - 0.6.3-1
- bump to latest upstream

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019  Georg Sauthoff <mail@gms.tf> - 0.6.1-2
- bump to latest upstream

* Sun Dec 08 2019  Georg Sauthoff <mail@gms.tf> - 0.6.1-1
- bump to latest upstream

* Fri Dec 06 2019 Georg Sauthoff <mail@gms.tf> - 0.6.0-4
- remove superfluous watchdog dependency

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Georg Sauthoff <mail@gms.tf> - 0.6.0-1
- initial packaging
