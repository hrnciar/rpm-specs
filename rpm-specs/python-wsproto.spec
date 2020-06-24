# what it's called on pypi
%global srcname wsproto
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
wsproto is a pure-Python implementation of a WebSocket protocol stack.  It is
written from the ground up to be embeddable in whatever program you choose to
use, ensuring that you can communicate via WebSockets, as defined in RFC6455,
regardless of your programming paradigm.

wsproto does not provide a parsing layer, a network layer, or any rules about
concurrency.  Instead, it is a purely in-memory solution, defined in terms of
data actions and WebSocket frames.  RFC6455 and Compression Extensions for
WebSocket via RFC7692 are fully supported.

wsproto supports Python 2.7 and 3.5 or higher.}

%bcond_without  tests


Name:           python-%{pkgname}
Version:        0.14.1
Release:        6%{?dist}
Summary:        WebSockets state-machine based protocol implementation
License:        MIT
URL:            https://github.com/python-hyper/wsproto
Source0:        %pypi_source
BuildArch:      noarch


%description %{common_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-h11 >= 0.8.1
%endif
Requires:       python%{python3_pkgversion}-h11 >= 0.8.1
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
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose test
%endif


%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{libname}
%exclude %{python3_sitelib}/test
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Carl George <carl@george.computer> - 0.14.1-1
- Latest upstream

* Mon Feb 25 2019 Carl George <carl@george.computer> - 0.13.0-1
- Latest upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Carl George <carl@george.computer> - 0.12.0-1
- Initial package
