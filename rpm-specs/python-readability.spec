%global pypi_name readability

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        1%{?dist}
Summary:        Measure the readability of a given text using surface characteristics

License:        ASL 2.0
URL:            https://github.com/andreasvc/readability/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
An implementation of traditional readability measures based on simple surface
characteristics. These measures are basically linear regressions based on the
number of words, syllables, and sentences.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
An implementation of traditional readability measures based on simple surface
characteristics. These measures are basically linear regressions based on the
number of words, syllables, and sentences.


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{_bindir}/readability
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info
%{python3_sitelib}/%{pypi_name}/


%changelog
* Fri Mar 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.1-1
- Initial package