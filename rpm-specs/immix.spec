%define maj_version 1.3
%define min_version 2

Name:           immix
Version:        %{maj_version}.%{min_version}
Release:        37%{?dist}
Summary:        An image mixer

License:        GPLv3+
URL:            http://immix.sourceforge.net/
Source0:        http://downloads.sourceforge.net/immix/immix-%{maj_version}-%{min_version}.tar.gz

BuildRequires:  qt4-devel
BuildRequires:  exiv2-devel
BuildRequires:  fftw-devel
BuildRequires:  desktop-file-utils

%description
Immix alignes and averages a set of similar images,
 thereby decreasing the numerical noise. It is especially
 useful with digital cameras images shot in a low light
 environment: multiple noisy, high-ISO setting images
 can be combined to get a single less noisy, low-ISO-like
 image, without the blur typically associated with low-ISO
 (motion during exposure) or noise reduction algorithms.


%prep
%setup -q -n %{name}-%{maj_version}
chmod 0644 *.{cpp,h}
# it seems that "lrelease" does'nt work on rawhide
sed -i -e s/lrelease/lrelease-qt4/ immix.pro

sed -i -e 's@Icon=/usr/share/pixmaps/%{name}.svg@Icon=%{name}@' packaging/%{name}.desktop

%build
%{qmake_qt4}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --delete-original \
  --mode 644 \
  $RPM_BUILD_ROOT%{_datadir}/applications/immix.desktop



%files
%doc COPYING
%{_bindir}/immix
%{_datadir}/applications/*immix.desktop
%{_datadir}/pixmaps/immix.svg

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-33
- rebuild (exiv2)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-28
- rebuild (exiv2)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-25
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-24
- rebuild (exiv2)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.2-22
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-19
- rebuild (exiv2)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.2-17
- Drop desktop vendor tag.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-15
- rebuild (exiv2)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-14
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-12
- rebuild (exiv2)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-10
- rebuild (exiv2)

* Mon May 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-9 
- rebuild (exiv2)

* Mon Jan 04 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-8 
- rebuild (exiv2)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-5
- respin (exiv2)

* Sat Nov 22 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 1.3.2-4
- Fix package summary
* Thu Jul  3 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 1.3.2-3
- lrelease-qt4 usage
- .desktop file changes
* Wed May 14 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 1.3.2-2
- Rebuild for F-9

* Wed Feb 13 2008 kwizart < kwizart at gmail.com > - 0.8-3
- Initial spec file (based on the upstream project).


