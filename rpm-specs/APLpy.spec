%global srcname APLpy

# Disable automatic dependency generators until we fixed (optional) deps
%{?python_disable_dependency_generator}

Name:           APLpy
Version:        2.0.3
Release:        8%{?dist}
Summary:        The Astronomical Plotting Library in Python

License:        MIT
URL:            http://aplpy.github.com
Source0:        https://pypi.io/packages/source/A/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel 

%description
APLpy (the Astronomical Plotting Library in Python) is a Python module aimed at 
producing publication-quality plots of astronomical imaging data in FITS format.
The module uses Matplotlib, a powerful and interactive plotting package. It is
capable of creating output files in several graphical formats, including EPS,
PDF, PS, PNG, and SVG.

%package -n python3-APLpy
Summary:        The Astronomical Plotting Library in Python
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-numpy
BuildRequires:  python3-matplotlib
BuildRequires:  python3-astropy
BuildRequires:  python3-pillow
BuildRequires:  python3-pytest

Requires:  python3-numpy
Requires:  python3-matplotlib
Requires:  python3-astropy
Recommends:  python3-pillow

%description -n python3-APLpy
APLpy (the Astronomical Plotting Library in Python) is a Python module aimed at 
producing publication-quality plots of astronomical imaging data in FITS format.
The module uses Matplotlib, a powerful and interactive plotting package. It is
capable of creating output files in several graphical formats, including EPS,
PDF, PS, PNG, and SVG.

%prep
%setup -q -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%check
# Empty matplotlibrc
mkdir matplotlib
touch matplotlib/matplotlibrc
export XDG_CONFIG_HOME=`pwd`
# Avoid writing bad pyc files
export PYTHONDONTWRITEBYTECODE=1
pushd %{buildroot}/%{python3_sitelib}
py.test-%{python3_version} aplpy || :
popd

%files -n python3-APLpy
%doc CHANGES.rst README.rst
%license LICENSE.md
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/aplpy/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-8
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-5
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 Christian Dersch <lupinix@mailbox.org> - 2.0.3-2
- Disable automatic dependency generators until we fixed (optional) deps

* Mon Feb 25 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 2.0.3-1
- New upstream version (2.0.3)

* Sun Feb 17 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 2.0-1
- New upstream version (2.0)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1.1-2
- Drop python2 subpackage

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Christian Dersch <lupinix@mailbox.org> - 1.1.1-6
- Failing tests are only deprecation warnings... Ignore them and report upstream

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1.1-1
- New upstream version (1.1.1)
- Include license file
- Do not write pyc files when running tests

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1-3
- Rebuild for Python 3.6

* Sun Oct 02 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1-2
- EVR bump

* Sun Sep 25 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1-1
- New upstream version (1.1)
- Updated spec
- Fixes bz #1380134

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0-4
- Disable some failing tests (https://github.com/aplpy/aplpy/issues/278)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0-1
- New upstream version (1.0)
- Use license macro

* Thu Dec 11 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.14-2
- Disable python3 tests

* Thu Dec 11 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.14-1
- New upstream source (0.9.14), several bug fixes

* Tue Oct 07 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.13-1
- New upstream source (0.9.13), fixes bug in 0.9.11 and 0.9.12

* Thu Sep 11 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.12-2
- Provide python3 subpackage
- Unbundle decorator

* Thu Sep 11 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.12-1
- New upstream source (0.9.12)
- Tests enabled

* Wed Sep 10 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.11-2
- Disable tests for the moment

* Tue Jul 08 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.11-1
- Updated to new version
- Run tests on installed version
- Use python2 macros

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Germán A. Racca <skytux@fedoraproject.org> - 0.9.8-1
- Updated to new version
- Included tests in %%check and corresponding BRs
- Packaged tests in %%doc section

* Mon Feb 06 2012 Germán A. Racca <skytux@fedoraproject.org> 0.9.6-3
- Minor changes to spec file after approval
- Removed INSTALL file

* Mon Jan 30 2012 Germán A. Racca <skytux@fedoraproject.org> 0.9.6-2
- Changed name of spec file to match the project name

* Mon Jan 23 2012 Germán A. Racca <skytux@fedoraproject.org> 0.9.6-1
- Initial release of RPM package

