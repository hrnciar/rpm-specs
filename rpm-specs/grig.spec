Name:           grig
Version:        0.8.1
Release:        12%{?dist}
Summary:        A Ham Radio Control graphical user interface

License:        GPLv2+
URL:            http://groundstation.sourceforge.net/grig/
Source0:        http://prdownloads.sourceforge.net/groundstation/%{name}-%{version}.tar.gz
Source1:        grig.desktop

BuildRequires:  gcc
BuildRequires:  hamlib-devel >= 1.2.5
BuildRequires:  gtk2-devel >= 2.6.0
BuildRequires:  desktop-file-utils
BuildRequires:  gettext intltool

Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils


%description
Grig is a graphical user interface for the Ham Radio Control
Libraries. It is intended to be simple and generic, presenting the
user to the same interface regardless of which radio he or she uses.

%prep
%setup -q

%build
%configure --disable-dependency-tracking
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -fr $RPM_BUILD_ROOT%{_datadir}/%{name}

desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS README ChangeLog COPYING
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}
%{_datadir}/applications/*%{name}.desktop
%doc %{_mandir}/man1/%{name}*


%changelog
* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 0.8.1-12
- Rebuild for hamlib 4.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Richard Shaw <hobbes1069@gmail.com> - 0.8.1-3
- Rebuild for hamlib 3.1.

* Thu Feb 18 2016 Lucian Langa <lucilanga@gnome.eu.org> - 0.8.1-2
- modernize specfile

* Thu Feb 18 2016 Lucian Langa <lucilanga@gnome.eu.org> - 0.8.1-1
- update to latest upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Lucian Langa <cooly@gnome.eu.org> - 0.8.0-6
- fix ftbfs due to deprecated funcs

* Thu Apr 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.8.0-5
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 09 2011 cooly@gnome.eu.org - 0.8.0-1
- add language support
- drop all patches - fixed upstream
- new upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 08 2010 Lucian Langa <cooly@gnome.eu.org> - 0.7.2-9
- fix crash on clicking on lcd (#611947)

* Fri Nov 27 2009 Lucian Langa <cooly@gnome.eu.org> - 0.7.2-8
- improve desktop file (#530822)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 17 2008 Denis Leroy <denis@poolshark.org> - 0.7.2-5
- Rebuild with newer hamlib, gcc 4.3, EVR bump

* Tue Sep 25 2007 Denis Leroy <denis@poolshark.org> - 0.7.2-3
- Rebuild for new hamlib libraries

* Mon Aug 20 2007 Denis Leroy <denis@poolshark.org> - 0.7.2-2
- Updated License tag
- Added patch for new GtkTooltip interface

* Fri Dec 29 2006 Denis Leroy <denis@poolshark.org> - 0.7.2-1
- First version
