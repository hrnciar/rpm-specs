%global         srcname  zeep
%global         desc     Zeep inspects the WSDL document and generates the corresponding\
code to use the services and types in the document. This\
provides an easy to use programmatic interface to a SOAP server.

Name:           python-%{srcname}
Version:        3.4.0
Release:        8%{?dist}
Summary:        A fast and modern Python SOAP client

License:        MIT and BSD
URL:            https://github.com/mvantellingen/python-zeep
Source0:        %pypi_source

# Can probably dropped in releases > 3.4.0 as the changes are already
# present in the master branch
Patch0:         pytest-fix.diff

BuildArch:      noarch
# Since python-aiohttp excludes s390x we have to exclude it, as well
# (because python-aioresponses requires python aiohttp)
# See also:
# https://src.fedoraproject.org/rpms/python-aiohttp/blob/67855c61bee706fcd99305d1715aad02d898cbfc/f/python-aiohttp.spec#_22
# https://fedoraproject.org/wiki/EPEL/FAQ#RHEL_8.2B_has_binaries_in_the_release.2C_but_is_missing_some_corresponding_-devel_package._How_do_I_build_a_package_that_needs_that_missing_-devel_package.3F
%if %{defined el8}
ExcludeArch:    s390x
%endif

# required for py3_build macro
BuildRequires:  python3-devel

BuildRequires:  python3-setuptools


# from setup.py
BuildRequires: python3-appdirs
BuildRequires: python3-attrs
BuildRequires: python3-cached_property
BuildRequires: python3-defusedxml
BuildRequires: python3-isodate
BuildRequires: python3-lxml
BuildRequires: python3-requests
BuildRequires: python3-requests-toolbelt
BuildRequires: python3-six
BuildRequires: python3-pytz

## for tests
BuildRequires: python3-freezegun
BuildRequires: python3-mock
BuildRequires: python3-pretend
BuildRequires: python3-pytest-cov
BuildRequires: python3-pytest
BuildRequires: python3-requests-mock
BuildRequires: python3-pytest-tornado
BuildRequires: python3-aioresponses
BuildRequires: python3-pytest-asyncio
BuildRequires: python3-xmlsec
BuildRequires: python3-tornado

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

# disable linting dependencies and exact test dependencies
sed -i -e "s/\('\(isort\|flake\)\)/# \1/"  -e "s/\('[A-Za-z_-]\+\)==/\1>=/"  setup.py

%build
%py3_build


%install
%py3_install

%check
PYTHONPATH=src %{__python3} -m pytest tests

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst examples
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*-py*.egg-info/


%changelog
* Fri Sep 11 2020 Georg Sauthoff <mail@gms.tf> - 3.4.0-8
- add tornado dependency for tests
- cleanup dependencies

* Thu Sep 10 2020 Georg Sauthoff <mail@gms.tf> - 3.4.0-7
- EPEL8: exclude s390x because of aiohttp
- activate more tests

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Georg Sauthoff <mail@gms.tf> - 3.4.0-5
- Be more explicit regarding setuptools depenency,
  cf. https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GCPGM34ZGEOVUHSBGZTRYR5XKHTIJ3T7/

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Georg Sauthoff <mail@gms.tf> - 3.4.0-2
- fix date format

* Sun Dec 08 2019 Georg Sauthoff <mail@gms.tf> - 3.4.0-1
- bump to latest upstream

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Georg Sauthoff <mail@gms.tf> - 3.3.1-1
- initial packaging
