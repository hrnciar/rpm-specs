%global srcname pygments-style-solarized
%global sum Solarized style plugin for Pygments

Name:           python-%{srcname}
Version:        0.1.1
Release:        12.1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/shkumagai/pygments-style-solarized
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{sum}

%package -n     python3-%{srcname}
Summary:        %{sum}
Requires:       python3-pygments >= 1.5
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{sum}

%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install

%files -n python3-%{srcname}
%doc README.rst AUTHORS.rst HISTORY.rst
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-12.1
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-11.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-10.1
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-9.1
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-6.1
- Subpackage python2-pygments-style-solarized has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-4.1
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Mar 17 2017 Ed Marshall <esm@logic.net> - 0.1.1-2.1
- Force rebuild.

* Fri Mar 17 2017 Ed Marshall <esm@logic.net> - 0.1.1-2
- Specify python2-setuptools instead of python-setuptools.

* Fri Mar 17 2017 Ed Marshall <esm@logic.net> - 0.1.1-1
- Initial package.
