Name:           IQmol
Version:        2.14.3
Release:        1%{?dist}
Summary:        A free open-source molecular editor and visualization package
License:        BSD and GPLv2+ and GPLv3+
URL:            http://iqmol.org
Source0:        https://github.com/nutjunkie/IQmol/archive/v%{version}/%{name}-%{version}.tar.gz
# Build in Fedora
Patch0:         IQmol-2.13-fedora.patch
# Patch in correct fragment and QChem interface setting directory
Patch1:         IQmol-2.14.0-fragdir.patch
# Don't mess with OpenBabel's directories
Patch4:         IQmol-2.13-openbabel.patch
# Comment out broken Boost stuff
Patch6:         IQmol-2.13-boost.patch

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  desktop-file-utils
BuildRequires:  gl2ps-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libssh2-devel
BuildRequires:  libQGLViewer-qt5-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  openbabel-devel
BuildRequires:  openssl-devel
BuildRequires:  OpenMesh-devel
BuildRequires:  QMsgBox-qt5-devel
BuildRequires:  qt5-qtbase-devel

%description
IQmol is a free open-source molecular editor and visualization
package. It offers a range of features including a molecular editor,
surface generation (orbitals and densities) and animations
(vibrational modes and reaction pathways).

%package samples
Summary:       Sample structures for IQmol
BuildArch:     noarch

%description samples
This package contains samples for IQmol.

%prep
%setup -q
%patch0 -p1 -b .fedora
%patch1 -p1 -b .fragdir
%patch4 -p1 -b .openbabel
%patch6 -p1 -b .boost
# Get rid of bundled gl2ps
rm src/Old/gl2ps.{h,C}
# and of QMsgBox
rm src/Util/QMsgBox.{h,C}
# and of OpenMesh
rm -rf src/OpenMesh/

%build
pushd src/Main
gfortran %{optflags} -fPIC -c symmol.f90
popd

pushd src
%{qmake_qt5} IQmol.pro
make %{?_smp_mflags} VERBOSE=1

%install
install -D -p -m 755 IQmol %{buildroot}%{_bindir}/IQmol
install -D -p -m 644 src/Main/resources/IQmol.png %{buildroot}%{_datadir}/pixmaps/IQmol.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ src/Main/resources/IQmol.desktop
cp -pr share %{buildroot}%{_datadir}/IQmol

%files
%license LICENSE
%doc README
%{_datadir}/applications/IQmol.desktop
%{_datadir}/pixmaps/IQmol.png
%{_datadir}/IQmol/
%{_bindir}/IQmol

%files samples
%license LICENSE
%doc samples/*

%changelog
* Thu Jun 11 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.14.3-1
- Update to 2.14.3.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.14.0-1
- Update to 2.14.0.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.13-1
- Update to 2.13.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Jonathan Wakely <jwakely@redhat.com> - 2.11.0-2
- Patched for Boost 1.69.0 header changes.

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 2.11.0-2
- Rebuilt for Boost 1.69

* Thu Sep 13 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.11.0-1
- Update to 2.11.0.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.10.0-1
- Add gcc buildrequires.
- Update to 2.10.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jonathan Wakely <jwakely@redhat.com> - 2.9.1-2
- Rebuilt for Boost 1.66

* Tue Sep 05 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.9.1-1
- Update to 2.9.1.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Björn Esser <besser82@fedoraproject.org> - 2.7.1-8
- Rebuilt for Boost 1.64

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> - 2.7.1-7
- Rebuilt for Boost 1.63

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 2.7.1-6
- Rebuilt for libgfortran soname bump

* Fri Oct 14 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.7.1-5
- rebuild for openbabel-2.4.1

* Sat Aug 20 2016 Susi Lehtola <susi.lehtola@iki.fi> - 2.7.1-4
- Bump for rebuild against libQGLViewer.

* Thu Mar 24 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.7.1-4
- Fix linking order.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.7.1-2
- use %%qmake_qt5 to ensure proper build flags

* Sun Jan 31 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.7.1-1
- Update to 2.7.1.

* Sun Dec 27 2015 Björn Esser <fedora@besser82.io> - 2.6.0-2
- Use %%license

* Thu Oct 29 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0.

* Sun Sep 27 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.5.1-2
- Don't mess with OpenBabel's data directories.

* Tue Sep 22 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.5.1-1.1
- Bump spec due to OpenMesh rebuild.

* Mon Sep 14 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1.

* Sun Sep 06 2015 Susi Lehtola <susi.lehtola@iki.fi> - 2.3.0-9.1
- Bump spec due to boost rebuild.

* Wed Aug 19 2015 Jonathan Wakely <jwakely@redhat.com> 2.3.0-9
- Add IQmol-2.3.0-serialization.patch to fix build with Boost 1.58.0

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.3.0-7
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 24 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.3.0-4
- Rebuild for openbabel 2.90
- Fix build with gfortran-5.0 (needs to be linked with -lgfortran)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.3.0-3
- Rebuild for boost 1.57.0

* Wed Sep 17 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.0-2
- Fix default Q-Chem interface option directory.

* Fri Sep 05 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-10.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.0-9.1
- Rebuild due to updated QGLViewer.

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2.2.0-8
- Rebuild for boost 1.55.0

* Tue Mar 04 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.0-7
- Fix build against newer QGLViewer in rawhide.

* Wed Dec 18 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.0-6
- Review fixes.

* Mon Sep 16 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.0-5
- Removed bundled QsLog.

* Fri Aug 30 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.0-4
- Removed bundled QMsgBox.

* Thu Aug 08 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.0-3
- Fix build on ARM.

* Fri Jul 19 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.0-2
- Patch to get IQmol to build against OpenBabel 2.3.2.

* Thu Jul 18 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0.

* Fri Jul 12 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.0-1
- First release.
