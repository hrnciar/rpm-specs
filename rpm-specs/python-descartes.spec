%global srcname descartes

Name:           python-%{srcname}
Version:        1.1.0
Release:        15%{?dist}
Summary:        Use geometric objects as Matplotlib paths and patches
%global _description \
A Python module that allows using Shapely or GeoJSON-like geometric objects as \
Matplotlib paths and patches.

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-matplotlib
BuildRequires:  python3-shapely
Requires:       python3-numpy
Requires:       python3-matplotlib

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{srcname}
%doc README.txt
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.0-9
- Drop Python 2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 09 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.0-5
- Fix python2-* BR on old Fedora.

* Fri Dec 08 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.0-4
- Use python2-* BR.

* Sat Aug 12 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.0-3
- Simplify spec with more macros.

* Sun Jul 09 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.0-2
- Simplify spec a bit.

* Sat Mar 04 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.0-1
- Initial package release.
