%global srcname wikipedia

Name:           python-%{srcname}
Version:        1.4.5
Release:        16%{?dist}
Summary:        Wikipedia API for Python

License:        MIT
URL:            https://github.com/barrust/Wikipedia
Source0:        https://github.com/barrust/Wikipedia/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Search Wikipedia, get article summaries, get data like links and images
from a page, and more.

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-nose
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
Requires:       python3-beautifulsoup4
Requires:       python3-requests

%description -n python3-%{srcname}
Search Wikipedia, get article summaries, get data like links and images
from a page, and more.

%prep
%autosetup -n Wikipedia-%{version}

%build
%py3_build

%install
%py3_install

%check
nosetests-%{python3_version}

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.4.5-10
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.4.5-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-3
- Rebuild for Python 3.6

* Tue Oct 18 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.4.5-2
- Update to BR python2-requests
- Update to BR python2-setuptools

* Fri Oct 14 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.4.5-1
- Update to 1.4.5-1
- Cleanup spec file
- Use Requires python2-requests
- Write the content to Summary and in the rest use %%{summary} marco

* Sun Oct 02 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.4.4-1.gitb329024
- Initial package
