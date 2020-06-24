Name:			PerceptualDiff
Version:		1.1.1
Release:		25%{?dist}
Summary:		An image comparison utility

License:		GPLv2+
URL:			http://pdiff.sourceforge.net
Source:			http://downloads.sourceforge.net/pdiff/perceptualdiff-%{version}-src.tar.gz
Patch1:			PerceptualDiff-1.0.2-gcc44.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: cmake
BuildRequires: freeimage-devel
BuildRequires: libtiff-devel
BuildRequires: libpng-devel


%description
PerceptualDiff is an image comparison utility that makes use of a 
computational model of the human visual system to compare two images.

This software is released under the GNU General Public License.

%prep
%setup -q -c
%patch1 -p1 -b .gcc44


%build
mkdir build
cd build

%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} ..

%make_build VERBOSE=1


%install
cd build
%make_install

chmod 755 %{buildroot}%{_bindir}/perceptualdiff


%files
%doc README.txt
%license gpl.txt
%{_bindir}/perceptualdiff


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.1-15
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 20 2009 kwizart < kwizart at gmail.com > - 1.1.1-1
- Update to 1.1.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 kwizart < kwizart at gmail.com > - 1.0.2-4
- Fix and Rebuild for gcc44

* Mon Sep  1 2008 kwizart < kwizart at gmail.com > - 1.0.2-3
- Re-introduce gcc43 patch

* Mon Sep  1 2008 kwizart < kwizart at gmail.com > - 1.0.2-2
- Add Missing BR freeimage-devel

* Mon Sep  1 2008 kwizart < kwizart at gmail.com > - 1.0.2-1
- Update to 1.0.2

* Sat Feb  9 2008 kwizart < kwizart at gmail.com > - 1.0.1-8
- Rebuild for gcc43

* Fri Jan  4 2008 kwizart < kwizart at gmail.com > - 1.0.1-7
- Fix gcc43

* Tue Aug 14 2007 kwizart < kwizart at gmail.com > - 1.0.1-6
- Update the license field to GPLv2

* Tue Apr 17 2007 kwizart < kwizart at gmail.com > - 1.0.1-5
- Removed cflags calls at cmake step.

* Tue Apr 17 2007 kwizart < kwizart at gmail.com > - 1.0.1-4
- Fix CXXFLAGS
- Fix wrong-script-end-of-line-encoding and spurious-executable-perm

* Tue Apr 17 2007 kwizart < kwizart at gmail.com > - 1.0.1-3
- Fix RPATHs from cmake build from:
  http://fedoraproject.org/wiki/PackagingDrafts/cmake
- Make VERBOSE=1

* Sat Apr 14 2007 kwizart < kwizart at gmail.com > - 1.0.1-2
- Minor fixes wip

* Wed Apr 11 2007 kwizart < kwizart at gmail.com > - 1.0.1-1
- Update to 1.0.1
- Fix RPATHs
- Removed Exclude x86_64

* Sun Jan 21 2007 Tobias Sauerwein <tsauerwein@aqsis.org> 1.0-2
- BuildRequires fixed
- Excluded x86_64

* Thu Jan 18 2007 Tobias Sauerwein <tsauerwein@aqsis.org> 1.0-1
- Update to 1.0

* Mon Dec 11 2006 Tobias Sauerwein <tsauerwein@aqsis.org> 0.9
- Initial RPM/SPEC
