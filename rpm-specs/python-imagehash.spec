%global pypi_name imagehash

Name:           python-%{pypi_name}
Version:        4.0
Release:        7%{?dist}
Summary:        A Python perceptual image hashing module

License:        BSD
URL:            https://github.com/JohannesBuchner/imagehash
Source0:        https://github.com/JohannesBuchner/imagehash/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A image hashing library written in Python. ImageHash supports average hashing,
perception hashing, difference hashing and wavelet hashing.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pywt
BuildRequires:  python3-pillow
BuildRequires:  python3-scipy
BuildRequires:  python3-six
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A image hashing library written in Python. ImageHash supports average hashing,
perception hashing, difference hashing and wavelet hashing.

%package -n %{pypi_name}-demo
Summary:        %{summary}
Requires:       python3-%{pypi_name}

%description -n %{pypi_name}-demo
Demo tool for %{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/%{pypi_name}/tests/

%files -n %{pypi_name}-demo
%doc README.rst
%license LICENSE
%{_bindir}/find_similar_images.py

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 4.0-2
- Fix changelog entry (rhbz#1723103)
- Update BR
- Enable tests

* Fri Jun 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 4.0-1
- Initial package for Fedora
