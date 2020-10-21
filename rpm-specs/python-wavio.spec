%global pypi_name wavio

%global pypi_description wavio is simple a Python module that allows to \
read and write WAV files as numpy arrays.

Name: python-%{pypi_name}
Summary: Read and write WAV files as numpy arrays
License: BSD

Version: 0.0.4
Release: 3%{?dist}

URL: https://github.com/WarrenWeckesser/wavio
Source0: %pypi_source

BuildRequires: python3-devel
BuildRequires: python3-setuptools

BuildArch: noarch

%description
%{pypi_description}


%package -n python3-%{pypi_name}
Summary: %{summary}
BuildArch: noarch

%description -n python3-%{pypi_name}
%{pypi_description}


%prep
%autosetup -n %{pypi_name}-%{version}

# Extract license text from comment at top of source
awk 'BEGIN { start_print=0 }
/^-----$/ { start_print=1; next }
/^"""$/ { if ( start_print==1 ) exit }
/.*/ { if (start_print == 1) print $0 }' < wavio.py > LICENSE


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{python3_sitelib}/__pycache__/%{pypi_name}.*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Artur Iwicki <fedora@svgames.pl> - 0.0.4-2
- Fix installation directory (noarch package - goes in python sitelib, not sitearch)

* Sat Jul 11 2020 Artur Iwicki <fedora@svgames.pl> - 0.0.4-1
- Initial packaging
