%global modname libpagure

Name:           python-libpagure
Version:        0.21
Release:        8%{?dist}
Summary:        A Python library for Pagure APIs
License:        GPLv2+
URL:            https://pagure.io/libpagure/
Source0:        https://pagure.io/releases/libpagure/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description\
A Python library for Pagure APIs

%description %_description

%package -n python3-libpagure
Summary:        A Python library for Pagure APIs
%{?python_provide:%python_provide python3-libpagure}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:  python3-requests

%description -n python3-libpagure
A Python library for Pagure APIs

%prep
%setup -q -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-libpagure
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/libpagure*/

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.21-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.21-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.21-4
- Subpackage python2-libpagure has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.21-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> - 0.21-1
- Release 0.21

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Sep 07 2017 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> 0.10-1
- Updates to 0.10

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9-3
- Python 2 binary package renamed to python2-libpagure
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 11 2017 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> 0.9-1
- Updates to 0.9

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> 0.6-1
- Update the source to 0.6

* Thu Nov 26 2015 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> 0.5-1
- Update the source to 0.5

* Tue Nov 10 2015 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> 0.4-1
- Initial packaging
