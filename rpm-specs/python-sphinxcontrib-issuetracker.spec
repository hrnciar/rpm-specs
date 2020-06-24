%if 0%{?fedora}
%global with_python3 1
%else
%global with_python3 0
%endif
%if 0%{?fedora} < 30
%global with_python2 1
%else
%global with_python2 0
%endif

%global pyname sphinxcontrib-issuetracker

Name:           python-%{pyname}
Version:        0.11
Release:        21%{?dist}
Summary:        Sphinx integration with different issue trackers

License:        BSD
URL:            https://pypi.python.org/pypi/%{pyname}
Source0:        https://pypi.python.org/packages/source/s/%{pyname}/%{pyname}-%{version}.tar.gz

# https://github.com/ignatenkobrain/sphinxcontrib-issuetracker/pull/13
Patch1:         920200bfa32ed99637a7df12695e07f60180ff3c.patch

BuildArch:      noarch
%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-requests
BuildRequires:  python2-sphinx >= 1.1
%endif # if with_python2
%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-sphinx >= 1.1
%endif # if with_python3

%global _description\
A Sphinx extension to reference issues in issue trackers, either explicitly\
with an "issue" role or optionally implicitly by issue ids like #10 in plain\
text.\
\
Currently the following issue trackers are supported:\
\
 *  GitHub\
 *  BitBucket\
 *  Launchpad\
 *  Google Code\
 *  Debian BTS\
 *  Jira\
\
A simple API is provided to add support for other issue trackers.  If you\
added support for a new tracker, please consider sending a patch to make your\
work available to other users of this extension.\


%description %_description

%if 0%{?with_python2}
%package -n python2-%{pyname}
Summary: %summary
Requires:       python2-requests
Requires:       python2-sphinx >= 1.1
%{?python_provide:%python_provide python2-%{pyname}}

%description -n python2-%{pyname} %_description
%endif # if with_python2

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{pyname}
Summary:        Sphinx integration with different issue trackers for Python 3
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-sphinx >= 1.1

%description -n python%{python3_pkgversion}-%{pyname}
A Sphinx extension to reference issues in issue trackers, either explicitly
with an "issue" role or optionally implicitly by issue ids like #10 in plain
text.

Currently the following issue trackers are supported:

 *  GitHub
 *  BitBucket
 *  Launchpad
 *  Google Code
 *  Debian BTS
 *  Jira

A simple API is provided to add support for other issue trackers.  If you
added support for a new tracker, please consider sending a patch to make your
work available to other users of this extension.

This package contains the Python 3 version of the module.
%endif # with_python3


%prep
%setup -q -n %{pyname}-%{version}
%patch1 -p1
rm -rf *egg-info


%build
%if 0%{?with_python2}
%py2_build
%endif # with_python2

%if 0%{?with_python3}
%py3_build
%endif # with_python3


%install
%if 0%{?with_python2}
%py2_install
%endif # with_python2

%if 0%{?with_python3}
%py3_install
%endif # with_python3


%check
%if 0%{?with_python2}
%{__python2} setup.py test
%endif # with_python2

%if 0%{?with_python3}
%{__python3} setup.py test
%endif # with_python3

 
%if 0%{?with_python2}
%files -n python2-%{pyname}
%license LICENSE
%doc CHANGES.rst CREDITS README.rst doc
%{python2_sitelib}/*
%endif # with_python2

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{pyname}
%license LICENSE
%doc CHANGES.rst CREDITS README.rst doc
%{python3_sitelib}/*
%endif # with_python3


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11-21
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11-19
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11-18
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Orion Poplawski <orion@cora.nwra.com> - 0.11-15
- Drop Python 2 package for Fedora 30+ (bugz #1634900)
- Modernize spec

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11-13
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.11-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Dan Callaghan <dcallagh@redhat.com> - 0.11-10
- Fix KeyError: 'refdomain' with latest Sphinx (RHBZ#1523462)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.11-9
- Python 2 binary package renamed to python2-sphinxcontrib-issuetracker
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.11-6
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 7 2014 Orion Poplawski <orion@cora.nwra.com> - 0.11-2
- Add Requires on python-requests, python-sphinx
- Use %%license

* Fri Apr 18 2014 Orion Poplawski <orion@cora.nwra.com> - 0.11-1
- Initial package
