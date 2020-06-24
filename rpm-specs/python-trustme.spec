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
Release:        2%{?dist}
Summary:        #1 quality TLS certs while you wait, for the discerning tester
License:        MIT or ASL 2.0
URL:            https://github.com/python-trio/trustme
Source0:        %pypi_source
BuildArch:      noarch


%description %{common_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pyOpenSSL
BuildRequires:  python%{python3_pkgversion}-service-identity
BuildRequires:  python%{python3_pkgversion}-cryptography
BuildRequires:  python%{python3_pkgversion}-idna
%endif
Requires:       python%{python3_pkgversion}-cryptography
Requires:       python%{python3_pkgversion}-idna
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose
%endif


%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE LICENSE.MIT LICENSE.APACHE2
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
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
