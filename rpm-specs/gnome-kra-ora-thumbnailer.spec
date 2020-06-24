Name:           gnome-kra-ora-thumbnailer
Version:        1.4
Release:        3%{?dist}
Summary:        Thumbnailer for Krita and MyPaint images

License:        GPLv2+
URL:            https://gitlab.gnome.org/GNOME/gnome-kra-ora-thumbnailer
Source0:        http://download.gnome.org/sources/%{name}/1.4/%{name}-%{version}.tar.xz


BuildRequires:  gcc
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
Buildrequires:  pkgconfig(libarchive)


%description
Thumbnailer for Krita and MyPaint images


%prep
%autosetup -p1


%build
%configure
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install


%files
%{_bindir}/gnome-kra-thumbnailer
%{_bindir}/gnome-openraster-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/gnome-kra-thumbnailer.thumbnailer
%{_datadir}/thumbnailers/gnome-openraster-thumbnailer.thumbnailer
%license COPYING
%doc AUTHORS NEWS README


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Yanko Kaneti <yaneti@declera.com> - 1.4-1
- Update to 1.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan  6 2014 Yanko Kaneti <yaneti@declera.com> - 1.3-2
- Fix crashes on thumbnailing trash/recent files - #1046245

* Thu Dec 19 2013 Yanko Kaneti <yaneti@declera.com> - 1.3-1
- Update to 1.3. License change to GPLv2+

* Sat Dec 14 2013 Yanko Kaneti <yaneti@declera.com> - 1.2-1
- Initial packaging
