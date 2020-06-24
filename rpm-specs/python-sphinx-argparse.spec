%global srcname sphinx-argparse
%global sum Sphinx extension that automatically documents argparse commands and options

Name:           python-%{srcname}
Version:        0.2.2
Release:        10%{?dist}
Summary:        %{sum}
BuildArch:      noarch

License:        MIT
Url:            https://github.com/ribozz/%{srcname}/
Source0:        https://github.com/ribozz/%{srcname}/archive/%{version}.tar.gz

BuildRequires:  python3-devel python3-setuptools

%description
Sphinx extension that automatically documents argparse commands and options

%package -n python3-%{srcname}
Requires:       python3-sphinx
BuildRequires:  python3-sphinx
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Sphinx extension that automatically documents argparse commands and options


%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Brian C. Lane <bcl@redhat.com> - 0.2.2-4
- Remove python2 package from build (#1627431)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-2
- Rebuilt for Python 3.7

* Fri May 11 2018 Brian C. Lane <bcl@redhat.com> - 0.2.2-1
- Update to new upstream release

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.15-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.15-6
- Escape macros in %%changelog

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.15-3
- Rebuild for Python 3.6

* Tue Feb 02 2016 Brian C. Lane <bcl@redhat.com> 0.1.15-2
- Fix description typo
- Drop %%check section, upstream uses tox for testing.

* Mon Feb 01 2016 Brian C. Lane <bcl@redhat.com> 0.1.15-1
- Initial creation

