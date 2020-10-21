%global pypi_name sklearn-nature-inspired-algorithms
%global pretty_name sklearn_nature_inspired_algorithms
%global github_name Sklearn-Nature-Inspired-Algorithms

# Pulls in fonts, currently disabled
# We refer to upstream's documentation.
%bcond_with generated_docs
%bcond_without tests

%global _description %{expand:
Nature inspired algorithms for hyper-parameter tuning of scikit-learn models.
This package uses algorithms implementation from NiaPy.

Documentation is available at:
https://sklearn-nature-inspired-algorithms.readthedocs.io/en/stable/ }

Name:           python-%{pypi_name}
Version:        0.4.6
Release:        2%{?dist}
Summary:        Nature Inspired Algorithms for scikit-learn

License:        MIT
URL:            https://github.com/timzatko/%{github_name}
Source0:        %{url}/archive/v%{version}/%{github_name}-%{version}.tar.gz
# Update pyproject.toml to match Fedora package versions
Patch0:         0001-Allow-using-fedora-dep-versions.patch

# For the patch
BuildRequires:  git-core

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  pyproject-rpm-macros
BuildRequires: %{py3_dist lockfile}
BuildRequires: %{py3_dist packaging}
BuildRequires: %{py3_dist pep517}
BuildRequires: %{py3_dist poetry}
BuildRequires: %{py3_dist wheel}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%if %{with generated_docs}
%package doc
Summary:        %{summary}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}


%description doc
Generated documentation for %{name}.
%endif

%prep
%autosetup -n %{github_name}-%{version} -S git
rm -rf %{pretty_name}.egg-info
rm -fv poetry.lock

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

#not included in Pypi package
%if %{with generated_docs}
PYTHONPATH=. make -C docs SPHINXBUILD=sphinx-build-3 html
rm -rf docs/_build/html/{.doctrees,.buildinfo} -vf
%endif

%install
%pyproject_install
%pyproject_save_files sklearn_nature_inspired_algorithms

%check
%if %{with tests}
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m unittest tests
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%doc examples

%if %{with generated_docs}
%files doc
%license LICENSE
%doc docs/_build/html
%endif

%changelog
* Fri Oct 09 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.6-2
- Do not include generated docs: bundle lots of fonts
- Correct doc generation command

* Fri Aug 14 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.5-1
- Update to use poetry
- correct URLS
- add conditionals for test and docs

* Mon Jul 27 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.5-1
- Initial package
