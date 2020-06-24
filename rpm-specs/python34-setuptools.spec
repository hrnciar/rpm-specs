# This package is for EPEL only, python3_other only
# Python 2 setuptools are in RHEL (python-setuptools)
# Python 3.6 setuptools are in RHEL (python3-setuptools)

%global srcname setuptools

Name:           python34-%{srcname}
Version:        39.2.0
Release:        5%{?dist}
Summary:        Easily build and distribute Python 3.4 packages

# setuptools, six, pyparsing is MIT
# packaging is BSD or ASL 2.0
License:        MIT and (BSD or ASL 2.0)

URL:            https://github.com/pypa/setuptools
Source0:        %pypi_source %{srcname} %{version} zip

# In Fedora, sudo setup.py install installs to /usr/local/lib/pythonX.Y/site-packages
# But pythonX doesn't own that dir, that would be against FHS
# We need to create it if it doesn't exist
# https://bugzilla.redhat.com/show_bug.cgi?id=1576924
Patch0:         create-site-packages.patch

BuildRequires:  python34-devel
BuildRequires:  python34-pip
BuildRequires:  python34-pytest
BuildRequires:  python34-mock
BuildArch:      noarch

# see setuptools/_vendor/vendored.txt
Provides: bundled(python34-packaging) = 16.8
Provides: bundled(python34-pyparsing) = 2.1.10
Provides: bundled(python34-six) = 1.10.0


%description
Setuptools is a collection of enhancements to the Python 3.4 distutils that
allow you to more easily build and distribute Python 3.4 packages, especially
ones that have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.py.


%prep
%autosetup -p1 -n %{srcname}-%{version}

# We can't remove .egg-info (but it doesn't matter, since it'll be rebuilt):
#  The problem is that to properly execute setuptools' setup.py,
#   it is needed for setuptools to be loaded as a Distribution
#   (with egg-info or .dist-info dir), it's not sufficient
#   to just have them on PYTHONPATH
#  Running "setup.py install" without having setuptools installed
#   as a distribution gives warnings such as
#    ... distutils/dist.py:267: UserWarning: Unknown distribution option: 'entry_points'
#   and doesn't create "easy_install" and .egg-info directory
# Note: this is only a problem if bootstrapping wheel or building on RHEL,
#  otherwise setuptools are installed as dependency into buildroot

# Strip shbang
find %{srcname} -name \*.py | xargs sed -i -e '1 {/^#!\//d}'
# Remove bundled exes
rm -f %{srcname}/*.exe

# These tests require internet connection
rm %{srcname}/tests/test_integration.py

# These tests are not compatible with our ancient pytest version
rm pkg_resources/tests/test_working_set.py
rm %{srcname}/tests/test_bdist_egg.py
rm %{srcname}/tests/test_build_meta.py
rm %{srcname}/tests/test_egg_info.py
rm %{srcname}/tests/test_virtualenv.py

# These test require python34-wheel
rm %{srcname}/tests/test_wheel.py


%build
%py3_other_build


%install
%py3_other_install

rm -rf %{buildroot}%{python3_other_sitelib}/%{srcname}/tests
rm %{buildroot}%{_bindir}/easy_install

find %{buildroot}%{python3_other_sitelib} -type f -name '*.exe' -print -delete

# Don't ship these
rm -r docs/{Makefile,conf.py,_*}


%check
LANG=en_US.utf8 PYTHONPATH=$(pwd) py.test-3.4


%files
%license LICENSE
%doc docs/* CHANGES.rst README.rst
%{python3_other_sitelib}/easy_install.py
%{python3_other_sitelib}/__pycache__/easy_install.cpython-34*.py*
%{python3_other_sitelib}/pkg_resources/
%{python3_other_sitelib}/%{srcname}/
%{python3_other_sitelib}/%{srcname}-%{version}-py3.4.egg-info/
%{_bindir}/easy_install-3.4


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 39.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Miro Hrončok <mhroncok@redhat.com> - 39.2.0-4
- Split python34-setuptools from python3-setuptools

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 39.2.0-3
- Rebuilt to change main python from 3.4 to 3.6

* Fri Jan 11 2019 Miro Hrončok <mhroncok@redhat.com> - 39.2.0-2
- Create /usr/local/lib/pythonX.Y when needed (#1664722)

* Tue Dec 04 2018 Carl George <carl@george.computer> - 39.2.0-1
- Update to upstream 39.2.0

* Wed May 23 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 19.6.2-3
- Build for python3_other

* Sun Oct 09 2016 Tim Orling <ticotimo@gmail.com> - 19.6.2-2
- Fixes for EPEL6 build

* Wed Feb 3 2016 Orion Poplawski <orion@cora.nwra.com> - 19.6.2-1
- Update to 19.6.2
- Update license
- Fix python3 package file ownership

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 19.2-3
- Cleanup docs
- Add version info to summary and description

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 19.2-2
- Drop group tag
- Add bootstrap conditional
- Use specific pip version
- Use %%license
- Update license and license source
- Strip unneeded shbangs

* Tue Dec 29 2015 Orion Poplawski <orion@cora.nwra.com> - 19.2-1
- Update to 19.2

* Tue Dec 29 2015 Orion Poplawski <orion@cora.nwra.com> - 19.1.1-1
- Initial EPEL package
