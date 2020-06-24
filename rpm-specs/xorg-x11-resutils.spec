# Component versions
%global appres 1.0.5
%global editres 1.0.7
%global listres 1.0.4
%global viewres 1.0.5

Summary:    X.Org X11 X resource utilities
Name:       xorg-x11-resutils
Version:    7.7
Release:    5%{?dist}
License:    MIT
URL:        https://www.x.org

Source0:    https://www.x.org/pub/individual/app/appres-%{appres}.tar.bz2
Source1:    https://www.x.org/pub/individual/app/editres-%{editres}.tar.bz2
Source2:    https://www.x.org/pub/individual/app/listres-%{listres}.tar.bz2
Source3:    https://www.x.org/pub/individual/app/viewres-%{viewres}.tar.bz2

Patch0:     editres-1.0.6-format-security.patch

BuildRequires:  libtool
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Provides:   appres = %{appres}
Provides:   editres = %{editres}
Provides:   listres = %{listres}
Provides:   viewres = %{viewres}

%description
A collection of utilities for managing X resources.

%prep
%setup -q -c %{name}-%{version} -a1 -a2 -a3
%patch0 -p0 -b .fmt

%build
# Build all apps
{
    for app in * ; do
        pushd $app
            autoreconf -vif
            %configure --disable-xprint
            make %{?_smp_mflags}
        popd
    done
}

%install
# Install all apps
{
    for app in * ; do
        pushd $app
            %make_install
        popd
    done
}

%files
%{_bindir}/appres
%{_bindir}/editres
%{_bindir}/listres
%{_bindir}/viewres
%{_datadir}/X11/app-defaults/Editres
%{_datadir}/X11/app-defaults/Editres-color
%{_datadir}/X11/app-defaults/Viewres
%{_datadir}/X11/app-defaults/Viewres-color
%{_mandir}/man1/appres.1*
%{_mandir}/man1/editres.1*
%{_mandir}/man1/listres.1*
%{_mandir}/man1/viewres.1*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Adam Jackson <ajax@redhat.com> - 7.7-1
- appres 1.0.5
- editres 1.0.7
- listres 1.0.4
- viewres 1.0.5
- HTTPS URLs

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Peter Hutterer <peter.hutterer@redhat.com>
- s/define/global/

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 04 2014 Simone Caronni <negativo17@gmail.com> - 7.5-11
- Clean up SPEC file, fix rpmlint warnings.
- Simplify build requirements.
- appres 1.0.4
- listres 1.0.3

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Adam Jackson <ajax@redhat.com> 7.5-9
- Fix FTBFS with -Werror=format-security 

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Dave Airlie <airlied@redhat.com> 7.5-7
- autoreconf for aarch64

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Peter Hutterer <peter.hutterer@redhat.com> 7.5-5
- editres 1.0.6
- viewres 1.0.4

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 02 2010 Peter Hutterer <peter.hutterer@redhat.com> 7.5-1
- appres 1.0.3
- editres 1.0.5
- viewres 1.0.3
- listres 1.0.2

* Fri Mar 05 2010 Matěj Cepl <mcepl@redhat.com> - 7.1-10
- Fixed bad directory ownership of /usr/share/X11
