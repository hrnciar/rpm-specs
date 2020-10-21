%global sname urllib-gssapi
%global s_name urllib_gssapi

Name:           python-%{sname}
Version:        1.0.1
Release:        12%{?dist}
Summary:        A GSSAPI/SPNEGO authentication handler for urllib/urllib2

License:        ASL 2.0
URL:            https://github.com/pythongssapi/%{sname}
Source0:        https://github.com/pythongssapi/%{sname}/releases/download/v%{version}/%{s_name}-%{version}.tar.gz
BuildArch:      noarch

# Patches

BuildRequires:  git-core

BuildRequires:  python3-devel
BuildRequires:  python3-gssapi
BuildRequires:  python3-nose
BuildRequires:  python3-setuptools

%global _description\
urllib_gssapi is a backend for urllib.  It provides GSSAPI/SPNEGO\
authentication to HTTP servers.  urllib_gssapi replaces urllib_kerberos and\
behaves in the same ways.

%description %_description

%package -n python3-%{sname}
Summary:        %summary
Requires:       python3-gssapi
%{?python_provide:%python_provide python3-%{sname}}
%description -n python3-%{sname} %_description

%prep
%autosetup -S git -n %{s_name}-%{version}

%build
%py3_build


%install
%py3_install

%check
%{__python3} setup.py nosetests

%files -n python3-%{sname}
%doc README.md
%license COPYING
%{python3_sitelib}/%{s_name}*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Robbie Harwood <rharwood@redhat.com> - 1.0.1-5
- Drop python2 subpackage
- Resolves: #1655258

* Mon Sep 24 2018 Robbie Harwood <rharwood@redhat.com> - 1.0.1-4
- Drop requirement on python-requests
- Resolves: #1631938

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.7

* Fri Feb 23 2018 Robbie Harwood <rharwood@redhat.com> - 1.0.1-1
- New upstream release (v1.0.0)
- Adds COPYING and removes shebang
- Resolves: #1546835

* Mon Feb 19 2018 Robbie Harwood <rharwood@redhat.com> - 1.0.0-1
- New upstream release (v1.0.0)
