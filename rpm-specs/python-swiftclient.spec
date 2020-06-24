%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1

%global sname swiftclient

%global common_desc \
Client library and command line utility for interacting with Openstack \
Object Storage API.

Name:       python-swiftclient
Version:    3.9.0
Release:    1%{?dist}
Summary:    Client Library for OpenStack Object Storage API
License:    ASL 2.0
URL:        http://launchpad.net/python-swiftclient/
Source0:    https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:  noarch

%description
%{common_desc}

%package -n python3-%{sname}
Summary:    Client Library for OpenStack Object Storage API
%{?python_provide:%python_provide python3-swiftclient}
Obsoletes: python2-%{sname} < %{version}-%{release}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr

Requires:      python3-requests
Requires:      python3-six
Requires:      python3-keystoneclient

%description -n python3-%{sname}
%{common_desc}

%if 0%{?with_doc}
%package doc
Summary:    Documentation for OpenStack Object Storage API Client
Group:      Documentation

BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme

%description doc
Documentation for the client library for interacting with Openstack
Object Storage API.
%endif

%prep
%setup -q -n %{name}-%{upstream_version}

# Let RPM handle the dependencies
rm -rf *requirements.txt

%build
%{py3_build}

%install
%{py3_install}
# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s swift %{buildroot}%{_bindir}/swift-3

# Delete tests
rm -fr %{buildroot}%{python3_sitelib}/swiftclient/tests

%if 0%{?with_doc}
%{__python3} setup.py build_sphinx -b html
rm -rf doc/build/html/.{doctrees,buildinfo}

%{__python3} setup.py build_sphinx -b man
install -p -D -m 644 doc/build/man/*.1 %{buildroot}%{_mandir}/man1/
%endif

%files -n python3-%{sname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/swiftclient
%{python3_sitelib}/*.egg-info
%{_bindir}/swift
%{_bindir}/swift-3
%{_mandir}/man1/*

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif
%changelog
* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 3.9.0-1
- Update to upstream version 3.9.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.8.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Alfredo Moralejo <amoralej@redhat.com> 3.8.1-1
- Update to upstream version 3.8.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 3.7.0-1
- Update to 3.7.0

