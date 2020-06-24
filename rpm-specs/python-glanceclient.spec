%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname glanceclient
%global with_doc 1

%global common_desc \
This is a client for the OpenStack Glance API. There's a Python API (the \
glanceclient module), and a command-line script (glance). Each implements \
100% of the OpenStack Glance API.

Name:             python-glanceclient
Epoch:            1
Version:          3.1.1
Release:          1%{?dist}
Summary:          Python API and CLI for OpenStack Glance

License:          ASL 2.0
URL:              https://launchpad.net/python-glanceclient
Source0:          https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    git

%description
%{common_desc}

%package -n python3-%{sname}
Summary:          Python API and CLI for OpenStack Glance
%{?python_provide:%python_provide python3-glanceclient}
Obsoletes: python2-%{sname} < %{version}-%{release}

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    python3-pbr

Requires:         python3-keystoneauth1 >= 3.6.2
Requires:         python3-oslo-i18n >= 3.15.3
Requires:         python3-oslo-utils >= 3.33.0
Requires:         python3-pbr
Requires:         python3-prettytable
Requires:         python3-pyOpenSSL >= 17.1.0
Requires:         python3-requests
Requires:         python3-six >= 1.10.0
Requires:         python3-warlock
Requires:         python3-wrapt


%description -n python3-%{sname}
%{common_desc}

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Glance API Client

BuildRequires:    python3-sphinx
BuildRequires:    python3-openstackdocstheme
BuildRequires:    python3-keystoneauth1
BuildRequires:    python3-oslo-utils
BuildRequires:    python3-prettytable
BuildRequires:    python3-pyOpenSSL >= 17.1.0
BuildRequires:    python3-sphinxcontrib-apidoc
BuildRequires:    python3-warlock

%description      doc
%{common_desc}

This package contains auto-generated documentation.
%endif

%prep
%autosetup -n %{name}-%{upstream_version} -S git

rm -rf *requirements.txt

%build
%{py3_build}

%install
%{py3_install}

# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s glance %{buildroot}%{_bindir}/glance-3

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 644 tools/glance.bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/glance

# Delete tests
rm -fr %{buildroot}%{python3_sitelib}/glanceclient/tests

%if 0%{?with_doc}
# generate html docs
sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
# generate man page
sphinx-build -b man doc/source doc/build/man
install -p -D -m 644 doc/build/man/glance.1 %{buildroot}%{_mandir}/man1/glance.1
%endif

%files -n python3-%{sname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/glanceclient
%{python3_sitelib}/*.egg-info
%{_sysconfdir}/bash_completion.d
%if 0%{?with_doc}
%{_mandir}/man1/glance.1.gz
%endif
%{_bindir}/glance
%{_bindir}/glance-3

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 1:3.1.1-1
- Update to upstream version 3.1.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:2.17.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Alfredo Moralejo <amoralej@redhat.com> 1:2.17.0-1
- Update to upstream version 2.17.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:2.16.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:2.16.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 1:2.16.0-1
- Update to 2.16.0
