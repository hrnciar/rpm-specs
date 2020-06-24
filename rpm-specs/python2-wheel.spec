%global pypi_name wheel

Name:           python2-%{pypi_name}
Version:        0.29.0
Release:        3%{?dist}
Summary:        A built-package format for Python

# wheel is MIT
# pep425tags.py is vendored, MIT
# decorator.py is from pyramid, BSD
License:        MIT and BSD

# Versions are unknown
Provides:       bundled(python2-pep425tags)
Provides:       bundled(python2-pyramid)

URL:            https://bitbucket.org/pypa/wheel
Source0:        %{pypi_source}

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  pytest
BuildRequires:  pyxdg
BuildRequires:  python-keyring
BuildRequires:  python-jsonschema
BuildArch:      noarch

%{?python_provide:%python_provide python2-%{pypi_name}}

%description
A built-package format for Python.

A wheel is a ZIP-format archive with a specially formatted filename and the
.whl extension. It is designed to contain all the files for a PEP 376
compatible install in a way that is very close to the on-disk format.

Python 2 version.


%prep
%autosetup -n %{pypi_name}-%{version}
# remove unneeded shebangs
sed -ie '1d' %{pypi_name}/{egg2wheel,wininst2wheel}.py

%build
%py2_build

%install
%py2_install
mv %{buildroot}%{_bindir}/%{pypi_name}{,-%{python2_version}}
ln -s %{pypi_name}-%{python2_version} %{buildroot}%{_bindir}/%{pypi_name}-2
ln -s %{pypi_name}-2 %{buildroot}%{_bindir}/%{pypi_name}

%check
rm setup.cfg
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} -v --ignore build

%files
%license LICENSE.txt
%doc CHANGES.txt README.txt
%{_bindir}/%{pypi_name}
%{_bindir}/%{pypi_name}-2
%{_bindir}/%{pypi_name}-%{python2_version}
%{python2_sitelib}/%{pypi_name}*
%exclude %{python2_sitelib}/%{pypi_name}/test

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Miro Hrončok <mhroncok@redhat.com> - 0.29.0-2
- Split python2-wheel from the python-wheel package

* Mon Nov 21 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.29.0-1
- Update to 0.29.0
- Cleanups and fixes

* Thu Sep 01 2016 Felix Schwarz <fschwarz@fedoraproject.org> - 0.24.0-3
- remove build dependency to (orphaned) python-keyring package

* Sat Jan 03 2015 Matej Cepl <mcepl@redhat.com> - 0.24.0-2
- Make python3 conditional (switched off for RHEL-7; fixes #1131111).

* Mon Nov 10 2014 Slavek Kabrda <bkabrda@redhat.com> - 0.24.0-1
- Update to 0.24.0
- Remove patches merged upstream

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Matej Stuchlik <mstuchli@redhat.com> - 0.22.0-3
- Another rebuild with python 3.4

* Fri Apr 18 2014 Matej Stuchlik <mstuchli@redhat.com> - 0.22.0-2
- Rebuild with python 3.4

* Thu Nov 28 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.22.0-1
- Initial package.
