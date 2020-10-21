%global srcname rmtest
%global summary A simple framework for testing Redis modules
%if 0%{?rhel} > 7 || 0%{?fedora} >= 30
%global disable_python2 1
%else
%global disable_python2 0
%endif

Name:    python-%{srcname}
Version: 1.0.1
Release: 3%{?dist}
Summary: %{summary}

License: BSD
URL:     https://github.com/goodform/%{srcname}

Source0: https://github.com/goodform/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Source1: https://raw.githubusercontent.com/goodform/%{srcname}/master/LICENSE
Source2: https://raw.githubusercontent.com/goodform/%{srcname}/master/README.md

BuildArch:      noarch
%if !%{disable_python2}
BuildRequires:  python2-devel python2-redis
%endif
BuildRequires:  python3-devel python3-redis
BuildRequires:  redis-devel gcc
BuildRequires:  redis >= 4
Requires:       redis >= 4

%description
Simple framework for testing Redis modules using python
unit test and a disposable ephemeral Redis sub-process.

%if !%{disable_python2}
%package -n python2-%{srcname}
Summary:        %{summary}
Requires:       python2-redis
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Simple framework for testing Redis modules using python
unit test, and a disposable ephemeral Redis sub-process.
%endif

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-redis
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Simple framework for testing Redis modules using python
unit test, and a disposable ephemeral Redis sub-process.

%prep
%autosetup -n %{srcname}-%{version} -p1
cp %{S:1} %{S:2} .

%build
%if !%{disable_python2}
%py2_build
%endif
%py3_build

%install
%if !%{disable_python2}
%py2_install
%endif
%py3_install

%check
%if !%{disable_python2}
PYTHONPATH=%{buildroot}/%{python2_sitelib}/rmtest %{__python2} setup.py test
%endif
PYTHONPATH=%{buildroot}/%{python3_sitelib}/rmtest %{__python3} setup.py test

%if !%{disable_python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.9

* Tue Mar 17 2020 Nathan Scott <nathans@redhat.com> - 1.0.1-1
- Update to latest upstream sources.
- Resolves failure with latest python redis client (#1793007)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Nathan Scott <nathans@redhat.com> - 1.0.0-1
- Update to latest upstream sources (https://github.com/goodform).
- Drop spec workarounds for python3 and module build race - fixed upstream.
- Add spec file logic to disable python2 packages for Fedora30 onward.

* Fri Aug 10 2018 Nathan Scott <nathans@redhat.com> - 0.6.9-1
- Update to latest upstream sources.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.6-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.6-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Nathan Scott <nathans@redhat.com> - 0.6.6-1
- Initial redis module test package.
