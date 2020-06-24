Name: cfdg-fe
Version:  0.1
Release:  24%{?dist}
Summary: A front end to cfdg

License: GPLv2+
URL: http://impulzus.com/~tchibo/ 
Source0: http://impulzus.com/~tchibo/cfdg-fe.tgz_
Source1: cfdg-fe.desktop
Patch0: cfdg-fe-pixmap-path.patch
BuildRequires:  gcc
BuildRequires: autoconf, automake, desktop-file-utils, glib2-devel, gtk2-devel
Requires: cfdg

%description
A front end to cfdg

%prep
%setup -qn cfdg-fe

%patch0 -p0

%build
aclocal
autoconf
automake --add-missing
./configure --libdir=%{_libdir}
make CFLAGS="$RPM_OPT_FLAGS" LIBS="-lm"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 755 src/cfdg-fe %{buildroot}%{_bindir}/cfdg-fe
mkdir -p %{buildroot}%{_datadir}/cfdg-fe/
install -m 644 pixmaps/* %{buildroot}%{_datadir}/cfdg-fe/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 pixmaps/icon.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/cfdg-fe-icon.png

%files
%{_bindir}/cfdg-fe
%doc AUTHORS INSTALL COPYING README
%{_datadir}/icons/hicolor/32x32/apps/cfdg-fe-icon.png
%{_datadir}/applications/cfdg-fe.desktop
%{_datadir}/cfdg-fe
%{_datadir}/cfdg-fe/icon.png
%{_datadir}/cfdg-fe/logo.png

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1-19
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.1-10
- Drop desktop vendor tag.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Jon Ciesla <limb@jcomserv.net> - 0.1-7
- Rebuild for libpng 1.5.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 28 2010 Jon Ciesla <limb@jcomserv.net> - 0.1-5
- FTBFS fix, BZ 599822.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Jon Ciesla <limb@jcomserv.net> - 0.1-2
- Directory ownership fix, BZ 473634.

* Wed Jun 18 2008 Jon Ciesla <limb@jcomserv.net> - 0.1-1
- create.
