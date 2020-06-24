%global pypi_name reuse

Name:           reuse
Version:        0.8.0
Release:        3%{?dist}
Summary:        A tool for compliance with the REUSE recommendations
License:        GPLv3+ and CC-BY-SA and ASL 2.0
Url:            https://github.com/fsfe/reuse-tool
Source0:        %pypi_source
BuildRequires:  python3 >= 3.6
# Build
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  gettext
BuildRequires:  %{py3_dist setuptools-scm}
# Test
BuildRequires:  git
BuildRequires:  %{py3_dist pytest}
# Dependencies
BuildRequires:  %{py3_dist Jinja2}
BuildRequires:  %{py3_dist binaryornot}
BuildRequires:  %{py3_dist boolean.py}
BuildRequires:  %{py3_dist license-expression}
BuildRequires:  %{py3_dist python-debian}
BuildRequires:  %{py3_dist requests}
# Documentation
BuildRequires:  %{py3_dist Sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist sphinx-autodoc-typehints}
BuildRequires:  %{py3_dist sphinxcontrib-apidoc}
BuildRequires:  %{py3_dist recommonmark}
Requires:       python3 >= 3.6
Recommends:     git
BuildArch:      noarch

%description
A tool for compliance with the REUSE recommendations. Essentially,
it is a linter that checks for a project's compliance, and a compiler that
generates a project's bill of materials.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove this line when sphinx-autodoc-typehints is up-to-date.
sed -i "/sphinx_autodoc_typehints/d" docs/conf.py

%build
%py3_build
pushd docs
PBR_VERSION=%{version} sphinx-build-%{python3_version} . html
rm -rf html/.{doctrees,buildinfo}
popd

%install
%py3_install

%check
PYTHONDONTWRITEBYTECODE=1 LC_ALL=C.UTF-8 LANG=C.UTF-8 PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-3 tests/

%files
%license LICENSES/*.txt
%doc README.md CHANGELOG.md docs/html/
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.8.0-1
- New version
- Additional build dependency on setuptools-scm.
- Performance increase.
- Many additional translations.
- Deprecated licenses are now recognised.
- lint no longer accepts path arguments. Where previously one could do reuse
lint SUBDIRECTORY, this is no longer possible. When linting, you must always
lint the entire project. To change the project's root, use --root. 

* Thu Nov 28 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.7.0-1
- New version.
- Upstream PyPI package renamed from fsfe-reuse to reuse.
- No other changes.

* Fri Nov 22 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.6.0-1
- New upstream version.
- Git submodules are now ignored by default. `--include-submodules` reverses
  this behaviour.

* Mon Oct 28 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.5.2-1
- new version

* Fri Sep 06 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.5.0-1
- New upstream version.
- Now compatible with REUSE v3.0.
- Added Sphinx-generated documentation.
- Now also contains code under ASL 2.0.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.3.4-1
- New upstream version.
- Copyright lines can now start with © in addition to Copyright.

* Fri Nov 23 2018 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.3.3-1
- Initial package.
