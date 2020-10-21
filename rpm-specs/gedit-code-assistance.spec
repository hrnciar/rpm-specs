%global __python %{__python3}

Name:           gedit-code-assistance
Version:        3.16.0
Release:        13%{?dist}
Summary:        gedit plugin for code assistance for C, C++ and Objective-C

License:        GPLv3+
URL:            http://projects.gnome.org/gedit
Source0:        ftp://ftp.gnome.org/pub/gnome/sources/gedit-code-assistance/3.16/%{name}-%{version}.tar.xz

BuildRequires:  gedit-devel
BuildRequires:  gettext
BuildRequires:  cairo-devel
BuildRequires:  atk-devel
BuildRequires:  intltool
BuildRequires:  libpeas-devel
BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel
BuildRequires:  libgee-devel
BuildRequires:  libpeas-devel
BuildRequires:  python3-gobject
Requires:       python3-gobject
Requires:       gnome-code-assistance

%description
gedit code assistance is a gedit plugin providing code assistance support from
gnome-code-assistance services. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gedit-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing code identation backends for %{name}.


%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT/%{_libdir}/gedit/plugins -name "*.la" -exec rm {} \;

%files
%license COPYING
%doc README NEWS
%{_libdir}/gedit/plugins/*
%{_datadir}/appdata/*.metainfo.xml
%{_datadir}/gedit/plugins/codeassistance/codeassistance.css

%files devel
%{_datadir}/vala/vapi/gca.vapi
%{_includedir}/gedit-3.0/gca/gca.h

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Kalev Lember <klember@redhat.com> - 3.16.0-11
- Rebuild for gedit 3.36

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.14.3-1
- Update to 3.14.3

* Sat Mar 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2
- Use %%license macro for the COPYING file

* Fri Dec 19 2014 Elad Alfassa <elad@fedoraproject.org> - 3.14.1-1
- Update to 3.14.1
- Add -devel subpackage for those who want to build identation backends

* Fri Dec 19 2014 Richard Hughes <rhughes@redhat.com> - 3.14.0-1
- Update to 3.14.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Kalev Lember <kalevlember@gmail.com> - 0.3.1-4
- Adapt for gedit desktop file rename

* Wed Jun 11 2014 Richard Hughes <rhughes@redhat.com> - 0.3.1-3
- Add new experimental metainfo.xml file for GNOME Software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Elad Alfassa <elad@fedoraproject.org> - 0.3.1-1
- Latest upstream is actually 0.3.1, my bad
- Update description too

* Wed May 07 2014 Elad Alfassa <elad@fedoraproject.org> - 0.3.0-1
- Update to upstream 0.3, now uses gnome-code-assistance as a backend

* Tue Apr 15 2014 Adam Jackson <ajax@redhat.com> 0.2.0-5
- Rebuild against llvm 3.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 0.2.0-3
- We need python3 now.

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 0.2.0-2
- Rebuilt for gtksourceview3 soname bump

* Mon Mar 25 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 0.2.0-1
- Update to 0.2.0.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 20 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 0.1.5-1
- Update to 0.1.5.

* Mon Oct 15 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 0.1.4-1
- Update to 0.1.4.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 06 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 0.1.3-1
- Update to 0.1.3.

* Fri Feb 03 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 0.1.2-3
- Missing build requirement

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 19 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 0.1.2-1
- Update to 0.1.2.

* Sun Nov 13 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 0.1.1-1
- Update to 0.1.1.

* Sun Nov 13 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 0.1.0-1
- Initial version 0.1.0.
