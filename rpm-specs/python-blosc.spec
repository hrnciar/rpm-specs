Summary:        Python wrapper for the Blosc high performance compressor
Name:           python-blosc
Version:        1.8.1
Release:        8%{?dist}
License:        MIT
URL:            https://github.com/Blosc/python-blosc
Source0:        https://github.com/Blosc/python-blosc/archive/v%{version}/blosc-%{version}.tar.gz

# https://github.com/Blosc/python-blosc/pull/200
Patch1:         0001-blosc_extenion-constify-char-pointers-for-Py_BuildVa.patch
Patch2:         0002-setup.py-unbreak-build-on-architectures-which-don-t-.patch
Patch3:         0003-setup.py-catch-import-error-for-cpuinfo.patch
# https://github.com/Blosc/python-blosc/pull/202
Patch4:         0004-Read-os-release-instead-of-using-platform.linux_dist.patch
# Fix Python 3.9 compatibility
# https://github.com/Blosc/python-blosc/pull/218
Patch5:         0005-fix-python-3.9-compatibility.patch

BuildRequires:  gcc
BuildRequires:  blosc-devel >= 1.16.0
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-psutil
BuildRequires:  python%{python3_pkgversion}-cpuinfo

%description
%{summary}.

%package -n python%{python3_pkgversion}-blosc
Summary:        Python wrapper for the blosc high performance compressor
Requires:       blosc%{_isa} >= 1.16.0

%{?python_provide:%python_provide python%{python3_pkgversion}-blosc}
%{?fedora:Recommends: python%{python3_pkgversion}-numpy}

%description -n python%{python3_pkgversion}-blosc
%{summary}.

%prep
%autosetup -p1
# Remove bundled copy
rm cpuinfo.py

%build
export BLOSC_DIR=%{_libdir}/blosc CFLAGS="%{optflags}"
export DISABLE_BLOSC_AVX2=1
%py3_build

%install
%py3_install

%check
cd / # avoid interference with build dir
PYTHONPATH=%{buildroot}%{python3_sitearch} %__python3 -c 'import sys, blosc; sys.exit(blosc.test())'

%files -n python%{python3_pkgversion}-blosc
%{python3_sitearch}/blosc/
%{python3_sitearch}/blosc-%{version}*-py*.egg-info
%license LICENSES/PYTHON-BLOSC.txt
%doc README.rst RELEASE_NOTES.rst

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.8.1-7
- Fix Python 3.9 compatibility (#1792055)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May  5 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.8.1-1
- Update to latest version (#1684965)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.1-2
- Subpackage python2-blosc has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Jul 19 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.1-1
- Update to latest version (#1372856)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Dan Horák <dan[at]danny.cz> - 1.4.1-3
- remove build time CPU detection, fixed build on ppc64/ppc64le and s390(x)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-2
- Rebuild for Python 3.6

* Thu Jul 28 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.1-1
- Update to latest version (#1323008)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 14 2016 Thibault North <tnorth@fedoraproject.org> - 1.3.3-1
- Update to 1.3.3

* Mon May 16 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-1
- Update to 1.3.2

* Mon May 16 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.8-3
- Fix provides filter
- Use %%python3_pkgversion for EPEL7 compatibility

* Sat Feb 13 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 1.2.8-2
- Add dependency on psutil to check for leaks during build
- Fix build (#1307896)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.8-1
- Update to latest version (#1263680)
- Add python2 subpackage following the latest guidelines

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.7-3
- Run test suite

* Thu May 28 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.7-2
- Build python 3 subpackage
- Install license and readme files

* Thu May  7 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.7-1
- Update to 1.2.7 (#1212231)

* Mon Apr 20 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.5-1
- Update to 1.2.5 (#1212231)

* Tue Jan 06 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.4-1
- Update to 1.2.4

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-2
- Rebuild for blosc

* Sat Mar 22 2014 Thibault North <tnorth@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3 for blosc 1.3.4

* Wed Jan 08 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1-8
- Rebuild for blosc

* Tue Nov 05 2013 Thibault North <tnorth@fedoraproject.org> - 1.1-7
- Properly link with blosc shared lib

* Tue Nov 05 2013 Thibault North <tnorth@fedoraproject.org> - 1.1-6
- Disable SSE2 optimizations

* Tue Nov 05 2013 Thibault North <tnorth@fedoraproject.org> - 1.1-5
- Final cosmetic fixes

* Tue Nov 05 2013 Thibault North <tnorth@fedoraproject.org> - 1.1-4
- Fix wrong lib perms

* Fri Oct 18 2013 Thibault North <tnorth@fedoraproject.org> - 1.1-3
- Fixes, thanks to Christopher Meng

* Wed Oct 16 2013 Thibault North <tnorth@fedoraproject.org> - 1.1-2
- Various fixes

* Fri Sep 20 2013 Thibault North <tnorth@fedoraproject.org> - 1.1-1
- Sync to version 1.1

* Mon Jan 2 2012 Thibault North <tnorth@fedoraproject.org> - 1.0.7-1
- Initial package
