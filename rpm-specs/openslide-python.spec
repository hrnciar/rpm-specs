Name:           openslide-python
Version:        1.1.1
Release:        20%{?dist}
Summary:        Python bindings for the OpenSlide library

License:        LGPLv2
URL:            http://openslide.org/
Source0:        https://github.com/openslide/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

# Disable Intersphinx so it won't download inventories at build time
Patch0:         openslide-python-1.0.1-disable-intersphinx.patch
# Fix Sphinx underscore fixup on Sphinx 2.x
Patch1:         openslide-python-1.1.1-fix-sphinx-2.x.patch
# Remove usage of the deprecated Feature module from setuptools
# Resolved upstream: https://github.com/openslide/openslide-python/pull/76
Patch2:         remove-Feature-module-setuptools.patch

BuildRequires:  gcc
BuildRequires:  openslide >= 3.4.0
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pillow
BuildRequires:  python3-sphinx

%description
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.  This package allows Python
programs to use OpenSlide.


%package -n python3-openslide
Summary:        Python 3 bindings for the OpenSlide library
Requires:       openslide >= 3.4.0
Requires:       python3-pillow
Provides:       openslide-python3 = %{version}-%{release}
Provides:       openslide-python3%{?_isa} = %{version}-%{release}
Obsoletes:      openslide-python3 < 1.1.1-5
%{?python_provide:%python_provide python3-openslide}


%description -n python3-openslide
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.  This package allows Python 3
programs to use OpenSlide.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Examples include bundled jQuery and OpenSeadragon
rm -rf examples


%build
%py3_build
%{__python3} setup.py build_sphinx
rm build/sphinx/html/.buildinfo


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-openslide
%doc CHANGELOG.txt build/sphinx/html
%license LICENSE.txt lgpl-2.1.txt
%{python3_sitearch}/openslide/
%{python3_sitearch}/*.egg-info/


%changelog
* Thu Jun 18 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.1.1-20
- Fix compatibility with setuptools >= 46.0.0 (#1817697)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-19
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-16
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Benjamin Gilbert <bgilbert@backtick.net> - 1.1.1-14
- Fix build with Sphinx 2.x

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Benjamin Gilbert <bgilbert@backtick.net> - 1.1.1-12
- Avoid overbroad %%files glob per policy

* Wed Oct 03 2018 Benjamin Gilbert <bgilbert@backtick.net> - 1.1.1-11
- Drop Python 2 subpackage for https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-9
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 17 2017 Benjamin Gilbert <bgilbert@backtick.net> - 1.1.1-5
- Rename binary packages per policy
- Depend on Python 2 packages by their python2- names
- Drop Group tag

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jun 12 2016 Benjamin Gilbert <bgilbert@backtick.net> - 1.1.1-1
- New release
- Run tests in %%check

* Sun Feb 21 2016 Benjamin Gilbert <bgilbert@backtick.net> - 1.1.0-6
- BuildRequire gcc per new policy

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Oct 18 2015 Benjamin Gilbert <bgilbert@backtick.net> - 1.1.0-3
- Update to new Python guidelines
- Build docs with Python 3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Benjamin Gilbert <bgilbert@backtick.net> - 1.1.0-1
- New release

* Sun Mar 22 2015 Benjamin Gilbert <bgilbert@backtick.net> - 1.0.1-4
- Update build scripts to current Packaging:Python template
- Move license files to %%license

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 10 2014 Benjamin Gilbert <bgilbert@backtick.net> - 1.0.1-1
- New release
- Use versioned sitelib macro for Python 2

* Tue Feb 11 2014 Benjamin Gilbert <bgilbert@backtick.net> - 0.5.1-1
- Initial version
