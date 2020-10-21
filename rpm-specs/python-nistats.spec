# Py3 only as some deps are not provided for py2 any more

# Also test in mock since a test that downloads data is disabled in the spec
# mock -r fedora-rawhide-x86_64 rebuild <srpm> --enable-network --rpmbuild-opts="--with tests"
%bcond_without tests

# Require downloads, so we cannot generate them
%bcond_with doc

%global pypi_name nistats

%global desc %{expand: \
Nistats is a Python module for fast and easy modeling and statistical analysis
of functional Magnetic Resonance Imaging data.

It leverages the nilearn Python toolbox for neuroimaging data manipulation
(data downloading, visualization, masking).

This work is made available by a community of people, amongst which the INRIA
Parietal Project Team and D'esposito lab at Berkeley.

It is based on developments initiated in the nipy project.}


Name:           python-%{pypi_name}
Version:        0.0.1
Release:        0.7b0%{?dist}
Summary:        Modeling and Statistical analysis of fMRI data in Python

License:        BSD
URL:            https://nistats.github.io/
Source0:        https://github.com/%{pypi_name}/%{pypi_name}/archive/rel%{version}b/%{name}-%{version}.tar.gz

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist numpy} >= 1.11
BuildRequires:  %{py3_dist nibabel} >= 2.0.2
BuildRequires:  %{py3_dist scipy} >= 0.17
BuildRequires:  %{py3_dist scikit-learn} >= 0.18
BuildRequires:  %{py3_dist nilearn} >= 0.4
BuildRequires:  %{py3_dist pandas} >= 0.18
BuildRequires:  %{py3_dist patsy} >= 0.4.1
BuildRequires:  %{py3_dist nose} >= 1.2.1
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist pytz}
BuildRequires:  %{py3_dist matplotlib} >= 1.5.1
BuildRequires:  %{py3_dist boto3} >= 1.4
# For documentation
%if %{with doc}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist numpydoc}
BuildRequires:  %{py3_dist sphinx-gallery}
BuildRequires:  %{py3_dist pillow}
%endif

# Not in setup.py
Requires:  %{py3_dist six}

Recommends:  %{py3_dist matplotlib} >= 1.5.1
Recommends:  %{py3_dist boto3} >= 1.4
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-rel%{version}b
rm -rf %{pypi_name}.egg-info

# remove bundled numpydoc and sphinx_gallery
rm -rf ./doc/sphinxext/numpydoc
rm -rf ./doc/sphinxext/sphinx_gallery

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# Fixed upstream, but not released
# https://github.com/nistats/nistats/commit/2aa7e6d33c9f25728db8bfe2d47bc9ebe15829d2
sed -i 's/DataFrame().from_csv(path)/read_csv(path, index_col=0)/' nistats/tests/test_dmtx.py

%build
%py3_build

%if %{with doc}
pushd doc
    make SPHINXBUILD=sphinx-build-3 html
    rm -rf _build/html/.doctrees
    rm -rf _build/html/.buildinfo
popd
%endif

%install
%py3_install

%check
%if %{with tests}
# ignore dataset tests that tries to download data
nosetests-%{python3_version} -i test_datasets
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst AUTHORS.rst
%{python3_sitelib}/%{pypi_name}-%{version}b0-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%files doc
%license LICENSE
%doc examples
%if %{with doc}
%doc doc/_build/html
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-0.7b0
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.6b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.1-0.5b0
- Update pands API call
- https://bugzilla.redhat.com/show_bug.cgi?id=1750695

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-0.4b0
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.3b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.2b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 14 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.1-0.1b0
- Update BRs
- Correct description
- Initial build
- Enable tests
- Remove bundled bits
- Correct pre-release tag
