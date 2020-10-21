%global srcname sphinx-math-dollar

Name:           python-%{srcname}
Version:        1.2
Release:        1%{?dist}
Summary:        Sphinx extension to enable LaTeX math with $$

License:        MIT
URL:            https://www.sympy.org/%{srcname}/
Source0:        https://github.com/sympy/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest-doctestplus}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-testing}

%global _desc %{expand:
sphinx-math-dollar is a Sphinx extension to let you write LaTeX math
using $$.}

%description %_desc

%package     -n python3-%{srcname}
Summary:        Sphinx extension to enable LaTeX math with $$

%description -n python3-%{srcname} %_desc

%package        doc
Summary:        Documentation for %{srcname}

%description    doc
Documentation for %{srcname}.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

# Build the documentation
make -C docs html
rst2html --no-datestamp CHANGELOG.rst CHANGELOG.html
rst2html --no-datestamp README.rst README.html
rm -f docs/_build/html/.{buildinfo,nojekyll}

%install
%py3_install

%check
pytest

%files       -n python3-%{srcname}
%doc CHANGELOG.html README.html
%license LICENSE
%{python3_sitelib}/sphinx_math_dollar*

%files          doc
%doc docs/_build/html
%license LICENSE

%changelog
* Fri Sep 18 2020 Jerry James <loganjerry@gmail.com> - 1.2-1
- Version 1.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  2 2020 Jerry James <loganjerry@gmail.com> - 1.1.1-1
- Initial RPM
