%global commit0 3ff37a2a93f05f33ddd2baef017a677e8d02d18e
%global date0   20149631
%global scommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           python-vevents
# version 0.1.0 unofficially mentioned in sitepackages
Version:        0.1.0
Release:        0.5.%{date0}git%{scommit0}%{?dist}
Summary:        vSphere Events from the command-line

# license header in src/vevents-cli for BSD, PR#2
License:        BSD
URL:            https://github.com/dnaeon/py-vevents
Source0:        %{url}/archive/%{commit0}/%{name}-%{scommit0}.tar.gz

BuildArch:      noarch

%description
vEvents is an application that allows you to view and monitor
vSphere Events from the command-line.

%package     -n python%{python3_pkgversion}-vevents
Summary:        vSphere Events from the command-line
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pyvmomi
BuildRequires:  python%{python3_pkgversion}-docopt
BuildRequires:  python%{python3_pkgversion}-vconnector 
%{?python_provide:%python_provide python%{python3_pkgversion}-vevents}
# no magic dependencies in epel
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-pyvmomi
Requires:       python%{python3_pkgversion}-docopt
Requires:       python%{python3_pkgversion}-vconnector
%endif

%description -n python%{python3_pkgversion}-vevents
vEvents is an application that allows you to view and monitor
 vSphere Events from the command-line.


%prep
%autosetup -npy-vevents-%{commit0}

%build
%{py3_build}

%install
%{py3_install}


%files -n python%{python3_pkgversion}-vevents
#%%license add-license-file-here
%doc README.md
# egg-info only due to single binary
%{python3_sitelib}/vevents-%{version}-py%{python3_version}.egg-info/
%{_bindir}/vevents-cli


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-0.5.20149631git3ff37a2
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.4.20149631git3ff37a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-0.3.20149631git3ff37a2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Raphael Groner <projects.rg@smart.ms> - 0.1.0-0.2.20149631git3ff37a2
- drop brand

* Thu Jul 25 2019 Raphael Groner <projects.rg@smart.ms> - 0.1.0-0.1.20149631git3ff37a2
- initial
