%global srcname sphinx-copybutton

Name:           python-%{srcname}
Version:        0.3.0
Release:        4%{?dist}
Summary:        Add a copy button to code cells in Sphinx docs

License:        MIT
URL:            https://sphinx-copybutton.readthedocs.io/en/latest/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-ipython-sphinx
BuildRequires:  %{py3_dist setuptools}

%global _description %{expand:
Sphinx-copybutton does one thing: add a little "copy" button to the
right of your code blocks.  If the code block overlaps to the right of
the text area, you can just click the button to get the whole thing.}

%description %_description

%package     -n python3-%{srcname}
Summary:        Add a copy button to code cells in Sphinx docs

%description -n python3-%{srcname} %_description

%package        doc
Summary:        Documentation for %{srcname}

%description    doc
Documentation for %{srcname}.

%prep
%autosetup -n %{srcname}-%{version}

# Remove spurious executable bits
find -O3 . -type f -perm /0111 -exec chmod a-x {} \+

%build
%py3_build

# Build the documentation
PYTHONPATH=$PWD make -C doc html
rm doc/_build/html/.buildinfo

%install
%py3_install

%files       -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/sphinx_copybutton*

%files          doc
%doc doc/_build/html
%license LICENSE

%changelog
* Mon Oct  5 2020 Jerry James <loganjerry@gmail.com> - 0.3.0-4
- Explicitly BR setuptools

* Mon Sep 21 2020 Jerry James <loganjerry@gmail.com> - 0.3.0-3
- Remove pyproject and tox bits, not supported by this package (bz 1881047)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Jerry James <loganjerry@gmail.com> - 0.3.0-1
- Version 0.3.0

* Wed Jun 17 2020 Jerry James <loganjerry@gmail.com> - 0.2.12-1
- Version 0.2.12

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.11-2
- Rebuilt for Python 3.9

* Thu Apr 23 2020 Jerry James <loganjerry@gmail.com> - 0.2.11-1
- Version 0.2.11

* Thu Apr  2 2020 Jerry James <loganjerry@gmail.com> - 0.2.10-1
- Version 0.2.10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec  6 2019 Jerry James <loganjerry@gmail.com> - 0.2.6-2
- Ship the LICENSE file with the -doc subpackage too

* Thu Dec  5 2019 Jerry James <loganjerry@gmail.com> - 0.2.6-1
- Initial RPM
