%global srcname lightblue


#TODO file License issue missing in dist file upstream

Name:           python-lightblue
Version:        0.1.4
Release:        10%{?dist}
Summary:        A Python library to work with Lightblue database

License:        GPLv3
URL:            https://github.com/Allda/python-lightblue
Source0:        https://pypi.io/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-mock
BuildRequires:  python3-beanbag
BuildRequires:  python3-dpath

BuildArch:      noarch

%description
A Python library to work with Lightblue database API. More lightblue information
can be found at https://lightblue.io

%package -n python3-%{srcname}
Summary:        A Python library to work with Lightblue database

Requires:       python3-dpath
Requires:       python3-beanbag

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A Python library to work with Lightblue database API. More lightblue information
can be found at https://lightblue.io

%prep
%autosetup
# do not use rednose during rpm build
sed -i 's/rednose/\#rednose/' setup.cfg

%build

%py3_build

%install

%py3_install

%check

nosetests-%{python3_version}


%files -n python3-%{srcname}
%doc README.md
%{python3_sitelib}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.4-4
- Subpackage python2-lightblue has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-2
- Rebuilt for Python 3.7

* Wed May 16 2018 Ales Raszka <araszka@redhat.com> - 0.1.4-1
- Rebase to 0.1.4

* Sun Apr 29 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 0.1.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Apr 24 2018 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.3-2
- Fix summary macro

* Tue Apr 24 2018 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.3-1
- Initial version

