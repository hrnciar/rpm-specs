Name:               python-iniconfig
Version:            1.1.1
Release:            1%{?dist}
Summary:            Brain-dead simple parsing of ini files
License:            MIT
URL:                http://github.com/RonnyPfannschmidt/iniconfig
BuildArch:          noarch
BuildRequires:      python3-devel
BuildRequires:      pyproject-rpm-macros

Source0:            %{pypi_source iniconfig}

# pytest 6+ needs this and this uses pytest for tests
%bcond_without tests

%global _description %{expand:
iniconfig is a small and simple INI-file parser module
having a unique set of features:

* tested against Python2.4 across to Python3.2, Jython, PyPy
* maintains order of sections and entries
* supports multi-line values with or without line-continuations
* supports "#" comments everywhere
* raises errors with proper line-numbers
* no bells and whistles like automatic substitutions
* iniconfig raises an Error if two sections have the same name.}
%description %_description


%package -n python3-iniconfig
Summary:            %{summary}
%description -n python3-iniconfig %_description


%prep
%autosetup -n iniconfig-%{version}


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files iniconfig


%if %{with tests}
%check
%tox
%endif


%files -n python3-iniconfig -f %{pyproject_files}
%doc README.txt
%license LICENSE


%changelog
* Thu Oct 15 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.1.1-1
- Update to 1.1.1 (#1888157)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-1
- Initial package (#1856421)
