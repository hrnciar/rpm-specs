%global upstream_name pystalk

%if ! (0%{?fedora} || 0%{?rhel} > 7)
%bcond_without python2
%else
%bcond_with python2
%endif

Name:           python-%{upstream_name}
Version:        0.5.1
Release:        5%{?dist}
Summary:        Python client library for the beanstalkd work queue
License:        ISC
URL:            https://github.com/easypost/pystalk
Source0:        https://files.pythonhosted.org/packages/source/p/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
BuildArch:      noarch

%description
pystalk is an extremely simple client for beanstalkd.
It is compatible with both Python 2 and Python 3.
It was initially created for beancmd.
It does not support any asynchronous event loops
and has not been tested with gevent.
It's designed for simple, synchronous use.

%if %{with python2}
%package -n python2-%{upstream_name}
Summary:        Python 2 client library for the beanstalkd work queue
%{?python_provide:%python_provide python2-%{upstream_name}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
BuildRequires:  python2-mock
BuildRequires:  PyYAML
BuildRequires:  python2-attrs
BuildRequires:  python2-six
Requires:       PyYAML
Requires:       python2-attrs
Requires:       python2-six

%description -n python2-%{upstream_name}
pystalk is an extremely simple client for beanstalkd.
It is compatible with both Python 2 and Python 3.
It was initially created for beancmd.
It does not support any asynchronous event loops
and has not been tested with gevent.
It's designed for simple, synchronous use.
%endif

%package -n python%{python3_pkgversion}-%{upstream_name}
Summary:        Python %{python3_pkgversion} library for terminal coloring, styling, and positioning
%{?python_provide:%python_provide python%{python3_pkgversion}-%{upstream_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-attrs
BuildRequires:  python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-PyYAML
Requires:       python%{python3_pkgversion}-attrs
Requires:       python%{python3_pkgversion}-six

%description -n python%{python3_pkgversion}-%{upstream_name}
pystalk is an extremely simple client for beanstalkd.
It is compatible with both Python 2 and Python 3.
It was initially created for beancmd.
It does not support any asynchronous event loops
and has not been tested with gevent.
It's designed for simple, synchronous use.

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{upstream_name}
Summary:        Python %{python3_other_pkgversion} library for terminal coloring, styling, and positioning
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{upstream_name}}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-pytest
BuildRequires:  python%{python3_other_pkgversion}-PyYAML
BuildRequires:  python%{python3_other_pkgversion}-attrs
BuildRequires:  python%{python3_other_pkgversion}-six
Requires:       python%{python3_other_pkgversion}-PyYAML
Requires:       python%{python3_other_pkgversion}-attrs
Requires:       python%{python3_other_pkgversion}-six

%description -n python%{python3_other_pkgversion}-%{upstream_name}
pystalk is an extremely simple client for beanstalkd.
It is compatible with both Python 2 and Python 3.
It was initially created for beancmd.
It does not support any asynchronous event loops
and has not been tested with gevent.
It's designed for simple, synchronous use.
%endif

%prep
%setup -q -n %{upstream_name}-%{version}
rm -r *.egg-info

%build
%if %{with python2}
%py2_build
%endif
%py3_build
%if 0%{?with_python3_other}
%py3_other_build
%endif

%install
%if %{with python2}
%py2_install
%endif
%if 0%{?with_python3_other}
%py3_other_install
%endif
%py3_install

%check
%if %{with python2}
PYTHONPATH=. py.test-2.7 tests/unit/
%endif
PYTHONPATH=. pytest-%{python3_version} tests/unit/
%if 0%{?with_python3_other}
PYTHONPATH=. pytest-%{python3_other_version} tests/unit/
%endif

%if %{with python2}
%files -n python2-%{upstream_name}
%doc README.md
%license LICENSE.txt
%{python2_sitelib}/pystalk
%{python2_sitelib}/pystalk*.egg-info
%endif

%files -n python%{python3_pkgversion}-%{upstream_name}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/pystalk
%{python3_sitelib}/pystalk*.egg-info

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{upstream_name}
%doc README.md
%license LICENSE.txt
%{python3_other_sitelib}/pystalk
%{python3_other_sitelib}/pystalk*.egg-info
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-2
- Rebuilt for Python 3.8

* Thu Jul 04 2019 Dan Callaghan <dan.callaghan@opengear.com> - 0.5.1-1
- initial version
