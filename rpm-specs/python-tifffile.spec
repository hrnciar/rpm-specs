
%global srcname tifffile

Name: python-%{srcname}
Version: 2020.7.4
Release: 3%{?dist}
Summary: Read and write TIFF(r) files

License: BSD
URL: https://www.lfd.uci.edu/~gohlke/
Source0: %{pypi_source}

BuildArch: noarch

%global _description %{expand:
Tifffile is a Python library to:
 * store numpy arrays in TIFF (Tagged Image File Format) files, and
 * read image and metadata from TIFF-like files used in bioimaging.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# Testing
BuildRequires:  python3-pytest
BuildRequires:  python3-numpy

%description -n python3-%{srcname} %_description

%prep
# Remove shebang
%autosetup -n %{srcname}-%{version}
sed -i -e "1d" tifffile/lsm2bin.py 
sed -i 's/\r$//' README.rst

%build
%py3_build

%install
%py3_install

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
export PYTHONPATH="${PYTHONPATH:-%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}}"
# 7 tests fail out of 1000 
# these tests require network or additional packages not in Fedora
pytest-%{python3_version} -v tests \
 --deselect=tests/test_tifffile.py::test_issue_infinite_loop \
 --deselect=tests/test_tifffile.py::test_issue_jpeg_ia \
 --deselect=tests/test_tifffile.py::test_func_pformat_xml \
 --deselect=tests/test_tifffile.py::test_filehandle_seekable \
 --deselect=tests/test_tifffile.py::test_read_cfa \
 --deselect=tests/test_tifffile.py::test_read_tiles \
 --deselect=tests/test_tifffile.py::test_write_cfa \
 --deselect=tests/test_tifffile.py::test_write_volume_png

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{_bindir}/lsm2bin
%{_bindir}/tifffile
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 2020.7.4-2
- Fix license

* Wed Jul 08 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 2020.7.4-1
- Initial spec

