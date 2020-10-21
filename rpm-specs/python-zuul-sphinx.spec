%global srcname zuul-sphinx

Name:           python-%{srcname}
Version:        0.4.1
Release:        4%{?dist}
Summary:        Sphinx extension for Zuul jobs

License:        ASL 2.0
URL:            https://zuul-ci.org
Source0:        https://opendev.org/zuul/zuul-sphinx/archive/%{version}.tar.gz

BuildArch:      noarch


%description
A Sphinx extension for documenting Zuul jobs.


%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
Requires:       python3-pbr
Requires:       python3-sphinx
Requires:       python3-PyYAML
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A Sphinx extension for documenting Zuul jobs.


%prep
%setup -qn %{srcname}
# Remove bundled eggs
rm -rf *requirements.txt %{srcname}.egg-info


%build
export PBR_VERSION=%{version}
%py3_build


%install
export PBR_VERSION=%{version}
%py3_install


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/zuul_sphinx-%{version}-py3*.egg-info/
%{python3_sitelib}/zuul_sphinx/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Fabien Boucher <fboucher@redhat.com> - 0.4.1-1
- Bump to 0.4.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 0.2.1-1
- Import from software factory repository
