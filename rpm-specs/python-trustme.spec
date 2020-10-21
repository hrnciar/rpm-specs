# what it's called on pypi
%global srcname trustme
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
You wrote a cool network client or server.  It encrypts connections using TLS.
Your test suite needs to make TLS connections to itself.  Uh oh.  Your test
suite probably doesn't have a valid TLS certificate.  Now what?  trustme is a
tiny Python package that does one thing: it gives you a fake certificate
authority (CA) that you can use to generate fake TLS certs to use in your
tests.  Well, technically they are real certs, they are just signed by your CA,
which nobody trusts.  But you can trust it.  Trust me.}

%bcond_without  tests


Name:           python-%{pkgname}
Version:        0.6.0
Release:        4%{?dist}
Summary:        #1 quality TLS certs while you wait, for the discerning tester
License:        MIT or ASL 2.0
URL:            https://github.com/python-trio/trustme
Source0:        %pypi_source
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
%if %{with tests}
BuildRequires:  %{py3_dist pytest pyopenssl service-identity cryptography idna}
%endif
%{?python_provide:%python_provide python3-%{pkgname}}


%description -n python3-%{pkgname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
%if %{defined el8}
# The upstream test suite uses cryptography's rfc4514_string method, which
# wasn't added until version 2.5.  RHEL 8 currently only provides version 2.3.
# https://cryptography.io/en/latest/changelog/?highlight=rfc4514_string#v2-5
%pytest --verbose -k "not (test_ca_custom_names or test_issue_cert_custom_names)"
%else
%pytest --verbose
%endif

%endif


%files -n python3-%{pkgname}
%license LICENSE LICENSE.MIT LICENSE.APACHE2
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Oct 07 2020 Carl George <carl@george.computer> - 0.6.0-4
- Remove explicit run time requires in favor of automatically generated ones

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.9

* Tue Mar 17 2020 Carl George <carl@george.computer> - 0.6.0-1
- Latest upstream

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Carl George <carl@george.computer> - 0.5.2-1
- Latest upstream

* Tue Apr 16 2019 Carl George <carl@george.computer> - 0.5.1-1
- Latest upstream

* Fri Feb 22 2019 Carl George <carl@george.computer> - 0.5.0-1
- Latest upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Carl George <carl@george.computer> - 0.4.0-1
- Initial package
