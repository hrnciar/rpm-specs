%global tarname xorg-docs
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Summary:    X.Org X11 documentation
Name:       xorg-x11-docs
Version:    1.7.1
Release:    11%{?dist}
License:    MIT
URL:        http://www.x.org

BuildArch:  noarch

Source0:    http://www.x.org/pub/individual/doc/%{tarname}-%{version}.tar.bz2
Patch0:     docs-1.3-registry.patch

#BuildRequires:  fop
BuildRequires:  ghostscript
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xorg-sgml-doctools) >= 1.1.1
#BuildRequires:  xmlgraphics-commons
BuildRequires:  xmlto >= 0.0.22-2
BuildRequires:  xmlto-tex

%description
Protocol and other technical documentation for the X.Org X11 X Window System
implementation.

%prep
%setup -q -n %{tarname}-%{version}
%patch0 -p1 -b .registry

%build
autoreconf -v --install
%configure --docdir=%{_pkgdocdir} --without-fop
make

%install
%make_install
find %{buildroot} -name "*.db" -delete

%files
%{_pkgdocdir}
%{_mandir}/man7/*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Adam Jackson <ajax@redhat.com> - 1.7.1-5
- Drop BuildRequires: java-devel. Originally that was to force a specific
  JDK version, which we no longer need to do.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Peter Hutterer <peter.hutterer@redhat.com>
- s/define/global/

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Simone Caronni <negativo17@gmail.com> - 1.7.1-1
- Update to 1.7.1.
- Skip PDF document generation through fop. It fixes FTBFS on Fedora 22. Tarball
  is not yet compatible with Fedora xmlgraphics-commons >= 2.0.
- Remove useless db files.

* Tue Nov 04 2014 Simone Caronni <negativo17@gmail.com> - 1.7-1
- Update to 1.7.
- Clean up SPEC file, fix rpmlint warnings.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jul 26 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.6-7
- Install docs to %%{_pkgdocdir} where available.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Dave Airlie <airlied@redhat.com> 1.6-3
- update build requires + docdir + (temporary jdk 1.7 to workaround bug in rawhide)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Matěj Cepl <mcepl@redhat.com> - 1.6-1
- New upstream version (#640564)

* Mon Nov 22 2010 Adam Jackson <ajax@redhat.com> 1.3-7
- Fix ps-to-pdf conversion even harder.
