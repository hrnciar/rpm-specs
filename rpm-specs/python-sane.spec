%global srcname sane

Name:           python-%{srcname}
Version:        2.8.3
Release:        18%{?dist}
Summary:        Python SANE interface

License:        MIT
URL:            https://github.com/python-pillow/Sane
Source0:        https://github.com/python-pillow/Sane/archive/v%{version}/Sane-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  sane-backends-devel

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx

%filter_provides_in %{python3_sitearch}
%filter_setup

%description
This package contains the sane module for Python which provides access to
various raster scanning devices such as flatbed scanners and digital cameras.


%package -n python3-%{srcname}
Summary:        Python 3 module for using scanners
Requires:       python3-pillow
Requires:       python3-numpy
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This package contains the sane module for Python which provides access to
various raster scanning devices such as flatbed scanners and digital cameras.


%prep
%autosetup -p1 -n Sane-%{version}


%build
# Build Python 3 modules
%py3_build

make -C doc html BUILDDIR=_build_py3 SPHINXBUILD=sphinx-build-%python3_version
rm -f doc/_build_py3/html/.buildinfo


%install
# Install Python 3 modules
%py3_install

# Fix non-standard-executable-perm
chmod 0755 %{buildroot}%{python3_sitearch}/*.so


%files -n python3-%{srcname}
%doc CHANGES.rst sanedoc.txt example.py doc/_build_py3/html
%license COPYING
%{python3_sitearch}/*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8.3-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8.3-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8.3-14
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Sandro Mani <manisandro@gmail.com> - 2.8.3-13
- Drop python2 subpackage

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Sandro Mani <manisandro@gmail.com> - 2.8.3-11
- Drop docs in python2 build

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.8.3-8
- Rebuilt for Python 3.7

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 2.8.3-7
- Add missing BR: gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.8.3-3
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Sandro Mani <manisandro@gmail.com> - 2.8.3-1
- Update to 2.8.3

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.8.2-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Jul 02 2016 Sandro Mani <manisandro@gmail.com> - 2.8.2-4
- Modernize spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Aug 08 2015 Sandro Mani <manisandro@gmail.com> - 2.8.2-1
- Update to 2.8.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 27 2015 Sandro Mani <manisandro@gmail.com> - 2.8.1-1
- Update to 2.8.1

* Sat Mar 07 2015 Sandro Mani <manisandro@gmail.com> - 2.8.0-1
- Update to 2.8.0

* Fri Jan 02 2015 Sandro Mani <manisandro@gmail.com> - 2.7.0-1
- Initial package
