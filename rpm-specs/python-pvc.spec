%{?python_enable_dependency_generator}

Name:           python-pvc
Version:        0.3.0
Release:        9%{?dist}
Summary:        Python vSphere Client with a dialog interface
License:        BSD
URL:            https://github.com/dnaeon/pvc
Source0:        %{url}/archive/v%{version}.tar.gz#/pvc-%{version}.tar.gz
Patch0:         %{url}/commit/79a6f63f5b57622f1d3871b86ce8f048803d0914.patch

BuildArch:      noarch


%global _description \
PVC is an interactive text-mode vSphere Client with a dialog interface\
for GNU/Linux systems built on top of the pyVmomi vSphere API bindings.\
\
Using PVC allows you to quickly navigate in your vSphere environment\
and perform common tasks against various vSphere Managed Entities.

%description
%{_description}

%package        doc
Summary:        Documentation files for PVC (Python vSphere Client)
BuildArch:      noarch

%description    doc
%{_description}\
\
This package installs the documentation files.

%package     -n python%{python3_pkgversion}-pvc
Summary:        Python vSphere Client with a dialog interface
%{?python_provide:%python_provide python%{python3_pkgversion}-pvc}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-humanize
BuildRequires:  python%{python3_pkgversion}-pyvmomi
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-vconnector
BuildRequires:  python%{python3_pkgversion}-sphinx
Requires:       python%{python3_pkgversion}-dialog
# no magic dependencies in epel
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-humanize
Requires:       python%{python3_pkgversion}-pyvmomi
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-vconnector
%endif

%description -n python%{python3_pkgversion}-pvc
%{_description}


%prep
%autosetup -p1 -npvc-%{version}

%build
%{py3_build}
PYTHONPATH=../src %make_build -C docs html \
 SPHINXBUILD=sphinx-build-%{python3_version} \
 SPHINXOPTS=%{_smp_mflags}
rm -rf docs/_build/html/.{doctrees,buildinfo}

%install
%{py3_install}


%files doc
%license LICENSE
%doc docs/_build/html/

%files -n python%{python3_pkgversion}-pvc
%license LICENSE
%doc README.rst
%{python3_sitelib}/pvc/
%{python3_sitelib}/pvc-%{version}-py%{python3_version}.egg-info/
%{_bindir}/pvc-tui


%changelog
* Wed Jun 03 2020 Raphael Groner <projects.rg@smart.ms> - 0.3.0-9
- add patch to improve password input, upstream #28

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-8
- Rebuilt for Python 3.9

* Thu Feb 06 2020 Raphael Groner <projects.rg@smart.ms> - 0.3.0-7
- [epel7] fix call to sphinx with python3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-4
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Raphael Groner <projects.rg@smart.ms> - 0.3.0-3
- drop brand

* Sat Jul 27 2019 Raphael Groner <projects.rg@smart.ms> - 0.3.0-2
- fix URL
- fix description
- split doc subpackage
- add dialog dependencies for runtime
- ignore manpage warning of rpmlint due to interactive tui, later in scm

* Thu Jul 25 2019 Raphael Groner <projects.rg@smart.ms> - 0.3.0-1
- initial
