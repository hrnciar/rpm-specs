%global octpkg dicom

Name:           octave-%{octpkg}
Version:        0.4.0
Release:        1%{?dist}
Summary:        Dicom processing for Octave
License:        GPLv3+
URL:            http://octave.sourceforge.net/dicom/
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  octave-devel
BuildRequires:  gdcm-devel
BuildRequires:  libappstream-glib

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
The Octave-forge Image package provides functions for processing 
Digital communications in medicine (DICOM) files.

%prep
%autosetup -n %{octpkg}-%{version}

# Remove unneeded file that depends on python2
rm -f doc/mkfuncdocs.py

%build
# Tell it where gdcm headers are
export GDCM_CXXFLAGS="-I%{_includedir}/gdcm/"
%octave_pkg_build

%install
%octave_pkg_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}
%{octpkgdir}/
%{_metainfodir}/%{name}.metainfo.xml

%changelog
* Thu Sep 17 2020 Orion Poplawski <orion@nwra.com> - 0.4.0-1
- Update to 0.4.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.0-2
- Remove extra file that pulled in py2
- https://bugzilla.redhat.com/show_bug.cgi?id=1813872

* Thu Mar 12 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.0-1
- Update to new release
- Add metainfo file

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 0.2.2-4
- Rebuild with octave 64bit indexes

* Sat Sep 21 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.2-3
- Rebuild for gdcm 3.0.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr  8 2019 Orion Poplawski <orion@nwra.com> - 0.2.2-1
- Update to 0.2.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 0.2.1-2
- Rebuild for octave 4.4

* Sun Sep 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-19.20150707hg45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-18.20150707hg45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-17.20150707hg45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.1-16.20150707hg45
- Rebuild for octave 4.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-15.20150707hg45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 21 2015 Kalev Lember <klember@redhat.com> - 0.1.1-14.20150707hg45
- Rebuilt for gdcm soname bump

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 0.1.1-13.20150707hg45
- Use hg snapshot
- Add patch to support octave 4.0.0

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 0.1.1-12
- Rebuild for octave 4.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.1-10
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 29 2013 Orion Poplawski <orion@cora.nwra.com> - 0.1.1-7
- Rebuild for octave 3.8.0

* Tue Oct 29 2013 Mario Ceresa <mrceresa@fedoraproject.org> 0.1.1-6
- Release bump to build against new gdcm

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Mario Ceresa <mrceresa@fedoraproject.org> 0.1.1-4
- Fixed license
- Dropped buildroot removal in install section
- Excluded *.oct from provides

* Mon May 13 2013 Mario Ceresa <mrceresa@fedoraproject.org> 0.1.1-3
- Removed duplicated include in files
- Dropped obsolated octave-forge

* Mon May 13 2013 Mario Ceresa <mrceresa@fedoraproject.org> 0.1.1-2
- Fixed some initial problems found by fedora-review

* Mon May 13 2013 Mario Ceresa <mrceresa@fedoraproject.org> 0.1.1-1
- Initial Fedora package

