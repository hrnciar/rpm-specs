%global pypi_name guizero

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        3%{?dist}
Summary:        Python module to allow learners to easily create GUIs
License:        BSD
URL:            https://github.com/lawsie/guizero
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-tkinter
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  font(dejavusans)
BuildRequires:  font(dejavuserif)

%description
Guizero is designed to allow new learners to quickly and easily create
GUIs for their programs.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(pillow) >= 4.3
Requires:       python3-tkinter

%description -n python3-%{pypi_name}
Guizero is designed to allow new learners to quickly and easily create
GUIs for their programs.


%prep
%autosetup -n %{pypi_name}-%{version}

# use free fonts in tests
sed -i 's/Times New Roman/DejaVu Serif/g' tests/*.py
sed -i 's/Arial/DejaVu Sans/g' tests/*.py


%build
%py3_build


%install
%py3_install


%check
# if called form builddir, tests open a window when collecting and hang until closed
pushd tests
export PYTHONPATH=%{buildroot}%{python3_sitelib} 
xvfb-run %{__python3} -m pytest -v
popd


%files -n python3-%{pypi_name}
%doc README.md
%license license.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.9

* Tue Mar 17 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.4-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 27 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.4-1
- Update to 0.6.4 (#1745741)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 14 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-1
- Initial package
