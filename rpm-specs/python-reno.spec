%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name reno

# Currently, we cannot generate reno docs from a tarball due to
# https://bugs.launchpad.net/reno/+bug/1520096
%global with_docs 0

%global common_desc \
Reno is a release notes manager for storing \
release notes in a git repository and then building documentation from them. \
\
Managing release notes for a complex project over a long period \
of time with many releases can be time consuming and error prone. Reno \
helps automate the hard parts.

Name:           python-%{pypi_name}
Version:        3.0.1
Release:        1%{?dist}
Summary:        Release NOtes manager

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

%description
%{common_desc}

%package -n     python3-%{pypi_name}
Summary:        RElease NOtes manager
%{?python_provide:%python_provide python3-%{pypi_name}}
Obsoletes: python2-%{pypi_name} < %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-dulwich
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-sphinx

BuildRequires:  python3-PyYAML

Requires:  python3-pbr
Requires:  python3-dulwich
Requires:  git

Requires:  python3-PyYAML

%description -n python3-%{pypi_name}
%{common_desc}

%package -n python-%{pypi_name}-doc
Summary:        reno documentation
%description -n python-%{pypi_name}-doc
Documentation for reno

%prep
%autosetup -n %{pypi_name}-%{upstream_version}

%build
%{py3_build}

%install
%{py3_install}

%if 0%{?with_docs}
# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info

%files -n python-%{pypi_name}-doc
%if 0%{?with_docs}
%doc html
%endif
%license LICENSE

%changelog
* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 3.0.1-1
- Update to upstream version 3.0.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.11.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 2.11.3-1
- Update to upstream version 2.11.3

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.11.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.11.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 2.11.2-1
- Update to 2.11.2
