%global srcname winrm
%global sum Python libraries for interacting with windows remote management
%global gh_owner diyan
%global pypi_name py%{srcname}

Name:           python-%{srcname}
Version:        0.3.0
Release:        10%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/%{gh_owner}/%{pypi_name}/archive/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: python3-six
BuildRequires: python3-requests
BuildRequires: python3-xmltodict
BuildRequires: python3-pytest
BuildRequires: python3-mock
BuildRequires: python3-requests_ntlm

%description
This has the python libraries for interacting with Windows Remote Management

%package -n python3-%{srcname}
Summary:        %{sum}
Requires: python3-xmltodict
Requires: python3-requests_ntlm
Requires: python3-requests
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This has the python libraries for interacting with Windows Remote Management


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest winrm/tests

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python3-%{srcname}
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Subpackage python2-winrm has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.7

* Tue Apr 17 2018 James Hogarth <james.hogarth@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 James Hogarth <james.hogarth@gmail.com> - 0.2.2-1
- Update to 0.2.2
- Update requires to fix bz#1409670

* Tue Dec 20 2016 James Hogarth <james.hogarth@gmail.com> - 0.2.1-3
- Fix broken requires for epel

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuild for Python 3.6

* Mon Oct 24 2016 James Hogarth <james.hogarth@gmail.com> - 0.2.1-1
- Initial package
