%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname cinderclient

%global with_doc 1

%global common_desc \
Client library (cinderclient python module) and command line utility \
(cinder) for interacting with OpenStack Cinder (Block Storage) API.

Name:             python-cinderclient
Version:          7.0.0
Release:          1%{?dist}
Summary:          Python API and CLI for OpenStack Cinder

License:          ASL 2.0
URL:              http://github.com/openstack/python-cinderclient
Source0:          https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:        noarch

BuildRequires:    git

%description
%{common_desc}

%package -n python3-%{sname}
Summary:          Python API and CLI for OpenStack Cinder
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    python3-pbr

Requires:         python3-babel
Requires:         python3-pbr
Requires:         python3-prettytable
Requires:         python3-requests
Requires:         python3-six
Requires:         python3-keystoneauth1 >= 3.4.0
Requires:         python3-oslo-i18n >= 3.15.3
Requires:         python3-oslo-utils >= 3.33.0
Requires:         python3-simplejson

%description -n python3-%{sname}
%{common_desc}

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Cinder API Client
Group:            Documentation

BuildRequires:    python3-reno
BuildRequires:    python3-sphinx
BuildRequires:    python3-openstackdocstheme

%description      doc
%{common_desc}

This package contains auto-generated documentation.
%endif

%prep
%autosetup -n %{name}-%{upstream_version} -S git

# Remove bundled egg-info
rm -rf python_cinderclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
sphinx-build-3 -W -b html doc/source doc/build/html
sphinx-build-3 -W -b man doc/source doc/build/man

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo
%endif

%install
%{py3_install}
# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s cinder %{buildroot}%{_bindir}/cinder-3

# Delete tests
rm -fr %{buildroot}%{python3_sitelib}/cinderclient/tests

install -p -D -m 644 tools/cinder.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/cinder.bash_completion

%if 0%{?with_doc}
install -p -D -m 644 doc/build/man/cinder.1 %{buildroot}%{_mandir}/man1/cinder.1
%endif

%files -n python3-%{sname}
%doc README.rst
%license LICENSE
%{_bindir}/cinder
%{_bindir}/cinder-3
%{python3_sitelib}/cinderclient
%{python3_sitelib}/*.egg-info
%{_sysconfdir}/bash_completion.d/cinder.bash_completion
%if 0%{?with_doc}
%{_mandir}/man1/cinder.1*
%endif

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%endif

%changelog
* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 7.0.0-1
- Update to upstream version 7.0.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Alfredo Moralejo <amoralej@redhat.com> 5.0.0-1
- Update to upstream version 5.0.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 19 2019 RDO <dev@lists.rdoproject.org> 4.2.0-1
- Update to 4.2.0

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 4.1.0-1
- Update to 4.1.0

