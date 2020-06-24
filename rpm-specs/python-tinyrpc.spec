%global library tinyrpc
%global module tinyrpc

Name:       python-%{library}
Version:    1.0.3
Release:    3%{?dist}
Summary:    A modular RPC library
License:    MIT
URL:        https://github.com/mbr/%{library}

# tarball in pypy does not include tests
Source0:    https://github.com/mbr/%{library}/archive/%{version}.tar.gz

BuildArch:  noarch

%description
tinyrpc is a library for making and handling RPC calls in python.

%package -n python-%{library}-doc
Summary:   Documentation for tinyrpc library

%description -n python-%{library}-doc
Documentation for tinyrpc library

%package -n python3-%{library}
Summary:    A modular RPC library
%{?python_provide:%python_provide python3-%{library}}

BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-funcsigs
BuildRequires:  python3-gevent
BuildRequires:  python3-greenlet
BuildRequires:  python3-mock
BuildRequires:  python3-py
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-six
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-werkzeug
BuildRequires:  python3-zmq

Requires:  python3-gevent
Requires:  python3-greenlet
Requires:  python3-requests
Requires:  python3-six
Requires:  python3-werkzeug
Requires:  python3-zmq


%description -n python3-%{library}
tinyrpc is a library for making and handling RPC calls in python.

%package -n python3-%{library}-tests
Summary:    Tests for python2-tinyrpc library

Requires:  python3-funcsigs
Requires:  python3-gevent
Requires:  python3-greenlet
Requires:  python3-mock
Requires:  python3-py
Requires:  python3-pytest
Requires:  python3-requests
Requires:  python3-six
Requires:  python3-werkzeug
Requires:  python3-zmq
Requires:  python3-%{library} = %{version}-%{release}

%description -n python3-%{library}-tests
Tests for  python2-tinyrpc library

%prep
%autosetup -n %{library}-%{version} -S git
# requirements.txt is wrong, let's manage deps manually
rm -f requirements.txt

%build
%py3_build

# generate html docs
%{__python3} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf build/sphinx/html/.{doctrees,buildinfo}

%install
%py3_install
# Copy tests
mkdir -p %{buildroot}%%{python3_sitelib}/%{library}/tests
cp -r tests %{buildroot}%{python3_sitelib}/%{library}/tests

%check
export PYTHONPATH=.
# Disable test_dispatch because of https://github.com/mbr/tinyrpc/issues/75
py.test-3 -rs --ignore=tests/test_wsgi_transport.py --ignore=tests/test_dispatch.py

%files -n python-%{library}-doc
%license LICENSE
%doc build/sphinx/html README.rst

%files -n python3-%{library}
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-*.egg-info
%exclude %{python3_sitelib}/%{module}/tests

%files -n python3-%{library}-tests
%license LICENSE
%{python3_sitelib}/%{module}/tests

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 03 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.0.3-1
- Update to 1.0.3

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Alfredo Moralejo <amoralej@redhat.xom> - 1.0.1-1
- Update to 1.0.1
- Remove python2 subpackages as tinyrpc > 1 does not support python2.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Alfredo Moralejo <amoralej@redhat.com> - 0.9.1-4
- Remove python2 subpackages from Fedora.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-2
- Rebuilt for Python 3.7

* Wed Jun 06 2018 Alfredo Moralejo <amoralej@redhat.com> - 0.9.1-1
- Update to upstream version 0.9.1.

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5-7.20170523git1f38ac
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6.20170523git1f38ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5.20170523git1f38ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Lumír Balhar <lbalhar@redhat.com> - 0.5-4.20170523git1f38ac
- Move to the latest upstream commit
- Disable non-working tests
- Enable python3 subpackage

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Alfredo Moralejo <amoralej@redhat.com> 0.5-2
- Some fixes applied to spec.

* Thu Jan 12 2017 Alfredo Moralejo <amoralej@redhat.com> 0.5-1
- Initial spec
