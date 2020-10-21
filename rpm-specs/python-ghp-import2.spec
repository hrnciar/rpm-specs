%global pypi_name ghp-import2

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        8%{?dist}
Summary:        A GitHub Pages import tool

License:        Tumbolia
URL:            https://github.com/ionelmc/python-ghp-import
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
A GitHub Pages import tool.

Warning: This will **DESTROY** your gh-pages branch. If you love it,
you'll want to take backups before playing with this.

This script assumes that gh-pages is 100% derivative. You should never edit
files in your gh-pages branch by hand if you're using this script because you
will lose your work.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
A GitHub Pages import tool.

Warning: This will **DESTROY** your gh-pages branch. If you love it,
you'll want to take backups before playing with this.

This script assumes that gh-pages is 100% derivative. You should never edit
files in your gh-pages branch by hand if you're using this script because you
will lose your work.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# remove shebang line from the python scripts
for lib in $(find -type f -name '*.py'); do
 sed -i.python -e '1{\@^#!@d}' $lib
done

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/ghp-import
%{python3_sitelib}/ghp_import
%{python3_sitelib}/ghp_import2-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 José Matos <jamatos@fedoraproject.org> - 1.0.1-2
- fix source url, license short hand, description and summary.
- remove shebang lines from python scripts.

* Sat Sep  1 2018 José Matos <jamatos@fedoraproject.org> - 1.0.1-1
- initial package.
