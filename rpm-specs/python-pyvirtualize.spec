%global srcname pyVirtualize
%global modname pyvirtualize

%global date    20191018
%global commit0 dc2d971cb1ff51b91f31b7390c0a6a3151003e1f

# FIXME epel7 Could not import extension sphinx.ext.githubpages (exception: No module named githubpages)
%if 0%{?fedora}
%global with_build_doc 1
%endif

%global desc A python interface to access and manage pyvmomi.\
\
pyVirtualize is build over pyvmomi, hence it has ability\
to perform all the operations what vSphere client is able to.\
\
pyVirtualize provides easy interfaces to:\
Connect to ESX, ESXi, Virtual Center and Virtual Server hosts.\
Query hosts, datacenters, resource pools, virtual machines\
and perform various operations over them.\
VMs operations: power, file, process, snapshot, admin, utilities\
\
And of course, you can use it to access all the API through python.

Name:           python-%{modname}
# pypi tells current version
Version:        0.10
Release:        3.%{date}git%(c=%commit0; echo ${c:0:7} )%{?dist}
Summary:        Another python frontend to access and manage pyvmomi

License:        ASL 2.0
URL:            https://github.com/rocky1109/%{srcname}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{srcname}-%{commit0}.tar.gz

BuildArch:      noarch

%description
%desc

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-pyvmomi

%description -n python%{python3_pkgversion}-%{modname}
%desc

%if 0%{?python3_other_pkgversion}
%package -n python%{python3_other_pkgversion}-%{modname}
Summary:        %{summary}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{srcname}}
Requires:       python%{python3_other_pkgversion}-pyvmomi

%description -n python%{python3_other_pkgversion}-%{modname}
%desc
%endif

%package doc
Summary:        Documentation files for %{srcname}
BuildRequires:  web-assets-devel
Requires:       js-jquery
# some js files of documentation are licensed with BSD
License:        ASL 2.0 and BSD

%description doc
This package installs %{summary}.


%prep
%autosetup -n %{srcname}-%{commit0}
# skip backported dependencies
sed -i /typing/d requirements.txt

%build
%py3_build
%{?python3_other_pkgversion: %py3_other_build}
%if 0%{?with_build_doc}
# drop useless files
rm -rfv docs/build/*
sphinx-build -d docs/build/doctrees docs/source docs/build/html
# drop useless build garbage
find docs/build/html -name '.*' -print -delete
%endif
# unbundle jquery
rm -v docs/build/html/_static/jquery*.js
ln -fs %{_jsdir}/jquery/3/jquery.js docs/build/html/_static

%install
%{?python3_other_pkgversion: %py3_other_install}
%py3_install


%files -n python%{python3_pkgversion}-%{modname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-%{modname}
%license LICENSE
%doc README.md
%{python3_other_sitelib}/%{srcname}/
%{python3_other_sitelib}/%{srcname}-%{version}-py?.?.egg-info/
%endif

%files doc
%license LICENSE
%doc docs/build/html/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10-3.20191018gitdc2d971
- Rebuilt for Python 3.9

* Sun Apr 05 2020 Raphael Groner <projects.rg@smart.ms> - 0.10-2.20191018gitdc2d971
- skip backported dependency of module typing

* Thu Apr 02 2020 Raphael Groner <projects.rg@smart.ms> - 0.10-1.20191018gitdc2d971
- use latest snapshot, rhbz#1770851
- improve support for python3 and dependencies, see upstream commits
- drop support for python2
- get rid of useless build contionals

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9.20181003git57d2307
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-8.20181003git57d2307
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-7.20181003git57d2307
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Raphael Groner <projects.rg@smart.ms> - 0.9-6.20181003git57d2307
- drop brand
- group BR by python version and subpackage

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5.20181003git57d2307
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 02 2019 Raphael Groner <projects.rg@smart.ms> - 0.9-4.20181003git57d2307
- add more build macros to fix b0rken dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3.20181003git57d2307
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Raphael Groner <projects.rg@smart.ms> - 0.9-2.20181003git57d2307
- use current snapshot
- use python3 only in Fedora but still also python2 in EPEL
- introduce modname macro

* Tue Sep 04 2018 Raphael Groner <projects.rg@smart.ms> - 0.9-1.20180205git4b01f44
- initial

